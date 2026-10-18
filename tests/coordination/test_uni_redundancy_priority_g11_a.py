import copy
import json
import unittest
from pathlib import Path

from tools.uni_redundancy_audit_g10_a import build_report as build_g10_report
from tools.uni_redundancy_priority_g11_a import build_report, load_report


class UniRedundancyPriorityG11ATest(unittest.TestCase):
    def test_groups_only_connected_g10_pairs_and_preserves_every_pair(self) -> None:
        root = Path(__file__).parent / "fixtures" / "uni_redundancy_g10_a"
        g10 = build_g10_report(root)
        report = build_report(g10)

        self.assertEqual(report["schema_version"], "g11a.v1")
        self.assertEqual(report["input"]["candidate_pair_count"], len(g10["results"]["candidate_review"]))
        self.assertTrue(report["scope"]["relation_reused_without_recalculation"])
        self.assertFalse(report["scope"]["didactic_content_copied"])
        self.assertFalse(report["scope"]["automatic_deduplication"])

        source_pair_ids = sorted(
            pair["candidate_id"] for pair in g10["results"]["candidate_review"]
        )
        queued_pairs = [
            pair
            for component in report["results"]["queue"]
            for pair in component["pairs"]
        ]
        self.assertEqual(
            sorted(pair["candidate_id"] for pair in queued_pairs),
            source_pair_ids,
        )
        self.assertEqual(len(queued_pairs), len(source_pair_ids))
        self.assertEqual(
            len({pair["candidate_id"] for pair in queued_pairs}),
            len(queued_pairs),
        )
        self.assertTrue(all(component["human_review"]["required"] for component in report["results"]["queue"]))
        self.assertTrue(all(component["human_review"]["decision"] is None for component in report["results"]["queue"]))

    def test_priority_is_deterministic_and_coverage_is_explicit(self) -> None:
        root = Path(__file__).parent / "fixtures" / "uni_redundancy_g10_a"
        g10 = build_g10_report(root)
        first = build_report(g10)
        second = build_report(copy.deepcopy(g10))

        self.assertEqual(first, second)
        ranks = [component["priority_rank"] for component in first["results"]["queue"]]
        self.assertEqual(ranks, list(range(1, len(ranks) + 1)))
        for component in first["results"]["queue"]:
            key = component["priority_key"]
            coverage = component["coverage"]
            self.assertEqual(component["collision_count"], len(component["pairs"]))
            self.assertEqual(key["coverage_count"], coverage["pack_count"] + coverage["exam_count"])
            self.assertEqual(key["node_count"], len(component["unit_ids"]))
            self.assertEqual(component["source_group"], key["source_group"])
            self.assertTrue(set(component["unit_ids"]))
            self.assertFalse(set(component["coverage"]["source_paths"]) & set(component["unit_ids"]))

        # Both coverage dimensions are derived from G10 unit metadata, not
        # from didactic text.  The fixture keeps each exam component inside
        # one exam file, so exam coverage is explicit even when its count is 1.
        card_components = [
            component for component in first["results"]["queue"]
            if component["source_group"] == "cards"
        ]
        exam_components = [
            component for component in first["results"]["queue"]
            if component["source_group"] == "public_exams"
        ]
        self.assertTrue(card_components or exam_components)
        if card_components:
            self.assertTrue(all(component["coverage"]["pack_count"] >= 1 for component in card_components))
            self.assertTrue(all(component["coverage"]["exam_count"] == 0 for component in card_components))
        if exam_components:
            self.assertTrue(all(component["coverage"]["pack_count"] == 0 for component in exam_components))
            self.assertTrue(all(component["coverage"]["exam_count"] >= 1 for component in exam_components))

    def test_report_is_json_serializable_without_didactic_fields(self) -> None:
        root = Path(__file__).parent / "fixtures" / "uni_redundancy_g10_a"
        report = build_report(build_g10_report(root))
        encoded = json.dumps(report, ensure_ascii=False)
        self.assertNotIn("question_body", encoded)
        self.assertNotIn("card_text", encoded)
        self.assertNotIn("answer_key", encoded.lower())

    def test_tracked_report_matches_real_g10_input_and_has_303_pairs(self) -> None:
        root = Path(__file__).resolve().parents[2]
        input_path = root / "docs" / "coordination" / "UNI_REDUNDANCY_AUDIT_G10_A.json"
        output_path = root / "docs" / "coordination" / "UNI_REDUNDANCY_PRIORITY_G11_A.json"
        g10, input_sha256 = load_report(input_path)
        generated = build_report(
            g10,
            input_path="docs/coordination/UNI_REDUNDANCY_AUDIT_G10_A.json",
            input_report_sha256=input_sha256,
        )
        tracked = json.loads(output_path.read_text(encoding="utf-8"))
        self.assertEqual(tracked, generated)
        self.assertEqual(generated["results"]["candidate_pair_count"], 303)
        self.assertEqual(
            sum(component["collision_count"] for component in generated["results"]["queue"]),
            303,
        )


if __name__ == "__main__":
    unittest.main()
