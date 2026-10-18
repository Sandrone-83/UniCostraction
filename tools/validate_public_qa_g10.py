"""G10/G11 structural gate for protected exams and provenance audits.

The gate is deliberately negative and metadata-only.  It scans every tracked
text file below ``UNIVERSITA_EDILIZIA/ESAMI`` plus the G9/G10/G11 public audit
artifacts, looking only for structured answer, grading, explanation, solution,
or numeric question-to-value shapes.  G11 integrated artifacts also require a
metadata contract for limitations, states, and answer-key separation.  It
never reads or reconstructs an answer key.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PUBLIC_EXAMS_PREFIX = "UNIVERSITA_EDILIZIA/ESAMI/"
COORDINATION_PREFIX = "docs/coordination/"
PUBLIC_QA_ROOTS = ("docs/coordination", "reports")
EXPECTED_PUBLIC_EXAM_PAYLOAD_COUNT = 73
G11_ARTIFACT_PATHS = frozenset(
    {
        Path("docs/coordination/UNI_CANDIDATE_REVIEW_CLUSTERS_G11.json"),
        Path("docs/coordination/UNI_PRIORITY_QUEUES_G11.json"),
        Path("docs/coordination/UNI_EVIDENCE_LICENSE_MATRIX_G11.json"),
        Path("docs/coordination/UNI_QA_INTEGRATED_G11.md"),
    }
)
TEXT_SUFFIXES = frozenset(
    {".csv", ".json", ".jsonl", ".md", ".rst", ".tsv", ".txt", ".yaml", ".yml"}
)
JSON_SUFFIXES = frozenset({".json", ".jsonl"})
ALLOWED_STATES = frozenset({"blocked", "pending", "open", "resolved"})
CONTRACT_KEYS = frozenset(
    {"audit_contract", "ledger_contract", "publication_contract", "report_contract"}
)
G11_CONTRACT_KEYS = frozenset(
    {
        "candidate_review_contract",
        "priority_queue_contract",
        "evidence_license_matrix_contract",
    }
)

# The names are field names only.  A natural-language occurrence such as
# "quale risposta è corretta" is not a finding unless it has a field shape.
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
        "correct_choice",
        "correct_choices",
        "correct_response",
        "correct_letter",
        "correct_letters",
        "correct_answer_letter",
        "correct_answer_letters",
        "lettera",
        "lettere",
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
        "rationale",
        "motivazione",
        "motivazioni",
        "justification",
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
NUMERIC_MAPPING_PATTERN = re.compile(
    r"^\s*(?:[-*]\s+)?(?:[\"']?)(\d+)(?:[\"']?)\s*[:=]\s*.+$"
)
QUESTION_KEY_PATTERN = re.compile(r"^\d+$")


@lru_cache(maxsize=1)
def _tracked_paths() -> tuple[Path, ...]:
    result = subprocess.run(
        ["git", "-C", str(REPOSITORY_ROOT), "ls-files", "-z"],
        check=True,
        capture_output=True,
    )
    return tuple(
        Path(item.decode("utf-8")) for item in result.stdout.split(b"\0") if item
    )


@lru_cache(maxsize=1)
def public_exam_paths() -> tuple[Path, ...]:
    """Return every tracked file below the public exam directory."""

    return tuple(
        sorted(
            path
            for path in _tracked_paths()
            if path.as_posix().startswith(PUBLIC_EXAMS_PREFIX)
        )
    )


@lru_cache(maxsize=1)
def public_exam_payload_paths() -> tuple[Path, ...]:
    """Return the explicit 73 public ``*/domande.md`` exam payloads."""

    return tuple(
        sorted(
            Path(PUBLIC_EXAMS_PREFIX) / exam_dir.name / "domande.md"
            for exam_dir in (REPOSITORY_ROOT / PUBLIC_EXAMS_PREFIX.rstrip("/")).iterdir()
            if exam_dir.is_dir() and (exam_dir / "domande.md").is_file()
        )
    )


def _is_g9_public_artifact(path: Path) -> bool:
    path_text = path.as_posix()
    if not path_text.startswith(tuple(f"{root}/" for root in PUBLIC_QA_ROOTS)):
        return False
    if path.suffix.casefold() not in TEXT_SUFFIXES:
        return False
    return any(
        marker in path.name.casefold()
        for marker in ("ledger", "manifest", "report", "readiness", "remediation")
    )


def _is_g10_audit(path: Path) -> bool:
    path_text = path.as_posix().casefold()
    name = path.name.casefold()
    return (
        path_text.startswith(COORDINATION_PREFIX.casefold())
        and path.suffix.casefold() in TEXT_SUFFIXES
        and "g10" in name
        and any(marker in name for marker in ("audit", "provenance", "redundancy", "qa"))
    )


def _is_g11_integrated_artifact(path: Path) -> bool:
    """Recognise only the checked-in G11 integrated QA artifact set."""

    return path in G11_ARTIFACT_PATHS and path.suffix.casefold() in TEXT_SUFFIXES


def public_artifact_paths() -> tuple[Path, ...]:
    """Return all public exams and G9/G10/G11 audit artifacts."""

    exam_paths = set(public_exam_paths())
    existing_g11_paths = {
        path for path in G11_ARTIFACT_PATHS if (REPOSITORY_ROOT / path).is_file()
    }
    paths = {
        path
        for path in _tracked_paths()
        if (
            path in exam_paths
            or _is_g9_public_artifact(path)
            or _is_g10_audit(path)
            or _is_g11_integrated_artifact(path)
        )
    }
    return tuple(sorted(paths | existing_g11_paths))


def _normalise_field_name(name: str) -> str:
    return re.sub(r"[\s-]+", "_", name.casefold().strip())


def _looks_like_numeric_scalar_map(value: dict[Any, Any]) -> bool:
    """Detect a question-number to scalar map by shape only."""

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
    """Return findings without including any field value or answer text."""

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


def _text_numeric_map_issues(text: str) -> list[str]:
    positions = [
        line_number
        for line_number, line in enumerate(text.splitlines(), start=1)
        if NUMERIC_MAPPING_PATTERN.match(line)
    ]
    if len(positions) < 3:
        return []
    return [
        f"lines {positions[0]}-{positions[-1]}: numeric question-to-scalar map"
    ]


def _text_structure_issues(text: str) -> list[str]:
    issues = [
        f"line {line_number}: forbidden structured field"
        for line_number, line in enumerate(text.splitlines(), start=1)
        if not DOCUMENTARY_MARKER_PATTERN.search(line)
        if STRUCTURED_FIELD_PATTERN.search(line)
    ]
    issues.extend(_text_numeric_map_issues(text))
    return issues


def _json_values(path: Path) -> Iterable[Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.casefold() == ".jsonl":
        return (json.loads(line) for line in text.splitlines() if line.strip())
    return (json.loads(text),)


def _non_empty_strings(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(
        isinstance(item, str) and item.strip() for item in value
    )


def _contract_issues(payload: Any) -> list[str]:
    if not isinstance(payload, dict):
        return ["$: public audit artifact must be a JSON object"]
    found = next(
        (
            (key, value)
            for key, value in payload.items()
            if key in CONTRACT_KEYS | G11_CONTRACT_KEYS and isinstance(value, dict)
        ),
        None,
    )
    if found is None:
        return ["$: missing public QA or audit contract"]

    contract_name, contract = found
    issues: list[str] = []
    if not _non_empty_strings(contract.get("limitations")):
        issues.append(f"$.{contract_name}.limitations: non-empty strings required")
    allowed = contract.get("allowed_states")
    if not _non_empty_strings(allowed):
        issues.append(f"$.{contract_name}.allowed_states: non-empty strings required")
        allowed_set: set[str] = set()
    else:
        allowed_set = set(allowed)
        if not allowed_set <= ALLOWED_STATES:
            issues.append(
                f"$.{contract_name}.allowed_states: only {sorted(ALLOWED_STATES)} allowed"
            )
    state = contract.get("state")
    if state is not None and state not in allowed_set:
        issues.append(f"$.{contract_name}.state: state is not declared in allowed_states")
    if contract_name in G11_CONTRACT_KEYS:
        if state is None:
            issues.append(f"$.{contract_name}.state: required for G11 integrated artifacts")
        separation = contract.get("answer_key_separation")
        if not isinstance(separation, dict):
            issues.append(
                f"$.{contract_name}.answer_key_separation: metadata object required"
            )
        else:
            if separation.get("status") != "separate":
                issues.append(
                    f"$.{contract_name}.answer_key_separation.status: must be separate"
                )
            if separation.get("public") is not False:
                issues.append(
                    f"$.{contract_name}.answer_key_separation.public: must be false"
                )
    return issues


def issues_for_file(path: Path) -> list[str]:
    """Validate a public text artifact while keeping findings value-free."""

    if path.suffix.casefold() not in TEXT_SUFFIXES:
        return [f"{path}: unsupported non-text public artifact"]
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


def integrated_g11_contract_issues(path: Path) -> list[str]:
    """Apply the G11 contract to one known integrated JSON artifact."""

    if path not in G11_ARTIFACT_PATHS or path.suffix.casefold() != ".json":
        return []
    try:
        payload = next(iter(_json_values(REPOSITORY_ROOT / path)))
    except (FileNotFoundError, json.JSONDecodeError) as error:
        return [f"{path.as_posix()}: invalid G11 JSON artifact ({error})"]
    return _contract_issues(payload)


def validate_public_artifacts(root: Path = REPOSITORY_ROOT) -> list[str]:
    if root != REPOSITORY_ROOT:
        raise ValueError("the G10 checker is bound to its repository root")
    findings = [
        f"{path.as_posix()}: {issue}"
        for path in public_artifact_paths()
        for issue in issues_for_file(REPOSITORY_ROOT / path)
    ]
    payload_paths = public_exam_payload_paths()
    if len(payload_paths) != EXPECTED_PUBLIC_EXAM_PAYLOAD_COUNT:
        findings.append(
            "UNIVERSITA_EDILIZIA/ESAMI: expected "
            f"{EXPECTED_PUBLIC_EXAM_PAYLOAD_COUNT} explicit domande.md payloads, "
            f"found {len(payload_paths)}"
        )
    findings.extend(
        f"{path.as_posix()}: {issue}"
        for path in payload_paths
        for issue in issues_for_file(REPOSITORY_ROOT / path)
        if path not in public_artifact_paths()
    )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
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
    print(
        f"valid: {len(args.paths) or len(public_artifact_paths())} public G10/G11 artifacts"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
