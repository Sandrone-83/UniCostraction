"""G20/G23/G24/G25/G26 structural validator for skill evaluation cases.

The validator checks the evaluation contract and its one-to-one relationship
with the skill IDs declared by ``manifest.json``.  It deliberately validates
metadata and shape only: it does not score model outputs, resolve evidence,
or establish factual, educational, professional, legal, or safety
correctness.
"""

from __future__ import annotations

from datetime import date

import argparse
import json
import re
from pathlib import Path
from typing import Any, Iterable


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LIBRARY = REPOSITORY_ROOT / "skills"
MANIFEST_NAME = "manifest.json"
EVALS_RELATIVE_PATH = Path("evals") / "evals.json"

REQUIRED_EVAL_FIELDS = frozenset(
    {
        "case_id",
        "skill_id",
        "prompt",
        "boundary",
        "evidence",
        "rubric",
        "negative_case",
        "negative_case_markers",
    }
)
ALLOWED_EVAL_FIELDS = REQUIRED_EVAL_FIELDS
PUBLISHED_EVAL_FIELDS = frozenset(
    {
        "case_id",
        "skill_id",
        "prompt",
        "expected_behavior",
        "required_boundaries",
        "evidence_expectation",
        "grading_rubric",
    }
)
PUBLISHED_ENVELOPE_REQUIRED_FIELDS = frozenset(
    {
        "schema_version",
        "library",
        "milestone",
        "purpose",
        "rights_and_safety",
        "cases",
    }
)
PUBLISHED_ENVELOPE_ALLOWED_FIELDS = PUBLISHED_ENVELOPE_REQUIRED_FIELDS
PUBLISHED_SCHEMA_VERSION = "g19-skill-library-evals-1"
PUBLISHED_MANIFEST_FIELDS = frozenset(
    {"library", "version", "generated_at", "skills", "rights_policy"}
)
PUBLISHED_MANIFEST_ENTRY_FIELDS = frozenset(
    {"id", "path", "title", "domain", "scope", "source_refs", "rights_state"}
)
PUBLISHED_SOURCE_REF_FIELDS = frozenset({"url", "authority", "purpose", "rights_state"})
MANIFEST_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MANIFEST_SKILL_PATH_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*/SKILL\.md$")
RIGHTS_AND_SAFETY_FIELDS = frozenset(
    {
        "content_origin",
        "source_policy",
        "evaluation_limit",
        "escalation_policy",
    }
)
GRADING_RUBRIC_LEVELS = frozenset({"score_0", "score_2", "score_4"})
SAFE_NEGATIVE_CASE_MARKERS = frozenset(
    {
        "ambiguous-input",
        "conflicting-evidence",
        "missing-context",
        "out-of-scope",
        "professional-review-required",
        "unsafe-automation",
    }
)
FORBIDDEN_ANSWER_KEY_FIELDS = frozenset(
    {
        "answer",
        "answerkey",
        "answer_key",
        "correctanswer",
        "correct_answer",
        "expectedanswer",
        "expected_answer",
        "goldanswer",
        "gold_answer",
        "referenceanswer",
        "reference_answer",
        "solution",
        "targetanswer",
        "target_answer",
    }
)
SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MILESTONE_PATTERN = re.compile(r"^G[0-9]+$")
PROFESSIONAL_BOUNDARY_PATTERN = re.compile(
    r"\b(?:do not|never|non|professional|qualified|competent|authority|authori[sz]|"
    r"approval|approve|certif|legal|compliance|signature|escalat|stop-work|without)\b",
    re.IGNORECASE,
)

class DuplicateJSONKeyError(ValueError):
    """Raised when a JSON object repeats a key."""


def _object_pairs_without_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJSONKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_object_pairs_without_duplicates)


def _is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())

def _is_iso_date(value: Any) -> bool:
    if not isinstance(value, str) or not MANIFEST_DATE_PATTERN.fullmatch(value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _is_slug(value: Any) -> bool:
    return isinstance(value, str) and bool(SLUG_PATTERN.fullmatch(value))


def _non_empty_string_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(_is_non_empty_string(item) for item in value)


def _non_empty_string_mapping(value: Any) -> bool:
    return (
        isinstance(value, dict)
        and bool(value)
        and all(_is_non_empty_string(key) and _is_non_empty_string(item) for key, item in value.items())
    )


def _published_manifest_issues(manifest: Any, location: str) -> list[str]:
    """Validate the published manifest envelope when its metadata is present."""

    if not isinstance(manifest, dict):
        return []
    metadata_fields = PUBLISHED_MANIFEST_FIELDS - {"skills"}
    if not any(field in manifest for field in metadata_fields):
        return []

    issues: list[str] = []
    missing = sorted(PUBLISHED_MANIFEST_FIELDS - set(manifest))
    issues.extend(f"{location}: missing required field {field}" for field in missing)
    unknown = sorted(set(manifest) - PUBLISHED_MANIFEST_FIELDS)
    issues.extend(f"{location}: unknown field {field}" for field in unknown)

    for field in ("library", "version", "rights_policy"):
        if field in manifest and not _is_non_empty_string(manifest[field]):
            issues.append(f"{location}.{field}: non-empty string required")
    generated_at = manifest.get("generated_at")
    if not _is_iso_date(generated_at):
        if "generated_at" in manifest:
            issues.append(f"{location}.generated_at: YYYY-MM-DD date required")

    skills = manifest.get("skills")
    if not isinstance(skills, list) or not skills:
        if "skills" in manifest:
            issues.append(f"{location}.skills: non-empty list required")
        return issues

    seen_paths: set[str] = set()
    for index, entry in enumerate(skills):
        entry_location = f"{location}.skills[{index}]"
        if not isinstance(entry, dict):
            issues.append(f"{entry_location}: manifest entry must be an object")
            continue
        missing_entry = sorted(PUBLISHED_MANIFEST_ENTRY_FIELDS - set(entry))
        issues.extend(f"{entry_location}: missing required field {field}" for field in missing_entry)
        unknown_entry = sorted(set(entry) - PUBLISHED_MANIFEST_ENTRY_FIELDS)
        issues.extend(f"{entry_location}: unknown field {field}" for field in unknown_entry)
        for field in ("id", "path", "title", "domain", "scope", "rights_state"):
            if field in entry and not _is_non_empty_string(entry[field]):
                issues.append(f"{entry_location}.{field}: non-empty string required")
        skill_id = entry.get("id")
        if "id" in entry and not _is_slug(skill_id):
            issues.append(f"{entry_location}.id: lowercase hyphenated skill ID required")
        skill_path = entry.get("path")
        if "path" in entry and (
            not isinstance(skill_path, str)
            or not MANIFEST_SKILL_PATH_PATTERN.fullmatch(skill_path)
            or (isinstance(skill_id, str) and skill_path != f"{skill_id}/SKILL.md")
        ):
            issues.append(f"{entry_location}.path: normalized <skill-id>/SKILL.md path required")
        elif skill_path in seen_paths:
            issues.append(f"{entry_location}.path: duplicate exact skill path")
        elif isinstance(skill_path, str):
            seen_paths.add(skill_path)

        source_refs = entry.get("source_refs")
        if not isinstance(source_refs, list) or not source_refs:
            if "source_refs" in entry:
                issues.append(f"{entry_location}.source_refs: non-empty list required")
            continue
        for source_index, source in enumerate(source_refs):
            source_location = f"{entry_location}.source_refs[{source_index}]"
            if not isinstance(source, dict):
                issues.append(f"{source_location}: source reference must be an object")
                continue
            missing_source = sorted(PUBLISHED_SOURCE_REF_FIELDS - set(source))
            issues.extend(f"{source_location}: missing required field {field}" for field in missing_source)
            unknown_source = sorted(set(source) - PUBLISHED_SOURCE_REF_FIELDS)
            issues.extend(f"{source_location}: unknown field {field}" for field in unknown_source)
            for field in PUBLISHED_SOURCE_REF_FIELDS:
                if field in source and not _is_non_empty_string(source[field]):
                    issues.append(f"{source_location}.{field}: non-empty string required")
    return issues


def _manifest_skill_ids(manifest: Any) -> tuple[set[str], list[str]]:
    """Return valid manifest IDs and deterministic manifest findings."""

    if not isinstance(manifest, dict):
        return set(), ["manifest.json: JSON object required"]

    skills = manifest.get("skills")
    if not isinstance(skills, list) or not skills:
        return set(), ["manifest.json.skills: non-empty list required"]

    findings: list[str] = []
    skill_ids: set[str] = set()
    for index, entry in enumerate(skills):
        location = f"manifest.json.skills[{index}]"
        if not isinstance(entry, dict):
            findings.append(f"{location}: manifest entry must be an object")
            continue
        if "id" not in entry:
            findings.append(f"{location}: missing required field id")
            continue
        skill_id = entry["id"]
        if not _is_slug(skill_id):
            findings.append(f"{location}.id: lowercase hyphenated skill ID required")
            continue
        if skill_id in skill_ids:
            findings.append(f"{location}.id: duplicate exact skill ID")
        skill_ids.add(skill_id)
    return skill_ids, findings


def _normalised_field_name(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return value.casefold().replace("-", "").replace(" ", "")


_FORBIDDEN_NORMALISED_FIELDS = frozenset(_normalised_field_name(field) for field in FORBIDDEN_ANSWER_KEY_FIELDS)


def _answer_key_findings(value: Any, location: str) -> Iterable[str]:
    if isinstance(value, dict):
        for key, child in value.items():
            if _normalised_field_name(key) in _FORBIDDEN_NORMALISED_FIELDS:
                yield f"{location}.{key}: answer-key field is prohibited"
            yield from _answer_key_findings(child, f"{location}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _answer_key_findings(child, f"{location}[{index}]")


def _published_envelope_issues(
    envelope: dict[str, Any],
    manifest: Any,
    location: str,
    expected_milestone: str | None = None,
) -> list[str]:
    issues: list[str] = []
    missing = sorted(PUBLISHED_ENVELOPE_REQUIRED_FIELDS - set(envelope))
    issues.extend(f"{location}: missing required field {field}" for field in missing)
    unknown = sorted(set(envelope) - PUBLISHED_ENVELOPE_ALLOWED_FIELDS)
    issues.extend(f"{location}: unknown field {field}" for field in unknown)

    if envelope.get("schema_version") != PUBLISHED_SCHEMA_VERSION:
        issues.append(f"{location}.schema_version: exact value {PUBLISHED_SCHEMA_VERSION} required")
    for field in ("library", "purpose"):
        if field in envelope and not _is_non_empty_string(envelope[field]):
            issues.append(f"{location}.{field}: non-empty string required")
    milestone = envelope.get("milestone")
    if not _is_non_empty_string(milestone) or not MILESTONE_PATTERN.fullmatch(milestone):
        if "milestone" in envelope:
            issues.append(f"{location}.milestone: G<number> milestone required")
    if expected_milestone is not None:
        if not isinstance(expected_milestone, str) or not MILESTONE_PATTERN.fullmatch(expected_milestone):
            issues.append(f"{location}.milestone: expected selector G<number> required")
        elif milestone != expected_milestone:
            issues.append(f"{location}.milestone: expected {expected_milestone}")

    manifest_library = manifest.get("library") if isinstance(manifest, dict) else None
    if _is_non_empty_string(manifest_library) and _is_non_empty_string(envelope.get("library")):
        if envelope["library"] != manifest_library:
            issues.append(f"{location}.library: must match manifest.json.library")

    rights = envelope.get("rights_and_safety")
    if not isinstance(rights, dict):
        if "rights_and_safety" in envelope:
            issues.append(f"{location}.rights_and_safety: object required")
    else:
        missing_rights = sorted(RIGHTS_AND_SAFETY_FIELDS - set(rights))
        issues.extend(f"{location}.rights_and_safety: missing required field {field}" for field in missing_rights)
        unknown_rights = sorted(set(rights) - RIGHTS_AND_SAFETY_FIELDS)
        issues.extend(f"{location}.rights_and_safety: unknown field {field}" for field in unknown_rights)
        for field in sorted(RIGHTS_AND_SAFETY_FIELDS):
            if field in rights and not _is_non_empty_string(rights[field]):
                issues.append(f"{location}.rights_and_safety.{field}: non-empty string required")

    cases = envelope.get("cases")
    if not isinstance(cases, list) or not cases:
        if "cases" in envelope:
            issues.append(f"{location}.cases: non-empty list required")
    return issues


def _evaluation_cases(payload: Any) -> tuple[list[Any] | None, bool]:
    """Return cases and whether the payload is the published envelope form."""

    if isinstance(payload, dict):
        cases = payload.get("cases")
        return (cases if isinstance(cases, list) else None), True
    return (payload if isinstance(payload, list) else None), False

def _eval_field_issues(record: Any, location: str, published_schema: bool | None = None):
    if not isinstance(record, dict):
        return [f"{location}: evaluation case must be an object"]

    issues: list[str] = []
    if published_schema is None:
        published_schema = any(field in record for field in (PUBLISHED_EVAL_FIELDS - {"case_id", "skill_id", "prompt"}))
    required_fields = PUBLISHED_EVAL_FIELDS if published_schema else REQUIRED_EVAL_FIELDS
    allowed_fields = PUBLISHED_EVAL_FIELDS if published_schema else ALLOWED_EVAL_FIELDS
    missing = sorted(required_fields - set(record))
    issues.extend(f"{location}: missing required field {field}" for field in missing)
    unknown = sorted(set(record) - allowed_fields)
    issues.extend(f"{location}: unknown field {field}" for field in unknown)
    issues.extend(_answer_key_findings(record, location))

    for field in ("case_id", "skill_id", "prompt"):
        if field in record and not _is_non_empty_string(record[field]):
            issues.append(f"{location}.{field}: non-empty string required")
    if "case_id" in record and not _is_slug(record["case_id"]):
        issues.append(f"{location}.case_id: lowercase hyphenated case ID required")
    if "skill_id" in record and not _is_slug(record["skill_id"]):
        issues.append(f"{location}.skill_id: lowercase hyphenated skill ID required")

    if published_schema:
        for field in ("expected_behavior", "required_boundaries", "evidence_expectation"):
            if field in record and not _non_empty_string_list(record[field]):
                issues.append(f"{location}.{field}: non-empty list of strings required")
        grading = record.get("grading_rubric")
        if not _non_empty_string_mapping(grading):
            if "grading_rubric" in record:
                issues.append(f"{location}.grading_rubric: non-empty string mapping required")
        elif set(grading) != GRADING_RUBRIC_LEVELS:
            missing_levels = sorted(GRADING_RUBRIC_LEVELS - set(grading))
            extra_levels = sorted(set(grading) - GRADING_RUBRIC_LEVELS)
            if missing_levels:
                issues.append(f"{location}.grading_rubric: missing score levels {', '.join(missing_levels)}")
            if extra_levels:
                issues.append(f"{location}.grading_rubric: unknown score levels {', '.join(extra_levels)}")
        boundaries = record.get("required_boundaries")
        if _non_empty_string_list(boundaries) and not any(
            PROFESSIONAL_BOUNDARY_PATTERN.search(item) for item in boundaries
        ):
            issues.append(f"{location}.required_boundaries: explicit professional boundary marker required")
        return issues
    if "boundary" in record and not _is_non_empty_string(record["boundary"]):
        issues.append(f"{location}.boundary: non-empty string required")
    if "evidence" in record and not _non_empty_string_list(record["evidence"]):
        issues.append(f"{location}.evidence: non-empty list of strings required")
    if "rubric" in record and not _non_empty_string_list(record["rubric"]):
        issues.append(f"{location}.rubric: non-empty list of strings required")

    negative_case = record.get("negative_case")
    if not isinstance(negative_case, bool):
        if "negative_case" in record:
            issues.append(f"{location}.negative_case: boolean required")
    markers = record.get("negative_case_markers")
    if not isinstance(markers, list) or any(not _is_non_empty_string(marker) for marker in markers):
        if "negative_case_markers" in record:
            issues.append(f"{location}.negative_case_markers: list of non-empty strings required")
    else:
        marker_set = set(markers)
        for marker in sorted(marker_set - SAFE_NEGATIVE_CASE_MARKERS):
            issues.append(f"{location}.negative_case_markers: unsupported safe marker {marker}")
        if len(marker_set) != len(markers):
            issues.append(f"{location}.negative_case_markers: duplicate marker")
        if negative_case is True and not markers:
            issues.append(f"{location}.negative_case_markers: at least one marker required for negative case")
        if negative_case is False and markers:
            issues.append(f"{location}.negative_case_markers: must be empty for non-negative case")
    return issues

def validate_evals(
    manifest: Any,
    evaluations: Any,
    expected_milestone: str | None = None,
) -> list[str]:
    """Validate in-memory data; an optional selector pins the published milestone exactly."""

    manifest_ids, findings = _manifest_skill_ids(manifest)
    findings.extend(_published_manifest_issues(manifest, "manifest.json"))
    findings.extend(_answer_key_findings(manifest, "manifest.json"))
    cases, published_envelope = _evaluation_cases(evaluations)
    if published_envelope and isinstance(evaluations, dict):
        findings.extend(_published_envelope_issues(evaluations, manifest, "evals/evals.json", expected_milestone))
        findings.extend(_answer_key_findings(evaluations, "evals/evals.json"))
    if not cases:
        findings.append("evals/evals.json: non-empty cases list required")
        return sorted(set(findings))
    seen_case_ids: dict[str, str] = {}
    skill_references: dict[str, list[str]] = {}
    case_container = "evals/evals.json.cases" if published_envelope else "evals/evals.json"
    for index, record in enumerate(cases):
        location = f"{case_container}[{index}]"
        findings.extend(_eval_field_issues(record, location, published_schema=True if published_envelope else None))
        if not isinstance(record, dict):
            continue
        case_id = record.get("case_id")
        if isinstance(case_id, str):
            previous = seen_case_ids.get(case_id)
            if previous is not None:
                findings.append(f"{location}.case_id: duplicate exact case ID (first seen at {previous})")
            else:
                seen_case_ids[case_id] = location
        skill_id = record.get("skill_id")
        if not isinstance(skill_id, str):
            continue
        skill_references.setdefault(skill_id, []).append(location)
        if skill_id not in manifest_ids:
            findings.append(f"{location}.skill_id: ID is not declared by manifest.json.skills: {skill_id}")

    for skill_id, locations in sorted(skill_references.items()):
        if len(locations) > 1:
            findings.append(
                f"evals/evals.json.skill_id: one-to-one coverage violated for {skill_id} "
                f"({len(locations)} cases)"
            )
    for skill_id in sorted(manifest_ids - set(skill_references)):
        findings.append(f"evals/evals.json.skill_id: missing one-to-one coverage for {skill_id}")
    if len(cases) != len(manifest_ids):
        findings.append(
            "evals/evals.json: one-to-one skill coverage requires "
            f"{len(manifest_ids)} cases for {len(manifest_ids)} manifest skill IDs; found {len(cases)}"
        )
    return sorted(set(findings))


def count_evaluation_cases(root: Path) -> int:
    """Return the published case count, or zero for an unreadable artifact."""

    try:
        payload = _read_json(Path(root).resolve() / EVALS_RELATIVE_PATH)
    except (OSError, UnicodeDecodeError, DuplicateJSONKeyError, ValueError, json.JSONDecodeError):
        return 0
    cases, _ = _evaluation_cases(payload)
    return len(cases) if cases is not None else 0

def _read_json_findings(path: Path, label: str) -> tuple[Any | None, list[str]]:
    if path.is_symlink():
        return None, [f"{label}: symlinked files are not allowed"]
    if not path.is_file():
        return None, [f"{label}: required JSON file"]
    try:
        return _read_json(path), []
    except UnicodeDecodeError:
        return None, [f"{label}: file must be valid UTF-8"]
    except DuplicateJSONKeyError:
        return None, [f"{label}: valid UTF-8 JSON without duplicate keys required"]
    except json.JSONDecodeError:
        return None, [f"{label}: valid UTF-8 JSON required"]
    except ValueError:
        return None, [f"{label}: valid UTF-8 JSON required"]


def validate_library(
    root: Path = DEFAULT_LIBRARY,
    expected_milestone: str | None = None,
) -> list[str]:
    """Validate the library envelope, optionally requiring an exact milestone."""

    root = Path(root).resolve()
    if not root.exists():
        return [f"library: directory does not exist: {root}"]
    if not root.is_dir():
        return [f"library: directory required: {root}"]

    manifest, manifest_findings = _read_json_findings(root / MANIFEST_NAME, MANIFEST_NAME)
    evaluations, eval_findings = _read_json_findings(root / EVALS_RELATIVE_PATH, EVALS_RELATIVE_PATH.as_posix())
    findings = [*manifest_findings, *eval_findings]
    if manifest is not None and evaluations is not None:
        findings.extend(validate_evals(manifest, evaluations, expected_milestone))
    return sorted(set(findings))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("library", nargs="?", type=Path, default=DEFAULT_LIBRARY, help="skill-library root")
    parser.add_argument(
        "--milestone",
        dest="expected_milestone",
        help="require this published G<number> milestone, for example G26",
    )
    args = parser.parse_args(argv)
    findings = validate_library(args.library, args.expected_milestone)
    if findings:
        print("\n".join(findings))
        return 1
    print("valid: G20 skill evaluations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
