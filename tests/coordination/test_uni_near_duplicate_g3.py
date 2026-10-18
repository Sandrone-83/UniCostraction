import json
import unittest
from pathlib import Path

from tools.uni_near_duplicate_g3 import build_report


ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = ROOT / "docs" / "coordination" / "UNI_NEAR_DUPLICATE_G3.json"


class UniNearDuplicateG3Test(unittest.TestCase):
    def test_bounded_report_is_deterministic_and_every_candidate_has_evidence(self) -> None:
        root = Path(__file__).parent / "fixtures" / "uni_near_duplicate_g3"
        first = build_report(root)
        second = build_report(root)

        self.assertEqual(first, second)
        self.assertEqual(first["schema_version"], "g3.v1")
        self.assertTrue(first["scope"]["bounded"])
        self.assertEqual(first["scope"]["deduplicated"], False)
        self.assertEqual(first["interpretation"]["human_review_required"], True)

        candidates = first["interpretation"]["possible_near_duplicate_groups"]
        signals = {candidate["signal"] for candidate in candidates}
        self.assertIn("normalized_text_digest_match", signals)
        self.assertIn("normalized_token_digest_match", signals)
        self.assertIn("structured_digest_match", signals)
        self.assertIn("title_match", signals)
        self.assertIn("identifier_match", signals)
        self.assertTrue(all(candidate["review_status"] == "pending_human_review" for candidate in candidates))
        self.assertTrue(all(candidate["duplicate_confirmed"] is False for candidate in candidates))
        self.assertTrue(all(candidate["evidence"] for candidate in candidates))
        self.assertTrue(all(len(candidate["paths"]) > 1 for candidate in candidates))
        self.assertTrue(all(candidate["candidate_id"].startswith("G3-") for candidate in candidates))
        json.dumps(first, ensure_ascii=False)

    def test_scope_excludes_g1_fixture_directories_and_non_target_files(self) -> None:
        root = Path(__file__).parent / "fixtures" / "uni_near_duplicate_g3"
        report = build_report(root)

        paths = [entry["path"] for entry in report["evidence"]["files"]]
        self.assertNotIn("tests/hidden/COURSE.yaml", paths)
        self.assertNotIn("work/README.md", paths)
        self.assertNotIn("notes.txt", paths)
        self.assertTrue(paths)

    def test_tracked_report_matches_the_selected_checkout(self) -> None:
        generated = build_report(ROOT)
        tracked = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(tracked, generated)
        candidates = generated["interpretation"]["possible_near_duplicate_groups"]
        self.assertTrue(all(candidate["evidence"] for candidate in candidates))
        self.assertTrue(all(candidate["duplicate_confirmed"] is False for candidate in candidates))


if __name__ == "__main__":
    unittest.main()
