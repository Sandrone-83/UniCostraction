"""G6-C cross-corpus guard for public coordination and audit artifacts.

The production-facing material is checked through the tracked-file scope. The
fixtures below exercise only field names, nulls, and placeholders: they do not
contain an expected answer, option letter, explanation text, solution, or
score. This is a structural repository-boundary guard, not a didactic,
factual, normative, or professional validation.
"""

from __future__ import annotations

import unittest
from pathlib import Path

from tests.coordination.test_public_exam_key_guard_g4 import (
    COORDINATION_PREFIX,
    REPOSITORY_ROOT,
    TEXT_SUFFIXES,
    _guarded_paths,
    _issues_for_file,
    _is_corpus_document,
    _is_coordination_document,
    _json_field_issues,
    _text_field_issues,
    _tracked_paths,
)


AUDIT_DASHBOARD_MARKERS = frozenset({"audit", "dashboard", "review"})


def _is_audit_dashboard_document(path: Path) -> bool:
    """Select text audit/review/dashboard artifacts without reading binaries."""

    name = path.name.casefold()
    return (
        path.suffix.casefold() in TEXT_SUFFIXES
        and any(marker in name for marker in AUDIT_DASHBOARD_MARKERS)
    )


def _is_g6_cross_corpus_document(path: Path) -> bool:
    """Cover G5 coordination/corpus material and planned audit artifacts."""

    return (
        _is_coordination_document(path)
        or _is_corpus_document(path)
        or _is_audit_dashboard_document(path)
    )


def _g6_cross_corpus_paths() -> tuple[Path, ...]:
    return tuple(sorted(path for path in _tracked_paths() if _is_g6_cross_corpus_document(path)))


class CrossCorpusKeyGuardG6Tests(unittest.TestCase):
    def test_scope_covers_g5_coordination_corpus_and_audit_shapes(self) -> None:
        paths = _g6_cross_corpus_paths()
        self.assertTrue(paths)
        self.assertTrue(any(_is_coordination_document(path) for path in paths))
        self.assertTrue(any(_is_corpus_document(path) for path in paths))
        self.assertTrue(any(_is_audit_dashboard_document(path) for path in paths))

        anticipated = (
            Path("docs/coordination/UNI_CORPUS_LOTTO_G5_ECFR.json"),
            Path("docs/coordination/UNI_SOURCE_RECORD_SCHEMA_G5.json"),
            Path("docs/coordination/UNI_PACK_EXAM_REVIEW_G5.json"),
            Path("docs/coordination/UNI_PACK_EXAM_REVIEW_G5.md"),
            Path("reports/dashboard_audit_g5.json"),
        )
        self.assertTrue(all(_is_g6_cross_corpus_document(path) for path in anticipated))

    def test_tracked_cross_corpus_material_has_no_forbidden_structure(self) -> None:
        failures = [
            f"{path.as_posix()}: {issue}"
            for path in _g6_cross_corpus_paths()
            for issue in _issues_for_file(REPOSITORY_ROOT / path)
        ]
        self.assertEqual([], failures)

    def test_positive_metadata_and_review_fixtures_are_allowed(self) -> None:
        positive_json = (
            {
                "schema_version": "G5-source-metadata",
                "metadata_only": True,
                "source_records": [],
                "verification_status": {"state": "observed_local"},
                "limitations": ["not assessed"],
            },
            {
                "schema_version": "g5.v1",
                "review_status": "pending",
                "decision": {"outcome": None},
                "counts": {"pending": 0},
            },
        )
        for fixture in positive_json:
            with self.subTest(fixture=fixture):
                self.assertEqual([], _json_field_issues(fixture))

        for fixture in (
            "Risposte NON presenti: la chiave resta fuori repository.",
            "Il report registra solo metadati osservati e stato di revisione.",
            "Quale affermazione è corretta?",
        ):
            with self.subTest(fixture=fixture):
                self.assertEqual([], _text_field_issues(fixture))

    def test_negative_fixtures_reject_only_structural_field_shapes(self) -> None:
        negative_json = (
            {"answer_key": None},
            {"correct_letter": None},
            {"solution": None},
            {"explanation": None},
            {"score": None},
            {"1": None, "2": None, "3": None},
        )
        for fixture in negative_json:
            with self.subTest(fixture=fixture):
                self.assertTrue(_json_field_issues(fixture))

        for fixture in (
            "answer_key: placeholder",
            "correct_letter: placeholder",
            "solution: placeholder",
            "explanation: placeholder",
            "score: placeholder",
            "punteggio: placeholder",
        ):
            with self.subTest(fixture=fixture):
                self.assertTrue(_text_field_issues(fixture))


if __name__ == "__main__":
    unittest.main()
