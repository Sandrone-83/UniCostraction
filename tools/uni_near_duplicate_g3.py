"""Build a deterministic, bounded near-duplicate review report.

This G3 check starts from the G1 inventory contract but narrows the corpus to
``COURSE.yaml``, ``README.md`` and ``schede.jsonl``.  It emits only review
signals.  It never edits, moves, merges, overwrites, or deletes corpus files,
and it never labels a candidate as a confirmed duplicate.

The report is intentionally bounded:

* source files are limited by byte size;
* structured metadata reads a fixed number of JSONL records and values;
* candidates are produced by digest/metadata indexes, not an unbounded
  all-pairs comparison;
* all ordering is sorted before serialization.

Usage::

    python tools/uni_near_duplicate_g3.py
    python tools/uni_near_duplicate_g3.py --root . \
        --output docs/coordination/UNI_NEAR_DUPLICATE_G3.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_NEAR_DUPLICATE_G3.json")
TARGET_FILENAMES = frozenset({"COURSE.yaml", "README.md", "schede.jsonl"})
IGNORED_DIRECTORY_NAMES = frozenset({".git", "tests", "work"})

MAX_FILE_BYTES = 2_000_000
MAX_JSONL_RECORDS = 512
MAX_METADATA_VALUES = 256
MAX_CANDIDATE_GROUPS = 5_000

KEY_VALUE_RE = re.compile(r"^\s*([A-Za-z][A-Za-z0-9_-]*)\s*:\s*(.*?)\s*$")
README_TITLE_RE = re.compile(r"^\s{0,3}#\s+(.+?)\s*#*\s*$")
README_METADATA_RE = re.compile(
    r"^\s*(?:[-*]\s*)?(id|course[_ -]?id|pack[_ -]?id|slug|codice|code|identifier|identificativo)\s*[:=]\s*(.+?)\s*$",
    re.IGNORECASE,
)
TOKEN_RE = re.compile(r"[\w]+", re.UNICODE)

TITLE_KEYS = frozenset(
    {
        "corso",
        "course",
        "title",
        "titolo",
        "nome",
        "name",
        "subject",
        "materia",
    }
)
IDENTIFIER_KEYS = frozenset(
    {
        "id",
        "course_id",
        "courseid",
        "course-id",
        "pack_id",
        "packid",
        "pack-id",
        "slug",
        "codice",
        "code",
        "identifier",
        "identificativo",
    }
)


def _relative_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def discover_files(root: Path) -> list[Path]:
    """Discover only the three G3 target file names in stable order."""

    root = root.resolve()
    found: set[Path] = set()
    for current, directory_names, file_names in os.walk(root, topdown=True, followlinks=False):
        current_path = Path(current)
        directory_names[:] = sorted(
            name
            for name in directory_names
            if name not in IGNORED_DIRECTORY_NAMES and not (current_path / name).is_symlink()
        )
        for name in sorted(file_names):
            candidate = current_path / name
            if name not in TARGET_FILENAMES or candidate.is_symlink() or not candidate.is_file():
                continue
            found.add(candidate)
    return sorted(found, key=lambda path: _relative_path(path, root))


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _decode(data: bytes) -> tuple[str | None, str | None]:
    try:
        return data.decode("utf-8-sig"), None
    except UnicodeDecodeError as error:
        return None, f"invalid_utf8:{error.start}"


def _normalise_text(text: str) -> str:
    """Normalize Unicode, case, line endings and whitespace only."""

    normalized = unicodedata.normalize("NFKC", text)
    normalized = normalized.replace("\r\n", "\n").replace("\r", "\n")
    normalized = normalized.casefold()
    return " ".join(normalized.split())


def _normalise_tokens(text: str) -> str:
    """Return a punctuation-insensitive, deterministic token stream."""

    normalized = unicodedata.normalize("NFKC", text).casefold()
    return " ".join(TOKEN_RE.findall(normalized))


def _clean_scalar(value: Any) -> str | None:
    if not isinstance(value, (str, int, float, bool)):
        return None
    cleaned = unicodedata.normalize("NFKC", str(value)).strip()
    if len(cleaned) >= 2 and cleaned[0] == cleaned[-1] and cleaned[0] in {'"', "'"}:
        cleaned = cleaned[1:-1].strip()
    if cleaned.endswith(","):
        cleaned = cleaned[:-1].rstrip()
    return cleaned or None


def _key_key(key: str) -> str:
    return key.strip().casefold().replace(" ", "_")


def _bounded_values(values: Iterable[str]) -> tuple[list[str], int, bool]:
    unique = sorted(set(value for value in values if value))
    return unique[:MAX_METADATA_VALUES], len(unique), len(unique) > MAX_METADATA_VALUES


def _metadata_from_course(text: str) -> tuple[list[str], list[str], int, bool]:
    titles: list[str] = []
    identifiers: list[str] = []
    for line in text.splitlines():
        match = KEY_VALUE_RE.match(line)
        if not match:
            continue
        key = _key_key(match.group(1))
        value = _clean_scalar(match.group(2))
        if not value:
            continue
        if key in TITLE_KEYS:
            titles.append(value)
        if key in IDENTIFIER_KEYS:
            identifiers.append(value)
    title_values, title_count, title_truncated = _bounded_values(titles)
    identifier_values, identifier_count, identifier_truncated = _bounded_values(identifiers)
    return (
        title_values,
        identifier_values,
        max(title_count, identifier_count),
        title_truncated or identifier_truncated,
    )


def _metadata_from_readme(text: str) -> tuple[list[str], list[str], int, bool]:
    titles: list[str] = []
    identifiers: list[str] = []
    title_seen = False
    for line in text.splitlines():
        heading = README_TITLE_RE.match(line)
        if heading and not title_seen:
            value = _clean_scalar(heading.group(1))
            if value:
                titles.append(value)
                title_seen = True
        metadata = README_METADATA_RE.match(line)
        if metadata:
            value = _clean_scalar(metadata.group(2))
            if value:
                identifiers.append(value)
    title_values, title_count, title_truncated = _bounded_values(titles)
    identifier_values, identifier_count, identifier_truncated = _bounded_values(identifiers)
    return (
        title_values,
        identifier_values,
        max(title_count, identifier_count),
        title_truncated or identifier_truncated,
    )


def _walk_json_scalars(value: Any, titles: list[str], identifiers: list[str], *, key: str = "") -> None:
    if len(titles) >= MAX_METADATA_VALUES and len(identifiers) >= MAX_METADATA_VALUES:
        return
    if isinstance(value, dict):
        for raw_key, child in value.items():
            child_key = _key_key(str(raw_key))
            if child_key in TITLE_KEYS:
                scalar = _clean_scalar(child)
                if scalar:
                    titles.append(scalar)
            elif child_key in IDENTIFIER_KEYS:
                scalar = _clean_scalar(child)
                if scalar:
                    identifiers.append(scalar)
            elif isinstance(child, (dict, list)):
                _walk_json_scalars(child, titles, identifiers, key=child_key)
    elif isinstance(value, list):
        for child in value:
            _walk_json_scalars(child, titles, identifiers, key=key)


def _metadata_from_jsonl(text: str) -> tuple[list[str], list[str], int, bool, list[Any], bool]:
    titles: list[str] = []
    identifiers: list[str] = []
    records: list[Any] = []
    parse_complete = True
    for index, line in enumerate(text.splitlines()):
        if index >= MAX_JSONL_RECORDS:
            parse_complete = False
            break
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            parse_complete = False
            continue
        records.append(record)
        _walk_json_scalars(record, titles, identifiers)
    title_values, title_count, title_truncated = _bounded_values(titles)
    identifier_values, identifier_count, identifier_truncated = _bounded_values(identifiers)
    return (
        title_values,
        identifier_values,
        max(title_count, identifier_count),
        title_truncated or identifier_truncated,
        records,
        parse_complete,
    )


def _structured_digest(path: Path, text: str) -> tuple[str | None, bool]:
    """Canonicalize simple structured files without requiring PyYAML."""

    if path.name == "COURSE.yaml":
        pairs: list[tuple[str, str]] = []
        for line in text.splitlines():
            match = KEY_VALUE_RE.match(line)
            if not match:
                continue
            value = _clean_scalar(match.group(2))
            if value is not None:
                pairs.append((_key_key(match.group(1)), _normalise_text(value)))
        if not pairs:
            return None, False
        canonical = json.dumps(sorted(pairs), ensure_ascii=False, separators=(",", ":"))
        return _sha256(canonical.encode("utf-8")), True

    if path.name == "schede.jsonl":
        titles, identifiers, count, truncated, records, parse_complete = _metadata_from_jsonl(text)
        del titles, identifiers, count, truncated
        if not records or not parse_complete:
            return None, False
        canonical_records = [json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")) for record in records]
        canonical = "\n".join(canonical_records)
        return _sha256(canonical.encode("utf-8")), True

    return None, False


def _metadata(path: Path, text: str) -> tuple[dict[str, Any], dict[str, set[str]], bool]:
    if path.name == "COURSE.yaml":
        titles, identifiers, count, truncated = _metadata_from_course(text)
        parse_complete = True
    elif path.name == "README.md":
        titles, identifiers, count, truncated = _metadata_from_readme(text)
        parse_complete = True
    else:
        titles, identifiers, count, truncated, _, parse_complete = _metadata_from_jsonl(text)

    title_keys = {_normalise_tokens(value) for value in titles if _normalise_tokens(value)}
    identifier_keys = {_normalise_tokens(value) for value in identifiers if _normalise_tokens(value)}
    report_metadata = {
        "titles": titles,
        "identifiers": identifiers,
        "metadata_value_count": count,
        "metadata_truncated": truncated,
    }
    return report_metadata, {"title": title_keys, "identifier": identifier_keys}, parse_complete


def _build_entry(root: Path, path: Path) -> dict[str, Any]:
    data = path.read_bytes()
    text, decode_error = _decode(data)
    entry: dict[str, Any] = {
        "path": _relative_path(path, root),
        "category": {"COURSE.yaml": "course_manifest", "README.md": "readme", "schede.jsonl": "course_cards"}[path.name],
        "sha256": _sha256(data),
        "size_bytes": len(data),
        "signals": [],
    }
    if len(data) > MAX_FILE_BYTES:
        entry["bounded_skip"] = "file_exceeds_max_bytes"
        return entry
    if decode_error or text is None:
        entry["bounded_skip"] = decode_error or "invalid_utf8"
        return entry

    normalized_text = _normalise_text(text)
    normalized_tokens = _normalise_tokens(text)
    entry["normalized_text_sha256"] = _sha256(normalized_text.encode("utf-8"))
    entry["normalized_token_sha256"] = _sha256(normalized_tokens.encode("utf-8"))
    structured_digest, structured_complete = _structured_digest(path, text)
    if structured_digest is not None:
        entry["structured_sha256"] = structured_digest
        entry["structured_complete"] = structured_complete
    report_metadata, index_metadata, parse_complete = _metadata(path, text)
    entry["metadata"] = report_metadata
    entry["metadata_parse_complete"] = parse_complete
    entry["_index_metadata"] = index_metadata
    return entry


def _groups(entries: Iterable[dict[str, Any]], field: str) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        value = entry.get(field)
        if not isinstance(value, str) or entry.get("bounded_skip"):
            continue
        grouped[value].append(entry)
    return {value: sorted(items, key=lambda item: str(item["path"])) for value, items in grouped.items() if len(items) > 1}


def _index_metadata(entries: Iterable[dict[str, Any]], kind: str) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        metadata = entry.get("_index_metadata")
        if not isinstance(metadata, dict):
            continue
        for value in metadata.get(kind, set()):
            grouped[value].append(entry)
    result: dict[str, list[dict[str, Any]]] = {}
    for value, items in grouped.items():
        unique = {str(item["path"]): item for item in items}
        if len(unique) > 1:
            result[value] = [unique[path] for path in sorted(unique)]
    return result


def _evidence(entries: list[dict[str, Any]], signal: str, value: str) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for entry in entries:
        item: dict[str, Any] = {
            "path": entry["path"],
            "category": entry["category"],
            "sha256": entry["sha256"],
            "size_bytes": entry["size_bytes"],
        }
        for field in ("normalized_text_sha256", "normalized_token_sha256", "structured_sha256"):
            if field in entry:
                item[field] = entry[field]
        if signal in {"title_match", "identifier_match"}:
            metadata = entry.get("metadata", {})
            key = "titles" if signal == "title_match" else "identifiers"
            item["matching_values"] = [
                current
                for current in metadata.get(key, [])
                if _normalise_tokens(current) == value
            ]
        output.append(item)
    return output


def _candidate(signal: str, value: str, entries: list[dict[str, Any]], explanation: str) -> dict[str, Any]:
    paths = sorted(str(entry["path"]) for entry in entries)
    return {
        "signal": signal,
        "value": value,
        "paths": paths,
        "evidence": _evidence(entries, signal, value),
        "review_status": "pending_human_review",
        "duplicate_confirmed": False,
        "interpretation": explanation,
    }


def build_report(root: Path) -> dict[str, Any]:
    """Build the complete deterministic G3 report for *root*."""

    root = root.resolve()
    entries = [_build_entry(root, path) for path in discover_files(root)]
    usable = [entry for entry in entries if not entry.get("bounded_skip")]
    raw_groups = _groups(usable, "sha256")
    normalized_groups = _groups(usable, "normalized_text_sha256")
    token_groups = _groups(usable, "normalized_token_sha256")
    structured_groups = _groups(usable, "structured_sha256")
    title_groups = _index_metadata(usable, "title")
    identifier_groups = _index_metadata(usable, "identifier")

    candidate_groups: list[dict[str, Any]] = []
    for value, group in sorted(raw_groups.items()):
        candidate_groups.append(
            _candidate(
                "exact_sha256_match",
                value,
                group,
                "Same bytes are evidence of a possible copy; human review is required and no duplicate is confirmed.",
            )
        )
    for value, group in sorted(normalized_groups.items()):
        if len({entry["sha256"] for entry in group}) == 1:
            continue
        candidate_groups.append(
            _candidate(
                "normalized_text_digest_match",
                value,
                group,
                "Text matches after Unicode, case, line-ending and whitespace normalization while raw bytes differ; inspect provenance and intent.",
            )
        )
    for value, group in sorted(token_groups.items()):
        if len({entry.get("normalized_text_sha256") for entry in group}) == 1:
            continue
        candidate_groups.append(
            _candidate(
                "normalized_token_digest_match",
                value,
                group,
                "Punctuation-insensitive token streams match while normalized text differs; this is a bounded near-duplicate signal, not a semantic decision.",
            )
        )
    for value, group in sorted(structured_groups.items()):
        if len({entry["sha256"] for entry in group}) == 1:
            continue
        candidate_groups.append(
            _candidate(
                "structured_digest_match",
                value,
                group,
                "Canonical structured values match while raw bytes differ; review ordering, provenance and intended reuse before any action.",
            )
        )
    for value, group in sorted(title_groups.items()):
        candidate_groups.append(
            _candidate(
                "title_match",
                value,
                group,
                "Normalized titles collide across files; shared pack structure or a thematic title is not proof of duplicate content.",
            )
        )
    for value, group in sorted(identifier_groups.items()):
        candidate_groups.append(
            _candidate(
                "identifier_match",
                value,
                group,
                "Normalized identifiers collide across files; verify ownership and intended references before treating this as redundancy.",
            )
        )

    candidate_groups.sort(key=lambda group: (str(group["signal"]), str(group["value"]), group["paths"]))
    bounded_candidate_count = len(candidate_groups)
    truncated_candidates = bounded_candidate_count > MAX_CANDIDATE_GROUPS
    candidate_groups = candidate_groups[:MAX_CANDIDATE_GROUPS]
    for index, group in enumerate(candidate_groups, start=1):
        group["candidate_id"] = f"G3-{index:04d}"

    counts = Counter(str(entry["category"]) for entry in entries)
    public_entries = []
    for entry in entries:
        public_entry = {key: value for key, value in entry.items() if not key.startswith("_")}
        public_entries.append(public_entry)
    return {
        "schema_version": "g3.v1",
        "tool": "tools/uni_near_duplicate_g3.py",
        "inputs": {
            "previous_g1_report": "docs/coordination/UNI_DUPLICATE_MATRIX_G1.json",
            "previous_g2_review": "docs/coordination/UNI_DUPLICATE_REVIEW_G2.md",
            "source_of_truth": "filesystem bytes in the selected checkout",
        },
        "scope": {
            "root": ".",
            "included": ["**/COURSE.yaml", "**/README.md", "**/schede.jsonl"],
            "excluded_directories": sorted(IGNORED_DIRECTORY_NAMES),
            "deduplicated": False,
            "bounded": True,
        },
        "limits": {
            "max_file_bytes": MAX_FILE_BYTES,
            "max_jsonl_records_per_file": MAX_JSONL_RECORDS,
            "max_metadata_values_per_file": MAX_METADATA_VALUES,
            "max_candidate_groups": MAX_CANDIDATE_GROUPS,
            "candidate_generation": "indexed signals only; no unbounded all-pairs comparison",
        },
        "evidence": {
            "files": public_entries,
            "counts_by_category": dict(sorted(counts.items())),
        },
        "interpretation": {
            "possible_near_duplicate_groups": candidate_groups,
            "candidate_count_before_bound": bounded_candidate_count,
            "candidate_count": len(candidate_groups),
            "candidates_truncated": truncated_candidates,
            "human_review_required": True,
            "boundaries": [
                "Every candidate is an evidence-backed review signal, not a duplicate decision.",
                "duplicate_confirmed is always false in this report; a human must review provenance, scope and intent.",
                "No source file was deduplicated, moved, overwritten, merged or deleted.",
                "A shared title, identifier, schema, topic or pack structure is not by itself evidence of duplicate content.",
                "Digest equality does not establish educational, factual, legal, licensing or semantic equivalence.",
            ],
        },
    }


def write_report(root: Path, output: Path) -> None:
    report = build_report(root)
    output_path = output if output.is_absolute() else root / output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="checkout root (default: current directory)")
    parser.add_argument(
        "--output",
        type=Path,
        default=REPORT_RELATIVE_PATH,
        help=f"JSON report path relative to --root (default: {REPORT_RELATIVE_PATH.as_posix()})",
    )
    args = parser.parse_args(argv)
    write_report(args.root.resolve(), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
