#!/usr/bin/env python3
"""CI-only publisher for derived library indexes, not a VPS sync tool."""

import argparse
import os
from pathlib import Path
import subprocess
import sys
import tempfile


class PublishError(RuntimeError):
    """Publication stopped without overwriting another writer's work."""


class PushRejected(PublishError):
    """A failed push can be retried only by rebuilding from fresh main."""


def run(repo, *command, env=None, check=True):
    result = subprocess.run(command, cwd=repo, env=env, capture_output=True, text=True)
    if check and result.returncode:
        detail = "\n".join(part.strip() for part in (result.stdout, result.stderr) if part.strip())
        raise PublishError(f"{' '.join(command)} failed (exit {result.returncode}): {detail}")
    return result


def git(repo, *args, **kwargs):
    return run(repo, "git", *args, **kwargs)


def publish(repo, attempts=3):
    """Publish from a fresh disposable worktree, leaving checkout HEAD alone."""
    if not 1 <= attempts <= 5:
        raise PublishError("attempts must be between 1 and 5")
    repo = Path(repo).resolve()
    if git(repo, "status", "--porcelain=v1", "--untracked-files=all").stdout:
        raise PublishError("initial checkout is dirty; refusing publication")
    for attempt in range(1, attempts + 1):
        print(f"library-index: attempt {attempt}/{attempts}")
        try:
            return publish_attempt(repo)
        except PushRejected as error:
            print(f"library-index: push failed on attempt {attempt}: {error}", file=sys.stderr)
    raise PublishError(f"publication failed after {attempts} attempts")


def publish_attempt(repo):
    """Never reuse a rejected commit or its index patch."""
    git(repo, "fetch", "--no-tags", "origin", "refs/heads/main")
    base = git(repo, "rev-parse", "FETCH_HEAD").stdout.strip()
    with tempfile.TemporaryDirectory(prefix="library-index-publish-") as temporary:
        tree = Path(temporary) / "tree"
        git(repo, "worktree", "add", "--detach", str(tree), base)
        try:
            run(tree, sys.executable, "-B", "scripts/index-library.py")
            indexes = ["library/index-library.md"]
            indexes.extend(
                f"library/{domain.name}/index-{domain.name}.md"
                for domain in sorted((tree / "library").iterdir())
                if domain.is_dir() and domain.name != "quarantine"
            )
            changed = set()
            for args in (("diff", "--name-only", "-z"),
                         ("diff", "--cached", "--name-only", "-z"),
                         ("ls-files", "--others", "--exclude-standard", "-z")):
                changed.update(filter(None, git(tree, *args).stdout.split("\0")))
            unexpected = changed - set(indexes)
            if unexpected:
                raise PublishError("generator changed non-index paths: " +
                                   ", ".join(sorted(unexpected)))
            git(tree, "--literal-pathspecs", "add", "--", *indexes)
            if not git(tree, "diff", "--cached", "--name-only").stdout:
                print("library-index: No index changes to commit")
                return False
            identity = os.environ.copy()
            for role in ("AUTHOR", "COMMITTER"):
                identity[f"GIT_{role}_NAME"] = "Library Index Bot"
                identity[f"GIT_{role}_EMAIL"] = "library-index@suggi-workspace.dev"
            git(tree, "-c", "commit.gpgsign=false", "commit", "-m",
                "library: auto-regenerate indexes", env=identity)
            pushed = git(tree, "push", "origin", "HEAD:main", check=False)
            if pushed.returncode:
                raise PushRejected(pushed.stderr.strip())
            print("library-index: pushed regenerated indexes")
            return True
        finally:
            # Only this helper's disposable tree is removed, never the checkout.
            git(repo, "worktree", "remove", "--force", str(tree))


def require_ci_checkout(repo):
    """Refuse persistent VPS clones and anything but the Actions workspace."""
    repo = Path(repo).resolve()
    if repo == Path("/srv") or Path("/srv") in repo.parents:
        raise PublishError("refusing persistent /srv checkout")
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise PublishError("requires GITHUB_ACTIONS=true")
    workspace = os.environ.get("GITHUB_WORKSPACE")
    if not workspace or Path(workspace).resolve() != repo:
        raise PublishError("repository must match GITHUB_WORKSPACE")
    location_variables = (
        "GIT_DIR", "GIT_COMMON_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE",
        "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES",
    )
    if any(name in os.environ for name in location_variables):
        raise PublishError("refusing Git environment location overrides")
    metadata = repo / ".git"
    if metadata.is_symlink() or not metadata.is_dir():
        raise PublishError("GITHUB_WORKSPACE must be an ordinary checkout with its own .git")
    if Path(git(repo, "rev-parse", "--show-toplevel").stdout.strip()).resolve() != repo:
        raise PublishError("GITHUB_WORKSPACE must be the ordinary checkout root")
    return repo


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--attempts", type=int, default=3, help="attempt limit, 1-5 (default: 3)")
    args = parser.parse_args(argv)
    try:
        repo = require_ci_checkout(args.repo)
        publish(repo, attempts=args.attempts)
        return 0
    except PublishError as error:
        print(f"library-index: ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
