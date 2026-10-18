"""G14-C QA for cluster-progress and per-pack evidence workflows."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools.validate_full_checkout_g13 import (
    ALLOWED_STATES,
    G14_REQUIRED_RECORD_FIELDS,
    REPOSITORY_ROOT,
    _contract_issues,
    _text_structure_issues,
    forbidden_structure_issues,
    validate_checkout,
)


G14_ARTIFACTS = (
    Path("docs/coordination/UNI_CLUSTER_PROGRESS_REGISTRY_G14.json"),
    Path("docs/coordination/UNI_PER_PACK_QUEUE_G14.json"),
)


class WorkflowEvidenceG14Tests(unittest.TestCase):
    def test_g14_artifacts_have_full_workflow_contracts(self) -> None:
        for relative_path in G14_ARTIFACTS:
            payload = json.loads((REPOSITORY_ROOT / relative_path).read_text(encoding="utf-8"))
            contract_name = next(key for key in payload if key.endswith("_contract"))
            contract = payload[contract_name]
            self.assertEqual(ALLOWED_STATES, set(contract["allowed_states"]))
            self.assertTrue({"blocked", "open"} <= set(contract["required_unresolved_states"]))
            self.assertTrue(G14_REQUIRED_RECORD_FIELDS <= set(contract["record_requirements"]))
            collection_name = next(key for key in payload if key != contract_name)
            states = {record["state"] for record in payload[collection_name]}
            self.assertTrue({"blocked", "open"} <= states)
            for record in payload[collection_name]:
                for field in G14_REQUIRED_RECORD_FIELDS:
                    self.assertIsInstance(record[field], str)
                    self.assertTrue(record[field].strip())

    def test_full_checkout_guard_includes_g14_workflows(self) -> None:
        self.assertEqual([], validate_checkout(REPOSITORY_ROOT))

    def test_blocked_and_open_records_cannot_carry_decisions_or_promotions(self) -> None:
        contract = {
            "state": "pending",
            "allowed_states": sorted(ALLOWED_STATES),
            "required_unresolved_states": ["blocked", "pending", "open"],
            "record_requirements": sorted(G14_REQUIRED_RECORD_FIELDS),
            "limitations": ["placeholder"],
            "answer_key_separation": {"status": "separate", "public": False},
        }
        payload = {
            "cluster_progress_contract": contract,
            "cluster_progress_registries": [
                {
                    "state": "blocked",
                    "evidence_ref": "placeholder",
                    "reviewer": "placeholder",
                    "rationale": "placeholder",
                    "decision": "placeholder",
                },
                {
                    "state": "open",
                    "evidence_ref": "placeholder",
                    "reviewer": "placeholder",
                    "rationale": "placeholder",
                    "promoted": True,
                },
            ],
        }
        findings = _contract_issues(payload)
        self.assertTrue(any("decision" in issue for issue in findings))
        self.assertTrue(any("promotion" in issue for issue in findings))

    def test_required_review_metadata_and_states_are_enforced(self) -> None:
        contract = {
            "state": "pending",
            "allowed_states": sorted(ALLOWED_STATES),
            "required_unresolved_states": ["blocked", "pending", "open"],
            "record_requirements": sorted(G14_REQUIRED_RECORD_FIELDS),
            "limitations": ["placeholder"],
            "answer_key_separation": {"status": "separate", "public": False},
        }
        payload = {
            "per_pack_queue_contract": contract,
            "per_pack_queue": [{"state": "placeholder"}],
        }
        findings = _contract_issues(payload)
        self.assertTrue(any("allowed_states" in issue for issue in findings))
        self.assertTrue(any("evidence_ref" in issue for issue in findings))
        self.assertTrue(any("reviewer" in issue for issue in findings))
        self.assertTrue(any("rationale" in issue for issue in findings))
        self.assertTrue(any("missing workflow state blocked" in issue for issue in findings))
        self.assertTrue(any("missing workflow state open" in issue for issue in findings))

    def test_forbidden_answer_and_numeric_shapes_remain_rejected(self) -> None:
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
        self.assertTrue(_text_structure_issues("correct option: placeholder"))
        self.assertTrue(_text_structure_issues("1: None\n2: placeholder\n3: None"))


if __name__ == "__main__":
    unittest.main()
