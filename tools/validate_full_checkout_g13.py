"""G13-C full-checkout guard for the protected public QA contract.

The command scans the tracked text material in ``ESAMI``, coordination
documents, and files named as manifests, audits, or ledgers.  It is negative
and metadata-only: it rejects structured answer-key, response, grade,
solution, score, correct-option, explanation, and numeric question-to-value
shapes, while allowing documentary prose and ``None``/``placeholder``
workflow fixtures.

It also checks the metadata contract: limitations and allowed states must be
declared, states must belong to the declared set, resolved records need a
non-empty ``evidence_ref``, and non-null decisions need an evidence pointer.
Manifest file paths and SHA-256 values are checked when a public fixture
manifest exposes that shape.  The guard never reads or reconstructs an
answer key and cannot establish educational, factual, normative, legal, or
professional correctness.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any, Iterable


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PUBLIC_EXAMS_PREFIX = "UNIVERSITA_EDILIZIA/ESAMI/"
COORDINATION_PREFIX = "docs/coordination/"
TEXT_SUFFIXES = frozenset(
    {".csv", ".json", ".jsonl", ".md", ".rst", ".tsv", ".txt", ".yaml", ".yml"}
)
JSON_SUFFIXES = frozenset({".json", ".jsonl"})
ALLOWED_STATES = frozenset({"blocked", "pending", "open", "resolved"})
EXPECTED_PUBLIC_EXAM_PAYLOAD_COUNT = 73
REQUIRED_COORDINATION_ARTIFACTS = frozenset(
    {
        "PUBLIC_EXAM_FIXTURE_MANIFEST_G3.json",
        "PUBLICATION_READINESS_MANIFEST_G7.json",
        "PUBLIC_QA_GATE_REPORT_G9.json",
        "UNI_EVIDENCE_LEDGER_G8.json",
        "UNI_PROVENANCE_AUDIT_G10.json",
        "UNI_REDUNDANCY_AUDIT_G10.json",
        "UNI_CANDIDATE_REVIEW_CLUSTERS_G11.json",
        "UNI_PRIORITY_QUEUES_G11.json",
        "UNI_EVIDENCE_LICENSE_MATRIX_G11.json",
        "UNI_REDUNDANCY_DECISION_RECORDS_G12.json",
        "UNI_SOURCE_LICENSE_CHECKLIST_G12.json",
    }
)

# These are payload field names, not ordinary prose.  ``answer_key_separation``
# is intentionally absent: it is the allowed metadata declaration that the
# protected key remains outside the public checkout.
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
        "correct_answer",
        "correct_answers",
        "correct_option",
        "correct_options",
        "correct_response",
        "correct_responses",
        "correct_choice",
        "correct_choices",
        "correct_letter",
        "correct_letters",
        "correct_answer_letter",
        "correct_answer_letters",
        "lettera_corretta",
        "lettere_corrette",
        "lettera_esatta",
        "lettere_esatte",
        "opzione_corretta",
        "opzioni_corrette",
        "risposta",
        "risposte",
        "risposta_corretta",
        "risposte_corrette",
        "risposta_esatta",
        "risposte_esatte",
        "points",
        "point",
        "punteggio",
        "punteggi",
        "total_score",
        "max_score",
        "question_score",
        "score",
        "scores",
        "grade",
        "grades",
        "grading",
        "voto",
        "voti",
        "valutazione",
        "valutazioni",
        "solution",
        "solutions",
        "soluzione",
        "soluzioni",
        "explanation",
        "explanations",
        "spiegazione",
        "spiegazioni",
        "answer_explanation",
        "spiegazione_risposta",
    }
)


def _field_pattern(name: str) -> str:
    return re.escape(name).replace("_", r"[\s_-]+")


_FIELD_ALTERNATION = "|".join(
    sorted((_field_pattern(name) for name in FORBIDDEN_FIELDS), key=len, reverse=True)
)
STRUCTURED_FIELD_PATTERN = re.compile(
    rf"(?ix)^\s*(?:[-*]\s+)?(?:\|\s*)?(?:[*_`\"']*\s*)"
    rf"(?:{_FIELD_ALTERNATION})(?![a-z0-9_])\s*(?:[*_`\"']*\s*)"
    rf"(?=[:=|])"
)
DOCUMENTARY_MARKER_PATTERN = re.compile(
    r"(?ix)^\s*(?:[-*]\s+)?(?:\|\s*)?"
    r"(?:risposte?\s+non\s+presenti\b|"
    r"(?:la\s+)?chiav(?:e|i)\s+(?:resta|restano|e|sono)\s+fuori\s+repository\b|"
    r"(?:the\s+)?answer\s+key\s+(?:is\s+)?(?:outside|separate|not\s+published)\b|"
    r"(?:il\s+)?punteggio\s+non\s+(?:e\s+)?pubblicat[oa]\b)"
)
NUMERIC_MAPPING_PATTERN = re.compile(r"^\s*(?:[-*]\s+)?(?:[\"']?)(\d+)(?:[\"']?)\s*[:=]\s*.+$")
QUESTION_KEY_PATTERN = re.compile(r"^\d+$")


def _normalise_field_name(name: str) -> str:
    return re.sub(r"[\s-]+", "_", name.casefold().strip())


def _tracked_paths(root: Path) -> tuple[Path, ...]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z"],
        check=True,
        capture_output=True,
    )
    return tuple(
        Path(item.decode("utf-8")) for item in result.stdout.split(b"\0") if item
    )


def _is_scoped_path(path: Path) -> bool:
    path_text = path.as_posix()
    path_folded = path_text.casefold()
    if path.suffix.casefold() not in TEXT_SUFFIXES:
        return False
    if path_folded.startswith(PUBLIC_EXAMS_PREFIX.casefold()):
        return True
    if path_folded.startswith(COORDINATION_PREFIX.casefold()):
        return True
    return any(marker in path.name.casefold() for marker in ("manifest", "audit", "ledger"))


def scoped_paths(root: Path = REPOSITORY_ROOT) -> tuple[Path, ...]:
    """Return the unique tracked text files covered by the G13 contract."""

    return tuple(sorted(path for path in _tracked_paths(root) if _is_scoped_path(path)))


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
    """Find forbidden field names and numeric question-to-scalar maps."""

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
    issues = [
        f"line {line_number}: forbidden structured field"
        for line_number, line in enumerate(text.splitlines(), start=1)
        if not DOCUMENTARY_MARKER_PATTERN.search(line)
        if STRUCTURED_FIELD_PATTERN.search(line)
    ]
    positions = [
        line_number
        for line_number, line in enumerate(text.splitlines(), start=1)
        if NUMERIC_MAPPING_PATTERN.match(line)
    ]
    if len(positions) >= 3:
        issues.append(
            f"lines {positions[0]}-{positions[-1]}: numeric question-to-scalar map"
        )
    return issues


def _json_values(path: Path) -> Iterable[tuple[str, Any]]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.casefold() == ".jsonl":
        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.strip():
                yield f"line {line_number}", json.loads(line)
    else:
        yield "$", json.loads(text)


def _non_empty_strings(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(
        isinstance(item, str) and item.strip() for item in value
    )


def _contract_issues(payload: Any, location: str = "$") -> list[str]:
    """Validate every declared ``*_contract`` object and its records."""

    if not isinstance(payload, dict):
        return []
    issues: list[str] = []
    contracts = [
        (key, value)
        for key, value in payload.items()
        if isinstance(key, str) and key.endswith("_contract")
    ]
    for contract_name, contract in contracts:
        contract_location = f"{location}.{contract_name}"
        if not isinstance(contract, dict):
            issues.append(f"{contract_location}: contract must be an object")
            continue
        limitations = contract.get("limitations")
        if not _non_empty_strings(limitations):
            issues.append(f"{contract_location}.limitations: non-empty strings required")
        allowed = contract.get("allowed_states")
        if not _non_empty_strings(allowed):
            issues.append(f"{contract_location}.allowed_states: non-empty strings required")
            allowed_set: set[str] = set()
        else:
            allowed_set = set(allowed)
            if not allowed_set <= ALLOWED_STATES:
                issues.append(
                    f"{contract_location}.allowed_states: only {sorted(ALLOWED_STATES)} allowed"
                )
        state = contract.get("state")
        if state is not None and state not in allowed_set:
            issues.append(f"{contract_location}.state: not declared in allowed_states")
        unresolved = contract.get("required_unresolved_states")
        if unresolved is not None and (
            not _non_empty_strings(unresolved) or not set(unresolved) <= allowed_set
        ):
            issues.append(
                f"{contract_location}.required_unresolved_states: must be non-empty and allowed"
            )
        resolved_requires = contract.get("resolved_requires")
        if resolved_requires is not None and not _non_empty_strings(resolved_requires):
            issues.append(
                f"{contract_location}.resolved_requires: non-empty strings required"
            )
        separation = contract.get("answer_key_separation")
        if separation is not None:
            if not isinstance(separation, dict):
                issues.append(f"{contract_location}.answer_key_separation: object required")
            else:
                if separation.get("status") != "separate":
                    issues.append(
                        f"{contract_location}.answer_key_separation.status: must be separate"
                    )
                if separation.get("public") is not False:
                    issues.append(
                        f"{contract_location}.answer_key_separation.public: must be false"
                    )

        # Records are checked from the payload, not from the contract itself.
        # Contract state describes the workflow container and does not itself
        # require an evidence_ref.
        for key, value in payload.items():
            if key.endswith("_contract"):
                continue
            issues.extend(
                _record_coherence_issues(
                    value,
                    f"{location}.{key}",
                    allowed_set,
                )
            )
    return issues


def _record_coherence_issues(
    value: Any, location: str, allowed_states: set[str]
) -> list[str]:
    issues: list[str] = []
    if isinstance(value, dict):
        state = value.get("state")
        if state is not None:
            if not isinstance(state, str) or not state.strip():
                issues.append(f"{location}.state: non-empty state required")
            elif state not in allowed_states:
                issues.append(f"{location}.state: not declared in allowed_states")
            elif state == "resolved":
                evidence_ref = value.get("evidence_ref")
                if not isinstance(evidence_ref, str) or not evidence_ref.strip():
                    issues.append(
                        f"{location}.evidence_ref: non-empty string required when resolved"
                    )
        if "decision" in value and value["decision"] is not None:
            evidence_ref = value.get("evidence_ref")
            if not isinstance(evidence_ref, str) or not evidence_ref.strip():
                issues.append(
                    f"{location}.evidence_ref: non-empty string required when decision is non-null"
                )
        for key, child in value.items():
            if key not in {"state", "decision", "evidence_ref"}:
                issues.extend(_record_coherence_issues(child, f"{location}.{key}", allowed_states))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            issues.extend(_record_coherence_issues(child, f"{location}[{index}]", allowed_states))
    return issues


def _manifest_issues(payload: Any, root: Path, location: str) -> list[str]:
    """Validate public fixture manifest paths and digests when present."""

    if not isinstance(payload, dict):
        return []
    files = payload.get("files")
    if not isinstance(files, list) or not files or not all(isinstance(item, dict) for item in files):
        return []
    if not all("path" in item and "sha256" in item for item in files):
        return []
    issues: list[str] = []
    file_count = payload.get("file_count")
    if file_count != len(files):
        issues.append(f"{location}.file_count: does not match files length")
    paths = [item.get("path") for item in files]
    if len(paths) != len(set(paths)):
        issues.append(f"{location}.files: duplicate manifest path")
    for index, item in enumerate(files):
        relative = item.get("path")
        digest = item.get("sha256")
        entry_location = f"{location}.files[{index}]"
        if not isinstance(relative, str) or not relative.strip() or Path(relative).is_absolute():
            issues.append(f"{entry_location}.path: repository-relative path required")
            continue
        target = root / Path(relative)
        try:
            target.resolve().relative_to(root.resolve())
        except ValueError:
            issues.append(f"{entry_location}.path: path escapes checkout")
            continue
        if not target.is_file():
            issues.append(f"{entry_location}.path: file is missing")
            continue
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", digest):
            issues.append(f"{entry_location}.sha256: 64-hex digest required")
            continue
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual.casefold() != digest.casefold():
            issues.append(f"{entry_location}.sha256: digest mismatch")
    return issues


def issues_for_file(path: Path, root: Path) -> list[str]:
    """Return value-free structural findings for one scoped file."""

    text = path.read_text(encoding="utf-8")
    issues = _text_structure_issues(text)
    if path.suffix.casefold() not in JSON_SUFFIXES:
        return issues
    try:
        for label, payload in _json_values(path):
            location = f"$[{label}]" if path.suffix.casefold() == ".jsonl" else "$"
            issues.extend(
                f"{location}.{issue}" if issue.startswith("$") else issue
                for issue in forbidden_structure_issues(payload)
            )
            issues.extend(_contract_issues(payload, location))
            issues.extend(_manifest_issues(payload, root, location))
    except json.JSONDecodeError as error:
        issues.append(f"JSON parse error: {error.msg}")
    return issues


def validate_checkout(root: Path = REPOSITORY_ROOT) -> list[str]:
    """Scan a complete checkout and return deterministic, value-free findings."""

    root = root.resolve()
    paths = scoped_paths(root)
    findings: list[str] = []
    exam_payloads = [
        path
        for path in paths
        if path.as_posix().casefold().startswith(PUBLIC_EXAMS_PREFIX.casefold())
        and path.name.casefold() == "domande.md"
    ]
    coordination_names = {path.name for path in paths if path.as_posix().startswith(COORDINATION_PREFIX)}
    if len(exam_payloads) != EXPECTED_PUBLIC_EXAM_PAYLOAD_COUNT:
        findings.append(
            f"{PUBLIC_EXAMS_PREFIX}: expected {EXPECTED_PUBLIC_EXAM_PAYLOAD_COUNT} domande.md payloads, found {len(exam_payloads)}"
        )
    missing = sorted(REQUIRED_COORDINATION_ARTIFACTS - coordination_names)
    findings.extend(f"docs/coordination: missing required artifact {name}" for name in missing)
    if not any(path.as_posix().casefold().startswith(PUBLIC_EXAMS_PREFIX.casefold()) for path in paths):
        findings.append("scope: ESAMI text material is missing")
    if not any(path.as_posix().casefold().startswith(COORDINATION_PREFIX.casefold()) for path in paths):
        findings.append("scope: docs/coordination text material is missing")
    for path in paths:
        absolute = root / path
        findings.extend(f"{path.as_posix()}: {issue}" for issue in issues_for_file(absolute, root))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "checkout",
        nargs="?",
        type=Path,
        default=REPOSITORY_ROOT,
        help="complete Git checkout to scan (default: repository containing this command)",
    )
    args = parser.parse_args()
    try:
        paths = scoped_paths(args.checkout.resolve())
        findings = validate_checkout(args.checkout)
    except (OSError, subprocess.CalledProcessError, UnicodeError) as error:
        print(f"G13-C error: {error}")
        return 2
    if findings:
        print("\n".join(findings))
        return 1
    print(f"valid: G13-C full checkout ({len(paths)} scoped text files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
