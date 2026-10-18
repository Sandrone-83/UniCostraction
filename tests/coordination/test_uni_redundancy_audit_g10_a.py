import json
import unittest
from pathlib import Path

from tools.uni_redundancy_audit_g10_a import build_report


class UniRedundancyAuditG10ATest(unittest.TestCase):
    def test_fixture_is_deterministic_and_separates_exact_review_and_distinct(self) -> None:
        root = Path(__file__).parent / "fixtures" / "uni_redundancy_g10_a"
        first = build_report(root)
        second = build_report(root)

        self.assertEqual(first, second)
        self.assertEqual(first["schema_version"], "g10a.v1")
        self.assertFalse(first["scope"]["answers_read"])
        self.assertFalse(first["scope"]["automatic_deduplication"])
        self.assertEqual(first["similarity"]["metric"], "token_set_jaccard")

        self.assertEqual(first["evidence"]["file_counts_by_source_group"], {"cards": 2, "public_exams": 2})
        self.assertEqual(first["evidence"]["unit_counts_by_source_group"], {"cards": 3, "public_exams": 4})
        self.assertEqual(len(first["results"]["duplicate_exact"]), 2)
        self.assertTrue(first["results"]["candidate_review"])
        self.assertTrue(first["results"]["distinct"]["unit_ids"])

        exact_ids = {
            unit_id
            for group in first["results"]["duplicate_exact"]
            for unit_id in group["unit_ids"]
        }
        candidate_ids = {
            unit_id
            for item in first["results"]["candidate_review"]
            for unit_id in (item["left_unit_id"], item["right_unit_id"])
        }
        self.assertTrue(any(unit_id.startswith("card:") for unit_id in exact_ids))
        self.assertTrue(any(unit_id.startswith("exam:") for unit_id in exact_ids))
        self.assertTrue(all(item["score"] >= item["threshold"] for item in first["results"]["candidate_review"]))
        self.assertTrue(candidate_ids - exact_ids)
        self.assertTrue(all("question_body" not in unit for unit in first["evidence"]["units"]))

        exam_files = [item for item in first["evidence"]["files"] if item["source_group"] == "public_exams"]
        formats = {format_name for item in exam_files for format_name in item["question_formats"]}
        self.assertEqual(formats, {"standard_heading", "legacy_d_heading"})
        json.dumps(first, ensure_ascii=False)

    def test_tracked_report_matches_checkout_and_scope(self) -> None:
        root = Path(__file__).resolve().parents[2]
        report_path = root / "docs" / "coordination" / "UNI_REDUNDANCY_AUDIT_G10_A.json"
        generated = build_report(root)
        tracked = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertEqual(tracked, generated)
        self.assertEqual(generated["evidence"]["file_counts_by_source_group"], {"cards": 71, "public_exams": 73})
        self.assertEqual(generated["scope"]["included"], [
            "UNIVERSITA_EDILIZIA/**/schede/schede.jsonl",
            "UNIVERSITA_EDILIZIA/ESAMI/**/domande.md",
        ])
        self.assertFalse(generated["results"]["candidate_pairs_truncated"])


if __name__ == "__main__":
    unittest.main()
