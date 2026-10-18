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
from collections import Counter
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
G14_CONTRACT_KEYS = frozenset(
    {
        "cluster_progress_contract",
        "per_pack_queue_contract",
    }
)
G14_COLLECTION_KEYS = {
    "cluster_progress_contract": "cluster_progress_registries",
    "per_pack_queue_contract": "per_pack_queue",
}
G14_REQUIRED_RECORD_FIELDS = frozenset({"evidence_ref", "reviewer", "rationale"})
G14_REQUIRED_UNRESOLVED_STATES = frozenset({"blocked", "open"})
G14_PROMOTION_KEYS = frozenset(
    {
        "promoted",
        "promotion",
        "promotion_status",
        "promotion_state",
        "promoted_to",
        "published",
        "publication_status",
        "released",
        "release_status",
        "approved",
        "approval_status",
    }
)
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
        "UNI_CLUSTER_PROGRESS_REGISTRY_G14.json",
        "UNI_PER_PACK_QUEUE_G14.json",
        "UNI_QA_WORKFLOW_EVIDENCE_G14.md",
    }
)

# G15-C freezes the metadata-only report inventory that G10-G14 expose.  The
# values are workflow counts, not content or correctness claims.  Keeping the
# expected state counts here makes a missing, duplicated, or silently promoted
# report fail closed during a full-checkout scan.
G15_REPORT_SPECS: dict[str, dict[str, Any]] = {
    "UNI_PROVENANCE_AUDIT_G10.json": {
        "state_paths": ("audit_contract.state", "provenance_review.state"),
        "count_paths": {"scope.file_count": 76, "scope.text_file_count": 76},
        "source_manifest": "docs/coordination/PUBLIC_EXAM_FIXTURE_MANIFEST_G3.json",
    },
    "UNI_REDUNDANCY_AUDIT_G10.json": {
        "state_paths": ("audit_contract.state", "duplicate_review.state"),
        "count_paths": {"scope.file_count": 76, "scope.text_file_count": 76},
    },
    "UNI_CANDIDATE_REVIEW_CLUSTERS_G11.json": {
        "state_paths": ("candidate_review_contract.state",),
        "collections": {"candidate_review_clusters": {"count": 1, "states": {"pending": 1}}},
    },
    "UNI_PRIORITY_QUEUES_G11.json": {
        "state_paths": ("priority_queue_contract.state",),
        "collections": {"priority_queues": {"count": 1, "states": {"open": 1}}},
    },
    "UNI_EVIDENCE_LICENSE_MATRIX_G11.json": {
        "state_paths": ("evidence_license_matrix_contract.state",),
        "collections": {"evidence_license_matrix": {"count": 1, "states": {"pending": 1}}},
    },
    "UNI_REDUNDANCY_DECISION_RECORDS_G12.json": {
        "state_paths": ("redundancy_decision_contract.state",),
        "collections": {"redundancy_decision_records": {"count": 1, "states": {"pending": 1}}},
    },
    "UNI_SOURCE_LICENSE_CHECKLIST_G12.json": {
        "state_paths": ("source_license_checklist_contract.state",),
        "collections": {"source_license_checklist": {"count": 2, "states": {"pending": 2}}},
    },
    "UNI_CLUSTER_PROGRESS_REGISTRY_G14.json": {
        "state_paths": ("cluster_progress_contract.state",),
        "collections": {
            "cluster_progress_registries": {
                "count": 2,
                "states": {"blocked": 1, "open": 1},
            }
        },
    },
    "UNI_PER_PACK_QUEUE_G14.json": {
        "state_paths": ("per_pack_queue_contract.state",),
        "collections": {"per_pack_queue": {"count": 2, "states": {"blocked": 1, "open": 1}}},
    },
}
EXPECTED_PUBLIC_EXAM_FILE_COUNT = 76

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


def determinism_issues(
    root: Path = REPOSITORY_ROOT, paths: tuple[Path, ...] | None = None
) -> list[str]:
    """Check that the full-checkout inventory has a stable, unique order."""

    root = root.resolve()
    first = scoped_paths(root) if paths is None else tuple(paths)
    second = scoped_paths(root)
    issues: list[str] = []
    if first != second:
        issues.append("scope: repeated tracked-path inventory is not deterministic")
    if first != tuple(sorted(first)):
        issues.append("scope: tracked-path inventory is not sorted")
    if len(first) != len(set(first)):
        issues.append("scope: tracked-path inventory contains duplicates")
    return issues


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

        if contract_name in G14_CONTRACT_KEYS:
            required_fields = contract.get("record_requirements")
            if not _non_empty_strings(required_fields) or not G14_REQUIRED_RECORD_FIELDS <= set(
                required_fields
            ):
                issues.append(
                    f"{contract_location}.record_requirements: evidence_ref, reviewer and rationale required"
                )
            unresolved = contract.get("required_unresolved_states")
            if not _non_empty_strings(unresolved) or not G14_REQUIRED_UNRESOLVED_STATES <= set(
                unresolved
            ):
                issues.append(
                    f"{contract_location}.required_unresolved_states: blocked and open required"
                )
            collection_name = G14_COLLECTION_KEYS[contract_name]
            records = payload.get(collection_name)
            if not isinstance(records, list) or not records:
                issues.append(f"{location}.{collection_name}: non-empty list required")
            else:
                seen_states: set[str] = set()
                for index, record in enumerate(records):
                    record_location = f"{location}.{collection_name}[{index}]"
                    issues.extend(_g14_record_issues(record, record_location, allowed_set))
                    if isinstance(record, dict) and isinstance(record.get("state"), str):
                        seen_states.add(record["state"])
                missing_states = sorted(G14_REQUIRED_UNRESOLVED_STATES - seen_states)
                issues.extend(
                    f"{location}.{collection_name}: missing workflow state {state}"
                    for state in missing_states
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


def _normalise_key(key: str) -> str:
    return re.sub(r"[\s-]+", "_", key.casefold().strip())


def _promotion_issues(value: Any, location: str) -> list[str]:
    """Reject positive publication/promotion flags in G14 workflow records."""

    issues: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if isinstance(key, str) and _normalise_key(key) in G14_PROMOTION_KEYS:
                safe_values = {
                    None,
                    False,
                    "",
                    "none",
                    "not_promoted",
                    "not_published",
                    "not_released",
                    "not_approved",
                    "placeholder",
                }
                normalised_value = (
                    _normalise_key(child) if isinstance(child, str) else child
                )
                if normalised_value not in safe_values:
                    issues.append(f"{location}.{key}: promotion/publication must remain negative")
            issues.extend(_promotion_issues(child, f"{location}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            issues.extend(_promotion_issues(child, f"{location}[{index}]"))
    return issues


def _g14_record_issues(
    record: Any, location: str, allowed_states: set[str]
) -> list[str]:
    """Validate the required evidence workflow shape for G14-C records."""

    if not isinstance(record, dict):
        return [f"{location}: record must be an object"]
    issues: list[str] = []
    state = record.get("state")
    if not isinstance(state, str) or not state.strip():
        issues.append(f"{location}.state: non-empty state required")
    elif state not in allowed_states:
        issues.append(f"{location}.state: not declared in allowed_states")
    for field in sorted(G14_REQUIRED_RECORD_FIELDS):
        value = record.get(field)
        if not isinstance(value, str) or not value.strip():
            issues.append(f"{location}.{field}: non-empty string required")
    if state in {"blocked", "open"}:
        if record.get("decision") is not None:
            issues.append(f"{location}.decision: blocked/open records cannot carry a decision")
        if record.get("resolved") is True:
            issues.append(f"{location}.resolved: blocked/open records cannot be resolved")
    issues.extend(_promotion_issues(record, location))
    return issues


_MISSING = object()


def _value_at_path(payload: Any, dotted_path: str) -> Any:
    value = payload
    for part in dotted_path.split("."):
        if not isinstance(value, dict) or part not in value:
            return _MISSING
        value = value[part]
    return value


def _state_counts(records: Any) -> Counter[str]:
    if not isinstance(records, list):
        return Counter({"<not-a-list>": 1})
    counts: Counter[str] = Counter()
    for record in records:
        if not isinstance(record, dict):
            counts["<non-object>"] += 1
            continue
        state = record.get("state")
        counts[state if isinstance(state, str) and state.strip() else "<missing>"] += 1
    return counts


def report_state_count_issues(root: Path = REPOSITORY_ROOT) -> list[str]:
    """Validate deterministic states and cardinalities for G10-G14 reports."""

    root = root.resolve()
    issues: list[str] = []
    tracked = frozenset(_tracked_paths(root))
    for filename, spec in sorted(G15_REPORT_SPECS.items()):
        relative = Path(COORDINATION_PREFIX) / filename
        location = f"{relative.as_posix()}"
        path = root / relative
        if relative not in tracked or not path.is_file():
            issues.append(f"{location}: required report is missing or untracked")
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            issues.append(f"{location}: cannot read JSON report ({error})")
            continue
        if not isinstance(payload, dict):
            issues.append(f"{location}: report must be a JSON object")
            continue

        for state_path in spec.get("state_paths", ()):
            value = _value_at_path(payload, state_path)
            if not isinstance(value, str) or value not in ALLOWED_STATES:
                issues.append(
                    f"{location}.{state_path}: state must be one of {sorted(ALLOWED_STATES)}"
                )

        for count_path, expected in spec.get("count_paths", {}).items():
            value = _value_at_path(payload, count_path)
            if value != expected:
                issues.append(
                    f"{location}.{count_path}: expected count {expected}, found {value!r}"
                )

        for collection_name, contract in spec.get("collections", {}).items():
            records = payload.get(collection_name, _MISSING)
            expected_count = contract["count"]
            expected_states = Counter(contract["states"])
            if not isinstance(records, list):
                issues.append(f"{location}.{collection_name}: expected list")
                continue
            if len(records) != expected_count:
                issues.append(
                    f"{location}.{collection_name}: expected count {expected_count}, found {len(records)}"
                )
            actual_states = _state_counts(records)
            if actual_states != expected_states:
                issues.append(
                    f"{location}.{collection_name}: expected state counts "
                    f"{dict(sorted(expected_states.items()))}, found {dict(sorted(actual_states.items()))}"
                )

        source_manifest = spec.get("source_manifest")
        if isinstance(source_manifest, str):
            manifest_path = Path(source_manifest)
            if manifest_path not in tracked or not (root / manifest_path).is_file():
                issues.append(
                    f"{location}.scope.source_manifest: tracked manifest is missing"
                )
    return issues


def _manifest_issues(
    payload: Any,
    root: Path,
    location: str,
    tracked_paths: frozenset[Path] | None = None,
) -> list[str]:
    """Validate public fixture manifest paths and digests when present."""

    if not isinstance(payload, dict):
        return []
    files = payload.get("files")
    if not isinstance(files, list) or not files or not all(isinstance(item, dict) for item in files):
        return []
    if not all("path" in item and "sha256" in item for item in files):
        return []
    issues: list[str] = []
    if payload.get("algorithm") != "sha256":
        issues.append(f"{location}.algorithm: sha256 required")
    file_count = payload.get("file_count")
    if file_count != len(files):
        issues.append(f"{location}.file_count: does not match files length")
    paths = [item.get("path") for item in files]
    if len(paths) != len(set(paths)):
        issues.append(f"{location}.files: duplicate manifest path")
    string_paths = [path for path in paths if isinstance(path, str)]
    if len(string_paths) != len({path.casefold() for path in string_paths}):
        issues.append(f"{location}.files: duplicate manifest path by case")
    if string_paths != sorted(string_paths):
        issues.append(f"{location}.files: paths must be sorted deterministically")
    if tracked_paths is None:
        tracked_paths = frozenset(_tracked_paths(root))
    for index, item in enumerate(files):
        relative = item.get("path")
        digest = item.get("sha256")
        entry_location = f"{location}.files[{index}]"
        if (
            not isinstance(relative, str)
            or not relative.strip()
            or "\\" in relative
            or Path(relative).is_absolute()
            or relative != Path(relative).as_posix()
            or any(part in {"", ".", ".."} for part in Path(relative).parts)
        ):
            issues.append(
                f"{entry_location}.path: normalized repository-relative POSIX path required"
            )
            continue
        relative_path = Path(relative)
        if relative_path not in tracked_paths:
            issues.append(f"{entry_location}.path: path is not tracked by Git")
        target = root / relative_path
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


def issues_for_file(
    path: Path, root: Path, tracked_paths: frozenset[Path] | None = None
) -> list[str]:
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
            issues.extend(_manifest_issues(payload, root, location, tracked_paths))
    except json.JSONDecodeError as error:
        issues.append(f"JSON parse error: {error.msg}")
    return issues


def validate_checkout(root: Path = REPOSITORY_ROOT) -> list[str]:
    """Scan a complete checkout and return deterministic, value-free findings."""

    root = root.resolve()
    tracked_paths = frozenset(_tracked_paths(root))
    paths = scoped_paths(root)
    findings: list[str] = []
    findings.extend(determinism_issues(root, paths))
    exam_payloads = [
        path
        for path in paths
        if path.as_posix().casefold().startswith(PUBLIC_EXAMS_PREFIX.casefold())
        and path.name.casefold() == "domande.md"
    ]
    exam_text_files = [
        path
        for path in paths
        if path.as_posix().casefold().startswith(PUBLIC_EXAMS_PREFIX.casefold())
    ]
    coordination_names = {path.name for path in paths if path.as_posix().startswith(COORDINATION_PREFIX)}
    if len(exam_payloads) != EXPECTED_PUBLIC_EXAM_PAYLOAD_COUNT:
        findings.append(
            f"{PUBLIC_EXAMS_PREFIX}: expected {EXPECTED_PUBLIC_EXAM_PAYLOAD_COUNT} domande.md payloads, found {len(exam_payloads)}"
        )
    if len(exam_text_files) != EXPECTED_PUBLIC_EXAM_FILE_COUNT:
        findings.append(
            f"{PUBLIC_EXAMS_PREFIX}: expected {EXPECTED_PUBLIC_EXAM_FILE_COUNT} text files, found {len(exam_text_files)}"
        )
    missing = sorted(REQUIRED_COORDINATION_ARTIFACTS - coordination_names)
    findings.extend(f"docs/coordination: missing required artifact {name}" for name in missing)
    findings.extend(report_state_count_issues(root))
    if not any(path.as_posix().casefold().startswith(PUBLIC_EXAMS_PREFIX.casefold()) for path in paths):
        findings.append("scope: ESAMI text material is missing")
    if not any(path.as_posix().casefold().startswith(COORDINATION_PREFIX.casefold()) for path in paths):
        findings.append("scope: docs/coordination text material is missing")
    for path in paths:
        absolute = root / path
        findings.extend(
            f"{path.as_posix()}: {issue}"
            for issue in issues_for_file(absolute, root, tracked_paths)
        )
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
