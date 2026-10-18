"""G11-C integrated exam/report QA.

The negative fixtures contain only field names plus ``None`` or
``placeholder``.  They never contain real answers, option letters, solutions,
explanations, responses, grades, or scores.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools.validate_public_qa_g10 import (
    ALLOWED_STATES,
    EXPECTED_PUBLIC_EXAM_PAYLOAD_COUNT,
    G11_ARTIFACT_PATHS,
    REPOSITORY_ROOT,
    _contract_issues,
    _text_structure_issues,
    forbidden_structure_issues,
    issues_for_file,
    public_exam_payload_paths,
    validate_public_artifacts,
)


class IntegratedQAG11Tests(unittest.TestCase):
    def test_explicit_scan_covers_exactly_73_exam_payloads(self) -> None:
        payloads = public_exam_payload_paths()
        self.assertEqual(EXPECTED_PUBLIC_EXAM_PAYLOAD_COUNT, len(payloads))
        self.assertTrue(
            all(
                path.as_posix().startswith("UNIVERSITA_EDILIZIA/ESAMI/")
                and path.name == "domande.md"
                for path in payloads
            )
        )

    def test_integrated_artifacts_are_metadata_only_and_separate(self) -> None:
        for relative_path in sorted(G11_ARTIFACT_PATHS):
            path = REPOSITORY_ROOT / relative_path
            self.assertTrue(path.is_file(), path)
            if path.suffix == ".json":
                payload = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual([], issues_for_file(path))
                contract_names = [
                    key
                    for key in payload
                    if key.endswith("_contract") and key != "answer_key_separation"
                ]
                self.assertEqual(1, len(contract_names), path)
                contract = payload[contract_names[0]]
                self.assertEqual("pending", contract["state"])
                self.assertEqual(ALLOWED_STATES, set(contract["allowed_states"]))
                self.assertEqual("separate", contract["answer_key_separation"]["status"])
                self.assertFalse(contract["answer_key_separation"]["public"])

    def test_full_guard_includes_g11_artifacts_and_73_payloads(self) -> None:
        self.assertEqual([], validate_public_artifacts())

    def test_requested_forbidden_structures_are_rejected_with_safe_values(self) -> None:
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

    def test_g11_contract_requires_limits_states_and_separation(self) -> None:
        payload = {
            "candidate_review_contract": {
                "limitations": [],
                "allowed_states": ["placeholder"],
                "state": "placeholder",
                "answer_key_separation": {"status": "public", "public": True},
            }
        }
        findings = _contract_issues(payload)
        self.assertTrue(any("limitations" in issue for issue in findings))
        self.assertTrue(any("allowed_states" in issue for issue in findings))
        self.assertTrue(any("state" in issue for issue in findings))
        self.assertTrue(any("answer_key_separation.status" in issue for issue in findings))
        self.assertTrue(any("answer_key_separation.public" in issue for issue in findings))

    def test_integrated_report_declares_scope_and_limits(self) -> None:
        report = (
            REPOSITORY_ROOT / "docs/coordination/UNI_QA_INTEGRATED_G11.md"
        ).read_text(encoding="utf-8")
        for marker in (
            "73 payload",
            "candidate-review",
            "priority queues",
            "evidence/licenza",
            "Limiti",
            "chiave protetta resta separata",
        ):
            self.assertIn(marker, report)


if __name__ == "__main__":
    unittest.main()
