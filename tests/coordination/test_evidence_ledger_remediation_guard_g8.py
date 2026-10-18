"""G8-C structural gate for the evidence ledger and remediation validator.

The gate requires explicit limitations, blocked/pending/open states, and an
evidence reference for resolved entries.  It rejects answer-key, response,
grade, and solution structures.  Test fixtures contain only ``None`` or
``placeholder`` values; they never contain an expected answer or explanation.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools.validate_remediation_g8 import (
    ALLOWED_STATES,
    REQUIRED_UNRESOLVED_STATES,
    forbidden_structure_issues,
    validate_remediation,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
LEDGER_PATH = REPOSITORY_ROOT / "docs/coordination/UNI_EVIDENCE_LEDGER_G8.json"
REPORT_PATH = REPOSITORY_ROOT / "docs/coordination/UNI_EVIDENCE_LEDGER_G8.md"
VALIDATOR_PATH = REPOSITORY_ROOT / "tools/validate_remediation_g8.py"


class EvidenceLedgerRemediationGuardG8Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))

    def test_scope_contains_ledger_report_and_validator(self) -> None:
        self.assertTrue(LEDGER_PATH.is_file())
        self.assertTrue(REPORT_PATH.is_file())
        self.assertTrue(VALIDATOR_PATH.is_file())

    def test_ledger_passes_the_remediation_validator(self) -> None:
        self.assertEqual([], validate_remediation(self.ledger))

    def test_contract_declares_limits_and_required_states(self) -> None:
        contract = self.ledger["ledger_contract"]
        self.assertIsInstance(contract["limitations"], list)
        self.assertTrue(contract["limitations"])
        self.assertEqual(ALLOWED_STATES, set(contract["allowed_states"]))
        self.assertEqual(
            REQUIRED_UNRESOLVED_STATES,
            set(contract["required_unresolved_states"]),
        )

    def test_resolved_entries_require_evidence_ref(self) -> None:
        for entry in self.ledger["entries"]:
            if entry["state"] == "resolved":
                self.assertIsInstance(entry.get("evidence_ref"), str)
                self.assertTrue(entry["evidence_ref"].strip())

        missing_reference = {
            "ledger_contract": {
                "limitations": ["placeholder"],
                "allowed_states": sorted(ALLOWED_STATES),
                "required_unresolved_states": sorted(REQUIRED_UNRESOLVED_STATES),
            },
            "entries": [{"id": "placeholder", "state": "resolved"}],
        }
        self.assertTrue(
            any(
                "evidence_ref" in issue
                for issue in validate_remediation(missing_reference)
            )
        )

    def test_all_required_states_are_represented(self) -> None:
        states = {entry["state"] for entry in self.ledger["entries"]}
        self.assertTrue(REQUIRED_UNRESOLVED_STATES <= states)

    def test_forbidden_structures_are_rejected_with_placeholder_or_none(self) -> None:
        for fixture in (
            {"answer_key": None},
            {"response": "placeholder"},
            {"grade": None},
            {"solution": "placeholder"},
            {"nested": {"responses": [None]}},
            {"1": None, "2": None, "3": None},
        ):
            with self.subTest(fixture=fixture):
                self.assertTrue(forbidden_structure_issues(fixture), fixture)

    def test_safe_metadata_fixtures_are_allowed(self) -> None:
        for fixture in (
            {"state": "open", "evidence_ref": None, "note": "placeholder"},
            {"state": "resolved", "evidence_ref": "placeholder"},
        ):
            with self.subTest(fixture=fixture):
                self.assertEqual([], forbidden_structure_issues(fixture))

    def test_report_declares_limits_states_and_boundary(self) -> None:
        report = REPORT_PATH.read_text(encoding="utf-8")
        for marker in (
            "Limiti",
            "blocked",
            "pending",
            "open",
            "resolved",
            "evidence_ref",
            "answer key",
            "response",
            "grade",
            "solution",
        ):
            self.assertIn(marker, report)


if __name__ == "__main__":
    unittest.main()
