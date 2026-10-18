"""G16-C QA for human workflow review canonicals."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools.validate_full_checkout_g13 import (
    ALLOWED_STATES,
    G16_REQUIRED_RECORD_FIELDS,
    REPOSITORY_ROOT,
    _contract_issues,
    forbidden_structure_issues,
    report_state_count_issues,
    validate_checkout,
)


G16_ARTIFACTS = (
    Path("docs/coordination/UNI_TEMPLATE_IMPORT_EXPORT_REVIEW_G16.json"),
    Path("docs/coordination/UNI_REPORT_PACK_SOURCE_REVIEW_G16.json"),
)


class HumanWorkflowGuardG16Tests(unittest.TestCase):
    def test_initial_canonicals_require_null_decisions_and_review_metadata(self) -> None:
        for relative_path in G16_ARTIFACTS:
            payload = json.loads((REPOSITORY_ROOT / relative_path).read_text(encoding="utf-8"))
            contract_name = next(key for key in payload if key.endswith("_contract"))
            contract = payload[contract_name]
            collection_name = next(key for key in payload if key != contract_name)
            self.assertEqual(ALLOWED_STATES, set(contract["allowed_states"]))
            self.assertTrue(G16_REQUIRED_RECORD_FIELDS <= set(contract["record_requirements"]))
            for record in payload[collection_name]:
                self.assertIsNone(record["decision"])
                for field in G16_REQUIRED_RECORD_FIELDS - {"decision"}:
                    self.assertIsInstance(record[field], str)
                    self.assertTrue(record[field].strip())

    def test_full_checkout_guard_includes_g16_workflows(self) -> None:
        self.assertEqual([], report_state_count_issues(REPOSITORY_ROOT))
        self.assertEqual([], validate_checkout(REPOSITORY_ROOT))

    def test_decisions_need_resolved_state_and_review_metadata(self) -> None:
        contract = {
            "state": "pending",
            "allowed_states": sorted(ALLOWED_STATES),
            "record_requirements": sorted(G16_REQUIRED_RECORD_FIELDS),
            "limitations": ["placeholder"],
            "answer_key_separation": {"status": "separate", "public": False},
        }
        payload = {
            "template_import_export_review_contract": contract,
            "template_import_export_reviews": [
                {
                    "review_id": "placeholder",
                    "state": "pending",
                    "evidence_ref": "placeholder",
                    "reviewer": "placeholder",
                    "rationale": "placeholder",
                    "decision": "placeholder",
                }
            ],
        }
        findings = _contract_issues(payload)
        self.assertTrue(any("resolved state" in issue for issue in findings))

        payload["template_import_export_reviews"][0]["state"] = "resolved"
        payload["template_import_export_reviews"][0]["reviewer"] = ""
        payload["template_import_export_reviews"][0]["rationale"] = ""
        self.assertTrue(any("reviewer" in issue for issue in _contract_issues(payload)))
        self.assertTrue(any("rationale" in issue for issue in _contract_issues(payload)))

    def test_g16_missing_evidence_and_decision_are_rejected(self) -> None:
        contract = {
            "state": "pending",
            "allowed_states": sorted(ALLOWED_STATES),
            "record_requirements": sorted(G16_REQUIRED_RECORD_FIELDS),
            "limitations": ["placeholder"],
        }
        payload = {
            "report_pack_source_review_contract": contract,
            "report_pack_source_reviews": [{"state": "pending"}],
        }
        findings = _contract_issues(payload)
        self.assertTrue(any("evidence_ref" in issue for issue in findings))
        self.assertTrue(any("reviewer" in issue for issue in findings))
        self.assertTrue(any("rationale" in issue for issue in findings))
        self.assertTrue(any("decision" in issue for issue in findings))

    def test_protected_answer_and_numeric_shapes_remain_rejected(self) -> None:
        for payload in (
            {"answer_key": None},
            {"response": "placeholder"},
            {"grade": None},
            {"solution": "placeholder"},
            {"score": None},
            {"correct option": "placeholder"},
            {"1": None, "2": "placeholder", "3": None},
        ):
            with self.subTest(payload=payload):
                self.assertTrue(forbidden_structure_issues(payload))


if __name__ == "__main__":
    unittest.main()
