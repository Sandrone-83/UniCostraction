"""G10-C protected-exam and provenance-audit structural QA.

All negative fixtures contain only field names plus ``None`` or
``placeholder``.  They never contain an answer, option letter, explanation,
solution, response, grade, or score value.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools.validate_public_qa_g10 import (
    ALLOWED_STATES,
    REPOSITORY_ROOT,
    _contract_issues,
    _text_structure_issues,
    forbidden_structure_issues,
    issues_for_file,
    public_artifact_paths,
    public_exam_paths,
    validate_public_artifacts,
)


EXAMS_PREFIX = "UNIVERSITA_EDILIZIA/ESAMI/"
G10_AUDITS = {
    Path("docs/coordination/UNI_REDUNDANCY_AUDIT_G10.json"),
    Path("docs/coordination/UNI_PROVENANCE_AUDIT_G10.json"),
}
G10_REPORT = Path("docs/coordination/UNI_QA_PROVENANCE_G10.md")


def _safe_contract() -> dict[str, object]:
    return {"limitations": ["placeholder"], "allowed_states": sorted(ALLOWED_STATES)}


class PublicQAGateG10Tests(unittest.TestCase):
    def test_scope_covers_every_public_exam_file_and_new_audits(self) -> None:
        exam_paths = public_exam_paths()
        self.assertEqual(76, len(exam_paths))
        self.assertTrue(all(path.as_posix().startswith(EXAMS_PREFIX) for path in exam_paths))
        self.assertIn(Path("UNIVERSITA_EDILIZIA/ESAMI/AUDIT_CONTENT_LOCKED.md"), exam_paths)
        self.assertIn(Path("UNIVERSITA_EDILIZIA/ESAMI/README.md"), exam_paths)
        self.assertIn(Path("UNIVERSITA_EDILIZIA/ESAMI/PROTOCOLLO_VALUTAZIONE.md"), exam_paths)

        paths = set(public_artifact_paths())
        self.assertTrue(G10_AUDITS <= paths)
        self.assertIn(G10_REPORT, paths)

    def test_all_public_exam_files_and_audits_pass_the_gate(self) -> None:
        self.assertEqual([], validate_public_artifacts())

    def test_audit_contracts_are_metadata_only_and_pending(self) -> None:
        for relative_path in G10_AUDITS:
            payload = json.loads((REPOSITORY_ROOT / relative_path).read_text(encoding="utf-8"))
            self.assertEqual([], issues_for_file(REPOSITORY_ROOT / relative_path))
            self.assertIn("audit_contract", payload)
            self.assertEqual("pending", payload["audit_contract"]["state"])

    def test_positive_documentary_and_metadata_fixtures_are_allowed(self) -> None:
        self.assertEqual([], _text_structure_issues("Risposte NON presenti: la chiave resta fuori repository."))
        self.assertEqual([], _text_structure_issues("Quale affermazione è corretta?"))
        self.assertEqual([], _text_structure_issues("review_state: pending\nlimitations: [placeholder]"))
        self.assertEqual([], forbidden_structure_issues({"state": "open", "note": "placeholder"}))
        self.assertEqual([], forbidden_structure_issues({"question_count": 3, "state": "pending"}))

    def test_all_requested_structures_are_rejected_with_safe_values(self) -> None:
        for fixture in (
            {"answer_key": None},
            {"correct_option": "placeholder"},
            {"explanation": None},
            {"solution": "placeholder"},
            {"score": None},
            {"response": "placeholder"},
            {"grade": None},
            {"nested": {"risposta_corretta": None}},
            {"1": None, "2": "placeholder", "3": None},
        ):
            with self.subTest(fixture=fixture):
                self.assertTrue(forbidden_structure_issues(fixture), fixture)

        for fixture in (
            "answer_key: None",
            "correct_option: placeholder",
            "explanation: None",
            "solution: placeholder",
            "score: None",
            "response: placeholder",
            "grade: None",
            "1: None\n2: placeholder\n3: None",
        ):
            with self.subTest(fixture=fixture):
                self.assertTrue(_text_structure_issues(fixture), fixture)

    def test_contract_rejects_missing_limitations_and_unknown_state(self) -> None:
        payload = {
            "audit_contract": {"limitations": [], "allowed_states": ["placeholder"], "state": "placeholder"}
        }
        findings = _contract_issues(payload)
        self.assertTrue(any("limitations" in issue for issue in findings))
        self.assertTrue(any("allowed_states" in issue for issue in findings))
        self.assertTrue(any("state" in issue for issue in findings))

    def test_semantic_limits_are_declared_without_claiming_correctness(self) -> None:
        report = (REPOSITORY_ROOT / G10_REPORT).read_text(encoding="utf-8")
        for marker in (
            "Limiti semantici",
            "non valuta la correttezza",
            "testo libero",
            "stato resti",
        ):
            self.assertIn(marker, report)


if __name__ == "__main__":
    unittest.main()
