"""Real Git fixtures only: never publish or regenerate the live checkout."""

import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


SCRIPTS = Path(__file__).resolve().parents[1]
PUBLISHER = SCRIPTS / "library-index-publish.py"


class IndexPublishTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="library-index-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.env = {
            key: value for key, value in os.environ.items()
            if not key.startswith("GIT_") and not key.startswith("GITHUB_")
        }
        self.env.update({
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_TERMINAL_PROMPT": "0",
            "GIT_AUTHOR_NAME": "Fixture Author",
            "GIT_AUTHOR_EMAIL": "fixture@example.invalid",
            "GIT_COMMITTER_NAME": "Fixture Author",
            "GIT_COMMITTER_EMAIL": "fixture@example.invalid",
        })
        self.environment = mock.patch.dict(os.environ, self.env, clear=True)
        self.environment.start()
        self.addCleanup(self.environment.stop)
        self.remote = self.root / "remote.git"
        self.seed = self.root / "seed"
        self.checkout = self.root / "checkout"
        self.git(self.root, "init", "--bare", "--initial-branch=main", str(self.remote))
        self.git(self.remote, "config", "receive.denyNonFastForwards", "true")
        self.git(self.root, "init", "--initial-branch=main", str(self.seed))
        (self.seed / "scripts").mkdir()
        shutil.copyfile(SCRIPTS / "index-library.py", self.seed / "scripts/index-library.py")
        self.write(self.seed, "library/science/alpha.md", "# Alpha\n\nFirst topic.\n")
        self.write(self.seed, "library/science/anchor-science.md", "# Science\n")
        self.write(self.seed, "library/science/index-manual.md", "Hand-maintained.\n")
        self.write(self.seed, "notes/keep.txt", "Unrelated data.\n")
        self.git(self.seed, "add", ".")
        self.git(self.seed, "commit", "-m", "fixture seed")
        self.git(self.seed, "remote", "add", "origin", str(self.remote))
        self.git(self.seed, "push", "origin", "HEAD:main")
        # Match actions/checkout's default shallow history, using only file://.
        self.git(self.root, "clone", "--depth=1", self.remote.as_uri(), str(self.checkout))
        self.assertEqual(self.git(self.checkout, "rev-parse", "--is-shallow-repository"), "true")

    def git(self, repo, *args):
        return subprocess.run(
            ["git", "-C", str(repo), *args], check=True,
            capture_output=True, text=True, env=self.env,
        ).stdout.strip()

    def write(self, repo, relative, content):
        path = repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="ascii")
        return path

    def publisher(self):
        self.assertTrue(PUBLISHER.is_file(), "CI index publisher has not been implemented")
        spec = importlib.util.spec_from_file_location("library_index_publish", PUBLISHER)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def cli(self, repo=None, attempts=None, **environment):
        self.publisher()
        env = dict(self.env, **environment)
        command = [sys.executable, "-B", str(PUBLISHER), "--repo", str(repo or self.checkout)]
        if attempts is not None:
            command.extend(["--attempts", str(attempts)])
        return subprocess.run(
            command,
            cwd=self.root, env=env, capture_output=True, text=True,
        )

    def install_race_hook(self, always=False):
        """A real pre-push hook advances the local bare remote before our push."""
        log = self.root / "push-attempts.jsonl"
        hook = self.write(self.checkout, ".git/hooks/pre-push", f'''#!{sys.executable}
import json
import os
from pathlib import Path
import subprocess

env = os.environ.copy()
for key in ("GIT_DIR", "GIT_COMMON_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE",
            "GIT_PREFIX", "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES"):
    env.pop(key, None)
def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], env=env,
                          check=True, capture_output=True, text=True).stdout.strip()
log = Path({str(log)!r})
tree = Path.cwd()
entry = {{"head": git(tree, "rev-parse", "HEAD"),
         "parent": git(tree, "rev-parse", "HEAD^"),
         "index": (tree / "library/science/index-science.md").read_text()}}
with log.open("a", encoding="ascii") as handle:
    handle.write(json.dumps(entry) + "\\n")
attempt = len(log.read_text().splitlines())
if {always!r} or attempt == 1:
    seed = Path({str(self.seed)!r})
    (seed / "library/science/alpha.md").unlink(missing_ok=True)
    (seed / f"library/science/racer-{{attempt}}.md").write_text(
        f"# Racer {{attempt}}\\n\\nArrived during publication.\\n", encoding="ascii")
    (seed / "notes/keep.txt").write_text(f"Concurrent data {{attempt}}.\\n", encoding="ascii")
    git(seed, "add", ".")
    git(seed, "commit", "-m", f"concurrent writer {{attempt}}")
    git(seed, "push", "origin", "HEAD:main")
''')
        hook.chmod(0o755)
        return log

    def test_generator_failure_is_reported_without_push_or_retry(self):
        self.write(self.seed, "scripts/index-library.py",
                   "from pathlib import Path\n"
                   "Path('library/index-library.md').write_text('Incomplete.\\n')\n"
                   "print('fixture generator failed after partial output')\n"
                   "raise SystemExit(7)\n")
        self.git(self.seed, "add", "scripts/index-library.py")
        self.git(self.seed, "commit", "-m", "failing fixture generator")
        self.git(self.seed, "push", "origin", "HEAD:main")
        initial = self.git(self.remote, "rev-parse", "main")
        log = self.install_race_hook()

        result = self.cli(GITHUB_ACTIONS="true", GITHUB_WORKSPACE=str(self.checkout))

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("fixture generator failed after partial output", result.stderr)
        self.assertIn("exit 7", result.stderr)
        self.assertNotIn("attempt 2/", result.stdout)
        self.assertFalse(log.exists())
        self.assertEqual(self.git(self.remote, "rev-parse", "main"), initial)
        self.assertEqual(self.git(self.checkout, "status", "--porcelain"), "")
        self.assertEqual(len(self.git(self.checkout, "worktree", "list").splitlines()), 1)

    def test_cli_rejects_git_location_redirects_and_non_root_workspaces(self):
        linked = self.root / "linked"
        self.git(self.checkout, "worktree", "add", "--detach", str(linked), "HEAD")
        alias = self.root / "vps-alias"
        alias.symlink_to("/srv/disallowed-index-fixture", target_is_directory=True)
        cases = [
            (self.checkout / "scripts", {}, "ordinary checkout"),
            (linked, {}, "ordinary checkout"),
            (alias, {}, "/srv"),
            (self.checkout, {"GIT_DIR": str(self.seed / ".git"),
                             "GIT_WORK_TREE": str(self.seed)}, "Git environment"),
        ]
        for repo, extra, diagnostic in cases:
            with self.subTest(repo=repo, extra=extra):
                result = self.cli(repo, GITHUB_ACTIONS="true", GITHUB_WORKSPACE=str(repo), **extra)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(diagnostic, result.stderr)
        self.assertFalse((self.checkout / ".git/FETCH_HEAD").exists())
        self.assertFalse((self.seed / ".git/FETCH_HEAD").exists())

    def test_generator_cannot_smuggle_non_index_changes_into_commit(self):
        generator = self.seed / "scripts/index-library.py"
        generator.write_text(generator.read_text(encoding="ascii") +
                             "\nimport subprocess\n"
                             "from pathlib import Path\n"
                             "Path('notes/keep.txt').write_text('Unexpected rewrite.\\n')\n"
                             "subprocess.run(['git', 'add', 'notes/keep.txt'], check=True)\n"
                             "Path('library/science/index-manual.md').write_text('Wrong index.\\n')\n",
                             encoding="ascii")
        self.git(self.seed, "add", "scripts/index-library.py")
        self.git(self.seed, "commit", "-m", "fixture generator with unintended side effects")
        self.git(self.seed, "push", "origin", "HEAD:main")
        initial = self.git(self.remote, "rev-parse", "main")
        log = self.install_race_hook()

        result = self.cli(GITHUB_ACTIONS="true", GITHUB_WORKSPACE=str(self.checkout))

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("non-index", result.stderr)
        self.assertIn("notes/keep.txt", result.stderr)
        self.assertIn("library/science/index-manual.md", result.stderr)
        self.assertFalse(log.exists())
        self.assertEqual(self.git(self.remote, "rev-parse", "main"), initial)
        self.assertEqual((self.checkout / "notes/keep.txt").read_text(), "Unrelated data.\n")
        self.assertEqual(self.git(self.checkout, "status", "--porcelain"), "")
        self.assertEqual(len(self.git(self.checkout, "worktree", "list").splitlines()), 1)

    def test_invalid_attempt_limits_fail_before_fetch(self):
        for limit in (0, -1, 6):
            with self.subTest(limit=limit):
                result = self.cli(attempts=limit, GITHUB_ACTIONS="true",
                                  GITHUB_WORKSPACE=str(self.checkout))
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("attempts must be between 1 and 5", result.stderr)
                self.assertFalse((self.checkout / ".git/FETCH_HEAD").exists())

    def test_retry_exhaustion_is_bounded_and_leaves_remote_writers_intact(self):
        log = self.install_race_hook(always=True)
        initial = self.git(self.checkout, "rev-parse", "HEAD")
        limit = 2

        result = self.cli(attempts=limit, GITHUB_ACTIONS="true",
                          GITHUB_WORKSPACE=str(self.checkout))

        self.assertNotEqual(result.returncode, 0)
        self.assertIn(f"publication failed after {limit} attempts", result.stderr)
        attempts = [json.loads(line) for line in log.read_text().splitlines()]
        self.assertEqual(len(attempts), limit)
        self.assertIn("racer-1.md", attempts[1]["index"])
        self.assertNotIn("alpha.md", attempts[1]["index"])
        self.assertEqual(self.git(self.remote, "rev-parse", "main"),
                         self.git(self.seed, "rev-parse", "HEAD"))
        self.assertEqual(int(self.git(self.remote, "rev-list", "--count", f"{initial}..main")), limit)
        self.assertEqual(self.git(self.remote, "show", "main:notes/keep.txt"),
                         f"Concurrent data {limit}.")
        self.assertNotIn("library/index-library.md", self.git(
            self.remote, "ls-tree", "-r", "--name-only", "main").splitlines())
        self.assertEqual(self.git(self.checkout, "rev-parse", "HEAD"), initial)
        self.assertEqual(self.git(self.checkout, "status", "--porcelain"), "")
        self.assertEqual(len(self.git(self.checkout, "worktree", "list").splitlines()), 1)

    def test_rejected_push_regenerates_from_new_remote_tree(self):
        log = self.install_race_hook()
        initial = self.git(self.checkout, "rev-parse", "HEAD")

        result = self.cli(GITHUB_ACTIONS="true", GITHUB_WORKSPACE=str(self.checkout))

        self.assertEqual(result.returncode, 0, result.stderr)
        attempts = [json.loads(line) for line in log.read_text().splitlines()]
        self.assertEqual(len(attempts), 2)
        self.assertIn("[Alpha](alpha.md)", attempts[0]["index"])
        self.assertNotIn("racer-1.md", attempts[0]["index"])
        self.assertNotIn("alpha.md", attempts[1]["index"])
        self.assertIn("[Racer 1](racer-1.md)", attempts[1]["index"])
        self.assertEqual(attempts[0]["parent"], initial)
        self.assertEqual(attempts[1]["parent"], self.git(self.seed, "rev-parse", "HEAD"))
        self.assertEqual(self.git(self.remote, "rev-parse", "main"), attempts[1]["head"])
        self.assertEqual(self.git(self.remote, "rev-list", "--count", f"{initial}..main"), "2")
        self.assertEqual(self.git(self.remote, "show", "main:notes/keep.txt"), "Concurrent data 1.")
        self.assertEqual(self.git(self.checkout, "rev-parse", "HEAD"), initial)
        self.assertEqual(self.git(self.checkout, "status", "--porcelain"), "")
        self.assertEqual(len(self.git(self.checkout, "worktree", "list").splitlines()), 1)

    def test_byte_identical_generation_is_success_without_a_commit(self):
        # A deliberately deterministic fixture generator avoids the real
        # generator's minute-resolution timestamp making this test clock-bound.
        self.write(self.seed, "scripts/index-library.py",
                   "from pathlib import Path\n"
                   "root = Path(__file__).resolve().parents[1]\n"
                   "for relative in ('library/index-library.md', "
                   "'library/science/index-science.md'):\n"
                   "    (root / relative).write_text('Stable index.\\n', encoding='ascii')\n")
        for relative in ("library/index-library.md", "library/science/index-science.md"):
            self.write(self.seed, relative, "Stable index.\n")
        self.git(self.seed, "add", ".")
        self.git(self.seed, "commit", "-m", "already current deterministic indexes")
        self.git(self.seed, "push", "origin", "HEAD:main")
        initial = self.git(self.remote, "rev-parse", "main")

        result = self.cli(GITHUB_ACTIONS="true", GITHUB_WORKSPACE=str(self.checkout))

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("No index changes", result.stdout)
        self.assertFalse(self.publisher().publish(self.checkout))
        self.assertEqual(self.git(self.remote, "rev-parse", "main"), initial)
        self.assertEqual(self.git(self.checkout, "status", "--porcelain"), "")
        self.assertEqual(len(self.git(self.checkout, "worktree", "list").splitlines()), 1)

    def test_initial_dirty_checkout_is_refused_without_mutation(self):
        initial = self.git(self.remote, "rev-parse", "main")
        for kind in ("unstaged", "staged", "untracked"):
            with self.subTest(kind=kind):
                relative = "notes/new.txt" if kind == "untracked" else "notes/keep.txt"
                path = self.write(self.checkout, relative, "Unpublished user data.\n")
                if kind == "staged":
                    self.git(self.checkout, "add", "--", relative)
                before = self.git(self.checkout, "status", "--porcelain=v1")
                result = self.cli(GITHUB_ACTIONS="true", GITHUB_WORKSPACE=str(self.checkout))
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("dirty", result.stderr)
                self.assertEqual(path.read_text(), "Unpublished user data.\n")
                self.assertEqual(self.git(self.checkout, "status", "--porcelain=v1"), before)
                self.assertEqual(self.git(self.remote, "rev-parse", "main"), initial)
                self.assertFalse((self.checkout / ".git/FETCH_HEAD").exists())
                if kind == "untracked":
                    path.unlink()
                else:
                    self.git(self.checkout, "restore", "--staged", "--worktree", "--", relative)

    def test_cli_publishes_only_indexes_from_latest_remote_tree(self):
        self.write(self.checkout, ".git/info/exclude", "/notes/ignored.txt\n")
        self.write(self.checkout, "notes/ignored.txt", "Ignored local data.\n")
        self.write(self.checkout, "notes/local.txt", "Local-only committed data.\n")
        self.git(self.checkout, "add", "notes/local.txt")
        self.git(self.checkout, "commit", "-m", "local-only fixture commit")
        original_head = self.git(self.checkout, "rev-parse", "HEAD")
        self.write(self.seed, "library/science/beta.md", "# Beta\n\nLatest topic.\n")
        self.write(self.seed, "notes/keep.txt", "Concurrent unrelated data.\n")
        self.git(self.seed, "add", ".")
        self.git(self.seed, "commit", "-m", "remote advanced before publication")
        self.git(self.seed, "push", "origin", "HEAD:main")
        latest = self.git(self.remote, "rev-parse", "main")

        result = self.cli(GITHUB_ACTIONS="true", GITHUB_WORKSPACE=str(self.checkout))

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotEqual(self.git(self.remote, "rev-parse", "main"), latest)
        self.assertEqual(self.git(self.remote, "rev-parse", "main^"), latest)
        self.assertEqual(set(self.git(self.remote, "diff-tree", "--no-commit-id",
                                      "--name-only", "-r", "main").splitlines()), {
            "library/index-library.md", "library/science/index-science.md",
        })
        self.assertIn("[Beta](beta.md)", self.git(
            self.remote, "show", "main:library/science/index-science.md"))
        self.assertEqual(self.git(self.remote, "show", "main:notes/keep.txt"),
                         "Concurrent unrelated data.")
        self.assertEqual(self.git(self.remote, "show", "main:library/science/index-manual.md"),
                         "Hand-maintained.")
        self.assertEqual(self.git(self.remote, "show", "-s", "--format=%an|%ae|%cn|%ce", "main"),
                         "Library Index Bot|library-index@suggi-workspace.dev|"
                         "Library Index Bot|library-index@suggi-workspace.dev")
        self.assertIn("auto-regenerate indexes", self.git(
            self.remote, "show", "-s", "--format=%s", "main"))
        self.assertEqual(self.git(self.checkout, "rev-parse", "HEAD"), original_head)
        self.assertEqual((self.checkout / "notes/local.txt").read_text(),
                         "Local-only committed data.\n")
        self.assertEqual((self.checkout / "notes/ignored.txt").read_text(), "Ignored local data.\n")
        self.assertEqual(self.git(self.checkout, "status", "--porcelain"), "")
        self.assertEqual(len(self.git(self.checkout, "worktree", "list").splitlines()), 1)

    def test_cli_rejects_non_ci_or_wrong_workspace_before_publication(self):
        initial = self.git(self.remote, "rev-parse", "main")
        cases = [
            ({}, self.checkout, "GITHUB_ACTIONS=true"),
            ({"GITHUB_ACTIONS": "false"}, self.checkout, "GITHUB_ACTIONS=true"),
            ({"GITHUB_ACTIONS": "true"}, self.checkout, "GITHUB_WORKSPACE"),
            ({"GITHUB_ACTIONS": "true", "GITHUB_WORKSPACE": str(self.seed)},
             self.checkout, "GITHUB_WORKSPACE"),
            ({"GITHUB_ACTIONS": "true", "GITHUB_WORKSPACE": "/srv/disallowed-index-fixture"},
             Path("/srv/disallowed-index-fixture"), "/srv"),
        ]
        for env, repo, diagnostic in cases:
            with self.subTest(env=env, repo=repo):
                result = self.cli(repo, **env)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(diagnostic, result.stderr)
        self.assertEqual(self.git(self.remote, "rev-parse", "main"), initial)
        self.assertEqual(self.git(self.checkout, "status", "--porcelain"), "")


class IndexWorkflowTests(unittest.TestCase):
    def test_workflow_tests_before_guarded_publisher_and_keeps_loop_controls(self):
        workflow = (SCRIPTS.parent / ".github/workflows/library-index.yml").read_text(encoding="ascii")
        tests = "python3 -B -m unittest discover -s scripts/tests -p 'test_library*.py'"
        publish = 'python3 -B scripts/library-index-publish.py --repo "$GITHUB_WORKSPACE" --attempts 3'
        self.assertIn(tests, workflow)
        self.assertIn(publish, workflow)
        self.assertLess(workflow.index(tests), workflow.index(publish))
        for trigger in ("library/**", "scripts/index-library.py", "scripts/library-index-publish.py", "scripts/library-publish.py",
                        "scripts/tests/test_library*.py", ".github/workflows/library-index.yml"):
            self.assertIn(f"- '{trigger}'", workflow)
        self.assertIn("group: library-index-${{ github.ref }}", workflow)
        self.assertIn("cancel-in-progress: true", workflow)
        self.assertIn("!contains(github.event.head_commit.message, 'auto-regenerate indexes')", workflow)
        self.assertIn("ref: main", workflow)
        self.assertNotIn("git push", workflow)


if __name__ == "__main__":
    unittest.main()
