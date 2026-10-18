"""G17-C structural QA for the future UniCostraction skill library.

The validator is intentionally fail-closed.  A library is a directory whose
skill records are UTF-8 JSON files at ``<category>/<skill-id>.json``.  It
checks the record contract, deterministic paths, duplicate IDs, non-empty
workflows, source and licence/provenance metadata, and explicit safety/legal
boundaries.

This is metadata and structure QA only.  A passing result does not establish
that a source is authoritative, that a licence is usable, that a workflow is
technically correct, or that any legal, normative, safety, or professional
claim is true.  Those require a separate human or professional review.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path, PurePosixPath
from typing import Any


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LIBRARY = REPOSITORY_ROOT / "skills"
JSON_SUFFIX = ".json"

REQUIRED_FIELDS = frozenset(
    {
        "id",
        "title",
        "summary",
        "category",
        "path",
        "workflow",
        "source_refs",
        "license_status",
        "safety_legal_boundary",
        "provenance_status",
    }
)
OPTIONAL_FIELDS = frozenset({"license_evidence_ref", "provenance_evidence_ref", "tags"})
ALLOWED_FIELDS = REQUIRED_FIELDS | OPTIONAL_FIELDS

LICENSE_STATUS_VALUES = frozenset(
    {"unreviewed", "pending", "reviewed", "restricted", "not_applicable"}
)
PROVENANCE_STATUS_VALUES = frozenset({"unreviewed", "pending", "verified", "blocked"})
SOURCE_KIND_VALUES = frozenset(
    {"official", "normative", "institutional", "user_provided", "internal", "other"}
)
SAFETY_BOUNDARY_FIELDS = frozenset(
    {
        "human_review_required",
        "professional_review_required",
        "automatic_execution_prohibited",
        "legal_advice_prohibited",
        "factual_correctness_requires_review",
        "boundary_note",
    }
)
WORKFLOW_STEP_FIELDS = frozenset({"step_id", "action", "output"})
SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class DuplicateJSONKeyError(ValueError):
    """Raised when a JSON object repeats a key instead of silently replacing it."""


def _object_pairs_without_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJSONKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _is_slug(value: Any) -> bool:
    return isinstance(value, str) and bool(SLUG_PATTERN.fullmatch(value))


def _normalised_relative_path(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    if "\\" in value or value != PurePosixPath(value).as_posix():
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and all(part not in {"", ".", ".."} for part in path.parts)


def _read_json(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    return json.loads(text, object_pairs_hook=_object_pairs_without_duplicates)


def _field_issues(record: Any, location: str) -> list[str]:
    if not isinstance(record, dict):
        return [f"{location}: skill record must be a JSON object"]

    issues: list[str] = []
    missing = sorted(REQUIRED_FIELDS - set(record))
    issues.extend(f"{location}: missing required field {field}" for field in missing)
    unknown = sorted(set(record) - ALLOWED_FIELDS)
    issues.extend(f"{location}: unknown field {field}" for field in unknown)
    for field in ("id", "title", "summary"):
        if field in record and not _is_non_empty_string(record[field]):
            issues.append(f"{location}.{field}: non-empty string required")
    if "id" in record and not _is_slug(record["id"]):
        issues.append(f"{location}.id: lowercase hyphenated slug required")
    if "category" in record and not _is_slug(record["category"]):
        issues.append(f"{location}.category: lowercase hyphenated slug required")
    if "path" in record and not _normalised_relative_path(record["path"]):
        issues.append(f"{location}.path: normalized repository-relative POSIX path required")
    return issues


def _workflow_issues(workflow: Any, location: str) -> list[str]:
    if not isinstance(workflow, list) or not workflow:
        return [f"{location}: non-empty workflow list required"]
    issues: list[str] = []
    seen_step_ids: set[str] = set()
    for index, step in enumerate(workflow):
        step_location = f"{location}[{index}]"
        if not isinstance(step, dict):
            issues.append(f"{step_location}: workflow step must be an object")
            continue
        missing = sorted(WORKFLOW_STEP_FIELDS - set(step))
        issues.extend(f"{step_location}: missing required field {field}" for field in missing)
        unknown = sorted(set(step) - WORKFLOW_STEP_FIELDS)
        issues.extend(f"{step_location}: unknown field {field}" for field in unknown)
        for field in WORKFLOW_STEP_FIELDS:
            if field in step and not _is_non_empty_string(step[field]):
                issues.append(f"{step_location}.{field}: non-empty string required")
        step_id = step.get("step_id")
        if isinstance(step_id, str):
            if step_id in seen_step_ids:
                issues.append(f"{step_location}.step_id: duplicate exact step ID")
            seen_step_ids.add(step_id)
    return issues


def _source_issues(source_refs: Any, location: str) -> list[str]:
    if not isinstance(source_refs, list) or not source_refs:
        return [f"{location}: non-empty source reference list required"]
    issues: list[str] = []
    for index, source in enumerate(source_refs):
        source_location = f"{location}[{index}]"
        if not isinstance(source, dict):
            issues.append(f"{source_location}: source reference must be an object")
            continue
        if not _is_non_empty_string(source.get("ref")):
            issues.append(f"{source_location}.ref: non-empty string required")
        if source.get("kind") not in SOURCE_KIND_VALUES:
            issues.append(f"{source_location}.kind: unsupported source kind")
    return issues


def _boundary_issues(boundary: Any, location: str) -> list[str]:
    if not isinstance(boundary, dict):
        return [f"{location}: safety_legal_boundary object required"]
    issues: list[str] = []
    missing = sorted(SAFETY_BOUNDARY_FIELDS - set(boundary))
    issues.extend(f"{location}: missing required field {field}" for field in missing)
    unknown = sorted(set(boundary) - SAFETY_BOUNDARY_FIELDS)
    issues.extend(f"{location}: unknown field {field}" for field in unknown)
    for field in SAFETY_BOUNDARY_FIELDS - {"boundary_note"}:
        if boundary.get(field) is not True:
            issues.append(f"{location}.{field}: explicit true boundary flag required")
    if not _is_non_empty_string(boundary.get("boundary_note")):
        issues.append(f"{location}.boundary_note: non-empty string required")
    return issues


def _metadata_issues(record: dict[str, Any], location: str) -> list[str]:
    issues: list[str] = []
    issues.extend(_workflow_issues(record.get("workflow"), f"{location}.workflow"))
    issues.extend(_source_issues(record.get("source_refs"), f"{location}.source_refs"))
    issues.extend(
        _boundary_issues(record.get("safety_legal_boundary"), f"{location}.safety_legal_boundary")
    )

    license_status = record.get("license_status")
    if license_status not in LICENSE_STATUS_VALUES:
        issues.append(f"{location}.license_status: unsupported licence status")
    if license_status in {"reviewed", "restricted"} and not _is_non_empty_string(
        record.get("license_evidence_ref")
    ):
        issues.append(f"{location}.license_evidence_ref: required for reviewed/restricted status")

    provenance_status = record.get("provenance_status")
    if provenance_status not in PROVENANCE_STATUS_VALUES:
        issues.append(f"{location}.provenance_status: unsupported provenance status")
    if provenance_status == "verified" and not _is_non_empty_string(
        record.get("provenance_evidence_ref")
    ):
        issues.append(f"{location}.provenance_evidence_ref: required for verified status")

    if "tags" in record:
        tags = record["tags"]
        if not isinstance(tags, list) or not tags or not all(_is_slug(tag) for tag in tags):
            issues.append(f"{location}.tags: non-empty list of lowercase slugs required")
    return issues


def _path_mapping_issues(record: dict[str, Any], relative_path: Path, location: str) -> list[str]:
    issues: list[str] = []
    actual = relative_path.as_posix()
    declared = record.get("path")
    if declared != actual:
        issues.append(f"{location}.path: must match actual library-relative path")
    parts = relative_path.parts
    if len(parts) != 2:
        issues.append(f"{location}: skill file must be exactly <category>/<id>.json")
        return issues
    category, filename = parts
    if record.get("category") != category:
        issues.append(f"{location}.category: must match path category")
    if record.get("id") != Path(filename).stem:
        issues.append(f"{location}.id: must match skill filename stem")
    return issues


def _skill_files(root: Path) -> tuple[tuple[Path, ...], list[str]]:
    if not root.exists():
        return (), [f"library: directory does not exist: {root}"]
    if not root.is_dir():
        return (), [f"library: directory required: {root}"]
    files = sorted((path for path in root.rglob("*") if path.is_file()), key=lambda p: p.as_posix())
    issues: list[str] = []
    json_files: list[Path] = []
    for path in files:
        relative = path.relative_to(root)
        if path.is_symlink():
            issues.append(f"{relative.as_posix()}: symlinked skill files are not allowed")
        elif path.suffix != JSON_SUFFIX:
            issues.append(f"{relative.as_posix()}: unsupported file type; only UTF-8 JSON is allowed")
        else:
            json_files.append(path)
    if not json_files:
        issues.append("library: no skill JSON files found")
    return tuple(json_files), issues


def validate_library(root: Path = DEFAULT_LIBRARY) -> list[str]:
    """Return deterministic structural findings for a future skill library."""

    root = root.resolve()
    try:
        files, findings = _skill_files(root)
    except OSError:
        return ["library: cannot inspect library directory"]
    seen_ids: dict[str, Path] = {}
    for path in files:
        relative = path.relative_to(root)
        location = relative.as_posix()
        try:
            record = _read_json(path)
        except UnicodeDecodeError:
            findings.append(f"{location}: file must be valid UTF-8")
            continue
        except DuplicateJSONKeyError:
            findings.append(f"{location}: duplicate JSON object key")
            continue
        except (OSError, json.JSONDecodeError):
            findings.append(f"{location}: valid UTF-8 JSON object required")
            continue

        findings.extend(_field_issues(record, location))
        if not isinstance(record, dict):
            continue
        skill_id = record.get("id")
        if isinstance(skill_id, str):
            previous = seen_ids.get(skill_id)
            if previous is not None:
                findings.append(f"{location}.id: duplicate exact ID (first seen at {previous.as_posix()})")
            else:
                seen_ids[skill_id] = relative
        findings.extend(_path_mapping_issues(record, relative, location))
        findings.extend(_metadata_issues(record, location))
    return sorted(findings)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "library",
        nargs="?",
        type=Path,
        default=DEFAULT_LIBRARY,
        help="future skill-library directory (default: repository/skills)",
    )
    args = parser.parse_args()
    findings = validate_library(args.library)
    if findings:
        print("\n".join(findings))
        return 1
    files, _ = _skill_files(args.library.resolve())
    print(f"valid: G17-C skill library ({len(files)} UTF-8 JSON records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
