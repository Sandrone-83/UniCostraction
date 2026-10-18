"""G4/G5 guard for answer-key, scoring, and correct-answer leakage.

The guard inspects tracked files under the public ``ESAMI`` tree, coordination
documents, corpus documents, and tracked files whose name identifies a public
manifest.  It checks field names and data shapes, never expected answers,
option letters, scores, or answer-key fixtures.  Documentary prose such as
``Risposte NON presenti`` remains legal.

This is a repository-boundary check, not a semantic assessment of the
questions or their options.
"""

from __future__ import annotations

import json
import re
import subprocess
import unittest
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
PUBLIC_EXAMS_PREFIX = "UNIVERSITA_EDILIZIA/ESAMI/"
COORDINATION_PREFIX = "docs/coordination/"
TEXT_SUFFIXES = frozenset(
    {".csv", ".json", ".jsonl", ".md", ".rst", ".tsv", ".txt", ".yaml", ".yml"}
)

# These names describe a payload field, not ordinary prose.  In particular,
# generic ``chiave``/``chiavi`` are deliberately not listed because the public
# documentation uses them as legitimate notices.  ``risposte`` is guarded as
# a field but has an explicit absence-marker exception below.
FORBIDDEN_FIELD_NAMES = frozenset(
    {
        "answer",
        "answers",
        "answer_key",
        "answerkey",
        "correct_answer",
        "correct_answers",
        "correct_option",
        "correct_options",
        "correct_response",
        "correct_letter",
        "correct_letters",
        "lettera",
        "lettere",
        "lettera_corretta",
        "lettere_corrette",
        "lettera_esatta",
        "lettere_esatte",
        "points",
        "punteggio",
        "punteggi",
        "risposta",
        "risposte",
        "risposta_corretta",
        "risposta_esatta",
        "risposte_corrette",
        "risposte_esatte",
        "score",
        "scores",
        "solution",
        "soluzione",
        "solutions",
        "soluzioni",
        "explanation",
        "explanations",
        "spiegazione",
        "spiegazioni",
        "rationale",
        "motivazione",
        "justification",
        "answer_explanation",
        "spiegazione_risposta",
        "total_score",
        "max_score",
        "question_score",
        "chiave_risposte",
        "chiavi_risposte",
    }
)

_FIELD_ALTERNATION = "|".join(
    sorted((re.escape(name) for name in FORBIDDEN_FIELD_NAMES), key=len, reverse=True)
)
# A field-like line boundary is required.  This intentionally does not match
# natural-language occurrences such as ``quale risposta è corretta?`` or a
# quoted ``risposta:`` inside an option.
STRUCTURED_FIELD_PATTERN = re.compile(
    rf"(?ix)^\s*(?:[-*]\s+)?(?:\|\s*)?"
    rf"(?:[*_`\"']*\s*)"
    rf"(?:{_FIELD_ALTERNATION})"
    rf"(?![a-z0-9_])"
    rf"\s*(?:[*_`\"']*\s*)"
    rf"(?=[:=|])"
)

QUESTION_KEY_PATTERN = re.compile(r"^\d+$")
DOCUMENTARY_MARKER_PATTERN = re.compile(
    r"(?ix)^\s*(?:[-*]\s+)?(?:\|\s*)?"
    r"(?:risposte?\s+non\s+presenti\b|"
    r"(?:la\s+)?chiav(?:e|i)\s+(?:resta|restano|e|sono)\s+fuori\s+repository\b|"
    r"(?:il\s+)?punteggio\s+non\s+(?:e\s+)?pubblicat[oa]\b)"
)


@lru_cache(maxsize=1)
def _tracked_paths() -> tuple[Path, ...]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=REPOSITORY_ROOT,
        check=True,
        capture_output=True,
    )
    return tuple(
        Path(item)
        for item in result.stdout.decode("utf-8").split("\0")
        if item
    )


def _is_public_manifest(path: Path) -> bool:
    return "manifest" in path.name.casefold()


def _is_coordination_document(path: Path) -> bool:
    return path.as_posix().casefold().startswith(COORDINATION_PREFIX.casefold())


def _is_corpus_document(path: Path) -> bool:
    """Identify text metadata/document files in any corpus-named path.

    Binary CAD assets can live beside corpus metadata.  They are deliberately
    outside this textual structural guard; a binary/content review is a
    separate control.
    """
    return (
        any("corpus" in component.casefold() for component in path.parts)
        and path.suffix.casefold() in TEXT_SUFFIXES
    )


@lru_cache(maxsize=1)
def _guarded_paths() -> tuple[Path, ...]:
    return tuple(sorted(
        path
        for path in _tracked_paths()
        if path.as_posix().casefold().startswith(PUBLIC_EXAMS_PREFIX.casefold())
        or _is_public_manifest(path)
        or _is_coordination_document(path)
        or _is_corpus_document(path)
    ))


def _normalise_field_name(name: str) -> str:
    return re.sub(r"[\s-]+", "_", name.casefold().strip())


def _json_field_issues(value: Any, location: str = "$") -> list[str]:
    issues: list[str] = []
    if isinstance(value, dict):
        if _looks_like_numeric_scalar_map(value):
            issues.append(f"{location}: numeric question-to-scalar map")
        for key, child in value.items():
            if isinstance(key, str) and _normalise_field_name(key) in FORBIDDEN_FIELD_NAMES:
                issues.append(f"{location}.{key}: forbidden structured field")
            issues.extend(_json_field_issues(child, f"{location}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            issues.extend(_json_field_issues(child, f"{location}[{index}]"))
    return issues


def _looks_like_numeric_scalar_map(value: dict[Any, Any]) -> bool:
    """Detect an unlabelled question-number -> scalar answer/score map.

    The test uses only shape: it contains no expected answer values and does
    not compare any option text or score.
    """
    if len(value) < 3 or not all(isinstance(key, str) for key in value):
        return False
    if not all(QUESTION_KEY_PATTERN.fullmatch(key) for key in value):
        return False
    return all(
        item is None
        or (isinstance(item, (str, int, float, bool)) and not isinstance(item, bytes))
        for item in value.values()
    )


def _text_field_issues(text: str) -> list[str]:
    return [
        f"line {line_number}: structured answer/score marker"
        for line_number, line in enumerate(text.splitlines(), start=1)
        if not DOCUMENTARY_MARKER_PATTERN.search(line)
        if STRUCTURED_FIELD_PATTERN.search(line)
    ]


def _issues_for_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    issues = _text_field_issues(text)

    if path.suffix.casefold() in {".json", ".jsonl"}:
        if path.suffix.casefold() == ".jsonl":
            json_values: Iterable[Any] = (
                json.loads(line)
                for line in text.splitlines()
                if line.strip()
            )
        else:
            json_values = (json.loads(text),)

        for index, value in enumerate(json_values):
            try:
                issues.extend(_json_field_issues(value, f"$[{index}]"))
            except json.JSONDecodeError:
                # The text-level guard still protects malformed/line-oriented
                # public material; JSON validity is outside this G4 scope.
                continue
    return issues


class PublicExamKeyGuardG4Tests(unittest.TestCase):
    def test_guard_scope_is_tracked_public_material(self) -> None:
        paths = _guarded_paths()
        self.assertTrue(paths)
        self.assertTrue(
            any(
                path.as_posix().casefold().startswith(PUBLIC_EXAMS_PREFIX.casefold())
                for path in paths
            )
        )
        self.assertTrue(any(_is_public_manifest(path) for path in paths))
        self.assertTrue(any(_is_coordination_document(path) for path in paths))
        self.assertTrue(any(_is_corpus_document(path) for path in paths))
        self.assertEqual(len(paths), len(set(paths)))

    def test_tracked_exams_and_public_manifests_have_no_key_or_score_structure(self) -> None:
        findings = {
            path.as_posix(): _issues_for_file(REPOSITORY_ROOT / path)
            for path in _guarded_paths()
        }
        failures = [
            f"{path}: {issue}"
            for path, issues in findings.items()
            for issue in issues
        ]
        self.assertEqual([], failures)

    def test_documentary_markers_are_allowed(self) -> None:
        legal_markers = (
            "Risposte NON presenti: il file chiave è riservato (fuori repository).",
            "Le chiavi restano fuori repository e non sono committate.",
            "Quale affermazione è corretta?",
            "Il punteggio non è pubblicato nel materiale d'esame.",
        )
        for marker in legal_markers:
            self.assertEqual([], _text_field_issues(marker), marker)

    def test_structural_markers_are_rejected_without_expected_answers(self) -> None:
        for marker in (
            "risposta_corretta: non pubblicata",
            "correct_letter: placeholder",
            "explanation: testo esplicativo",
            "score: non pubblicato",
            "risposte: []",
            "spiegazioni: []",
        ):
            self.assertTrue(_text_field_issues(marker), marker)
        self.assertTrue(_json_field_issues({"answer_key": None}))
        self.assertTrue(_json_field_issues({"correct_letter": None}))
        self.assertTrue(_json_field_issues({"explanation": None}))
        self.assertTrue(_json_field_issues({"score": None}))
        self.assertTrue(
            _json_field_issues({"1": None, "2": None, "3": None})
        )


if __name__ == "__main__":
    unittest.main()
