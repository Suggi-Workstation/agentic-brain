"""Generator checks use disposable libraries, never the live indexes."""

from contextlib import redirect_stdout
from datetime import date, datetime, timezone
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest import mock


SCRIPTS = Path(__file__).resolve().parents[1]


class LibraryIndexTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="library-index-generator-test-")
        self.root = Path(self.temp.name)
        self.library = self.root / "library"
        self.library.mkdir()
        spec = importlib.util.spec_from_file_location("index_under_test", SCRIPTS / "index-library.py")
        assert spec is not None and spec.loader is not None
        self.index = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.index)
        setattr(self.index, "LIBRARY_DIR", str(self.library))

    def tearDown(self):
        self.temp.cleanup()
        self.assertFalse(self.root.exists())

    def write(self, relative, text):
        path = self.library / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="ascii")
        return path

    def generate(self, when):
        with mock.patch.object(self.index, "datetime") as clock, redirect_stdout(io.StringIO()):
            clock.now.return_value = when
            self.index.main()
        return (self.library / "index-library.md").read_text(encoding="ascii")

    def test_master_counts_reviewed_and_overdue_without_changing_domain_stamps(self):
        self.write("science/anchor-science.md", "# Science\n\n## Anchor\n\nUnchanged description.\n")
        self.write("science/never.md", "---\nname: never\n---\n# Never\n\nNever reviewed.\n")
        self.write("science/current.md", "---\nreviewed: 2026-09-14\n---\n# Current\n\nCurrent topic.\n")
        self.write("science/due.md", "---\nreviewed: 2026-03-14\n---\n# Due\n\nDue topic.\n")
        master = self.generate(datetime(2026, 9, 14, tzinfo=timezone.utc))
        self.assertIn("| Domain | Topics | Reviewed | Description |", master)
        self.assertIn("| [science](science/index-science.md) | 3 | 2 (1 overdue) | Unchanged description. |", master)
        domain = (self.library / "science/index-science.md").read_text()
        self.assertIn("-- [reviewed: never] -- Never reviewed.", domain)
        self.assertIn("-- [reviewed: 2026-09-14] -- Current topic.", domain)
        self.assertIn("-- [reviewed: 2026-03-14] -- Due topic.", domain)

    def test_invalid_review_metadata_fails_before_any_index_write(self):
        master = self.write("index-library.md", "Previous master.\n")
        domain = self.write("science/index-science.md", "Previous domain.\n")
        for metadata in (
                "reviewed: ", "reviewed: never", "reviewed: 2026-02-30",
                "reviewed: 2026-09-15", "reviewed: 20260314", "reviewed: 2026-W11-6",
                "reviewed: 2026-09-14\nreviewed: 2026-03-14",
                "note: " + "x" * 2500 + "\nreviewed: 2999-01-01"):
            with self.subTest(metadata=metadata[:70]):
                self.write("science/invalid.md", f"---\n{metadata}\n---\n# Invalid\n")
                with self.assertRaisesRegex(ValueError, "invalid.md"):
                    self.generate(datetime(2026, 9, 14, tzinfo=timezone.utc))
                self.assertEqual(master.read_text(), "Previous master.\n")
                self.assertEqual(domain.read_text(), "Previous domain.\n")

    def test_complete_frontmatter_is_read_and_body_dates_are_not_metadata(self):
        self.write("science/long.md", "---\nnote: " + "x" * 2500 +
                   "\nreviewed: '2026-09-14'\n---\n# Long\n\nA topic.\n")
        self.write("science/body.md", "---\nname: body\n---\n# Body\n\nreviewed: 2026-09-14\n")
        master = self.generate(datetime(2026, 9, 14, tzinfo=timezone.utc))
        self.assertIn("| 2 | 1 (0 overdue) |", master)
        self.assertIn("[Long](long.md)", (self.library / "science/index-science.md").read_text())

    def test_calendar_boundaries_match_existing_review_eligibility(self):
        spec = importlib.util.spec_from_file_location("review_publisher", SCRIPTS / "library-publish.py")
        assert spec is not None and spec.loader is not None
        publisher = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(publisher)
        for today, stamp in (
                (date(2026, 9, 14), "2026-03-14"), (date(2026, 9, 14), "2026-03-15"),
                (date(2024, 8, 31), "2024-02-29"), (date(2024, 8, 31), "2024-03-01"),
                (date(2025, 8, 31), "2025-02-28"), (date(2025, 8, 31), "2025-03-01"),
                (date(2026, 1, 31), "2025-07-31"), (date(2026, 1, 31), "2025-08-01"),
                (date(2026, 3, 31), "2025-09-30"), (date(2026, 3, 31), "2025-10-01"),
                (date(2026, 9, 14), '"2026-03-14"')):
            with self.subTest(today=today, stamp=stamp):
                due = publisher.review_due(f"---\nreviewed: {stamp}\n---\n", today)
                self.assertEqual(self.index.count_reviews([("topic.md", "Topic", "", stamp)], today),
                                 (1, int(due)))

    def test_clock_only_refresh_is_stable_but_crossing_cutoff_updates_index(self):
        self.write("science/topic.md", "---\nreviewed: 2026-03-14\n---\n# Topic\n\nA topic.\n")
        first = self.generate(datetime(2026, 9, 12, tzinfo=timezone.utc))
        domain = (self.library / "science/index-science.md").read_bytes()
        second = self.generate(datetime(2026, 9, 13, tzinfo=timezone.utc))
        self.assertEqual(second, first)
        third = self.generate(datetime(2026, 9, 14, tzinfo=timezone.utc))
        self.assertIn("1 (0 overdue)", first)
        self.assertIn("1 (1 overdue)", third)
        self.assertIn("<!-- Regenerated 2026-09-14 00:00 UTC -->", third)
        self.assertEqual((self.library / "science/index-science.md").read_bytes(), domain)


if __name__ == "__main__":
    unittest.main()
