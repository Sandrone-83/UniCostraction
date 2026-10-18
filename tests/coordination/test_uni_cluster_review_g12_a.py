import copy
import json
import unittest
from pathlib import Path

from tools.uni_cluster_review_g12_a import (
    ALLOWED_DECISIONS,
    build_report,
    load_report,
    validate_review_report,
)


class UniClusterReviewG12ATest(unittest.TestCase):
    def _fixture_report(self) -> dict:
        path = Path(__file__).parent / "fixtures" / "uni_cluster_review_g12_a" / "priority.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def test_fixture_uses_null_placeholders_and_allowed_decisions(self) -> None:
        report = build_report(self._fixture_report(), expected_component_count=2)

        validate_review_report(report, expected_component_count=2)
        self.assertEqual(report["scope"]["initial_decision"], None)
        self.assertEqual(report["scope"]["allowed_decisions"], ALLOWED_DECISIONS)
        self.assertEqual(report["coverage"], {
            "component_count": 2,
            "pending_count": 2,
            "decided_count": 0,
            "all_decisions_null": True,
        })
        for item in report["review_queue"]:
            self.assertEqual(item["review"], {
                "decision": None,
                "evidence_ref": None,
                "reviewer": None,
                "rationale": None,
            })
        encoded = json.dumps(report, ensure_ascii=False)
        self.assertNotIn("answer_key", encoded.lower())
        self.assertNotIn("question_body", encoded)

    def test_build_is_deterministic(self) -> None:
        first = build_report(self._fixture_report(), expected_component_count=2)
        second = build_report(copy.deepcopy(self._fixture_report()), expected_component_count=2)
        self.assertEqual(first, second)
        self.assertEqual(
            [item["priority_rank"] for item in first["review_queue"]],
            [1, 2],
        )

    def test_non_null_decision_requires_evidence_reviewer_and_rationale(self) -> None:
        report = build_report(self._fixture_report(), expected_component_count=2)
        report["review_queue"][0]["review"] = {
            "decision": "merge_candidate",
            "evidence_ref": "docs/evidence/cluster-0001.md#review",
            "reviewer": "human-reviewer",
            "rationale": "Evidence is sufficient for a human merge candidate review.",
        }
        report["coverage"] = {
            "component_count": 2,
            "pending_count": 1,
            "decided_count": 1,
            "all_decisions_null": False,
        }
        validate_review_report(report, expected_component_count=2)

        for field in ("evidence_ref", "reviewer", "rationale"):
            invalid = copy.deepcopy(report)
            invalid["review_queue"][0]["review"][field] = None
            with self.assertRaises(ValueError):
                validate_review_report(invalid, expected_component_count=2)

        invalid_decision = copy.deepcopy(report)
        invalid_decision["review_queue"][0]["review"]["decision"] = "merge_now"
        with self.assertRaises(ValueError):
            validate_review_report(invalid_decision, expected_component_count=2)

    def test_tracked_contract_covers_85_components_without_exam_answers(self) -> None:
        root = Path(__file__).resolve().parents[2]
        input_path = root / "docs" / "coordination" / "UNI_REDUNDANCY_PRIORITY_G11_A.json"
        output_path = root / "docs" / "coordination" / "UNI_CLUSTER_REVIEW_G12_A.json"
        g11, input_sha256 = load_report(input_path)
        generated = build_report(
            g11,
            input_path="docs/coordination/UNI_REDUNDANCY_PRIORITY_G11_A.json",
            input_report_sha256=input_sha256,
        )
        tracked = json.loads(output_path.read_text(encoding="utf-8"))

        self.assertEqual(tracked, generated)
        self.assertEqual(generated["coverage"]["component_count"], 85)
        self.assertEqual(generated["coverage"]["pending_count"], 85)
        self.assertEqual(generated["coverage"]["decided_count"], 0)
        self.assertTrue(generated["coverage"]["all_decisions_null"])
        self.assertTrue(all(item["review"]["decision"] is None for item in generated["review_queue"]))
        self.assertFalse(generated["scope"]["automatic_card_modification"])
        self.assertFalse(generated["scope"]["automatic_exam_modification"])
        encoded = json.dumps(generated, ensure_ascii=False)
        self.assertNotIn("answer_key", encoded.lower())
        self.assertNotIn("question_body", encoded)


if __name__ == "__main__":
    unittest.main()
