import json
import unittest
from pathlib import Path

from tools.uni_pack_exam_review_g5 import build_review_report


ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = ROOT / "docs" / "coordination" / "UNI_PACK_EXAM_REVIEW_G5.json"


class UniPackExamReviewG5Test(unittest.TestCase):
    def test_fixture_queue_is_deterministic_and_keeps_uncertainty(self) -> None:
        root = Path(__file__).parent / "fixtures" / "uni_pack_exam_map_g4"
        first = build_review_report(root)
        second = build_review_report(root)

        self.assertEqual(first, second)
        self.assertEqual(first["schema_version"], "g5.v1")
        self.assertFalse(first["method"]["semantic_inference"])
        self.assertEqual(first["counts"], {
            "queue_items": 3,
            "ambiguous_pack": 1,
            "ambiguous_exam": 1,
            "legacy_unmatched_exam": 1,
            "pending": 3,
        })
        self.assertEqual(
            [item["queue_id"] for item in first["review_queue"]],
            ["pack:SHARED_ALPHA_PACK", "exam:SHARED", "exam:LEGACY"],
        )
        self.assertNotIn("exam:EXAM_ONLY", [item["queue_id"] for item in first["review_queue"]])
        for item in first["review_queue"]:
            self.assertEqual(item["review_status"], "pending")
            self.assertIsNone(item["decision"]["selected_id"])
            self.assertTrue(item["uncertainty"])

    def test_tracked_report_matches_selected_checkout_and_target_scope(self) -> None:
        generated = build_review_report(ROOT)
        tracked = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(tracked, generated)
        self.assertEqual(generated["counts"], {
            "queue_items": 6,
            "ambiguous_pack": 2,
            "ambiguous_exam": 2,
            "legacy_unmatched_exam": 2,
            "pending": 6,
        })
        self.assertEqual(
            [item["queue_id"] for item in generated["review_queue"]],
            [
                "pack:AEROPORTI_E_INFRASTRUTTURE_DI_VOLO_PACK",
                "pack:FORMULARIO_STRUTTURE_PACK",
                "exam:INFRASTRUTTURE",
                "exam:STRUTTURE",
                "exam:IMPIANTI_FV_EOLICO",
                "exam:MATERIALEDILE",
            ],
        )
        legacy = [
            item for item in generated["review_queue"] if item["uncertainty"] == "unmatched_legacy_domain"
        ]
        self.assertEqual(len(legacy), 2)
        self.assertTrue(all(item["legacy_observed"] for item in legacy))
        self.assertTrue(all(item["candidate_ids"] == [] for item in legacy))
        self.assertTrue(all(item["decision"]["outcome"] is None for item in generated["review_queue"]))


if __name__ == "__main__":
    unittest.main()
