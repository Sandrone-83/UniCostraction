"""G9-C tests for the reusable public QA artifact gate.

Fixtures are intentionally synthetic: forbidden fields and numeric maps contain
only ``None`` or ``placeholder``.  They never contain an answer, option letter,
response, grade, solution, explanation, or score value.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools.validate_public_qa_g9 import (
    ALLOWED_STATES,
    REPOSITORY_ROOT,
    _contract_issues,
    _text_structure_issues,
    forbidden_structure_issues,
    issues_for_file,
    public_artifact_paths,
    validate_public_artifacts,
)


REPORT_PATH = REPOSITORY_ROOT / "docs/coordination/PUBLIC_QA_GATE_REPORT_G9.json"
README_PATH = REPOSITORY_ROOT / "docs/coordination/UNI_QA_GENERALIZED_REPORT_G9.md"


def _safe_contract() -> dict[str, object]:
    return {
        "limitations": ["placeholder"],
        "allowed_states": sorted(ALLOWED_STATES),
    }


class PublicQAGateG9Tests(unittest.TestCase):
    def test_scope_discovers_public_reports_manifests_and_ledgers(self) -> None:
        paths = public_artifact_paths()
        self.assertTrue(paths)
        self.assertIn(Path("docs/coordination/PUBLIC_EXAM_FIXTURE_MANIFEST_G3.json"), paths)
        self.assertIn(Path("docs/coordination/PUBLICATION_READINESS_MANIFEST_G7.json"), paths)
        self.assertIn(Path("docs/coordination/UNI_EVIDENCE_LEDGER_G8.json"), paths)
        self.assertIn(Path("docs/coordination/PUBLIC_QA_GATE_REPORT_G9.json"), paths)

    def test_all_discovered_public_artifacts_pass_the_generalized_gate(self) -> None:
        self.assertEqual([], validate_public_artifacts())

    def test_g9_report_is_valid_and_declares_structural_limits(self) -> None:
        self.assertEqual([], issues_for_file(REPORT_PATH))
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
        contract = report["report_contract"]
        self.assertTrue(contract["limitations"])
        self.assertEqual(ALLOWED_STATES, set(contract["allowed_states"]))
        self.assertEqual("placeholder", report["entries"][-1]["evidence_ref"])

        documentation = README_PATH.read_text(encoding="utf-8")
        for marker in ("Limiti", "allowed_states", "resolved", "evidence_ref"):
            self.assertIn(marker, documentation)

    def test_resolved_requires_non_empty_evidence_reference(self) -> None:
        payload = {"report_contract": _safe_contract(), "entries": [{"state": "resolved"}]}
        findings = _contract_issues(payload)
        self.assertTrue(any("evidence_ref" in issue for issue in findings))

    def test_unknown_states_are_rejected(self) -> None:
        payload = {
            "report_contract": _safe_contract(),
            "entries": [{"state": "placeholder"}],
        }
        self.assertTrue(any("allowed_states" in issue for issue in _contract_issues(payload)))

    def test_missing_limitations_and_states_are_rejected(self) -> None:
        payload = {
            "report_contract": {"limitations": [], "allowed_states": []},
            "entries": [],
        }
        findings = _contract_issues(payload)
        self.assertTrue(any("limitations" in issue for issue in findings))
        self.assertTrue(any("allowed_states" in issue for issue in findings))

    def test_forbidden_fields_and_numeric_maps_are_rejected_with_safe_values(self) -> None:
        for fixture in (
            {"answer_key": None},
            {"response": "placeholder"},
            {"grade": None},
            {"solution": "placeholder"},
            {"nested": {"answer_key": "placeholder"}},
            {"1": None, "2": "placeholder", "3": None},
        ):
            with self.subTest(fixture=fixture):
                self.assertTrue(forbidden_structure_issues(fixture), fixture)

    def test_text_guard_rejects_only_structured_forbidden_fields(self) -> None:
        for fixture in (
            "answer_key: placeholder",
            "response: None",
            "grade: placeholder",
            "solution: None",
        ):
            with self.subTest(fixture=fixture):
                self.assertTrue(_text_structure_issues(fixture), fixture)
        self.assertEqual([], _text_structure_issues("The answer key is outside the repository."))


if __name__ == "__main__":
    unittest.main()
