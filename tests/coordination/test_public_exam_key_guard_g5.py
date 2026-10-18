"""Deterministic G5-C regression tests for the extended public-material guard.

The cases exercise only structural names, shapes, and documentary markers;
they contain no expected answer, option letter, explanation, or score.
"""

from __future__ import annotations

import unittest

from tests.coordination.test_public_exam_key_guard_g4 import (
    COORDINATION_PREFIX,
    _guarded_paths,
    _is_coordination_document,
    _is_corpus_document,
    _json_field_issues,
    _text_field_issues,
)


class PublicExamKeyGuardG5Tests(unittest.TestCase):
    def test_scope_discovers_coordination_and_corpus_documents(self) -> None:
        paths = _guarded_paths()
        self.assertTrue(any(_is_coordination_document(path) for path in paths))
        self.assertTrue(any(_is_corpus_document(path) for path in paths))
        self.assertTrue(
            any(path.as_posix().startswith(COORDINATION_PREFIX) for path in paths)
        )

    def test_documentary_absence_markers_remain_allowed(self) -> None:
        allowed = (
            "Risposte NON presenti: il file chiave è riservato (fuori repository).",
            "Le chiavi restano fuori repository e non sono committate.",
            "Quale affermazione è corretta?",
            "Il punteggio non è pubblicato nel materiale d'esame.",
        )
        for marker in allowed:
            self.assertEqual([], _text_field_issues(marker), marker)

    def test_answer_letter_explanation_and_score_fields_are_rejected(self) -> None:
        forbidden = (
            "answers: []",
            "correct_letter: placeholder",
            "lettere_corrette: []",
            "explanation: placeholder",
            "spiegazione: placeholder",
            "score: placeholder",
            "punteggio: placeholder",
        )
        for marker in forbidden:
            self.assertTrue(_text_field_issues(marker), marker)

    def test_nested_json_shapes_are_rejected_without_answer_values(self) -> None:
        for payload in (
            {"answer_key": None},
            {"items": [{"correct_letter": None}]},
            {"review": {"explanation": None}},
            {"results": {"score": None}},
            {"1": None, "2": None, "3": None},
        ):
            self.assertTrue(_json_field_issues(payload), payload)


if __name__ == "__main__":
    unittest.main()
