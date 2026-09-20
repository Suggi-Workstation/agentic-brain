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


    def prepare_write(self):
        queue = self.repo / "library/candidate-queue.md"
        block = self.candidate()
        queue.write_text("# Candidate queue\n\n" + block, encoding="ascii")
        git(self.repo, "add", "library/candidate-queue.md")
        git(self.repo, "commit", "-qm", "fixture candidate")
        self.baseline = git(self.repo, "rev-parse", "HEAD")
        draft = self.root / "topic.md"
        draft.write_text("---\nname: fixture-topic\nid: 20260101T123456Z\ntier: library-topic\n"
                         "domain: science\nauthor: Test Agent\ntags: [fixture, transaction, test]\n"
                         "links: [library/science/anchor-science.md]\n---\n# Fixture Topic\n\nFixture body.\n", encoding="ascii")
        return self.request(kind="write", queue={"remove": hashlib.sha256(block.strip().encode("ascii")).hexdigest()},
                            expected={"library/science/fixture-topic.md": None},
                            writes={"library/science/fixture-topic.md": str(draft)},
                            log={"ref": "library/science/fixture-topic.md", "body": "WROTE: fixture topic.\n"})

    def candidate(self, title="Fixture Topic", domain="science", status="proposed"):
        return (f"## Candidate: {title}\n- **Domain:** {domain}\n"
                "- **Proposed by:** Test Agent\n- **Date:** 2026-01-01\n"
                "- **Discovery score:** 9.0/10.0 (gap=9.0, compounding=9.0, timeliness=9.0, balance=9.0)\n"
                f"- **Scope:** A fixture for transactional publication.\n- **Status:** {status}\n")

    def prepare_discovery(self, batch=None):
        draft = self.root / "discovery.md"
        draft.write_text(self.candidate("Second Topic") if batch is None else batch, encoding="ascii")
        return self.request(kind="discover", queue={"append": str(draft)},
                            log={"ref": "library/candidate-queue.md", "body": "Discovery cycle: fixture addition.\n"})

    def repo_state(self):
        files = {str(path.relative_to(self.repo)): path.read_bytes()
                 for path in self.repo.rglob("*")
                 if ".git" not in path.relative_to(self.repo).parts and path.is_file()}
        return git(self.repo, "rev-parse", "HEAD"), git(self.repo, "status", "--porcelain"), files

    def assert_rejected_unchanged(self, request, reason):
        before = self.repo_state()
        result = self.run_request(request)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(reason, result.stderr)
        self.assertEqual(self.repo_state(), before)

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


    def test_writer_operation_preserves_a_concurrently_appended_candidate(self):
        request = self.prepare_write()
        queue = self.repo / "library/candidate-queue.md"
        selected = "## Candidate:" + queue.read_text().split("## Candidate:", 1)[1]
        request["queue"] = {"remove": hashlib.sha256(selected.strip().encode("ascii")).hexdigest()}
        appended = selected.replace("Fixture Topic", "Concurrent Topic")
        queue.write_text(queue.read_text() + "\n" + appended, encoding="ascii")
        git(self.repo, "add", "library/candidate-queue.md")
        git(self.repo, "commit", "-qm", "concurrent discovery")
        before_log = (self.repo / "logbook/library.log").read_bytes()
        result = self.run_request(request)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(queue.read_text(), "# Candidate queue\n\n" + appended)
        self.assertTrue((self.repo / "library/science/fixture-topic.md").is_file())
        self.assertTrue((self.repo / "logbook/library.log").read_bytes().startswith(before_log))
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

    def test_changed_candidate_cannot_overwrite_a_peer_change(self):
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

    def test_expected_keys_must_be_exactly_topic_writes(self):
        writer = self.prepare_write()
        for extra in ("library/candidate-queue.md", "library/science/anchor-science.md", "library/index-library.md"):
            with self.subTest(extra=extra):
                request = json.loads(json.dumps(writer))
                path = self.repo / extra
                request["expected"][extra] = hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None
                self.assert_rejected_unchanged(request, "Expected keys must exactly match topic writes")
        writer["expected"] = {}
        self.assert_rejected_unchanged(writer, "Expected keys must exactly match topic writes")
        self.assert_rejected_unchanged(self.request(expected={"library/index-library.md": None}),
                                       "Expected keys must exactly match topic writes")

    def test_legacy_catalog_and_raw_queue_drafts_are_rejected(self):
        writer = self.prepare_write()
        for request in (writer, self.prepare_discovery(), self.request()):
            with self.subTest(kind=request["kind"]):
                self.assert_rejected_unchanged(dict(request, catalog="0" * 64), "Invalid request fields")
                queue = "library/candidate-queue.md"
                raw = self.root / "old-api-queue.md"
                raw.write_bytes((self.repo / queue).read_bytes())
                legacy = dict(request, writes={queue: str(raw)},
                              expected={queue: hashlib.sha256(raw.read_bytes()).hexdigest()})
                self.assert_rejected_unchanged(legacy, "Only topic draft paths are writable")

    def test_queue_operations_are_required_and_role_specific(self):
        writer = self.prepare_write()
        discoverer = self.prepare_discovery()
        dispose = dict(writer, kind="dispose", writes={}, expected={},
                       log={"ref": "library/candidate-queue.md", "body": "REJECT: fixture.\n"})
        for request in (writer, discoverer, dispose):
            with self.subTest(kind=request["kind"]):
                missing = dict(request)
                del missing["queue"]
                self.assert_rejected_unchanged(missing, '"status": "HALT"')
                wrong = discoverer["queue"] if request["kind"] != "discover" else writer["queue"]
                assert isinstance(request["queue"], dict)
                extra = request["queue"].copy()
                extra["unknown"] = "value"
                for operation in (None, {}, wrong, extra, {**writer["queue"], **discoverer["queue"]}):
                    self.assert_rejected_unchanged(dict(request, queue=operation), '"status": "HALT"')
        for digest in (None, [], "not-sha256", writer["queue"]["remove"].upper()):
            self.assert_rejected_unchanged(dict(writer, queue={"remove": digest}), "Candidate changed")

    def test_discovery_and_disposition_cannot_publish_topic_drafts(self):
        writer = self.prepare_write()
        for kind, operation in (("discover", self.prepare_discovery()["queue"]), ("dispose", writer["queue"])):
            with self.subTest(kind=kind):
                request = dict(writer, kind=kind, queue=operation,
                               log={"ref": "library/candidate-queue.md", "body": "REJECT: fixture.\n"})
                self.assert_rejected_unchanged(request, '"status": "HALT"')
        self.assert_rejected_unchanged(dict(writer, kind="dispose", writes={}, expected={}),
                                       "Disposition requires a logged FLAG, REJECT, or DUPLICATE")

    def test_writer_requires_one_absent_topic_in_selected_domain(self):
        writer = self.prepare_write()
        self.assert_rejected_unchanged(dict(writer, writes={}, expected={}), "exactly one topic")
        name = "library/science/fixture-topic.md"
        two = dict(writer, writes={**writer["writes"], "library/science/second.md": writer["writes"][name]},
                   expected={**writer["expected"], "library/science/second.md": None})
        self.assert_rejected_unchanged(two, "exactly one topic")
        (self.repo / "library/other").mkdir()
        (self.repo / "library/other/anchor-other.md").write_text("# Other\n", encoding="ascii")
        (self.repo / name).write_bytes(Path(writer["writes"][name]).read_bytes())
        git(self.repo, "add", "library")
        git(self.repo, "commit", "-qm", "fixture existing topic and other domain")
        self.assert_rejected_unchanged(dict(writer, writes={"library/other/fixture-topic.md": writer["writes"][name]},
                                           expected={"library/other/fixture-topic.md": None}), "must match the candidate domain")
        self.assert_rejected_unchanged(writer, "Source changed")
        writer["expected"][name] = hashlib.sha256((self.repo / name).read_bytes()).hexdigest()
        self.assert_rejected_unchanged(writer, "must not exist")

    def test_actor_cannot_inject_logbook_fields(self):
        result = self.run_request(self.request(actor="Test Agent | error"))
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.baseline)

    def test_log_body_cannot_forge_another_entry(self):
        result = self.run_request(self.request(log={"ref": "library/candidate-queue.md",
                                                  "body": "ERROR: fixture.\n## [ENT-999] | forged\n"}))
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.baseline)

    def test_removal_preserves_comments_header_and_other_candidate_blocks(self):
        request = self.prepare_write()
        queue = self.repo / "library/candidate-queue.md"
        header = "# Candidate queue\n\n<!--\n" + self.candidate("Format Example") + "-->"
        rejected = self.candidate("Rejected", status="rejected").rstrip() + "\n\n<!-- prior note -->"
        note = "<!-- keep this queue note -->"
        selected = self.candidate().rstrip() + "\n\n" + note
        later = self.candidate("Later").rstrip() + "\n\n<!-- final note -->"
        queue.write_text("\n\n".join((header, rejected, selected, later)) + "\n", encoding="ascii")
        git(self.repo, "add", "library/candidate-queue.md")
        git(self.repo, "commit", "-qm", "fixture comments and rejected candidate")
        request["queue"]["remove"] = hashlib.sha256(selected.encode("ascii")).hexdigest()
        result = self.run_request(request)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(queue.read_text(), "\n\n".join((header, rejected, note, later)) + "\n")
        self.assertEqual(git(self.repo, "status", "--porcelain"), "")

    def test_wrong_candidate_disposition_is_rejected(self):
        request = self.prepare_write()
        request["queue"]["remove"] = "0" * 64
        self.assert_rejected_unchanged(request, "Candidate changed")

    def test_unrelated_topic_and_index_changes_do_not_invalidate_writer(self):
        request = self.prepare_write()
        (self.repo / "library/science/peer-topic.md").write_text("# Peer topic\n", encoding="ascii")
        (self.repo / "library/index-library.md").write_text("# Regenerated index\n", encoding="ascii")
        git(self.repo, "add", "library")
        git(self.repo, "commit", "-qm", "peer topic and generated index")
        result = self.run_request(request)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.repo / "library/science/peer-topic.md").read_text(), "# Peer topic\n")
        self.assertEqual((self.repo / "library/index-library.md").read_text(), "# Regenerated index\n")


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
        self.assertNotIn("catalog", snapshot)
        self.assertIn("candidate", snapshot)
        self.assertIsNone(snapshot["candidate"])
        self.assertEqual(git(self.repo, "status", "--porcelain"), "")
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.baseline)

    def test_snapshot_candidate_is_null_for_absent_or_rejected_only_queue(self):
        queue = self.repo / "library/candidate-queue.md"
        for body in ("# Queue\n\n" + self.candidate(status="rejected"), None):
            with self.subTest(body=body):
                if body is None:
                    queue.unlink()
                else:
                    queue.write_text(body, encoding="ascii")
                git(self.repo, "add", "library/candidate-queue.md")
                git(self.repo, "commit", "-qm", "fixture no proposed candidate")
                before = self.repo_state()
                result = subprocess.run([sys.executable, "-B", str(SCRIPT), "--repo", str(self.repo),
                                         "snapshot", "library/candidate-queue.md"], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                snapshot = json.loads(result.stdout)
                self.assertIn("candidate", snapshot)
                self.assertIsNone(snapshot["candidate"])
                self.assertEqual(snapshot["files"]["library/candidate-queue.md"], body)
                self.assertEqual(self.repo_state(), before)

    def test_snapshot_fingerprints_only_first_proposed_parsed_block(self):
        queue = self.repo / "library/candidate-queue.md"
        selected = self.candidate() + "\n<!-- selected note -->\n"
        queue.write_text("# Candidate queue\n\n<!-- " + self.candidate("Example") + "-->\n\n"
                         + self.candidate("Rejected", status="rejected") + "\n" + selected
                         + "\n" + self.candidate("Later"), encoding="ascii")
        git(self.repo, "add", "library/candidate-queue.md")
        git(self.repo, "commit", "-qm", "fixture mixed queue")
        before = self.repo_state()
        for paths in (("library/candidate-queue.md",), ("library/science/anchor-science.md",)):
            with self.subTest(paths=paths):
                result = subprocess.run([sys.executable, "-B", str(SCRIPT), "--repo", str(self.repo),
                                         "snapshot", *paths], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                snapshot = json.loads(result.stdout)
                self.assertNotIn("catalog", snapshot)
                if "library/candidate-queue.md" in paths:
                    self.assertEqual(snapshot.get("candidate"), {
                        "title": "Fixture Topic", "domain": "science",
                        "sha256": hashlib.sha256(selected.strip().encode("ascii")).hexdigest()})
                    self.assertEqual(snapshot["files"][paths[0]], queue.read_text())
                else:
                    self.assertNotIn("candidate", snapshot)
        self.assertEqual(self.repo_state(), before)

    def test_discovery_appends_candidates_with_log_in_one_commit(self):
        self.prepare_write()
        old = (self.repo / "library/candidate-queue.md").read_text()
        request = self.prepare_discovery()
        result = self.run_request(request)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.repo / "library/candidate-queue.md").read_text(), old + "\n" + self.candidate("Second Topic"))
        self.assertEqual(set(git(self.repo, "show", "--format=", "--name-only", "HEAD").splitlines()),
                         {"library/candidate-queue.md", "logbook/library.log"})


    def test_discovery_creates_absent_queue_with_canonical_header(self):
        queue = self.repo / "library/candidate-queue.md"
        queue.unlink()
        git(self.repo, "add", "library/candidate-queue.md")
        git(self.repo, "commit", "-qm", "fixture absent queue")
        result = self.run_request(self.prepare_discovery())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(queue.read_text(),
                         "# Library Candidate Queue -- topics proposed for the writing process\n\n"
                         + self.candidate("Second Topic"))
        self.assertEqual(set(git(self.repo, "show", "--format=", "--name-only", "HEAD").splitlines()),
                         {"library/candidate-queue.md", "logbook/library.log"})
        self.assertEqual(git(self.repo, "status", "--porcelain"), "")

    def test_discovery_rejects_entire_non_candidate_or_malformed_batch(self):
        self.prepare_write()
        valid = self.candidate("Valid Addition")
        malformed = {
            "empty": "", "whitespace": "\n  \n", "header": "# Queue\n\n" + valid,
            "comment": valid + "\n<!-- note -->\n",
            "commented candidate": "<!--\n" + self.candidate("Example") + "-->\n" + valid,
            "trailing text": valid + "Not a candidate.\n",
            "rejected": valid + "\n" + self.candidate("Rejected", status="rejected"),
            "missing field": valid + "\n" + self.candidate("Missing").replace("- **Domain:** science\n", ""),
            "extra field": valid + "- **Extra:** unexpected\n",
            "empty title": valid + "\n" + self.candidate("   "),
            "empty scope": valid.replace("A fixture for transactional publication.", "   "),
        }
        for case, batch in malformed.items():
            with self.subTest(case=case):
                batch = batch.replace("Valid Addition", case + " Valid Addition")
                self.assert_rejected_unchanged(self.prepare_discovery(batch), '"status": "HALT"')

    def test_discovery_rejects_duplicate_titles(self):
        self.prepare_write()
        for batch in (self.candidate("Unique Topic") + "\n" + self.candidate("  FIXTURE   Topic  "),
                      self.candidate("Second Topic") + "\n" + self.candidate(" second  topic ")):
            with self.subTest(batch=batch):
                self.assert_rejected_unchanged(self.prepare_discovery(batch), "duplicate titles")

    def test_discovery_preserves_rejected_history_when_reproposing(self):
        queue = self.repo / "library/candidate-queue.md"
        old = "# Candidate queue\n\n" + self.candidate("Prior Topic", status="rejected")
        queue.write_text(old, encoding="ascii")
        git(self.repo, "add", "library/candidate-queue.md")
        git(self.repo, "commit", "-qm", "fixture rejected candidate")
        revised = self.candidate(" prior   TOPIC ").replace(
            "A fixture for transactional publication.", "A differentiated scope addressing the prior rejection.")
        request = self.prepare_discovery(revised)
        result = self.run_request(request)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(queue.read_text(), old + "\n" + revised)
        self.assert_rejected_unchanged(request, "duplicate")

    def test_discovery_rejects_queue_overflow(self):
        self.prepare_write()
        batch = "\n".join(self.candidate(f"Topic {i}") for i in range(25))
        self.assert_rejected_unchanged(self.prepare_discovery(batch), "exceeds capacity")

    def test_discovery_accepts_batch_up_to_capacity_preserving_existing_queue(self):
        self.prepare_write()
        queue = self.repo / "library/candidate-queue.md"
        old = queue.read_text() + "\n" + self.candidate("Rejected", status="rejected") + "\n<!-- note -->\n"
        queue.write_text(old, encoding="ascii")
        git(self.repo, "add", "library/candidate-queue.md")
        git(self.repo, "commit", "-qm", "fixture rejected candidate and comment")
        batch = "\n".join(self.candidate(f"Topic {i}") for i in range(24))
        result = self.run_request(self.prepare_discovery(batch))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(queue.read_text(), old + "\n" + batch)
        self.assertEqual(queue.read_text().count("- **Status:** proposed"), 25)
        self.assertEqual(git(self.repo, "status", "--porcelain"), "")

    def test_discovery_rejects_entire_batch_with_invalid_domain(self):
        for domain in ("nonexistent", "../science", "quarantine"):
            with self.subTest(domain=domain):
                batch = self.candidate("Valid Addition") + "\n" + self.candidate("Invalid Domain", domain=domain)
                self.assert_rejected_unchanged(self.prepare_discovery(batch), '"status": "HALT"')

    def test_writer_cannot_remove_an_additional_candidate(self):
        request = self.prepare_write()
        queue = self.repo / "library/candidate-queue.md"
        block = "## Candidate:" + queue.read_text().split("## Candidate:", 1)[1]
        queue.write_text(queue.read_text() + "\n" + block.replace("Fixture Topic", "Second Topic"), encoding="ascii")
        git(self.repo, "add", "library/candidate-queue.md")
        git(self.repo, "commit", "-qm", "second candidate")
        draft = self.root / "raw-queue.md"
        draft.write_text("# Candidate queue\n", encoding="ascii")
        request["writes"]["library/candidate-queue.md"] = str(draft)
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

    def prepare_review(self):
        self.assertEqual(self.run_request(self.prepare_write()).returncode, 0)
        path = "library/science/fixture-topic.md"
        original = (self.repo / path).read_text()
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        draft = self.root / "review.md"
        draft.write_text(original.replace("\n---\n", f"\nreviewed: {today}\n---\n", 1)
                         .replace("Fixture body.", "Corrected fixture body."), encoding="ascii")
        return self.request(kind="review", actor="Reviewer Agent",
                            expected={path: hashlib.sha256(original.encode("ascii")).hexdigest()},
                            writes={path: str(draft)}, log={"ref": path, "body": "Review cycle: fixture corrected.\n"})

    def test_review_updates_existing_topic_and_log_preserving_identity(self):
        request = self.prepare_review()
        path = "library/science/fixture-topic.md"
        result = self.run_request(request)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.repo / path).read_bytes(), Path(request["writes"][path]).read_bytes())
        self.assertIn("author: Test Agent\n", (self.repo / path).read_text())
        self.assertEqual(set(git(self.repo, "show", "--format=", "--name-only", "HEAD").splitlines()),
                         {path, "logbook/library.log"})
        repeated = self.run_request(request)
        self.assertNotEqual(repeated.returncode, 0)

    def test_log_and_review_cannot_supply_queue_operations(self):
        review = self.prepare_review()
        for request in (self.request(), review):
            for operation in ({"remove": "0" * 64}, {"append": str(self.root / "unused.md")}, None, {}):
                with self.subTest(kind=request["kind"], operation=operation):
                    self.assert_rejected_unchanged(dict(request, queue=operation),
                                                   "Only discover, write, and dispose may operate on the queue")

    def test_review_rejects_changed_original_even_if_it_is_still_due(self):
        request = self.prepare_review()
        name = "library/science/fixture-topic.md"
        topic = self.repo / name
        topic.write_text(topic.read_text().replace("Fixture body.", "Peer correction."), encoding="ascii")
        git(self.repo, "add", name)
        git(self.repo, "commit", "-qm", "fixture peer correction")
        self.assert_rejected_unchanged(request, "Source changed")

    def test_review_preserves_identity_and_requires_current_review_stamp(self):
        request = self.prepare_review()
        draft = Path(request["writes"]["library/science/fixture-topic.md"])
        valid = draft.read_text()
        today = datetime.now(timezone.utc).date().isoformat()
        for before, after in (("author: Test Agent", "author: Reviewer Agent"),
                              ("id: 20260101T123456Z", "id: 20260102T123456Z"),
                              ("name: fixture-topic", "name: changed"),
                              ("domain: science", "domain: other"),
                              ("tier: library-topic", "tier: other"),
                              (f"reviewed: {today}", "reviewed: 2000-01-01")):
            with self.subTest(field=before):
                draft.write_text(valid.replace(before, after), encoding="ascii")
                self.assert_rejected_unchanged(request, '"status": "HALT"')

    def test_review_batch_limit_rejects_two_and_accepts_one(self):
        self.assertEqual(self.run_request(self.prepare_write()).returncode, 0)
        base = (self.repo / "library/science/fixture-topic.md").read_text()
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        expected, writes, originals = {}, {}, {}
        for index in range(2):
            slug = f"review-fixture-{index}"
            path = f"library/science/{slug}.md"
            original = base.replace("name: fixture-topic", f"name: {slug}")
            (self.repo / path).write_text(original, encoding="ascii")
            originals[path] = original
            expected[path] = hashlib.sha256(original.encode("ascii")).hexdigest()
            draft = self.root / f"{slug}.md"
            draft.write_text(original.replace("\n---\n", f"\nreviewed: {today}\n---\n", 1), encoding="ascii")
            writes[path] = str(draft)
        git(self.repo, "add", *originals)
        git(self.repo, "commit", "-qm", "fixture review batch")
        before = git(self.repo, "rev-parse", "HEAD")
        old_log = (self.repo / "logbook/library.log").read_bytes()
        request = self.request(kind="review", expected=expected, writes=writes,
                               log={"ref": next(iter(writes)), "body": "Review cycle: fixture batch.\n"})
        rejected = self.run_request(request)
        self.assertNotEqual(rejected.returncode, 0)
        self.assertIn("exactly one existing topic", rejected.stderr)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), before)
        self.assertEqual((self.repo / "logbook/library.log").read_bytes(), old_log)
        self.assertEqual(git(self.repo, "status", "--porcelain"), "")
        omitted = next(reversed(writes))
        del writes[omitted]
        del expected[omitted]
        accepted = self.run_request(request)
        self.assertEqual(accepted.returncode, 0, accepted.stderr)
        self.assertEqual(set(git(self.repo, "show", "--format=", "--name-only", "HEAD").splitlines()),
                         set(writes) | {"logbook/library.log"})
        self.assertEqual((self.repo / omitted).read_text(), originals[omitted])

    def test_deliberate_duplicate_disposition_removes_only_candidate_and_logs(self):
        request = self.prepare_write()
        request.update(kind="dispose", writes={}, expected={},
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

    def assert_writer_discoverer_result(self, writer, discoverer):
        queue = self.repo / "library/candidate-queue.md"
        self.assertEqual(queue.read_text(), "# Candidate queue\n\n" + self.candidate("Second Topic"))
        name = "library/science/fixture-topic.md"
        self.assertEqual((self.repo / name).read_bytes(), Path(writer["writes"][name]).read_bytes())
        log = (self.repo / "logbook/library.log").read_text()
        for request in (writer, discoverer):
            self.assertEqual(log.count(request["log"]["body"]), 1)
        for entry in ("ENT-010", "ENT-011"):
            self.assertEqual(log.count(f"## [{entry}]"), 1)
        self.assertEqual(git(self.repo, "rev-list", "--count", self.baseline + "..HEAD"), "2")
        self.assertEqual(git(self.repo, "status", "--porcelain"), "")

    def test_discoverer_then_writer_both_publish_from_same_snapshot(self):
        writer = self.prepare_write()
        discoverer = self.prepare_discovery()
        for request in (discoverer, writer):
            result = self.run_request(request)
            self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_writer_discoverer_result(writer, discoverer)

    def test_writer_then_discoverer_both_publish_from_same_snapshot(self):
        writer = self.prepare_write()
        discoverer = self.prepare_discovery()
        for request in (writer, discoverer):
            result = self.run_request(request)
            self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_writer_discoverer_result(writer, discoverer)

    def test_concurrent_writer_and_discoverer_preserve_both_operations_and_logs(self):
        writer = self.prepare_write()
        discoverer = self.prepare_discovery()
        processes = []
        with (self.repo / ".git/repo-pull.sync.lock").open("w") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            try:
                for index, request in enumerate((writer, discoverer)):
                    path = self.root / f"concurrent-{index}.json"
                    path.write_text(json.dumps(request), encoding="ascii")
                    processes.append(subprocess.Popen(
                        [sys.executable, "-B", str(SCRIPT), "--repo", str(self.repo), "publish", str(path)],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True))
                for process in processes:
                    with self.assertRaises(subprocess.TimeoutExpired):
                        process.communicate(timeout=0.2)
                self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.baseline)
            finally:
                fcntl.flock(lock, fcntl.LOCK_UN)
                results = []
                for process in processes:
                    try:
                        results.append(process.communicate(timeout=10))
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.communicate()
                        raise
        for process, (output, error) in zip(processes, results):
            self.assertEqual(process.returncode, 0, error)
            self.assertEqual(json.loads(output)["status"], "PASS")
        self.assert_writer_discoverer_result(writer, discoverer)

    def test_candidate_missing_changed_or_not_first_rejects_write_and_dispose(self):
        writer = self.prepare_write()
        dispose = dict(writer, kind="dispose", writes={}, expected={},
                       log={"ref": "library/candidate-queue.md", "body": "REJECT: fixture.\n"})
        queue = self.repo / "library/candidate-queue.md"
        cases = {
            "missing": self.candidate("Later"),
            "changed": self.candidate().replace("transactional publication", "changed scope"),
            "not first": self.candidate("Earlier") + "\n" + self.candidate(),
            "no proposed": self.candidate(status="rejected"),
            "queue absent": None,
        }
        for case, body in cases.items():
            with self.subTest(case=case):
                if body is None:
                    queue.unlink()
                else:
                    queue.write_text("# Candidate queue\n\n" + body, encoding="ascii")
                git(self.repo, "add", "library/candidate-queue.md")
                git(self.repo, "commit", "-qm", "fixture " + case)
                for request in (writer, dispose):
                    self.assert_rejected_unchanged(request, "Candidate changed")

    def test_repeated_writer_and_dispose_cannot_consume_the_next_candidate(self):
        for kind in ("write", "dispose"):
            with self.subTest(kind=kind):
                request = self.prepare_write()
                if kind == "dispose":
                    request.update(kind="dispose", writes={}, expected={},
                                   log={"ref": "library/candidate-queue.md", "body": "FLAG: fixture.\n"})
                result = self.run_request(self.prepare_discovery())
                self.assertEqual(result.returncode, 0, result.stderr)
                result = self.run_request(request)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assert_rejected_unchanged(request, "Source changed" if kind == "write" else "Candidate changed")
                self.assertEqual((self.repo / "library/candidate-queue.md").read_text(),
                                 "# Candidate queue\n\n" + self.candidate("Second Topic"))

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
        hook = self.repo / ".git/hooks/pre-commit"
        hook.write_text("#!/bin/sh\nexit 1\n", encoding="ascii")
        hook.chmod(0o755)
        self.assert_rejected_unchanged(request, "Git command failed: -c")

    def test_rejected_discovery_commit_restores_generated_queue_and_log(self):
        hook = self.repo / ".git/hooks/pre-commit"
        hook.write_text("#!/bin/sh\nexit 1\n", encoding="ascii")
        hook.chmod(0o755)
        request = self.prepare_discovery()
        self.assert_rejected_unchanged(request, "Git command failed: -c")
        hook.unlink()
        (self.repo / "library/candidate-queue.md").unlink()
        git(self.repo, "add", "library/candidate-queue.md")
        git(self.repo, "commit", "-qm", "fixture absent queue")
        hook.write_text("#!/bin/sh\nexit 1\n", encoding="ascii")
        hook.chmod(0o755)
        self.assert_rejected_unchanged(request, "Git command failed: -c")

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
