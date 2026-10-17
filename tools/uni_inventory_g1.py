"""Build a deterministic, non-destructive UniCostraction duplicate matrix.

The tool only reports candidates.  It never edits, moves, or deletes source
files.  ``evidence.files`` contains one entry per indexed file; the
``interpretation`` section contains derived candidate groups and explicitly
does not claim semantic equivalence.

Usage::

    python tools/uni_inventory_g1.py
    python tools/uni_inventory_g1.py --root . --output docs/coordination/UNI_DUPLICATE_MATRIX_G1.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable, Mapping


REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_DUPLICATE_MATRIX_G1.json")
TARGET_FILENAMES = frozenset({"COURSE.yaml", "README.md", "schede.jsonl"})
IGNORED_DIRECTORY_NAMES = frozenset({".git", "tests", "work"})
COURSE_TITLE_RE = re.compile(r"^\s*corso\s*:\s*(.*?)\s*$", re.IGNORECASE)


def _relative_path(path: Path, root: Path) -> str:
    """Return a stable, repository-style relative path."""

    return path.relative_to(root).as_posix()


def _is_exam_path(path: Path, root: Path) -> bool:
    """Whether *path* is inside a directory named ``ESAMI``."""

    try:
        relative_parts = path.relative_to(root).parts
    except ValueError:
        return False
    return any(part.casefold() == "esami" for part in relative_parts)


def _category(path: Path, root: Path) -> str:
    """Assign a stable category without parsing or rewriting source content."""

    if _is_exam_path(path, root):
        if path.name == "domande.md":
            return "exam_questions"
        if path.name == "README.md":
            return "exam_readme"
        return "exam_document"
    if path.name == "COURSE.yaml":
        return "course_manifest"
    if path.name == "schede.jsonl":
        return "course_cards"
    return "readme"


def discover_files(root: Path) -> list[Path]:
    """Discover target files in deterministic order.

    ``os.walk`` is used with sorted directory and file names so the result is
    independent of filesystem enumeration order.  Symlinked directories are
    not traversed, and repository metadata, tests, and scratch directories
    are excluded so the corpus report cannot self-index its own fixtures.
    """

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
            if candidate.is_symlink() or not candidate.is_file():
                continue
            if name in TARGET_FILENAMES or _is_exam_path(candidate, root):
                found.add(candidate)
    return sorted(found, key=lambda path: _relative_path(path, root))


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _normalised_text_sha256(data: bytes) -> str | None:
    """Hash text after line-ending normalization, or return ``None``.

    This is a deliberately narrow signal: it catches byte-level copies that
    differ only by line endings, without attempting semantic or YAML/JSON
    normalization.
    """

    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError:
        return None
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return _sha256(normalized.encode("utf-8"))


def _course_title(data: bytes) -> str | None:
    """Extract the first simple ``corso:`` scalar as an objective signal."""

    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError:
        return None
    for line in text.splitlines():
        match = COURSE_TITLE_RE.match(line)
        if not match:
            continue
        value = match.group(1).strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        return value
    return None


def _normalized_key(value: str) -> str:
    return " ".join(value.casefold().split())


def _group_by(entries: Iterable[Mapping[str, object]], key: str) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for entry in entries:
        value = entry.get(key)
        if not isinstance(value, str) or not value:
            continue
        groups[value].append(str(entry["path"]))
    return {value: sorted(paths) for value, paths in groups.items() if len(paths) > 1}


def _candidate_group(signal: str, value: str, paths: list[str], explanation: str) -> dict[str, object]:
    return {
        "signal": signal,
        "value": value,
        "paths": paths,
        "interpretation": explanation,
    }


def build_report(root: Path) -> dict[str, object]:
    """Build the complete deterministic report for *root*."""

    root = root.resolve()
    entries: list[dict[str, object]] = []
    for path in discover_files(root):
        data = path.read_bytes()
        category = _category(path, root)
        entry: dict[str, object] = {
            "path": _relative_path(path, root),
            "sha256": _sha256(data),
            "category": category,
            "size_bytes": len(data),
            "signals": [],
        }
        normalized_hash = _normalised_text_sha256(data)
        if normalized_hash is not None:
            entry["normalized_text_sha256"] = normalized_hash
        if category == "course_manifest":
            title = _course_title(data)
            if title is not None:
                entry["course_title"] = title
                entry["course_title_key"] = _normalized_key(title)
        entries.append(entry)

    exact_groups = _group_by(entries, "sha256")
    normalized_groups = _group_by(entries, "normalized_text_sha256")
    title_groups = _group_by(
        (entry for entry in entries if entry.get("category") == "course_manifest"),
        "course_title_key",
    )

    candidate_groups: list[dict[str, object]] = []
    for value, paths in sorted(exact_groups.items()):
        candidate_groups.append(
            _candidate_group(
                "exact_sha256_match",
                value,
                paths,
                "Same bytes are objective evidence of a possible copied file; this is not a semantic equivalence or deletion instruction.",
            )
        )
    for value, paths in sorted(normalized_groups.items()):
        exact_values = {entry["sha256"] for entry in entries if entry.get("normalized_text_sha256") == value}
        if len(exact_values) == 1:
            continue
        candidate_groups.append(
            _candidate_group(
                "normalized_text_match",
                value,
                paths,
                "Text matches after line-ending normalization but differs at byte level; inspect provenance before treating it as redundant.",
            )
        )
    for value, paths in sorted(title_groups.items()):
        candidate_groups.append(
            _candidate_group(
                "course_title_match",
                value,
                paths,
                "Manifest titles normalize to the same value; this is a thematic/name collision signal, not proof that the courses are duplicates.",
            )
        )

    groups_by_path: dict[str, list[dict[str, object]]] = defaultdict(list)
    for group in candidate_groups:
        for path in group["paths"]:  # type: ignore[index]
            groups_by_path[str(path)].append(
                {"signal": group["signal"], "value": group["value"], "candidate_paths": group["paths"]}
            )
    for entry in entries:
        entry["signals"] = groups_by_path.get(str(entry["path"]), [])

    counts = Counter(str(entry["category"]) for entry in entries)
    return {
        "schema_version": "g1.v1",
        "tool": "tools/uni_inventory_g1.py",
        "scope": {
            "root": ".",
            "included": ["**/COURSE.yaml", "**/README.md", "**/schede.jsonl", "**/ESAMI/**"],
            "excluded_directories": sorted(IGNORED_DIRECTORY_NAMES),
            "deduplicated": False,
            "source_of_truth": "filesystem bytes in the selected checkout",
        },
        "evidence": {
            "files": entries,
            "counts_by_category": dict(sorted(counts.items())),
        },
        "interpretation": {
            "possible_duplicate_groups": candidate_groups,
            "boundaries": [
                "Signals are candidates for human review, not duplicate decisions.",
                "No source file was deduplicated, moved, overwritten, or deleted.",
                "A shared schema, topic, or exam/pack name is not by itself evidence of duplicate content.",
            ],
        },
    }


def write_report(root: Path, output: Path) -> None:
    report = build_report(root)
    output_path = output if output.is_absolute() else root / output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )


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
    root = args.root.resolve()
    write_report(root, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
