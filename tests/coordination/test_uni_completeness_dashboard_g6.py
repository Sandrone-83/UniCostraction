import json
import unittest
from pathlib import Path

from tools.uni_completeness_dashboard_g6 import build_dashboard


ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = ROOT / "docs" / "coordination" / "UNI_COMPLETENESS_DASHBOARD_G6.json"


class UniCompletenessDashboardG6Test(unittest.TestCase):
    def test_fixture_keeps_observed_cards_unmatched_and_pending_separate(self) -> None:
        root = Path(__file__).parent / "fixtures" / "uni_pack_exam_map_g4"
        report = build_dashboard(root)

        self.assertEqual(report["observed"]["packs"], 4)
        self.assertEqual(report["observed"]["schede"]["jsonl_rows"], 0)
        self.assertEqual(report["observed"]["exams"], 5)
        self.assertEqual(report["mapping"]["observed_pair_count"], 4)
        self.assertEqual(report["unmatched"]["pack_count"], 1)
        self.assertEqual(report["unmatched"]["exam_count"], 2)
        self.assertEqual(report["pending_human_review"]["pending_count"], 3)
        self.assertEqual(report["pending_human_review"]["status_counts"]["decided"], 0)
        self.assertFalse(report["scope"]["content_modified"])

    def test_tracked_report_is_deterministic_and_matches_g5_boundaries(self) -> None:
        first = build_dashboard(ROOT)
        second = build_dashboard(ROOT)
        tracked = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

        self.assertEqual(first, second)
        self.assertEqual(tracked, first)
        self.assertEqual(first["observed"]["packs"], 71)
        self.assertEqual(first["observed"]["schede"]["jsonl_rows"], 963)
        self.assertEqual(first["observed"]["exams"], 73)
        self.assertEqual(first["observed"]["exam_pack_pairs"], 73)
        self.assertEqual(first["mapping"]["pair_relation_counts"], {"exact_name": 14, "alias_observed": 59})
        self.assertEqual(first["unmatched"], {"pack_count": 0, "exam_count": 2, "total_items": 2})
        self.assertEqual(first["pending_human_review"]["pending_count"], 6)
        self.assertEqual(first["pending_human_review"]["status_counts"]["decided"], 0)
        self.assertEqual(first["pack_card_completeness"]["packs_with_matching_declared_observed_schede"], 71)

    def test_card_rows_are_observed_without_promoting_invalid_or_missing_data(self) -> None:
        root = Path(__file__).parent / "fixtures" / "uni_completeness_g6"
        report = build_dashboard(root)

        self.assertEqual(report["observed"]["schede"]["jsonl_rows"], 2)
        self.assertEqual(report["observed"]["schede"]["malformed_json_rows"], 1)
        self.assertEqual(report["observed"]["schede"]["declared_total"], 2)
        self.assertEqual(report["pack_card_completeness"]["status_counts"]["jsonl_invalid"], 1)
        self.assertEqual(report["pending_human_review"]["pending_count"], 0)


if __name__ == "__main__":
    unittest.main()
