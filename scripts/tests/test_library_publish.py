"""Publication regressions. All writes and Git operations use disposable repos."""
import hashlib
import fcntl
import importlib.util
import json
import os
from datetime import date, datetime, timezone
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "library-publish.py"


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True).strip()


class PublisherTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="library-publish-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        git(self.repo, "init", "-q", "-b", "main")
        git(self.repo, "config", "user.name", "Fixture Owner")
        git(self.repo, "config", "user.email", "fixture@example.test")
        (self.repo / "logbook").mkdir()
        (self.repo / "logbook/library.log").write_text(
            "<!-- fixture -->\n\n## [ENT-009] | fixture\nEarlier record.\n", encoding="ascii")
        (self.repo / "library/science").mkdir(parents=True)
        (self.repo / "library/science/anchor-science.md").write_text("# Science\n", encoding="ascii")
        (self.repo / "library/candidate-queue.md").write_text("# Candidate queue\n", encoding="ascii")
        git(self.repo, "add", ".")
        git(self.repo, "commit", "-qm", "fixture baseline")
        self.baseline = git(self.repo, "rev-parse", "HEAD")

    def request(self, **updates):
        data = {
            "kind": "log", "actor": "Test Agent", "email": "test@example.test",
            "message": "library: fixture outcome", "expected": {}, "writes": {},
            "log": {"ref": "library/candidate-queue.md", "body": "EMPTY: fixture queue.\n"},
        }
        data.update(updates)
        return data

    def run_request(self, data, *extra):
        self.assertTrue(SCRIPT.is_file(), "The approved publication helper is not implemented")
        request = self.root / "request.json"
        request.write_text(json.dumps(data), encoding="ascii")
        return subprocess.run([sys.executable, "-B", str(SCRIPT), "--repo", str(self.repo),
                               *extra, "publish", str(request)], capture_output=True, text=True)

    def catalog(self):
        paths = sorted(str(p.relative_to(self.repo)) for p in self.repo.glob("library/*/*.md")
                       if not p.name.startswith(("anchor-", "index-")))
        return hashlib.sha256("\n".join(paths).encode("ascii")).hexdigest()

    def prepare_write(self):
        queue = self.repo / "library/candidate-queue.md"
        block = ("## Candidate: Fixture Topic\n- **Domain:** science\n"
                 "- **Proposed by:** Test Agent\n- **Date:** 2026-01-01\n"
                 "- **Discovery score:** 9.0/10.0 (gap=9.0, compounding=9.0, timeliness=9.0, balance=9.0)\n"
                 "- **Scope:** A fixture for transactional publication.\n- **Status:** proposed\n")
        queue.write_text("# Candidate queue\n\n" + block, encoding="ascii")
        git(self.repo, "add", "library/candidate-queue.md")
        git(self.repo, "commit", "-qm", "fixture candidate")
        self.baseline = git(self.repo, "rev-parse", "HEAD")
        draft = self.root / "topic.md"
        draft.write_text("---\nname: fixture-topic\nid: 20260101T123456Z\ntier: library-topic\n"
                         "domain: science\nauthor: Test Agent\ntags: [fixture, transaction, test]\n"
                         "links: [library/science/anchor-science.md]\n---\n# Fixture Topic\n\nFixture body.\n", encoding="ascii")
        next_queue = self.root / "queue.md"
        next_queue.write_text("# Candidate queue\n", encoding="ascii")
        return self.request(kind="write", catalog=self.catalog(),
                            expected={"library/candidate-queue.md": hashlib.sha256(queue.read_bytes()).hexdigest(),
                                      "library/science/fixture-topic.md": None},
                            writes={"library/candidate-queue.md": str(next_queue),
                                    "library/science/fixture-topic.md": str(draft)},
                            log={"ref": "library/science/fixture-topic.md", "body": "WROTE: fixture topic.\n"})

    def test_log_publication_allocates_id_and_commits_only_log_as_actor(self):
        before = (self.repo / "logbook/library.log").read_bytes()
        result = self.run_request(self.request())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["status"], "PASS")
        after = (self.repo / "logbook/library.log").read_bytes()
        self.assertTrue(after.startswith(before + b"\n## [ENT-010] | "))
        self.assertTrue(after.endswith(b"EMPTY: fixture queue.\n"))
        self.assertIn(b"| Test Agent | library |", after)
        self.assertEqual(git(self.repo, "show", "--format=", "--name-only", "HEAD"), "logbook/library.log")
        self.assertEqual(git(self.repo, "log", "-1", "--format=%an <%ae>"), "Test Agent <test@example.test>")
        self.assertEqual(git(self.repo, "status", "--porcelain"), "")

    def test_existing_watcher_lock_prevents_any_publication_until_released(self):
        request = self.root / "locked.json"
        request.write_text(json.dumps(self.request()), encoding="ascii")
        with (self.repo / ".git/repo-pull.sync.lock").open("w") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            process = subprocess.Popen([sys.executable, "-B", str(SCRIPT), "--repo", str(self.repo),
                                        "publish", str(request)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            try:
                with self.assertRaises(subprocess.TimeoutExpired):
                    process.communicate(timeout=0.5)
                self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.baseline)
            finally:
                fcntl.flock(lock, fcntl.LOCK_UN)
                output, error = process.communicate(timeout=10)
        self.assertEqual(process.returncode, 0, error)
        self.assertEqual(json.loads(output)["status"], "PASS")

    def test_failed_commit_restores_original_log_and_staging(self):
        hook = self.repo / ".git/hooks/pre-commit"
        hook.write_text("#!/bin/sh\nexit 1\n", encoding="ascii")
        hook.chmod(0o755)
        before = (self.repo / "logbook/library.log").read_bytes()
        result = self.run_request(self.request())
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((self.repo / "logbook/library.log").read_bytes(), before)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.baseline)
        self.assertEqual(git(self.repo, "status", "--porcelain"), "")


    def test_write_commits_topic_queue_removal_and_log_together(self):
        request = self.prepare_write()
        result = self.run_request(request)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(git(self.repo, "rev-list", "--count", self.baseline + "..HEAD"), "1")
        self.assertEqual(set(git(self.repo, "show", "--format=", "--name-only", "HEAD").splitlines()),
                         {"library/science/fixture-topic.md", "library/candidate-queue.md", "logbook/library.log"})
        self.assertNotIn("## Candidate:", (self.repo / "library/candidate-queue.md").read_text())
        self.assertEqual((self.repo / "library/science/fixture-topic.md").read_bytes(),
                         Path(request["writes"]["library/science/fixture-topic.md"]).read_bytes())

    def test_stale_queue_cannot_overwrite_a_peer_change(self):
        request = self.prepare_write()
        queue = self.repo / "library/candidate-queue.md"
        queue.write_text(queue.read_text() + "\n<!-- peer addition -->\n", encoding="ascii")
        git(self.repo, "add", "library/candidate-queue.md")
        git(self.repo, "commit", "-qm", "peer change")
        peer_head = git(self.repo, "rev-parse", "HEAD")
        result = self.run_request(request)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), peer_head)
        self.assertIn("peer addition", queue.read_text())
        self.assertFalse((self.repo / "library/science/fixture-topic.md").exists())
        self.assertEqual(git(self.repo, "status", "--porcelain"), "")


    def test_publication_cannot_write_outside_library_topic_scope(self):
        request = self.prepare_write()
        request["writes"]["policy.md"] = request["writes"].pop("library/science/fixture-topic.md")
        request["expected"]["policy.md"] = request["expected"].pop("library/science/fixture-topic.md")
        result = self.run_request(request)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.repo / "policy.md").exists())
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.baseline)

    def test_actor_cannot_inject_logbook_fields(self):
        result = self.run_request(self.request(actor="Test Agent | error"))
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.baseline)

    def test_log_body_cannot_forge_another_entry(self):
        result = self.run_request(self.request(log={"ref": "library/candidate-queue.md",
                                                  "body": "ERROR: fixture.\n## [ENT-999] | forged\n"}))
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.baseline)

    def test_wrong_candidate_disposition_is_rejected(self):
        request = self.prepare_write()
        Path(request["writes"]["library/candidate-queue.md"]).write_bytes(
            (self.repo / "library/candidate-queue.md").read_bytes())
        result = self.run_request(request)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.repo / "library/science/fixture-topic.md").exists())

    def test_topic_catalog_change_requires_rechecking_duplicates(self):
        request = self.prepare_write()
        (self.repo / "library/science/peer-topic.md").write_text("# Peer topic\n", encoding="ascii")
        git(self.repo, "add", "library/science/peer-topic.md")
        git(self.repo, "commit", "-qm", "peer topic")
        peer_head = git(self.repo, "rev-parse", "HEAD")
        result = self.run_request(request)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), peer_head)


    def test_snapshot_returns_hashes_and_exact_text_without_writes(self):
        result = subprocess.run([sys.executable, "-B", str(SCRIPT), "--repo", str(self.repo),
                                 "snapshot", "library/candidate-queue.md", "library/science/absent.md"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        snapshot = json.loads(result.stdout)
        raw = (self.repo / "library/candidate-queue.md").read_bytes()
        self.assertEqual(snapshot["expected"]["library/candidate-queue.md"], hashlib.sha256(raw).hexdigest())
        self.assertEqual(snapshot["files"]["library/candidate-queue.md"], raw.decode("ascii"))
        self.assertIsNone(snapshot["expected"]["library/science/absent.md"])
        self.assertEqual(snapshot["catalog"], self.catalog())
        self.assertEqual(git(self.repo, "status", "--porcelain"), "")
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.baseline)

    def test_discovery_appends_candidates_with_log_in_one_commit(self):
        request = self.prepare_write()
        old = (self.repo / "library/candidate-queue.md").read_text()
        new_block = old.split("## Candidate:", 1)[1].replace("Fixture Topic", "Second Topic")
        draft = self.root / "discovery.md"
        draft.write_text(old + "\n## Candidate:" + new_block, encoding="ascii")
        request.update(kind="discover", writes={"library/candidate-queue.md": str(draft)},
                       expected={"library/candidate-queue.md": request["expected"]["library/candidate-queue.md"]},
                       log={"ref": "library/candidate-queue.md", "body": "Discovery cycle: fixture addition.\n"})
        result = self.run_request(request)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.repo / "library/candidate-queue.md").read_text(), draft.read_text())
        self.assertEqual(set(git(self.repo, "show", "--format=", "--name-only", "HEAD").splitlines()),
                         {"library/candidate-queue.md", "logbook/library.log"})


    def test_discovery_rejects_duplicate_titles(self):
        request = self.prepare_write()
        old = (self.repo / "library/candidate-queue.md").read_text()
        block = "## Candidate:" + old.split("## Candidate:", 1)[1]
        draft = self.root / "discover-invalid.md"
        request.update(kind="discover", writes={"library/candidate-queue.md": str(draft)},
                       expected={"library/candidate-queue.md": request["expected"]["library/candidate-queue.md"]},
                       log={"ref": "library/candidate-queue.md", "body": "Discovery cycle: fixture.\n"})
        for suffix in ("\n" + block,):
            with self.subTest(suffix_length=len(suffix)):
                draft.write_text(old + suffix, encoding="ascii")
                result = self.run_request(request)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.baseline)

    def test_discovery_rejects_queue_overflow(self):
        request = self.prepare_write()
        old = (self.repo / "library/candidate-queue.md").read_text()
        block = "## Candidate:" + old.split("## Candidate:", 1)[1]
        draft = self.root / "overflow.md"
        draft.write_text(old + "".join("\n" + block.replace("Fixture Topic", f"Topic {i}") for i in range(25)), encoding="ascii")
        request.update(kind="discover", writes={"library/candidate-queue.md": str(draft)},
                       expected={"library/candidate-queue.md": request["expected"]["library/candidate-queue.md"]},
                       log={"ref": "library/candidate-queue.md", "body": "Discovery cycle: fixture.\n"})
        result = self.run_request(request)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.baseline)

    def test_writer_cannot_remove_an_additional_candidate(self):
        request = self.prepare_write()
        queue = self.repo / "library/candidate-queue.md"
        block = "## Candidate:" + queue.read_text().split("## Candidate:", 1)[1]
        queue.write_text(queue.read_text() + "\n" + block.replace("Fixture Topic", "Second Topic"), encoding="ascii")
        git(self.repo, "add", "library/candidate-queue.md")
        git(self.repo, "commit", "-qm", "second candidate")
        request["expected"]["library/candidate-queue.md"] = hashlib.sha256(queue.read_bytes()).hexdigest()
        result = self.run_request(request)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.repo / "library/science/fixture-topic.md").exists())


    def test_review_due_uses_six_calendar_months_and_rejects_invalid_dates(self):
        spec = importlib.util.spec_from_file_location("publisher_under_test", SCRIPT)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertTrue(callable(getattr(module, "review_due", None)), "Review eligibility is not implemented")
        for today, stamp, expected in [
                (date(2026, 9, 8), None, True), (date(2026, 9, 8), "2026-03-08", True),
                (date(2026, 9, 8), "2026-03-09", False), (date(2024, 8, 31), "2024-02-29", True),
                (date(2025, 8, 31), "2025-03-01", False)]:
            content = "---\nname: fixture\n" + (f"reviewed: {stamp}\n" if stamp else "") + "---\n# Fixture\n"
            self.assertEqual(module.review_due(content, today), expected, (today, stamp))
        for stamp in ("not-a-date", "2999-01-01", "2026-02-30"):
            with self.assertRaises(module.PublicationError):
                module.review_due(f"---\nreviewed: {stamp}\n---\n", date(2026, 9, 8))

    def test_review_updates_existing_topic_and_log_preserving_identity(self):
        self.assertEqual(self.run_request(self.prepare_write()).returncode, 0)
        path = "library/science/fixture-topic.md"
        original = (self.repo / path).read_text()
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        draft = self.root / "review.md"
        draft.write_text(original.replace("\n---\n", f"\nreviewed: {today}\n---\n", 1)
                         .replace("Fixture body.", "Corrected fixture body."), encoding="ascii")
        request = self.request(kind="review", actor="Reviewer Agent",
                               expected={path: hashlib.sha256(original.encode("ascii")).hexdigest()},
                               writes={path: str(draft)}, log={"ref": path, "body": "Review cycle: fixture corrected.\n"})
        result = self.run_request(request)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.repo / path).read_text(), draft.read_text())
        self.assertIn("author: Test Agent\n", (self.repo / path).read_text())
        self.assertEqual(set(git(self.repo, "show", "--format=", "--name-only", "HEAD").splitlines()),
                         {path, "logbook/library.log"})
        repeated = self.run_request(request)
        self.assertNotEqual(repeated.returncode, 0)

    def test_deliberate_duplicate_disposition_removes_only_candidate_and_logs(self):
        request = self.prepare_write()
        request.update(kind="dispose", writes={"library/candidate-queue.md": request["writes"]["library/candidate-queue.md"]},
                       expected={"library/candidate-queue.md": request["expected"]["library/candidate-queue.md"]},
                       log={"ref": "library/candidate-queue.md", "body": "DUPLICATE: fixture candidate already covered.\n"})
        result = self.run_request(request)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.repo / "library/science/fixture-topic.md").exists())
        self.assertEqual(set(git(self.repo, "show", "--format=", "--name-only", "HEAD").splitlines()),
                         {"library/candidate-queue.md", "logbook/library.log"})


    def test_log_file_hardlink_cannot_modify_an_external_file(self):
        log = self.repo / "logbook/library.log"
        old = log.read_bytes()
        external = self.root / "external.log"
        external.write_bytes(old)
        log.unlink()
        os.link(external, log)
        result = self.run_request(self.request())
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(external.read_bytes(), old)

    def test_duplicate_source_log_ids_fail_closed(self):
        log = self.repo / "logbook/library.log"
        log.write_text(log.read_text() + "\n## [ENT-009] | duplicate\nDuplicate record.\n", encoding="ascii")
        git(self.repo, "add", "logbook/library.log")
        git(self.repo, "commit", "-qm", "fixture duplicate IDs")
        before = git(self.repo, "rev-parse", "HEAD")
        result = self.run_request(self.request())
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), before)

    def test_duplicate_json_keys_are_not_silently_overridden(self):
        path = self.root / "duplicate.json"
        raw = json.dumps(self.request()).replace('"actor": "Test Agent"', '"actor": "Ignored", "actor": "Test Agent"')
        path.write_text(raw, encoding="ascii")
        result = subprocess.run([sys.executable, "-B", str(SCRIPT), "--repo", str(self.repo),
                                 "publish", str(path)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('"status": "HALT"', result.stderr)

    def test_log_cross_reference_is_preserved(self):
        result = self.run_request(self.request(log={"ref": "library/candidate-queue.md",
                                                  "see": "20260101T123456Z", "body": "EMPTY: fixture.\n"}))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("| see: 20260101T123456Z\n", (self.repo / "logbook/library.log").read_text())

    def test_inherited_git_author_cannot_override_requested_identity(self):
        path = self.root / "author.json"
        path.write_text(json.dumps(self.request()), encoding="ascii")
        env = dict(os.environ, GIT_AUTHOR_NAME="Wrong Agent", GIT_AUTHOR_EMAIL="wrong@example.test")
        result = subprocess.run([sys.executable, "-B", str(SCRIPT), "--repo", str(self.repo),
                                 "publish", str(path)], capture_output=True, text=True, env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(git(self.repo, "log", "-1", "--format=%an <%ae>"), "Test Agent <test@example.test>")

    def test_role_specific_git_identity_config_cannot_override_requested_actor(self):
        settings = {"author.name": "Other Author", "author.email": "other-author@example.test",
                    "committer.name": "Other Committer", "committer.email": "other-committer@example.test"}
        for key, value in settings.items():
            git(self.repo, "config", key, value)
        result = self.run_request(self.request())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(git(self.repo, "log", "-1", "--format=%an <%ae>|%cn <%ce>"),
                         "Test Agent <test@example.test>|Test Agent <test@example.test>")
        for key, value in settings.items():
            self.assertEqual(git(self.repo, "config", "--get", key), value)

    def test_post_commit_identity_mismatch_is_not_reported_as_success(self):
        expected = {"GIT_AUTHOR_NAME": "Test Agent", "GIT_AUTHOR_EMAIL": "test@example.test",
                    "GIT_COMMITTER_NAME": "Test Agent", "GIT_COMMITTER_EMAIL": "test@example.test"}
        for field in expected:
            with self.subTest(field=field):
                identity = dict(expected)
                identity[field] = "Wrong Agent" if field.endswith("NAME") else "wrong@example.test"
                hook = self.repo / ".git/hooks/post-commit"
                hook.write_text("#!/bin/sh\n" + " ".join(f"{key}='{value}'" for key, value in identity.items())
                                + " git -c core.hooksPath=/dev/null commit --amend --no-edit --reset-author\n",
                                encoding="ascii")
                hook.chmod(0o755)
                result = self.run_request(self.request())
                self.assertEqual(git(self.repo, "log", "-1", "--format=%an%x00%ae%x00%cn%x00%ce").split("\x00"),
                                 list(identity.values()))
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('"status": "HALT"', result.stderr)
                self.assertIn("read-back failed", result.stderr)

    def test_two_writers_of_same_candidate_publish_only_once(self):
        request = self.prepare_write()
        paths = [self.root / f"writer-{i}.json" for i in range(2)]
        for path in paths:
            path.write_text(json.dumps(request), encoding="ascii")
        processes = [subprocess.Popen([sys.executable, "-B", str(SCRIPT), "--repo", str(self.repo),
                                       "publish", str(path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                     for path in paths]
        for process in processes:
            process.communicate(timeout=10)
        self.assertEqual(sorted(process.returncode for process in processes), [0, 1])
        self.assertEqual(git(self.repo, "rev-list", "--count", self.baseline + "..HEAD"), "1")
        self.assertEqual((self.repo / "logbook/library.log").read_text().count("## [ENT-010]"), 1)

    def test_concurrent_log_appends_both_survive_with_distinct_ids(self):
        paths = [self.root / f"log-{i}.json" for i in range(2)]
        for i, path in enumerate(paths):
            path.write_text(json.dumps(self.request(log={"ref": "library/candidate-queue.md", "body": f"ERROR: fixture {i}.\n"})), encoding="ascii")
        processes = [subprocess.Popen([sys.executable, "-B", str(SCRIPT), "--repo", str(self.repo),
                                       "publish", str(path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                     for path in paths]
        for process in processes:
            _, error = process.communicate(timeout=10)
            self.assertEqual(process.returncode, 0, error)
        text = (self.repo / "logbook/library.log").read_text()
        self.assertIn("## [ENT-010]", text)
        self.assertIn("## [ENT-011]", text)
        self.assertIn("ERROR: fixture 0.", text)
        self.assertIn("ERROR: fixture 1.", text)


    def test_dirty_or_staged_peer_work_is_never_committed_or_reset(self):
        peer = self.repo / "peer.md"
        peer.write_text("Peer work.\n", encoding="ascii")
        for staged in (False, True):
            if staged:
                git(self.repo, "add", "peer.md")
            before = git(self.repo, "status", "--porcelain")
            result = self.run_request(self.request())
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(git(self.repo, "status", "--porcelain"), before)
            self.assertEqual(peer.read_text(), "Peer work.\n")

    def test_rejected_writer_commit_restores_candidate_and_removes_new_topic(self):
        request = self.prepare_write()
        before = (self.repo / "library/candidate-queue.md").read_bytes()
        hook = self.repo / ".git/hooks/pre-commit"
        hook.write_text("#!/bin/sh\nexit 1\n", encoding="ascii")
        hook.chmod(0o755)
        result = self.run_request(request)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((self.repo / "library/candidate-queue.md").read_bytes(), before)
        self.assertFalse((self.repo / "library/science/fixture-topic.md").exists())
        self.assertEqual(git(self.repo, "status", "--porcelain"), "")

    def test_nonfinite_or_negative_lock_wait_is_rejected(self):
        for value in ("nan", "inf", "-1"):
            with self.subTest(timeout=value):
                result = self.run_request(self.request(), "--lock-timeout", value)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.baseline)

    def test_request_cannot_stamp_a_recent_topic_again(self):
        self.assertEqual(self.run_request(self.prepare_write()).returncode, 0)
        name = "library/science/fixture-topic.md"
        today = datetime.now(timezone.utc).date().isoformat()
        old = (self.repo / name).read_text().replace("\n---\n", f"\nreviewed: {today}\n---\n", 1)
        (self.repo / name).write_text(old, encoding="ascii")
        git(self.repo, "add", name)
        git(self.repo, "commit", "-qm", "fixture already reviewed")
        draft = self.root / "recent.md"
        draft.write_text(old.replace("Fixture body.", "Should not be applied."), encoding="ascii")
        result = self.run_request(self.request(kind="review", expected={name: hashlib.sha256(old.encode()).hexdigest()},
                                               writes={name: str(draft)}, log={"ref": name, "body": "Review cycle: fixture.\n"}))
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((self.repo / name).read_text(), old)


    def test_branch_is_rechecked_after_waiting_for_lock(self):
        path = self.root / "branch.json"
        path.write_text(json.dumps(self.request()), encoding="ascii")
        with (self.repo / ".git/repo-pull.sync.lock").open("w") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            process = subprocess.Popen([sys.executable, "-B", str(SCRIPT), "--repo", str(self.repo),
                                        "publish", str(path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            try:
                with self.assertRaises(subprocess.TimeoutExpired):
                    process.communicate(timeout=0.3)
                git(self.repo, "checkout", "-qb", "peer-branch")
            finally:
                fcntl.flock(lock, fcntl.LOCK_UN)
                process.communicate(timeout=10)
        self.assertNotEqual(process.returncode, 0)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.baseline)

    def test_post_commit_mutation_is_not_reported_as_success(self):
        hook = self.repo / ".git/hooks/post-commit"
        hook.write_text("#!/bin/sh\nprintf 'Unexpected hook change.\\n' >> logbook/library.log\n", encoding="ascii")
        hook.chmod(0o755)
        result = self.run_request(self.request())
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('"status": "HALT"', result.stderr)
        self.assertNotEqual(git(self.repo, "rev-parse", "HEAD"), self.baseline)


if __name__ == "__main__":
    unittest.main()
