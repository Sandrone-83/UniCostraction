"""G7-C structural gate for public publication readiness and remediation.

The gate checks only publication-boundary metadata: explicit limitations,
pending/blocked states, and separation from the answer key.  JSON checks are
shape checks; all negative fixtures use only ``None`` or ``placeholder`` and
contain no real answer, option, explanation, solution, or score.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any

from tests.coordination.test_public_exam_key_guard_g4 import (
    REPOSITORY_ROOT,
    TEXT_SUFFIXES,
    _issues_for_file,
    _json_field_issues,
    _tracked_paths,
)


COORDINATION_PREFIX = "docs/coordination/"
PUBLICATION_STATUS_VALUES = frozenset({"pending", "blocked"})
PUBLICATION_TEXT_MARKERS = (
    re.compile(r"(?i)\b(?:limiti|limitations?)\b"),
    re.compile(r"(?i)\bpending\b"),
    re.compile(r"(?i)\bblocked\b"),
    re.compile(r"(?i)\banswer[_ ]key\b.*\b(?:separat|fuori|non)\b"),
)


def _is_public_manifest(path: Path) -> bool:
    return (
        path.as_posix().casefold().startswith(COORDINATION_PREFIX.casefold())
        and "manifest" in path.name.casefold()
        and path.suffix.casefold() in {".json", ".jsonl", ".md", ".yaml", ".yml"}
    )


def _is_readiness_or_remediation_report(path: Path) -> bool:
    return (
        path.suffix.casefold() in TEXT_SUFFIXES
        and not _is_public_manifest(path)
        and any(
            marker in path.name.casefold()
            for marker in ("readiness", "remediation")
        )
    )


def _publication_paths() -> tuple[Path, ...]:
    return tuple(
        sorted(
            path
            for path in _tracked_paths()
            if _is_public_manifest(path)
            or _is_readiness_or_remediation_report(path)
        )
    )


def _json_contract_issues(path: Path) -> list[str]:
    if path.suffix.casefold() != ".json":
        return []

    payload: Any = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        return ["root: publication manifest must be a JSON object"]

    contract = payload.get("publication_contract")
    if not isinstance(contract, dict):
        return ["$.publication_contract: missing object"]

    issues: list[str] = []
    if contract.get("state") not in PUBLICATION_STATUS_VALUES:
        issues.append("$.publication_contract.state: must be pending or blocked")
    if set(contract.get("allowed_states", [])) != PUBLICATION_STATUS_VALUES:
        issues.append(
            "$.publication_contract.allowed_states: must declare pending and blocked"
        )
    if not isinstance(contract.get("limitations"), list) or not contract["limitations"]:
        issues.append("$.publication_contract.limitations: non-empty list required")

    separation = contract.get("answer_key_separation")
    if not isinstance(separation, dict):
        issues.append("$.publication_contract.answer_key_separation: missing object")
    else:
        if separation.get("status") != "separate":
            issues.append(
                "$.publication_contract.answer_key_separation.status: must be separate"
            )
        if separation.get("public") is not False:
            issues.append(
                "$.publication_contract.answer_key_separation.public: must be false"
            )
    return issues


class PublicationReadinessGuardG7Tests(unittest.TestCase):
    def test_scope_covers_public_manifests_and_readiness_report(self) -> None:
        paths = _publication_paths()
        self.assertTrue(paths)
        self.assertTrue(any(_is_public_manifest(path) for path in paths))
        self.assertTrue(any(_is_readiness_or_remediation_report(path) for path in paths))

    def test_public_manifests_declare_the_publication_contract(self) -> None:
        failures = [
            f"{path.as_posix()}: {issue}"
            for path in _publication_paths()
            if _is_public_manifest(path)
            for issue in _json_contract_issues(REPOSITORY_ROOT / path)
        ]
        self.assertEqual([], failures)

    def test_readiness_or_remediation_reports_declare_limits_states_and_separation(self) -> None:
        failures: list[str] = []
        for relative_path in _publication_paths():
            if not _is_readiness_or_remediation_report(relative_path):
                continue
            text = (REPOSITORY_ROOT / relative_path).read_text(encoding="utf-8")
            for marker in PUBLICATION_TEXT_MARKERS:
                if not marker.search(text):
                    failures.append(f"{relative_path.as_posix()}: missing {marker.pattern}")
        self.assertEqual([], failures)

    def test_publication_artifacts_have_no_response_or_score_structure(self) -> None:
        failures = [
            f"{path.as_posix()}: {issue}"
            for path in _publication_paths()
            for issue in _issues_for_file(REPOSITORY_ROOT / path)
        ]
        self.assertEqual([], failures)

    def test_placeholder_and_none_metadata_are_allowed(self) -> None:
        positive = {
            "publication_contract": {
                "state": "blocked",
                "allowed_states": ["pending", "blocked"],
                "limitations": ["placeholder"],
                "answer_key_separation": {"status": "separate", "public": False},
            },
            "review": None,
        }
        self.assertEqual([], _json_field_issues(positive))

    def test_new_json_response_and_score_shapes_are_rejected(self) -> None:
        for payload in (
            {"response": None},
            {"responses": [None]},
            {"candidate_response": "placeholder"},
            {"submitted_answer": None},
            {"grade": None},
            {"grading": {"score": None}},
            {"1": None, "2": None, "3": None},
        ):
            with self.subTest(payload=payload):
                self.assertTrue(_json_field_issues(payload), payload)


if __name__ == "__main__":
    unittest.main()
