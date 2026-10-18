"""G12-C decision-record and source/licence checklist QA.

Negative fixtures contain only field names plus ``None`` or ``placeholder``.
They never contain real answers, option letters, solutions, explanations,
responses, grades, or scores.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools.validate_public_qa_g10 import (
    ALLOWED_STATES,
    G12_ARTIFACT_PATHS,
    REPOSITORY_ROOT,
    _contract_issues,
    _text_structure_issues,
    forbidden_structure_issues,
    issues_for_file,
    validate_public_artifacts,
)


class DecisionRecordsG12Tests(unittest.TestCase):
    def test_g12_artifacts_are_metadata_only_and_separate(self) -> None:
        for relative_path in sorted(G12_ARTIFACT_PATHS):
            path = REPOSITORY_ROOT / relative_path
            self.assertTrue(path.is_file(), path)
            if path.suffix == ".json":
                payload = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual([], issues_for_file(path))
                contract_names = [
                    key for key in payload if key.endswith("_contract")
                ]
                self.assertEqual(1, len(contract_names), path)
                contract = payload[contract_names[0]]
                self.assertEqual("pending", contract["state"])
                self.assertEqual(ALLOWED_STATES, set(contract["allowed_states"]))
                self.assertEqual(
                    "separate", contract["answer_key_separation"]["status"]
                )
                self.assertFalse(contract["answer_key_separation"]["public"])

    def test_full_guard_includes_g12_artifacts_and_exam_payloads(self) -> None:
        self.assertEqual([], validate_public_artifacts())

    def test_non_null_decisions_require_evidence_ref(self) -> None:
        contract = {
            "limitations": ["placeholder"],
            "allowed_states": sorted(ALLOWED_STATES),
            "state": "pending",
            "answer_key_separation": {"status": "separate", "public": False},
        }
        missing_reference = {
            "redundancy_decision_contract": contract,
            "redundancy_decision_records": [
                {
                    "state": "pending",
                    "decision": "placeholder",
                    "reviewer": "placeholder",
                    "rationale": "placeholder",
                }
            ],
        }
        self.assertTrue(any("evidence_ref" in issue for issue in _contract_issues(missing_reference)))

        null_decision = {
            "redundancy_decision_contract": contract,
            "redundancy_decision_records": [
                {
                    "state": "pending",
                    "decision": None,
                    "evidence_ref": None,
                    "reviewer": "placeholder",
                    "rationale": "placeholder",
                }
            ],
        }
        self.assertEqual([], _contract_issues(null_decision))

    def test_reviewer_rationale_and_state_are_required(self) -> None:
        contract = {
            "limitations": ["placeholder"],
            "allowed_states": sorted(ALLOWED_STATES),
            "state": "pending",
            "answer_key_separation": {"status": "separate", "public": False},
        }
        payload = {
            "redundancy_decision_contract": contract,
            "redundancy_decision_records": [
                {
                    "decision": None,
                    "reviewer": "",
                    "rationale": None,
                }
            ],
        }
        findings = _contract_issues(payload)
        self.assertTrue(any("state" in issue for issue in findings))
        self.assertTrue(any("reviewer" in issue for issue in findings))
        self.assertTrue(any("rationale" in issue for issue in findings))

    def test_forbidden_fields_and_numeric_maps_are_rejected_with_safe_values(self) -> None:
        for fixture in (
            {"answer_key": None},
            {"correct option": "placeholder"},
            {"explanation": None},
            {"solution": "placeholder"},
            {"score": None},
            {"response": "placeholder"},
            {"grade": None},
            {"nested": {"correct_option": None}},
            {"1": None, "2": "placeholder", "3": None},
        ):
            with self.subTest(fixture=fixture):
                self.assertTrue(forbidden_structure_issues(fixture), fixture)

        for fixture in (
            "answer_key: None",
            "correct option: placeholder",
            "explanation: None",
            "solution: placeholder",
            "score: None",
            "response: placeholder",
            "grade: None",
            "1: None\n2: placeholder\n3: None",
        ):
            with self.subTest(fixture=fixture):
                self.assertTrue(_text_structure_issues(fixture), fixture)

    def test_report_declares_workflow_and_limits(self) -> None:
        report = (
            REPOSITORY_ROOT / "docs/coordination/UNI_QA_DECISION_RECORDS_G12.md"
        ).read_text(encoding="utf-8")
        for marker in (
            "decision records",
            "source/licence",
            "evidence_ref",
            "reviewer",
            "rationale",
            "answer key",
            "blocked",
            "pending",
            "open",
            "resolved",
            "None",
            "placeholder",
        ):
            self.assertIn(marker, report)


if __name__ == "__main__":
    unittest.main()
