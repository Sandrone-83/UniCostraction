"""Build a deterministic, non-destructive redundancy audit for cards and exams.

The audit indexes JSONL card records and public exam question bodies.  It keeps
raw and content hashes, reports exact duplicate groups, and emits similarity
review pairs only when an explicit token-set Jaccard threshold is met.  No
source content is written, merged, deleted, or automatically deduplicated.

Usage::

    python tools/uni_redundancy_audit_g10_a.py
    python tools/uni_redundancy_audit_g10_a.py --root . \
        --output docs/coordination/UNI_REDUNDANCY_AUDIT_G10_A.json
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


REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_REDUNDANCY_AUDIT_G10_A.json")
CARD_ROOT = Path("UNIVERSITA_EDILIZIA")
EXAM_ROOT = CARD_ROOT / "ESAMI"
IGNORED_DIRECTORY_NAMES = frozenset({".git", "tests", "work"})

SIMILARITY_METRIC = "token_set_jaccard"
SIMILARITY_THRESHOLD = 0.90
MIN_UNIQUE_TOKENS = 12
MAX_TOKEN_POSTING_FREQUENCY = 16
MAX_CANDIDATE_PAIRS = 50_000

STANDARD_QUESTION_RE = re.compile(r"^\s*##\s*Domanda\s+(\d+)\s*(.*?)\s*$", re.IGNORECASE)
LEGACY_QUESTION_RE = re.compile(r"^\s*\*\*D(\d+)\.\*\*\s*(.*?)\s*$", re.IGNORECASE)
TOKEN_RE = re.compile(r"[\w]+", re.UNICODE)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _relative_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _normalise_line_endings(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def _normalise_text(text: str) -> str:
    """Apply conservative comparison normalization, not content rewriting."""

    normalized = unicodedata.normalize("NFKC", text)
    normalized = _normalise_line_endings(normalized).casefold()
    return " ".join(normalized.split())


def _tokens(text: str) -> frozenset[str]:
    return frozenset(TOKEN_RE.findall(_normalise_text(text)))


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _decode(data: bytes) -> tuple[str | None, str | None]:
    try:
        return data.decode("utf-8-sig"), None
    except UnicodeDecodeError as error:
        return None, f"invalid_utf8_at_byte_{error.start}"


def discover_card_files(root: Path) -> list[Path]:
    base = root / CARD_ROOT
    if not base.is_dir():
        return []
    return sorted(
        (
            path
            for path in base.rglob("schede.jsonl")
            if path.is_file()
            and not path.is_symlink()
            and not any(part in IGNORED_DIRECTORY_NAMES for part in path.relative_to(root).parts)
        ),
        key=lambda path: _relative_path(path, root),
    )


def discover_exam_files(root: Path) -> list[Path]:
    if not (root / EXAM_ROOT).is_dir():
        return []
    return sorted(
        (
            path
            for path in (root / EXAM_ROOT).rglob("domande.md")
            if path.is_file() and not path.is_symlink()
        ),
        key=lambda path: _relative_path(path, root),
    )


def _unit(
    *,
    unit_id: str,
    source_path: str,
    source_group: str,
    unit_kind: str,
    ordinal: int,
    content: str,
    raw_content: str,
    content_sha256: str,
) -> dict[str, Any]:
    normalized_content = _normalise_text(content)
    token_values = _tokens(content)
    return {
        "unit_id": unit_id,
        "source_path": source_path,
        "source_group": source_group,
        "unit_kind": unit_kind,
        "ordinal": ordinal,
        "raw_sha256": _sha256(raw_content.encode("utf-8")),
        "content_sha256": content_sha256,
        "normalized_content_sha256": _sha256(normalized_content.encode("utf-8")),
        "unique_token_count": len(token_values),
        "_tokens": token_values,
    }


def _read_card_file(root: Path, path: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    data = path.read_bytes()
    text, decode_error = _decode(data)
    relative = _relative_path(path, root)
    file_entry: dict[str, Any] = {
        "path": relative,
        "source_group": "cards",
        "unit_kind": "card",
        "raw_sha256": _sha256(data),
        "normalized_file_sha256": None,
        "unit_count": 0,
        "parse_errors": [],
        "parse_complete": False,
    }
    if decode_error or text is None:
        file_entry["parse_errors"] = [decode_error or "invalid_utf8"]
        return file_entry, []

    normalized_text = _normalise_line_endings(text)
    file_entry["normalized_file_sha256"] = _sha256(normalized_text.encode("utf-8"))
    units: list[dict[str, Any]] = []
    for line_number, line in enumerate(normalized_text.split("\n"), start=1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            file_entry["parse_errors"].append(f"line_{line_number}:{error.msg}")
            continue
        if not isinstance(record, dict):
            file_entry["parse_errors"].append(f"line_{line_number}:record_is_not_object")
            continue
        canonical = _canonical_json(record)
        units.append(
            _unit(
                unit_id=f"card:{relative}#line-{line_number:04d}",
                source_path=relative,
                source_group="cards",
                unit_kind="card",
                ordinal=line_number,
                content=canonical,
                raw_content=line,
                content_sha256=_sha256(canonical.encode("utf-8")),
            )
        )
    file_entry["unit_count"] = len(units)
    file_entry["parse_complete"] = not file_entry["parse_errors"]
    return file_entry, units


def _exam_questions(text: str) -> tuple[list[tuple[int, str, str]], list[str]]:
    """Return (number, format, body) tuples and parser diagnostics."""

    lines = _normalise_line_endings(text).split("\n")
    starts: list[tuple[int, int, str, str]] = []
    errors: list[str] = []
    for index, line in enumerate(lines):
        match = STANDARD_QUESTION_RE.match(line) or LEGACY_QUESTION_RE.match(line)
        if not match:
            continue
        format_name = "standard_heading" if STANDARD_QUESTION_RE.match(line) else "legacy_d_heading"
        starts.append((index, int(match.group(1)), format_name, match.group(2).strip()))

    if not starts:
        errors.append("no_question_headings")
        return [], errors

    numbers = [number for _, number, _, _ in starts]
    if len(numbers) != len(set(numbers)):
        errors.append("duplicate_question_numbers")
    if numbers != list(range(1, len(numbers) + 1)):
        errors.append("question_numbers_not_consecutive_from_one")

    questions: list[tuple[int, str, str]] = []
    for position, (start, number, format_name, inline_body) in enumerate(starts):
        end = starts[position + 1][0] if position + 1 < len(starts) else len(lines)
        body_lines = lines[start + 1 : end]
        body = "\n".join(([inline_body] if inline_body else []) + body_lines).strip()
        if not body:
            errors.append(f"question_{number}_empty_body")
        questions.append((number, format_name, body))
    return questions, errors


def _read_exam_file(root: Path, path: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    data = path.read_bytes()
    text, decode_error = _decode(data)
    relative = _relative_path(path, root)
    file_entry: dict[str, Any] = {
        "path": relative,
        "source_group": "public_exams",
        "unit_kind": "exam_question",
        "raw_sha256": _sha256(data),
        "normalized_file_sha256": None,
        "unit_count": 0,
        "question_formats": [],
        "parse_errors": [],
        "parse_complete": False,
    }
    if decode_error or text is None:
        file_entry["parse_errors"] = [decode_error or "invalid_utf8"]
        return file_entry, []

    normalized_text = _normalise_line_endings(text)
    file_entry["normalized_file_sha256"] = _sha256(normalized_text.encode("utf-8"))
    questions, errors = _exam_questions(normalized_text)
    file_entry["parse_errors"] = errors
    file_entry["question_formats"] = sorted({format_name for _, format_name, _ in questions})
    units: list[dict[str, Any]] = []
    for ordinal, (number, format_name, body) in enumerate(questions, start=1):
        units.append(
            _unit(
                unit_id=f"exam:{relative}#question-{ordinal:04d}",
                source_path=relative,
                source_group="public_exams",
                unit_kind="exam_question",
                ordinal=number,
                content=body,
                raw_content=body,
                content_sha256=_sha256(body.encode("utf-8")),
            )
        )
        units[-1]["question_number"] = number
        units[-1]["question_format"] = format_name
    file_entry["unit_count"] = len(units)
    file_entry["parse_complete"] = not errors
    return file_entry, units


def _public_unit(unit: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in unit.items() if not key.startswith("_")}


def _group_exact(units: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for unit in units:
        grouped[str(unit["content_sha256"])].append(unit)
    groups: list[dict[str, Any]] = []
    for content_sha256, members in sorted(grouped.items()):
        if len(members) < 2:
            continue
        ordered = sorted(members, key=lambda item: str(item["unit_id"]))
        groups.append(
            {
                "group_id": f"duplicate-exact-{len(groups) + 1:04d}",
                "match_basis": "content_sha256",
                "content_sha256": content_sha256,
                "unit_ids": [str(item["unit_id"]) for item in ordered],
                "source_groups": sorted({str(item["source_group"]) for item in ordered}),
                "interpretation": "Canonical content hash collision; this is evidence for review, not an instruction to delete or merge.",
            }
        )
    return groups


def _candidate_pairs(units: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], bool]:
    by_group: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for unit in units:
        by_group[str(unit["source_group"])].append(unit)

    candidates: list[tuple[str, str, dict[str, Any], dict[str, Any]]] = []
    for source_group, group in sorted(by_group.items()):
        postings: dict[str, list[str]] = defaultdict(list)
        units_by_id = {str(unit["unit_id"]): unit for unit in group}
        for unit in group:
            unit_id = str(unit["unit_id"])
            if int(unit["unique_token_count"]) < MIN_UNIQUE_TOKENS:
                continue
            for token in sorted(unit["_tokens"]):
                postings[token].append(unit_id)
        group_pairs: set[tuple[str, str]] = set()
        for token, posting in sorted(postings.items()):
            if len(posting) > MAX_TOKEN_POSTING_FREQUENCY:
                continue
            ordered = sorted(posting)
            for index, left_id in enumerate(ordered):
                for right_id in ordered[index + 1 :]:
                    group_pairs.add((left_id, right_id))

        for left_id, right_id in sorted(group_pairs):
            left = units_by_id.get(left_id)
            right = units_by_id.get(right_id)
            if left is None or right is None:
                continue
            if left["content_sha256"] == right["content_sha256"]:
                continue
            left_tokens = left["_tokens"]
            right_tokens = right["_tokens"]
            union = left_tokens | right_tokens
            if not union:
                continue
            score = len(left_tokens & right_tokens) / len(union)
            if score < SIMILARITY_THRESHOLD:
                continue
            candidates.append((left_id, right_id, left, right))

    output: list[dict[str, Any]] = []
    for left_id, right_id, left, right in sorted(candidates, key=lambda item: (item[0], item[1])):
        left_tokens = left["_tokens"]
        right_tokens = right["_tokens"]
        union = left_tokens | right_tokens
        score = len(left_tokens & right_tokens) / len(union) if union else 0.0
        if score < SIMILARITY_THRESHOLD:
            continue
        output.append(
            {
                "candidate_id": f"candidate-review-{len(output) + 1:05d}",
                "left_unit_id": left_id,
                "right_unit_id": right_id,
                "source_group": left["source_group"],
                "metric": SIMILARITY_METRIC,
                "score": round(score, 6),
                "threshold": SIMILARITY_THRESHOLD,
                "shared_token_count": len(left_tokens & right_tokens),
                "union_token_count": len(union),
                "interpretation": "Explicit token-set similarity above threshold; human review is required and semantic equivalence is not inferred.",
            }
        )
    output.sort(key=lambda item: (str(item["left_unit_id"]), str(item["right_unit_id"])))
    truncated = len(output) > MAX_CANDIDATE_PAIRS
    return output[:MAX_CANDIDATE_PAIRS], truncated


def build_report(root: Path) -> dict[str, Any]:
    root = root.resolve()
    files: list[dict[str, Any]] = []
    units: list[dict[str, Any]] = []
    for path in discover_card_files(root):
        file_entry, file_units = _read_card_file(root, path)
        files.append(file_entry)
        units.extend(file_units)
    for path in discover_exam_files(root):
        file_entry, file_units = _read_exam_file(root, path)
        files.append(file_entry)
        units.extend(file_units)
    files.sort(key=lambda item: str(item["path"]))
    units.sort(key=lambda item: str(item["unit_id"]))

    duplicate_exact = _group_exact(units)
    exact_unit_ids = {unit_id for group in duplicate_exact for unit_id in group["unit_ids"]}
    candidate_review, candidates_truncated = _candidate_pairs(units)
    candidate_unit_ids = {
        unit_id
        for candidate in candidate_review
        for unit_id in (candidate["left_unit_id"], candidate["right_unit_id"])
    }

    units_by_classification: dict[str, list[str]] = {
        "duplicate_exact": sorted(exact_unit_ids),
        "candidate_review": sorted(candidate_unit_ids - exact_unit_ids),
        "distinct": sorted(
            str(unit["unit_id"])
            for unit in units
            if str(unit["unit_id"]) not in exact_unit_ids | candidate_unit_ids
        ),
    }
    classification_by_unit = {
        unit_id: classification
        for classification, unit_ids in units_by_classification.items()
        for unit_id in unit_ids
    }
    public_units = []
    for unit in units:
        item = _public_unit(unit)
        item["classification"] = classification_by_unit[str(unit["unit_id"])]
        public_units.append(item)

    counts_by_group = Counter(str(file_entry["source_group"]) for file_entry in files)
    unit_counts = Counter(str(unit["source_group"]) for unit in units)
    classification_counts = {
        classification: len(unit_ids) for classification, unit_ids in units_by_classification.items()
    }
    return {
        "schema_version": "g10a.v1",
        "tool": "tools/uni_redundancy_audit_g10_a.py",
        "scope": {
            "root": ".",
            "included": [
                "UNIVERSITA_EDILIZIA/**/schede/schede.jsonl",
                "UNIVERSITA_EDILIZIA/ESAMI/**/domande.md",
            ],
            "excluded_directories": sorted(IGNORED_DIRECTORY_NAMES),
            "answers_read": False,
            "didactic_content_modified": False,
            "automatic_deduplication": False,
            "source_of_truth": "filesystem bytes in the selected checkout",
        },
        "normalization": {
            "version": "g10a-conservative-v1",
            "steps": [
                "decode UTF-8 with optional BOM",
                "normalize Unicode with NFKC for comparison text",
                "normalize CRLF/CR to LF",
                "casefold and collapse whitespace for similarity tokens only",
                "preserve JSON object values and field content for content_sha256",
            ],
            "content_hash_boundary": "content_sha256 uses sorted JSON keys for cards and line-ending-normalized question body bytes for exams; no semantic rewriting is applied",
        },
        "similarity": {
            "metric": SIMILARITY_METRIC,
            "threshold": SIMILARITY_THRESHOLD,
            "minimum_unique_tokens": MIN_UNIQUE_TOKENS,
            "maximum_token_posting_frequency": MAX_TOKEN_POSTING_FREQUENCY,
            "comparison_scope": "within_source_group_only",
            "candidate_bound": MAX_CANDIDATE_PAIRS,
            "candidate_generation": "shared-token inverted index followed by exact Jaccard calculation",
        },
        "evidence": {
            "files": files,
            "units": public_units,
            "file_counts_by_source_group": dict(sorted(counts_by_group.items())),
            "unit_counts_by_source_group": dict(sorted(unit_counts.items())),
        },
        "results": {
            "duplicate_exact": duplicate_exact,
            "candidate_review": candidate_review,
            "distinct": {
                "unit_ids": units_by_classification["distinct"],
                "interpretation": "No exact collision and no candidate met the configured explicit metric; this is not proof of semantic or didactic uniqueness.",
            },
            "classification_by_unit": classification_by_unit,
            "classification_counts": classification_counts,
            "candidate_pairs_truncated": candidates_truncated,
        },
        "boundaries": [
            "duplicate_exact means only that content_sha256 is equal for two or more indexed units; it is not an automatic deletion or merge decision.",
            "candidate_review means the explicit token_set_jaccard score meets the configured threshold; a human must inspect provenance, purpose and content.",
            "distinct means no configured signal was emitted, not that semantic, educational, factual, legal or licensing equivalence has been proven.",
            "Cards and exam questions are compared only within their source group; a question derived from a card is not automatically a duplicate.",
            "The audit does not inspect answer keys, decide correctness, or modify didactic files.",
        ],
    }


def write_report(root: Path, output: Path) -> None:
    report = build_report(root)
    output_path = output if output.is_absolute() else root / output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=REPORT_RELATIVE_PATH)
    args = parser.parse_args(argv)
    write_report(args.root.resolve(), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
