"""Structural validator for the G8 evidence ledger and remediation contract.

This validator checks metadata shape only.  It never evaluates an answer,
grade, solution, or the factual meaning of an evidence reference.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ALLOWED_STATES = frozenset({"blocked", "pending", "open", "resolved"})
REQUIRED_UNRESOLVED_STATES = frozenset({"blocked", "pending", "open"})
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
        "grade",
        "grading",
        "score",
        "scores",
        "solution",
        "solutions",
        "correct_answer",
        "correct_option",
        "correct_response",
        "explanation",
        "explanations",
        "rationale",
    }
)
QUESTION_KEY_PATTERN = re.compile(r"^\d+$")


def _normalise_field_name(name: str) -> str:
    return re.sub(r"[\s-]+", "_", name.casefold().strip())


def _looks_like_numeric_scalar_map(value: dict[Any, Any]) -> bool:
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
    """Return structural answer/response/grade/solution findings."""

    issues: list[str] = []
    if isinstance(value, dict):
        if _looks_like_numeric_scalar_map(value):
            issues.append(f"{location}: numeric question-to-scalar map")
        for key, child in value.items():
            if (
                isinstance(key, str)
                and _normalise_field_name(key) in FORBIDDEN_FIELDS
            ):
                issues.append(f"{location}.{key}: forbidden structured field")
            issues.extend(forbidden_structure_issues(child, f"{location}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            issues.extend(forbidden_structure_issues(child, f"{location}[{index}]"))
    return issues


def validate_remediation(payload: Any) -> list[str]:
    """Validate the G8 ledger contract and remediation entries."""

    issues = forbidden_structure_issues(payload)
    if not isinstance(payload, dict):
        return ["$: evidence ledger must be a JSON object", *issues]

    contract = payload.get("ledger_contract")
    if not isinstance(contract, dict):
        issues.append("$.ledger_contract: missing object")
    else:
        limitations = contract.get("limitations")
        if not isinstance(limitations, list) or not limitations or not all(
            isinstance(item, str) and item.strip() for item in limitations
        ):
            issues.append("$.ledger_contract.limitations: non-empty strings required")

        allowed_states = contract.get("allowed_states")
        if set(allowed_states or ()) != ALLOWED_STATES:
            issues.append(
                "$.ledger_contract.allowed_states: must declare blocked, pending, open, resolved"
            )

        required_states = contract.get("required_unresolved_states")
        if set(required_states or ()) != REQUIRED_UNRESOLVED_STATES:
            issues.append(
                "$.ledger_contract.required_unresolved_states: must declare blocked, pending, open"
            )

    entries = payload.get("entries")
    if not isinstance(entries, list) or not entries:
        issues.append("$.entries: non-empty list required")
        return issues

    for index, entry in enumerate(entries):
        location = f"$.entries[{index}]"
        if not isinstance(entry, dict):
            issues.append(f"{location}: entry must be an object")
            continue

        entry_id = entry.get("id")
        if not isinstance(entry_id, str) or not entry_id.strip():
            issues.append(f"{location}.id: non-empty string required")

        state = entry.get("state")
        if state not in ALLOWED_STATES:
            issues.append(f"{location}.state: unknown remediation state")

        if state == "resolved":
            evidence_ref = entry.get("evidence_ref")
            if not isinstance(evidence_ref, str) or not evidence_ref.strip():
                issues.append(
                    f"{location}.evidence_ref: non-empty string required when resolved"
                )

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path, help="G8 evidence ledger JSON path")
    args = parser.parse_args()
    payload = json.loads(args.ledger.read_text(encoding="utf-8"))
    issues = validate_remediation(payload)
    if issues:
        for issue in issues:
            print(issue)
        return 1
    print(f"valid: {args.ledger}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
