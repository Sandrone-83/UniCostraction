"""G18 structural QA for a Markdown SKILL.md library.

The validator is deliberately fail-closed. It checks only a local structural
contract: UTF-8 files, a strict JSON manifest, YAML-like front matter, the
required operational sections, declared source and rights statements, and
conservative professional/legal boundaries.

It does not fetch sources, interpret legal text, prove licence compatibility,
or establish factual, educational, technical, normative, safety, or
professional correctness. Those claims require a separate human or
professional review.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path, PurePosixPath
from typing import Any


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LIBRARY = REPOSITORY_ROOT / "skills"
MANIFEST_NAME = "manifest.json"
SKILL_FILENAME = "SKILL.md"
LEGACY_AUXILIARY_FILES = frozenset({"skill-library.schema.json", "evals/evals.json", "evals/README.md"})

REQUIRED_FRONT_MATTER = frozenset({"name", "description", "metadata"})
REQUIRED_METADATA = frozenset({"skill_id", "category"})
REQUIRED_MANIFEST_FIELDS = frozenset({"schema_version", "skills"})
ALLOWED_MANIFEST_FIELDS = frozenset({"schema_version", "skills"})
REQUIRED_ENTRY_FIELDS = frozenset({"id", "category", "path"})
ALLOWED_ENTRY_FIELDS = frozenset({"id", "category", "path"})

REQUIRED_SECTIONS = (
    "Purpose",
    "Inputs and Preconditions",
    "Operational Workflow",
    "Outputs and Handoff",
    "Sources and Provenance",
    "Rights and Use",
    "Professional and Legal Boundaries",
    "Verification and Escalation",
)

SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
KEY_PATTERN = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*$")
URL_OR_SOURCE_ID_PATTERN = re.compile(
    r"(?:https?://[^\s)]+|\bSRC-[A-Z0-9][A-Z0-9_-]*\b)", re.IGNORECASE
)
RIGHTS_PATTERN = re.compile(
    r"\b(?:licen[cs]e|rights?|redistribut(?:e|ion|able)|attribution|copyright|"
    r"permission|original\s+(?:work|procedure))\b",
    re.IGNORECASE,
)
BOUNDARY_PATTERNS = {
    "human review": re.compile(r"\bhuman\s+review\b", re.IGNORECASE),
    "professional review": re.compile(r"\bprofessional\s+review\b", re.IGNORECASE),
    "automatic execution": re.compile(r"\bautomatic\s+(?:execution|action)\b", re.IGNORECASE),
    "legal advice": re.compile(r"\blegal\s+advice\b", re.IGNORECASE),
    "factual correctness": re.compile(r"\bfactual\s+correctness\b", re.IGNORECASE),
}


class DuplicateJSONKeyError(ValueError):
    """Raised when a JSON object repeats a key."""


def _object_pairs_without_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJSONKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _slug(value: Any) -> bool:
    return isinstance(value, str) and bool(SLUG_PATTERN.fullmatch(value))


def _relative_posix_path(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip() or "\\" in value:
        return False
    path = PurePosixPath(value)
    return (
        not path.is_absolute()
        and value == path.as_posix()
        and all(part not in {"", ".", ".."} for part in path.parts)
    )


def _read_utf8(path: Path) -> str:
    data = path.read_bytes()
    if not data or not data.strip():
        raise ValueError("empty file")
    return data.decode("utf-8", errors="strict")


def _read_json(path: Path) -> Any:
    return json.loads(_read_utf8(path), object_pairs_hook=_object_pairs_without_duplicates)


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if value in {"true", "True"}:
        return True
    if value in {"false", "False"}:
        return False
    if value in {"null", "Null", "NULL", "~"}:
        return None
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _parse_front_matter(text: str) -> tuple[dict[str, Any] | None, str | None, list[str]]:
    """Parse the small, dependency-free front-matter subset used by G18."""

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, None, ["front matter must start with ---"]
    closing = next((index for index in range(1, len(lines)) if lines[index].strip() == "---"), None)
    if closing is None:
        return None, None, ["front matter closing --- is required"]

    values: dict[str, Any] = {}
    metadata: dict[str, Any] = {}
    metadata_started = False
    issues: list[str] = []
    for line_number, line in enumerate(lines[1:closing], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indentation = len(line) - len(line.lstrip(" "))
        if "\t" in line[:indentation]:
            issues.append(f"front matter line {line_number}: tabs are not allowed for indentation")
            continue
        if indentation == 0:
            if ":" not in line:
                issues.append(f"front matter line {line_number}: key: value required")
                continue
            key, raw_value = line.split(":", 1)
            key = key.strip()
            if not KEY_PATTERN.fullmatch(key):
                issues.append(f"front matter line {line_number}: invalid key")
                continue
            if key in values:
                issues.append(f"front matter line {line_number}: duplicate key {key}")
                continue
            if key == "metadata":
                metadata_started = True
                if raw_value.strip():
                    try:
                        parsed = json.loads(raw_value, object_pairs_hook=_object_pairs_without_duplicates)
                    except (DuplicateJSONKeyError, json.JSONDecodeError):
                        parsed = None
                    if isinstance(parsed, dict):
                        metadata.update(parsed)
                    else:
                        issues.append(f"front matter line {line_number}: metadata mapping required")
                values[key] = metadata
            else:
                values[key] = _parse_scalar(raw_value)
        elif metadata_started and indentation >= 2:
            if ":" not in line:
                issues.append(f"front matter line {line_number}: metadata key: value required")
                continue
            key, raw_value = line.strip().split(":", 1)
            if not KEY_PATTERN.fullmatch(key):
                issues.append(f"front matter line {line_number}: invalid metadata key")
                continue
            if key in metadata:
                issues.append(f"front matter line {line_number}: duplicate metadata key {key}")
                continue
            metadata[key] = _parse_scalar(raw_value)
        else:
            issues.append(f"front matter line {line_number}: unexpected indentation")
    if metadata_started:
        values["metadata"] = metadata
    return values, "\n".join(lines[closing + 1 :]), issues


def _heading_sections(body: str) -> dict[str, str]:
    lines = body.splitlines()
    headings: list[tuple[str, int]] = []
    for index, line in enumerate(lines):
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            headings.append((match.group(1).strip().rstrip(":").strip(), index))
    sections: dict[str, str] = {}
    for position, (title, start) in enumerate(headings):
        end = headings[position + 1][1] if position + 1 < len(headings) else len(lines)
        sections.setdefault(title, "\n".join(lines[start + 1 : end]).strip())
    return sections


def _front_matter_issues(front_matter: dict[str, Any] | None, location: str) -> list[str]:
    if front_matter is None:
        return [f"{location}: front matter is required"]
    issues: list[str] = []
    issues.extend(f"{location}: missing required front matter field {field}" for field in sorted(REQUIRED_FRONT_MATTER - set(front_matter)))
    issues.extend(f"{location}: unknown front matter field {field}" for field in sorted(set(front_matter) - REQUIRED_FRONT_MATTER))
    name = front_matter.get("name")
    if not _slug(name):
        issues.append(f"{location}.name: lowercase hyphenated skill ID required")
    if not _non_empty_string(front_matter.get("description")):
        issues.append(f"{location}.description: non-empty string required")
    metadata = front_matter.get("metadata")
    if not isinstance(metadata, dict) or not metadata:
        issues.append(f"{location}.metadata: non-empty mapping required")
        return issues
    issues.extend(f"{location}.metadata: missing required field {field}" for field in sorted(REQUIRED_METADATA - set(metadata)))
    skill_id = metadata.get("skill_id")
    category = metadata.get("category")
    if not _slug(skill_id):
        issues.append(f"{location}.metadata.skill_id: lowercase hyphenated skill ID required")
    if _slug(name) and skill_id != name:
        issues.append(f"{location}.metadata.skill_id: must match front matter name")
    if not _slug(category):
        issues.append(f"{location}.metadata.category: lowercase hyphenated category required")
    return issues


def _section_issues(body: str, location: str) -> list[str]:
    sections = _heading_sections(body)
    issues: list[str] = []
    for title in REQUIRED_SECTIONS:
        if title not in sections:
            issues.append(f"{location}: missing required section heading ## {title}")
        elif not sections[title]:
            issues.append(f"{location}.section[{title}]: non-empty section required")
    sources = sections.get("Sources and Provenance", "")
    if sources and not URL_OR_SOURCE_ID_PATTERN.search(sources):
        issues.append(f"{location}.section[Sources and Provenance]: source reference required")
    rights = sections.get("Rights and Use", "")
    if rights and not RIGHTS_PATTERN.search(rights):
        issues.append(f"{location}.section[Rights and Use]: rights or licence statement required")
    boundaries = sections.get("Professional and Legal Boundaries", "")
    for label, pattern in BOUNDARY_PATTERNS.items():
        if boundaries and not pattern.search(boundaries):
            issues.append(f"{location}.section[Professional and Legal Boundaries]: {label} boundary required")
    return issues


def _path_issues(entry: dict[str, Any], relative: Path, location: str) -> list[str]:
    issues: list[str] = []
    if entry.get("path") != relative.as_posix():
        issues.append(f"{location}.path: must match actual library-relative path")
    if len(relative.parts) != 3 or relative.parts[-1] != SKILL_FILENAME:
        issues.append(f"{location}: skill file must be exactly <category>/<skill-id>/SKILL.md")
        return issues
    category, skill_id, _ = relative.parts
    if entry.get("category") != category:
        issues.append(f"{location}.category: must match path category")
    if entry.get("id") != skill_id:
        issues.append(f"{location}.id: must match path skill ID")
    return issues


def _legacy_front_matter_issues(front_matter: dict[str, Any] | None, location: str, skill_id: str) -> list[str]:
    """Validate the v0.1 UniCostraction manifest/front-matter contract.

    G17 shipped a deliberately simpler layout (``<skill-id>/SKILL.md``) with
    Italian section headings and metadata describing the domain rather than a
    separate category.  Keep that contract explicit instead of silently
    coercing it into the future G18 JSON-shaped layout.
    """

    if front_matter is None:
        return [f"{location}: front matter is required"]
    issues: list[str] = []
    issues.extend(
        f"{location}: missing required front matter field {field}"
        for field in sorted(REQUIRED_FRONT_MATTER - set(front_matter))
    )
    name = front_matter.get("name")
    if not _slug(name):
        issues.append(f"{location}.name: lowercase hyphenated skill ID required")
    elif name != skill_id:
        issues.append(f"{location}.name: must match skill directory ID")
    if not _non_empty_string(front_matter.get("description")):
        issues.append(f"{location}.description: non-empty string required")
    metadata = front_matter.get("metadata")
    if not isinstance(metadata, dict) or not metadata:
        issues.append(f"{location}.metadata: non-empty mapping required")
        return issues
    for field in ("library", "version", "domain"):
        if not _non_empty_string(metadata.get(field)):
            issues.append(f"{location}.metadata: required non-empty field {field}")
    return issues


LEGACY_SECTIONS = (
    ("Attivazione", "Attivazione e input"),
    "Workflow",
    "Output",
    "Quality gates",
    ("Evidenza e provenienza", "Provenienza ed evidenza"),
    "Confini professionali e legali",
    "Failure modes",
    "Strumenti",
    "Fonti ufficiali e diritti",
)


def _legacy_section_issues(body: str, location: str) -> list[str]:
    sections = _heading_sections(body)
    issues: list[str] = []
    resolved: dict[str, str] = {}
    for expected in LEGACY_SECTIONS:
        aliases = (expected,) if isinstance(expected, str) else expected
        chosen = next((alias for alias in aliases if alias in sections), None)
        canonical = aliases[0]
        if chosen is None:
            # The combined heading is a valid representation of both activation
            # and input in the published G17 skills.
            issues.append(f"{location}: missing required section heading ## {canonical}")
        elif not sections[chosen]:
            issues.append(f"{location}.section[{canonical}]: non-empty section required")
        else:
            resolved[canonical] = sections[chosen]
    sources = resolved.get("Fonti ufficiali e diritti", "")
    if sources and not URL_OR_SOURCE_ID_PATTERN.search(sources):
        issues.append(f"{location}.section[Fonti ufficiali e diritti]: source reference required")
    if sources and not re.search(r"licen[cs]e?|licenz|rights?|diritt|copyright|redistribut|original|attribuz|riuso|termini", sources, re.IGNORECASE):
        issues.append(f"{location}.section[Fonti ufficiali e diritti]: rights or licence statement required")
    boundaries = resolved.get("Confini professionali e legali", "")
    # G17 uses an explicitly named, non-empty boundary section whose wording
    # is intentionally domain-specific. Requiring five English keywords here
    # would reject valid Italian boundaries (for example IFC privacy or model
    # authorisation limits) while testing vocabulary rather than structure.
    if boundaries and len(boundaries.strip()) < 20:
        issues.append(f"{location}.section[Confini professionali e legali]: substantive boundary note required")
    return issues


def _legacy_manifest_issues(manifest: Any, location: str) -> list[str]:
    if not isinstance(manifest, dict):
        return [f"{location}: manifest must be a JSON object"]
    required = {"library", "version", "skills"}
    allowed = required | {"generated_at", "rights_policy"}
    issues: list[str] = []
    issues.extend(f"{location}: missing required field {field}" for field in sorted(required - set(manifest)))
    issues.extend(f"{location}: unknown field {field}" for field in sorted(set(manifest) - allowed))
    skills = manifest.get("skills")
    if not isinstance(skills, list) or not skills:
        return issues + [f"{location}.skills: non-empty list required"]
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    for index, entry in enumerate(skills):
        entry_location = f"{location}.skills[{index}]"
        if not isinstance(entry, dict):
            issues.append(f"{entry_location}: manifest entry must be an object")
            continue
        for field in ("id", "path"):
            if not _non_empty_string(entry.get(field)):
                issues.append(f"{entry_location}: required non-empty field {field}")
        skill_id, path = entry.get("id"), entry.get("path")
        if not _slug(skill_id):
            issues.append(f"{entry_location}.id: lowercase hyphenated skill ID required")
        elif skill_id in seen_ids:
            issues.append(f"{entry_location}.id: duplicate exact skill ID")
        else:
            seen_ids.add(skill_id)
        if not _relative_posix_path(path):
            issues.append(f"{entry_location}.path: normalized repository-relative POSIX path required")
        elif path in seen_paths:
            issues.append(f"{entry_location}.path: duplicate exact skill path")
        else:
            seen_paths.add(path)
        if _relative_posix_path(path) and (Path(path).parts != (skill_id, SKILL_FILENAME)):
            issues.append(f"{entry_location}.path: must be exactly <skill-id>/SKILL.md")
    return issues


def _validate_legacy_library(root: Path, manifest: dict[str, Any]) -> list[str]:
    findings = _legacy_manifest_issues(manifest, "manifest.json")
    files = _library_files(root)
    skill_files: list[Path] = []
    for path in files:
        relative = path.relative_to(root)
        location = relative.as_posix()
        if path.is_symlink():
            findings.append(f"{location}: symlinked files are not allowed")
            continue
        relative_posix = relative.as_posix()
        if relative == Path(MANIFEST_NAME) or relative_posix in LEGACY_AUXILIARY_FILES:
            if relative_posix == "evals/evals.json":
                try:
                    evaluation_data = _read_json(path)
                    if not isinstance(evaluation_data, (dict, list)):
                        findings.append("evals/evals.json: JSON object or list required")
                except (DuplicateJSONKeyError, UnicodeDecodeError, ValueError, json.JSONDecodeError):
                    findings.append("evals/evals.json: valid UTF-8 JSON without duplicate keys required")
            continue
        if path.name != SKILL_FILENAME:
            findings.append(
                f"{location}: unsupported file; only root manifest.json, approved evaluation artifacts, optional schema JSON and SKILL.md are allowed"
            )
            continue
        skill_files.append(path)
        try:
            text = _read_utf8(path)
        except UnicodeDecodeError:
            findings.append(f"{location}: file must be valid UTF-8")
            continue
        except ValueError:
            findings.append(f"{location}: file must not be empty")
            continue
        front_matter, body, parse_findings = _parse_front_matter(text)
        skill_id = relative.parts[0] if len(relative.parts) == 2 else ""
        findings.extend(f"{location}: {issue}" for issue in parse_findings)
        if len(relative.parts) != 2 or relative.parts[-1] != SKILL_FILENAME or not _slug(skill_id):
            findings.append(f"{location}: skill file must be exactly <skill-id>/SKILL.md")
        findings.extend(_legacy_front_matter_issues(front_matter, location, skill_id))
        if body is not None:
            findings.extend(_legacy_section_issues(body, location))

    if not skill_files:
        findings.append("library: no SKILL.md files found")
    actual_paths = {path.relative_to(root).as_posix() for path in skill_files}
    entries = manifest.get("skills") if isinstance(manifest.get("skills"), list) else []
    manifest_paths = {
        entry.get("path") for entry in entries if isinstance(entry, dict) and isinstance(entry.get("path"), str)
    }
    for missing in sorted(actual_paths - manifest_paths):
        findings.append(f"manifest.json.skills: missing entry for {missing}")
    for extra in sorted(manifest_paths - actual_paths):
        findings.append(f"manifest.json.skills: path does not exist: {extra}")
    return sorted(set(findings))


def _manifest_issues(manifest: Any, location: str) -> list[str]:
    if not isinstance(manifest, dict):
        return [f"{location}: manifest must be a JSON object"]
    issues: list[str] = []
    issues.extend(f"{location}: missing required field {field}" for field in sorted(REQUIRED_MANIFEST_FIELDS - set(manifest)))
    issues.extend(f"{location}: unknown field {field}" for field in sorted(set(manifest) - ALLOWED_MANIFEST_FIELDS))
    if manifest.get("schema_version") != "g18":
        issues.append(f"{location}.schema_version: exact value g18 required")
    skills = manifest.get("skills")
    if not isinstance(skills, list) or not skills:
        issues.append(f"{location}.skills: non-empty list required")
        return issues
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    for index, entry in enumerate(skills):
        entry_location = f"{location}.skills[{index}]"
        if not isinstance(entry, dict):
            issues.append(f"{entry_location}: manifest entry must be an object")
            continue
        issues.extend(f"{entry_location}: missing required field {field}" for field in sorted(REQUIRED_ENTRY_FIELDS - set(entry)))
        issues.extend(f"{entry_location}: unknown field {field}" for field in sorted(set(entry) - ALLOWED_ENTRY_FIELDS))
        skill_id, category, path = entry.get("id"), entry.get("category"), entry.get("path")
        if not _slug(skill_id):
            issues.append(f"{entry_location}.id: lowercase hyphenated skill ID required")
        elif skill_id in seen_ids:
            issues.append(f"{entry_location}.id: duplicate exact skill ID")
        else:
            seen_ids.add(skill_id)
        if not _slug(category):
            issues.append(f"{entry_location}.category: lowercase hyphenated category required")
        if not _relative_posix_path(path):
            issues.append(f"{entry_location}.path: normalized repository-relative POSIX path required")
        elif path in seen_paths:
            issues.append(f"{entry_location}.path: duplicate exact skill path")
        else:
            seen_paths.add(path)
    return issues


def _library_files(root: Path) -> tuple[Path, ...]:
    if not root.exists() or not root.is_dir():
        return ()
    return tuple(sorted((path for path in root.rglob("*") if path.is_file()), key=lambda path: path.as_posix()))


def validate_library(root: Path = DEFAULT_LIBRARY) -> list[str]:
    """Return deterministic structural findings for a G18 Markdown library."""

    root = Path(root).resolve()
    if not root.exists():
        return [f"library: directory does not exist: {root}"]
    if not root.is_dir():
        return [f"library: directory required: {root}"]
    files = _library_files(root)
    if not files:
        return ["library: no manifest.json or SKILL.md files found"]

    findings: list[str] = []
    manifest_path = root / MANIFEST_NAME
    manifest: Any = None
    if manifest_path.is_symlink():
        findings.append("manifest.json: symlinked files are not allowed")
    elif not manifest_path.is_file():
        findings.append("manifest.json: required at library root")
    else:
        try:
            manifest = _read_json(manifest_path)
        except DuplicateJSONKeyError:
            findings.append("manifest.json: valid UTF-8 JSON object without duplicate keys required")
        except UnicodeDecodeError:
            findings.append("manifest.json: file must be valid UTF-8")
        except ValueError as error:
            findings.append("manifest.json: file must not be empty" if str(error) == "empty file" else "manifest.json: valid UTF-8 JSON object required")
        except json.JSONDecodeError:
            findings.append("manifest.json: valid UTF-8 JSON object without duplicate keys required")
        if manifest is not None:
            findings.extend(_manifest_issues(manifest, "manifest.json"))

        # The published G17/G18 corpus uses the original UniCostraction
        # manifest contract. Validate that layout natively; do not report
        # false failures merely because a future JSON contract differs.
        if (
            isinstance(manifest, dict)
            and "library" in manifest
            and "version" in manifest
            and "schema_version" not in manifest
        ):
            return _validate_legacy_library(root, manifest)

    skill_files: list[Path] = []
    for path in files:
        relative = path.relative_to(root)
        location = relative.as_posix()
        if path.is_symlink():
            findings.append(f"{location}: symlinked files are not allowed")
            continue
        if relative == Path(MANIFEST_NAME):
            continue
        if path.name != SKILL_FILENAME:
            try:
                _read_utf8(path)
            except UnicodeDecodeError:
                findings.append(f"{location}: file must be valid UTF-8")
            except ValueError:
                findings.append(f"{location}: file must not be empty")
            findings.append(f"{location}: unsupported file; only root manifest.json and SKILL.md are allowed")
            continue
        skill_files.append(path)
        try:
            text = _read_utf8(path)
        except UnicodeDecodeError:
            findings.append(f"{location}: file must be valid UTF-8")
            continue
        except ValueError:
            findings.append(f"{location}: file must not be empty")
            continue
        front_matter, body, parse_findings = _parse_front_matter(text)
        findings.extend(f"{location}: {issue}" for issue in parse_findings)
        findings.extend(_front_matter_issues(front_matter, location))
        if body is not None:
            findings.extend(_section_issues(body, location))

    if not skill_files:
        findings.append("library: no SKILL.md files found")

    actual_paths = {path.relative_to(root).as_posix() for path in skill_files}
    actual_ids: dict[str, str] = {}
    for path in skill_files:
        relative = path.relative_to(root)
        location = relative.as_posix()
        if len(relative.parts) == 3 and relative.parts[-1] == SKILL_FILENAME:
            category, skill_id, _ = relative.parts
            if not _slug(category) or not _slug(skill_id):
                findings.append(f"{location}: category and skill ID path components must be lowercase slugs")
            previous = actual_ids.get(skill_id)
            if previous is not None:
                findings.append(f"{location}.id: duplicate exact skill ID (first seen at {previous})")
            else:
                actual_ids[skill_id] = location

    if isinstance(manifest, dict) and isinstance(manifest.get("skills"), list):
        manifest_paths = {entry.get("path") for entry in manifest["skills"] if isinstance(entry, dict) and isinstance(entry.get("path"), str)}
        for missing in sorted(actual_paths - manifest_paths):
            findings.append(f"manifest.json.skills: missing entry for {missing}")
        for extra in sorted(manifest_paths - actual_paths):
            findings.append(f"manifest.json.skills: path does not exist: {extra}")
        manifest_by_path = {entry.get("path"): entry for entry in manifest["skills"] if isinstance(entry, dict) and isinstance(entry.get("path"), str)}
        for path in sorted(actual_paths & set(manifest_by_path)):
            findings.extend(_path_issues(manifest_by_path[path], Path(path), f"manifest.json.skills[{path}]"))
    return sorted(set(findings))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("library", nargs="?", type=Path, default=DEFAULT_LIBRARY, help="G18 Markdown skill-library directory (default: repository/skills)")
    args = parser.parse_args()
    findings = validate_library(args.library)
    if findings:
        print("\n".join(findings))
        return 1
    skill_count = sum(1 for path in _library_files(Path(args.library).resolve()) if path.name == SKILL_FILENAME)
    print(f"valid: G18 Markdown skill library ({skill_count} SKILL.md files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
