"""Reusable structural gate for public QA reports, manifests, and ledgers.

The checker validates metadata contracts only.  It does not establish factual,
educational, normative, legal, professional, or publication correctness, and
it does not inspect free text for semantically disguised answer material.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any, Iterable


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PUBLIC_ARTIFACT_ROOTS = ("docs/coordination", "reports")
PUBLIC_ARTIFACT_NAME_MARKERS = frozenset(
    {"ledger", "manifest", "report", "readiness", "remediation"}
)
TEXT_SUFFIXES = frozenset(
    {".csv", ".json", ".jsonl", ".md", ".rst", ".tsv", ".txt", ".yaml", ".yml"}
)
JSON_SUFFIXES = frozenset({".json", ".jsonl"})

ALLOWED_STATES = frozenset({"blocked", "pending", "open", "resolved"})
STATE_COLLECTION_KEYS = frozenset(
    {"artifacts", "checks", "entries", "findings", "items", "records"}
)
CONTRACT_KEYS = frozenset({"ledger_contract", "publication_contract", "report_contract"})
FORBIDDEN_FIELDS = frozenset(
    {
        "answer",
        "answers",
        "answer_key",
        "answerkey",
        "response",
        "responses",
        "candidate_response",
        "candidate_responses",
        "submitted_answer",
        "submitted_answers",
        "grade",
        "grading",
        "score",
        "scores",
        "solution",
        "solutions",
        "correct_answer",
        "correct_answers",
        "correct_option",
        "correct_options",
        "correct_response",
        "correct_letter",
        "correct_letters",
        "explanation",
        "explanations",
        "rationale",
        "answer_explanation",
    }
)
QUESTION_KEY_PATTERN = re.compile(r"^\d+$")
STRUCTURED_FIELD_PATTERN = re.compile(
    r"(?i)(?:^|[\[{,]\s*)[\"']?"
    r"(?:answer(?:s|_key)?|response(?:s)?|candidate_response(?:s)?|"
    r"submitted_answer(?:s)?|grade|grading|score(?:s)?|solution(?:s)?|"
    r"correct_(?:answer|answers|option|options|response|letter|letters)|"
    r"explanation(?:s)?|rationale|answer_explanation)"
    r"[\"']?\s*[:=]"
)
DOCUMENTARY_MARKER_PATTERN = re.compile(
    r"(?i)\b(?:non\s+presenti|fuori\s+repository|non\s+committat|"
    r"not\s+published|not\s+present|separate)\b"
)


def _normalise_field_name(name: str) -> str:
    return re.sub(r"[\s-]+", "_", name.casefold().strip())


def _tracked_paths() -> tuple[Path, ...]:
    result = subprocess.run(
        ["git", "-C", str(REPOSITORY_ROOT), "ls-files", "-z"],
        check=True,
        capture_output=True,
    )
    return tuple(
        Path(item.decode("utf-8"))
        for item in result.stdout.split(b"\0")
        if item
    )


def _is_public_artifact(path: Path) -> bool:
    path_text = path.as_posix()
    if not path_text.startswith(tuple(f"{root}/" for root in PUBLIC_ARTIFACT_ROOTS)):
        return False
    if path.suffix.casefold() not in TEXT_SUFFIXES:
        return False
    name = path.name.casefold()
    return any(marker in name for marker in PUBLIC_ARTIFACT_NAME_MARKERS)


def public_artifact_paths() -> tuple[Path, ...]:
    """Return tracked public QA reports, manifests, and ledgers."""

    return tuple(sorted(path for path in _tracked_paths() if _is_public_artifact(path)))


def _looks_like_numeric_scalar_map(value: dict[Any, Any]) -> bool:
    """Detect an unlabelled question-number -> scalar map by shape only."""

    if len(value) < 3 or not all(isinstance(key, str) for key in value):
        return False
    if not all(QUESTION_KEY_PATTERN.fullmatch(key) for key in value):
        return False
    return all(
        item is None
        or (isinstance(item, (str, int, float, bool)) and not isinstance(item, bytes))
        for item in value.values()
    )


def forbidden_structure_issues(value: Any, location: str = "$") -> list[str]:
    """Return answer/response/grade/solution and numeric-map findings."""

    issues: list[str] = []
    if isinstance(value, dict):
        if _looks_like_numeric_scalar_map(value):
            issues.append(f"{location}: numeric question-to-scalar map")
        for key, child in value.items():
            if isinstance(key, str) and _normalise_field_name(key) in FORBIDDEN_FIELDS:
                issues.append(f"{location}.{key}: forbidden structured field")
            issues.extend(forbidden_structure_issues(child, f"{location}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            issues.extend(forbidden_structure_issues(child, f"{location}[{index}]"))
    return issues


def _text_structure_issues(text: str) -> list[str]:
    return [
        f"line {line_number}: forbidden structured field"
        for line_number, line in enumerate(text.splitlines(), start=1)
        if not DOCUMENTARY_MARKER_PATTERN.search(line)
        if STRUCTURED_FIELD_PATTERN.search(line)
    ]


def _json_values(path: Path) -> Iterable[Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.casefold() == ".jsonl":
        return (json.loads(line) for line in text.splitlines() if line.strip())
    return (json.loads(text),)


def _contract(payload: dict[str, Any]) -> tuple[str, dict[str, Any]] | None:
    for key in CONTRACT_KEYS:
        value = payload.get(key)
        if isinstance(value, dict):
            return key, value
    return None


def _non_empty_strings(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(
        isinstance(item, str) and item.strip() for item in value
    )


def _contract_issues(payload: Any) -> list[str]:
    if not isinstance(payload, dict):
        return ["$: public QA artifact must be a JSON object"]

    found_contract = _contract(payload)
    if found_contract is None:
        return ["$: missing report, publication, or ledger contract"]

    contract_name, contract = found_contract
    issues: list[str] = []
    limitations = contract.get("limitations")
    if not _non_empty_strings(limitations):
        issues.append(f"$.{contract_name}.limitations: non-empty strings required")

    allowed_states = contract.get("allowed_states")
    if not _non_empty_strings(allowed_states):
        issues.append(f"$.{contract_name}.allowed_states: non-empty strings required")
        allowed = set()
    else:
        allowed = set(allowed_states)
        if not allowed <= ALLOWED_STATES:
            issues.append(
                f"$.{contract_name}.allowed_states: only {sorted(ALLOWED_STATES)} allowed"
            )

    contract_state = contract.get("state")
    if contract_state is not None and contract_state not in allowed:
        issues.append(f"$.{contract_name}.state: state is not declared in allowed_states")

    required_unresolved = contract.get("required_unresolved_states")
    if required_unresolved is not None:
        if not _non_empty_strings(required_unresolved) or not set(required_unresolved) <= allowed:
            issues.append(
                f"$.{contract_name}.required_unresolved_states: must be allowed states"
            )

    issues.extend(_state_collection_issues(payload, allowed))
    return issues


def _state_collection_issues(payload: Any, allowed_states: set[str]) -> list[str]:
    issues: list[str] = []

    def visit(value: Any, location: str) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if key in STATE_COLLECTION_KEYS and isinstance(child, list):
                    for index, entry in enumerate(child):
                        entry_location = f"{location}.{key}[{index}]"
                        if not isinstance(entry, dict):
                            continue
                        state = entry.get("state", entry.get("status"))
                        if state is not None and state not in allowed_states:
                            issues.append(
                                f"{entry_location}.state: state is not declared in allowed_states"
                            )
                        if state == "resolved":
                            evidence_ref = entry.get("evidence_ref")
                            if not isinstance(evidence_ref, str) or not evidence_ref.strip():
                                issues.append(
                                    f"{entry_location}.evidence_ref: non-empty string required when resolved"
                                )
                        visit(entry, entry_location)
                else:
                    visit(child, f"{location}.{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                visit(child, f"{location}[{index}]")

    visit(payload, "$")
    return issues


def issues_for_file(path: Path) -> list[str]:
    """Validate one public artifact using text and, where applicable, JSON shape."""

    text = path.read_text(encoding="utf-8")
    issues = _text_structure_issues(text)
    if path.suffix.casefold() in JSON_SUFFIXES:
        try:
            for index, payload in enumerate(_json_values(path)):
                issues.extend(
                    f"$[{index}].{issue}" if issue.startswith("$") else issue
                    for issue in forbidden_structure_issues(payload)
                )
                if path.suffix.casefold() == ".json":
                    issues.extend(_contract_issues(payload))
        except json.JSONDecodeError as error:
            issues.append(f"JSON parse error: {error.msg}")
    return issues


def validate_public_artifacts(root: Path = REPOSITORY_ROOT) -> list[str]:
    """Return all structural findings for the tracked public QA scope."""

    if root != REPOSITORY_ROOT:
        raise ValueError("the G9 checker is bound to its repository root")
    return [
        f"{path.as_posix()}: {issue}"
        for path in public_artifact_paths()
        for issue in issues_for_file(REPOSITORY_ROOT / path)
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="optional artifact paths; by default scan tracked public QA artifacts",
    )
    args = parser.parse_args()
    if args.paths:
        findings = [
            f"{path}: {issue}"
            for path in args.paths
            for issue in issues_for_file(path)
        ]
    else:
        findings = validate_public_artifacts()
    if findings:
        print("\n".join(findings))
        return 1
    print(f"valid: {len(args.paths) or len(public_artifact_paths())} public QA artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
