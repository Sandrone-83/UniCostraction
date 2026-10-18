import json
import unittest
from pathlib import Path

from tools.uni_release_readiness_g7 import build_release_readiness


ROOT = Path(__file__).resolve().parents[2]
G6_REPORT = ROOT / "docs" / "coordination" / "UNI_COMPLETENESS_DASHBOARD_G6.json"
G5_DOC = ROOT / "docs" / "coordination" / "UNI_PACK_EXAM_REVIEW_G5.md"


class UniReleaseReadinessG7Test(unittest.TestCase):
    def test_current_inventory_is_coherent_but_blocked_by_open_review(self) -> None:
        report = build_release_readiness(ROOT)

        self.assertEqual(report["status"], "blocked")
        self.assertFalse(report["release_ready"])
        self.assertEqual(report["review_state"], "pending")
        self.assertEqual(report["mismatch_count"], 0)
        self.assertEqual(report["open_review"], {
            "pending_g5": 6,
            "unmatched_legacy": 2,
            "automatic_resolution": False,
        })
        self.assertEqual(report["observed_snapshot"]["dashboard"]["observed.packs"], 71)
        self.assertEqual(report["observed_snapshot"]["dashboard"]["observed.schede.jsonl_rows"], 963)
        self.assertEqual(report["observed_snapshot"]["dashboard"]["observed.exams"], 73)
        self.assertEqual(report["observed_snapshot"]["dashboard"]["observed.exam_pack_pairs"], 73)
        self.assertEqual(report["observed_snapshot"]["review"]["counts.pending"], 6)
        self.assertEqual(report["observed_snapshot"]["review"]["counts.legacy_unmatched_exam"], 2)

    def test_report_drift_is_explicit_and_does_not_close_review_items(self) -> None:
        payload = json.loads(G6_REPORT.read_text(encoding="utf-8"))
        payload["observed"]["packs"] = 70
        report = build_release_readiness(ROOT, dashboard_report=payload)

        self.assertEqual(report["status"], "blocked")
        self.assertEqual(report["open_review"]["pending_g5"], 6)
        self.assertEqual(report["open_review"]["unmatched_legacy"], 2)
        mismatch = next(
            item
            for item in report["mismatches"]
            if item["check_id"] == "tracked_dashboard_matches_recomputed.observed.packs"
        )
        self.assertEqual(mismatch["expected"], 71)
        self.assertEqual(mismatch["observed"], 70)
        self.assertIn("coherence_mismatch", report["blocking_conditions"][-1])

    def test_documentation_marker_drift_is_explicit(self) -> None:
        drifted_g5_doc = G5_DOC.read_text(encoding="utf-8").replace(
            "queue_items=6; pending=6; legacy_unmatched=2",
            "queue_items=6; pending=5; legacy_unmatched=2",
        )
        report = build_release_readiness(ROOT, review_doc=drifted_g5_doc)

        mismatch = next(
            item
            for item in report["mismatches"]
            if item["check_id"] == "review_documentation.pending"
        )
        self.assertEqual(mismatch["expected"], 6)
        self.assertEqual(mismatch["observed"], 5)

    def test_legacy_queue_safety_remains_pending_and_unmatched(self) -> None:
        report = build_release_readiness(ROOT)
        safety = {
            item["check_id"]: item["status"]
            for item in report["checks"]
            if item["check_id"].startswith("review_safety.")
        }

        self.assertEqual(
            safety,
            {
                "review_safety.all_items_pending": "pass",
                "review_safety.all_decisions_null": "pass",
                "review_safety.legacy_items_have_no_candidates": "pass",
                "review_safety.legacy_items_pending": "pass",
            },
        )
        self.assertEqual(report["scope"]["pending_or_unmatched_closed"], False)


if __name__ == "__main__":
    unittest.main()
