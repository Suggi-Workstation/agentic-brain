#!/usr/bin/env python3
"""Publish prepared library work. No research, network calls, or model invocation."""
import argparse
import calendar
from contextlib import contextmanager
from datetime import date, datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile
import time


class PublicationError(Exception):
    """A failed precondition; publication must not be reported as successful."""


def ordinary_path(repo, path):
    for part in (path, *path.parents):
        if part == repo:
            break
        if part.is_symlink():
            raise PublicationError("Symbolic links are outside publication scope")
    if path.exists() and (not path.is_file() or path.stat().st_nlink != 1):
        raise PublicationError("Expected an ordinary, unshared file")
    if not path.parent.is_dir():
        raise PublicationError("Destination parent must already exist")
    return path


def library_path(repo, name, output=False):
    if not isinstance(name, str) or not re.fullmatch(
            r"library/(?:[a-z0-9-]+\.md|[a-z0-9-]+/[a-z0-9-]+\.md)", name):
        raise PublicationError("Invalid library path")
    path = repo / name
    if "quarantine" in path.relative_to(repo).parts:
        raise PublicationError("Quarantine is outside publication scope")
    if output and name != "library/candidate-queue.md":
        if len(path.relative_to(repo).parts) != 3 or path.name.startswith(("anchor-", "index-")):
            raise PublicationError("Only topic files and the candidate queue are writable")
    return ordinary_path(repo, path)


def catalog_hash(repo):
    names = sorted(str(p.relative_to(repo)) for p in repo.glob("library/*/*.md")
                   if not p.name.startswith(("anchor-", "index-")) and p.parent.name != "quarantine")
    for name in names:
        library_path(repo, name)
    return hashlib.sha256("\n".join(names).encode("ascii")).hexdigest()


def validate_request(repo, request):
    required = {"kind", "actor", "email", "message", "expected", "writes", "log"}
    if not isinstance(request, dict) or not required <= request.keys() or request.keys() - required - {"catalog"}:
        raise PublicationError("Invalid request fields")
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9 ()._-]{0,63}", request["actor"]):
        raise PublicationError("Invalid actor")
    if not re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", request["email"]):
        raise PublicationError("Invalid email")
    if not request["message"].startswith("library: ") or any(c in request["message"] for c in "\n\r\x00"):
        raise PublicationError("Expected a one-line library commit message")
    if not isinstance(request["writes"], dict) or not isinstance(request["expected"], dict):
        raise PublicationError("Expected and writes must be objects")
    for name, digest in request["expected"].items():
        library_path(repo, name)
        if digest is not None and not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise PublicationError("Expected hashes must be SHA-256 or null")
    for name in request["writes"]:
        library_path(repo, name, output=True)
    log = request["log"]
    if not isinstance(log, dict) or not {"ref", "body"} <= log.keys() or log.keys() - {"ref", "body", "see"}:
        raise PublicationError("Invalid log fields")
    library_path(repo, log["ref"])
    body = log["body"]
    if not isinstance(body, str) or not body.strip() or re.search(r"^## \[ENT-", body, re.M) or any(c in body for c in "\r\x00"):
        raise PublicationError("Log body is empty or contains an entry header/control character")
    if "see" in log and not re.fullmatch(r"(?:\d{8}T\d{6}Z|ENT-\d+)", log["see"]):
        raise PublicationError("Invalid log cross-reference")
    json.dumps(request, ensure_ascii=False).encode("ascii")


def parse_queue(text):
    if text.count("<!--") != text.count("-->"):
        raise PublicationError("Malformed queue comment")
    masked = re.sub(r"<!--.*?-->", lambda m: "".join("\n" if c == "\n" else " " for c in m[0]), text, flags=re.S)
    starts = list(re.finditer(r"^## Candidate: ([^\n]+)\n", masked, re.M))
    header = text[:starts[0].start()].strip() if starts else text.strip()
    blocks = []
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        fields = re.findall(r"^- \*\*([^*]+):\*\* ([^\n]+)$", masked[match.end():end], re.M)
        required = {"Domain", "Proposed by", "Date", "Discovery score", "Scope", "Status"}
        if len(fields) != len(required) or {key for key, value in fields} != required:
            raise PublicationError("Malformed candidate fields")
        values = dict(fields)
        if values["Status"] not in {"proposed", "rejected"}:
            raise PublicationError("Invalid candidate status")
        blocks.append({"title": match[1].strip(), "domain": values["Domain"],
                       "status": values["Status"], "text": text[match.start():end].strip()})
    return header, blocks


def validate_queue_change(repo, request, updates):
    queue = "library/candidate-queue.md"
    if queue not in updates:
        raise PublicationError("This operation requires a candidate queue update")
    old_text = (repo / queue).read_text(encoding="ascii") if (repo / queue).exists() else ""
    new_text = updates[queue].decode("ascii")
    old_header, old = parse_queue(old_text)
    new_header, new = parse_queue(new_text)
    proposed = [entry for entry in new if entry["status"] == "proposed"]
    titles = [" ".join(entry["title"].casefold().split()) for entry in proposed]
    if len(proposed) > 25 or len(titles) != len(set(titles)):
        raise PublicationError("Candidate queue exceeds capacity or contains duplicate proposed titles")
    for entry in new:
        anchor = library_path(repo, f"library/{entry['domain']}/anchor-{entry['domain']}.md")
        if not anchor.is_file():
            raise PublicationError("Candidate domain has no anchor")
    if request["kind"] == "discover":
        if set(updates) != {queue} or not new_text.startswith(old_text) or len(new) <= len(old):
            raise PublicationError("Discovery must only append candidates to the current queue")
        return
    selected = next((i for i, entry in enumerate(old) if entry["status"] == "proposed"), None)
    if selected is None or new_header != old_header or new != old[:selected] + old[selected + 1:]:
        raise PublicationError("Remove only the first proposed candidate, preserving all other entries")
    topics = set(updates) - {queue}
    if request["kind"] == "dispose":
        if topics or not re.match(r"^(FLAG|REJECT|DUPLICATE)\b", request["log"]["body"]):
            raise PublicationError("Disposition requires a logged FLAG, REJECT, or DUPLICATE and no topic write")
        return
    if len(topics) != 1:
        raise PublicationError("A write publishes exactly one topic with its queue disposition")
    topic = next(iter(topics))
    if Path(topic).parent.as_posix() != "library/" + old[selected]["domain"] or request["expected"][topic] is not None:
        raise PublicationError("The new topic must match the candidate domain and must not exist")


def frontmatter(text):
    if not text.startswith("---\n") or "\n---\n" not in text:
        raise PublicationError("Topic frontmatter is missing")
    head = text[4:].split("\n---\n", 1)[0]
    pairs = re.findall(r"^([a-z][a-z0-9_-]*):[ \t]*(.*)$", head, re.M)
    if len({key for key, value in pairs}) != len(pairs):
        raise PublicationError("Duplicate topic frontmatter key")
    return dict(pairs)


def review_due(text, today=None):
    today = today or datetime.now(timezone.utc).date()
    meta = frontmatter(text)
    if "reviewed" not in meta:
        return True
    value = meta["reviewed"]
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    try:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            raise ValueError("format")
        reviewed = date.fromisoformat(value)
    except ValueError:
        raise PublicationError("Invalid reviewed date") from None
    if reviewed > today:
        raise PublicationError("Reviewed date is in the future")
    year, month = divmod(today.year * 12 + today.month - 1 - 6, 12)
    month += 1
    cutoff = date(year, month, min(today.day, calendar.monthrange(year, month)[1]))
    return reviewed <= cutoff


def validate_topics(repo, request, updates):
    topics = set(updates) - {"library/candidate-queue.md"}
    if request["kind"] == "review" and (not 1 <= len(topics) <= 5 or len(topics) != len(updates)):
        raise PublicationError("Review changes only one to five existing topics")
    for name in topics:
        meta = frontmatter(updates[name].decode("ascii"))
        required = {"name", "id", "tier", "domain", "author", "tags", "links"}
        if not required <= meta.keys() or meta["tier"] != "library-topic":
            raise PublicationError("Required topic creation fields are missing")
        if meta["name"] != Path(name).stem or meta["domain"] != Path(name).parent.name:
            raise PublicationError("Topic name/domain do not match its path")
        anchor = library_path(repo, f"library/{meta['domain']}/anchor-{meta['domain']}.md")
        if not anchor.is_file():
            raise PublicationError("Topic domain has no anchor")
        if request["kind"] == "write":
            if "reviewed" in meta or meta["author"] != request["actor"]:
                raise PublicationError("New topics name their author and omit reviewed")
        else:
            original = library_path(repo, name).read_text(encoding="ascii")
            if request["expected"][name] is None or not review_due(original):
                raise PublicationError("Topic is not due for review")
            old = frontmatter(original)
            if any(meta[key] != old.get(key) for key in ("name", "id", "tier", "domain", "author")):
                raise PublicationError("Review must preserve topic identity and original author")
            if meta.get("reviewed") != datetime.now(timezone.utc).date().isoformat():
                raise PublicationError("Review must stamp the current UTC date")


def git(repo, *args):
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_TERMINAL_PROMPT="0")
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True,
                            text=True, timeout=60, env=env)
    if result.returncode:
        raise PublicationError("Git command failed: " + args[0])
    return result.stdout.strip()


@contextmanager
def publication_lock(repo, timeout=30):
    if not 0 <= timeout <= 60:
        raise PublicationError("Lock timeout must be finite and between zero and 60 seconds")
    if Path(git(repo, "rev-parse", "--show-toplevel")).resolve() != repo:
        raise PublicationError("Publication requires the repository root")
    gitdir = Path(git(repo, "rev-parse", "--absolute-git-dir"))
    if gitdir != repo / ".git" or gitdir.is_symlink() or not gitdir.is_dir():
        raise PublicationError("Publication requires a normal clone with its own Git directory")
    fd = os.open(gitdir / "repo-pull.sync.lock", os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o660)
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode) or os.fstat(fd).st_nlink != 1:
            raise PublicationError("Unexpected publication lock file")
        deadline = time.monotonic() + timeout
        while True:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if time.monotonic() >= deadline:
                    raise PublicationError("Publication lock is busy; retry later")
                time.sleep(0.05)
        if git(repo, "branch", "--show-current") != "main":
            raise PublicationError("Publication requires the main branch")
        yield
    finally:
        os.close(fd)


def publish(repo, request, timeout=30):
    with publication_lock(repo, timeout):
        return publish_locked(repo, request)


def snapshot(repo, names, timeout=30):
    with publication_lock(repo, timeout):
        if git(repo, "status", "--porcelain"):
            raise PublicationError("Working tree or staging area is not clean")
        data = {}
        for name in names:
            path = library_path(repo, name)
            data[name] = path.read_bytes() if path.exists() else None
        return {"status": "PASS", "catalog": catalog_hash(repo),
                "expected": {name: hashlib.sha256(raw).hexdigest() if raw is not None else None
                             for name, raw in data.items()},
                "files": {name: raw.decode("ascii") if raw is not None else None for name, raw in data.items()}}


def replace_file(path, data):
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o664
    fd, name = tempfile.mkstemp(prefix=".library-publish-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
            os.fchmod(handle.fileno(), mode)
        os.replace(name, path)
    finally:
        Path(name).unlink(missing_ok=True)


def publish_locked(repo, request):
    validate_request(repo, request)
    if git(repo, "status", "--porcelain"):
        raise PublicationError("Working tree or staging area is not clean")
    if request["kind"] not in {"log", "write", "discover", "dispose", "review"}:
        raise PublicationError("Unsupported publication kind")
    drafts = request["writes"]
    if request["kind"] in {"write", "discover", "dispose"} and request.get("catalog") != catalog_hash(repo):
        raise PublicationError("Topic catalog changed; recheck selection and duplicates")
    if request["kind"] == "log" and drafts:
        raise PublicationError("Log-only requests cannot change library files")
    if not set(drafts).issubset(request["expected"]):
        raise PublicationError("Every output needs an expected source hash")
    for name, expected in request["expected"].items():
        source = repo / name
        actual = hashlib.sha256(source.read_bytes()).hexdigest() if source.exists() else None
        if actual != expected:
            raise PublicationError("Source changed; read and prepare again: " + name)
    updates = {name: Path(draft).read_bytes() for name, draft in drafts.items()}
    for data in updates.values():
        data.decode("ascii")
    if request["kind"] in {"discover", "write", "dispose"}:
        validate_queue_change(repo, request, updates)
    if request["kind"] in {"write", "review"}:
        validate_topics(repo, request, updates)
    path = ordinary_path(repo, repo / "logbook/library.log")
    previous = path.read_text(encoding="ascii")
    ids = re.findall(r"^## \[ENT-(\d+)\]", previous, re.M)
    numbers = [int(value) for value in ids]
    if len(ids) != len(re.findall(r"^## \[ENT-", previous, re.M)) or any(b <= a for a, b in zip(numbers, numbers[1:])):
        raise PublicationError("Library log entry IDs are malformed, duplicated, or out of order")
    if not previous.endswith("\n") or previous.endswith("\n\n\n"):
        raise PublicationError("Library log has an invalid EOF boundary")
    number = int(ids[-1]) + 1 if ids else 1
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    header = f"## [ENT-{number:03d}] | {stamp} | {request['actor']} | library | ref: {request['log']['ref']}\n"
    if "see" in request["log"]:
        header = header.rstrip("\n") + " | see: " + request["log"]["see"] + "\n"
    body = request["log"]["body"].rstrip("\n") + "\n"
    separator = "" if previous.endswith("\n\n") else "\n"
    updates["logbook/library.log"] = (previous + separator + header + body).encode("ascii")
    backups = {name: (repo / name).read_bytes() if (repo / name).exists() else None for name in updates}
    before = git(repo, "rev-parse", "HEAD")
    try:
        for name, data in updates.items():
            replace_file(repo / name, data)
        git(repo, "add", "--", *sorted(updates))
        staged = set(git(repo, "diff", "--cached", "--name-only").splitlines())
        if staged != set(updates):
            raise PublicationError("Staged paths do not match this publication")
        git(repo, "-c", "user.name=" + request["actor"], "-c", "user.email=" + request["email"],
            "-c", "author.name=" + request["actor"], "-c", "author.email=" + request["email"],
            "-c", "committer.name=" + request["actor"], "-c", "committer.email=" + request["email"],
            "commit", "-m", request["message"])
    except BaseException:
        if git(repo, "rev-parse", "HEAD") == before:
            existing = [name for name, data in backups.items() if data is not None]
            created = [name for name, data in backups.items() if data is None]
            for name, data in backups.items():
                target = repo / name
                if data is None:
                    target.unlink(missing_ok=True)
                else:
                    replace_file(target, data)
            if existing:
                git(repo, "restore", "--staged", "--", *existing)
            if created:
                git(repo, "rm", "--cached", "--ignore-unmatch", "--", *created)
        raise
    commit = git(repo, "rev-parse", "HEAD")
    identity = git(repo, "show", "-s", "--format=%an%x00%ae%x00%cn%x00%ce", commit).split("\x00")
    if identity != [request["actor"], request["email"]] * 2:
        raise PublicationError("Commit exists but identity read-back failed; inspect before any retry: " + commit)
    committed = set(git(repo, "show", "--format=", "--name-only", commit).splitlines())
    if committed != set(updates) or git(repo, "status", "--porcelain") or any(
            (repo / name).read_bytes() != data for name, data in updates.items()):
        raise PublicationError("Commit exists but read-back failed; inspect before any retry: " + commit)
    return {"status": "PASS", "commit": commit, "entry": f"ENT-{number:03d}"}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise PublicationError("Duplicate JSON field: " + key)
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--lock-timeout", type=float, default=30)
    sub = parser.add_subparsers(dest="command", required=True)
    publish_parser = sub.add_parser("publish")
    publish_parser.add_argument("request", type=Path)
    snapshot_parser = sub.add_parser("snapshot")
    snapshot_parser.add_argument("paths", nargs="+")
    args = parser.parse_args()
    try:
        if args.command == "snapshot":
            result = snapshot(args.repo.resolve(), args.paths, args.lock_timeout)
        else:
            request = json.loads(args.request.read_text(encoding="ascii"), object_pairs_hook=unique_object)
            result = publish(args.repo.resolve(), request, args.lock_timeout)
        print(json.dumps(result))
        return 0
    except (PublicationError, OSError, ValueError, KeyError, TypeError, AttributeError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({"status": "HALT", "reason": str(exc)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
