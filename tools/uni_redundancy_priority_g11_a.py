"""Build a deterministic human-review queue from the G10 candidate relation.

This tool consumes the already calculated ``candidate_review`` pairs from the
G10 report.  It groups only connected components of that relation, keeps every
original pair record, and assigns a transparent component priority.  It never
reads answer keys, copies didactic text, deduplicates, deletes, or modifies
source content.

Usage::

    python tools/uni_redundancy_priority_g11_a.py
    python tools/uni_redundancy_priority_g11_a.py --root . \
        --input docs/coordination/UNI_REDUNDANCY_AUDIT_G10_A.json \
        --output docs/coordination/UNI_REDUNDANCY_PRIORITY_G11_A.json
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


INPUT_RELATIVE_PATH = Path("docs/coordination/UNI_REDUNDANCY_AUDIT_G10_A.json")
REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_REDUNDANCY_PRIORITY_G11_A.json")
TOOL_PATH = "tools/uni_redundancy_priority_g11_a.py"
SCHEMA_VERSION = "g11a.v1"

PRIORITY_ORDER = [
    "collision_count desc",
    "coverage_count desc",
    "pack_count desc",
    "exam_count desc",
    "node_count desc",
    "source_group asc",
    "component_id asc",
]


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _candidate_ids_sha256(candidates: Iterable[dict[str, Any]]) -> str:
    candidate_ids = [str(candidate["candidate_id"]) for candidate in candidates]
    return _sha256(_canonical_json(candidate_ids).encode("utf-8"))


def _candidate_records_sha256(candidates: Iterable[dict[str, Any]]) -> str:
    records = [copy.deepcopy(candidate) for candidate in candidates]
    return _sha256(_canonical_json(records).encode("utf-8"))


def _unit_metadata(input_report: dict[str, Any]) -> dict[str, dict[str, str]]:
    metadata: dict[str, dict[str, str]] = {}
    for unit in input_report["evidence"]["units"]:
        unit_id = str(unit["unit_id"])
        if unit_id in metadata:
            raise ValueError(f"duplicate unit_id in G10 evidence: {unit_id}")
        metadata[unit_id] = {
            "source_path": str(unit["source_path"]),
            "source_group": str(unit["source_group"]),
            "unit_kind": str(unit["unit_kind"]),
        }
    return metadata


def _validate_candidates(
    input_report: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, dict[str, str]]]:
    candidates = input_report["results"]["candidate_review"]
    if not isinstance(candidates, list):
        raise ValueError("G10 results.candidate_review must be an array")
    metadata = _unit_metadata(input_report)
    seen_candidate_ids: set[str] = set()
    seen_pairs: set[tuple[str, str]] = set()
    for candidate in candidates:
        candidate_id = str(candidate["candidate_id"])
        left_id = str(candidate["left_unit_id"])
        right_id = str(candidate["right_unit_id"])
        if candidate_id in seen_candidate_ids:
            raise ValueError(f"duplicate candidate_id in G10 relation: {candidate_id}")
        if left_id == right_id:
            raise ValueError(f"self-loop in G10 relation: {candidate_id}")
        if left_id not in metadata or right_id not in metadata:
            raise ValueError(f"candidate references missing G10 unit: {candidate_id}")
        if metadata[left_id]["source_group"] != metadata[right_id]["source_group"]:
            raise ValueError(f"cross-source candidate is outside G10 relation scope: {candidate_id}")
        if str(candidate["source_group"]) != metadata[left_id]["source_group"]:
            raise ValueError(f"candidate source_group disagrees with G10 evidence: {candidate_id}")
        pair_key = tuple(sorted((left_id, right_id)))
        if pair_key in seen_pairs:
            raise ValueError(f"duplicate undirected candidate pair in G10 relation: {candidate_id}")
        seen_candidate_ids.add(candidate_id)
        seen_pairs.add(pair_key)
    return candidates, metadata


def _connected_components(candidates: list[dict[str, Any]]) -> list[tuple[set[str], list[dict[str, Any]]]]:
    adjacency: dict[str, set[str]] = {}
    pair_by_unit: dict[str, list[dict[str, Any]]] = {}
    for candidate in candidates:
        left_id = str(candidate["left_unit_id"])
        right_id = str(candidate["right_unit_id"])
        adjacency.setdefault(left_id, set()).add(right_id)
        adjacency.setdefault(right_id, set()).add(left_id)
        pair_by_unit.setdefault(left_id, []).append(candidate)
        pair_by_unit.setdefault(right_id, []).append(candidate)

    unvisited = set(adjacency)
    components: list[tuple[set[str], list[dict[str, Any]]]] = []
    while unvisited:
        start = min(unvisited)
        stack = [start]
        nodes: set[str] = set()
        while stack:
            node = stack.pop()
            if node not in unvisited:
                continue
            unvisited.remove(node)
            nodes.add(node)
            stack.extend(sorted(adjacency[node], reverse=True))
        candidate_ids = {
            str(candidate["candidate_id"])
            for node in nodes
            for candidate in pair_by_unit[node]
        }
        pairs = sorted(
            (
                candidate
                for candidate in candidates
                if str(candidate["candidate_id"]) in candidate_ids
            ),
            key=lambda candidate: str(candidate["candidate_id"]),
        )
        components.append((nodes, pairs))
    return sorted(
        components,
        key=lambda item: (
            str(item[1][0]["candidate_id"]),
            min(item[0]),
        ),
    )


def _pack_path(source_path: str) -> str | None:
    parts = PurePosixPath(source_path).parts
    try:
        schede_index = parts.index("schede")
    except ValueError:
        return None
    if schede_index == 0:
        return None
    return "/".join(parts[:schede_index])


def _coverage(nodes: set[str], metadata: dict[str, dict[str, str]]) -> dict[str, Any]:
    source_paths = sorted({metadata[node]["source_path"] for node in nodes})
    pack_paths = sorted(
        {
            pack_path
            for node in nodes
            if (pack_path := _pack_path(metadata[node]["source_path"])) is not None
            and metadata[node]["source_group"] == "cards"
        }
    )
    exam_paths = sorted(
        {
            metadata[node]["source_path"]
            for node in nodes
            if metadata[node]["source_group"] == "public_exams"
        }
    )
    return {
        "source_paths": source_paths,
        "pack_paths": pack_paths,
        "exam_paths": exam_paths,
        "source_file_count": len(source_paths),
        "pack_count": len(pack_paths),
        "exam_count": len(exam_paths),
        "coverage_count": len(pack_paths) + len(exam_paths),
    }


def _component_record(
    component_id: str,
    nodes: set[str],
    pairs: list[dict[str, Any]],
    metadata: dict[str, dict[str, str]],
) -> dict[str, Any]:
    source_groups = sorted({metadata[node]["source_group"] for node in nodes})
    if len(source_groups) != 1:
        raise ValueError(f"component spans source groups: {component_id}")
    coverage = _coverage(nodes, metadata)
    collision_count = len(pairs)
    priority_key = {
        "collision_count": collision_count,
        "coverage_count": coverage["coverage_count"],
        "pack_count": coverage["pack_count"],
        "exam_count": coverage["exam_count"],
        "node_count": len(nodes),
        "source_group": source_groups[0],
        "component_id": component_id,
    }
    return {
        "component_id": component_id,
        "priority_rank": None,
        "priority_key": priority_key,
        "source_group": source_groups[0],
        "unit_ids": sorted(nodes),
        "coverage": coverage,
        "collision_count": collision_count,
        "pairs": [copy.deepcopy(pair) for pair in pairs],
        "human_review": {
            "required": True,
            "decision": None,
            "decision_values": [
                "keep_both",
                "not_redundant",
                "merge_candidate",
                "needs_source_review",
            ],
            "instruction": "A human must review every preserved pair, its provenance, purpose and content before any future action.",
        },
    }


def _priority_sort_key(component: dict[str, Any]) -> tuple[Any, ...]:
    key = component["priority_key"]
    return (
        -int(key["collision_count"]),
        -int(key["coverage_count"]),
        -int(key["pack_count"]),
        -int(key["exam_count"]),
        -int(key["node_count"]),
        str(key["source_group"]),
        str(key["component_id"]),
    )


def build_report(
    input_report: dict[str, Any],
    *,
    input_path: str = INPUT_RELATIVE_PATH.as_posix(),
    input_report_sha256: str | None = None,
) -> dict[str, Any]:
    candidates, metadata = _validate_candidates(input_report)
    components: list[dict[str, Any]] = []
    for ordinal, (nodes, pairs) in enumerate(_connected_components(candidates), start=1):
        components.append(
            _component_record(
                f"component-{ordinal:04d}",
                nodes,
                pairs,
                metadata,
            )
        )
    components.sort(key=_priority_sort_key)
    for priority_rank, component in enumerate(components, start=1):
        component["priority_rank"] = priority_rank

    preserved_pairs = [
        pair
        for component in components
        for pair in component["pairs"]
    ]
    preserved_pair_ids = [str(pair["candidate_id"]) for pair in preserved_pairs]
    expected_pair_ids = [str(pair["candidate_id"]) for pair in candidates]
    if sorted(preserved_pair_ids) != sorted(expected_pair_ids):
        raise ValueError("component queue does not preserve the G10 candidate relation exactly")

    unit_ids = sorted({unit_id for component in components for unit_id in component["unit_ids"]})
    return {
        "schema_version": SCHEMA_VERSION,
        "tool": TOOL_PATH,
        "input": {
            "path": input_path,
            "schema_version": input_report.get("schema_version"),
            "candidate_pair_count": len(candidates),
            "candidate_ids_sha256": _candidate_ids_sha256(candidates),
            "candidate_records_sha256": _candidate_records_sha256(candidates),
            "report_sha256": input_report_sha256,
        },
        "scope": {
            "relation_source": "G10 results.candidate_review",
            "relation_reused_without_recalculation": True,
            "answers_read": False,
            "didactic_content_copied": False,
            "didactic_content_modified": False,
            "automatic_deduplication": False,
            "files_deleted": False,
            "source_of_truth": "the selected G10 JSON report and its unit metadata",
        },
        "priority_rule": {
            "collision_count_definition": "number of preserved candidate_review pair records in the connected component; this is not an exact-hash duplicate count",
            "coverage_count_definition": "number of distinct pack paths plus distinct public exam file paths represented by component units",
            "ordering": PRIORITY_ORDER,
            "priority_rank_definition": "one-based position after applying the declared ordering; lower rank is earlier in the review queue",
            "tie_breakers_are_deterministic": True,
        },
        "results": {
            "candidate_pair_count": len(candidates),
            "connected_component_count": len(components),
            "unit_count": len(unit_ids),
            "candidate_pair_ids": preserved_pair_ids,
            "queue": components,
        },
        "boundaries": [
            "Only G10 candidate_review pairs are used as relation edges; no new relation is inferred.",
            "Connected components group pairs for review and do not assert semantic equivalence.",
            "Every original candidate pair is preserved exactly once in its component.",
            "Human review is required for every pair; no automatic merge, deletion or deduplication is performed.",
            "The report contains identifiers, hashes, metrics and provenance paths only; it does not copy didactic question or card text.",
        ],
    }


def load_report(path: Path) -> tuple[dict[str, Any], str]:
    raw = path.read_bytes()
    return json.loads(raw.decode("utf-8")), _sha256(raw)


def write_report(root: Path, input_path: Path, output_path: Path) -> None:
    resolved_input = input_path if input_path.is_absolute() else root / input_path
    resolved_output = output_path if output_path.is_absolute() else root / output_path
    input_report, input_sha256 = load_report(resolved_input)
    report = build_report(
        input_report,
        input_path=input_path.as_posix(),
        input_report_sha256=input_sha256,
    )
    resolved_output.parent.mkdir(parents=True, exist_ok=True)
    resolved_output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--input", type=Path, default=INPUT_RELATIVE_PATH)
    parser.add_argument("--output", type=Path, default=REPORT_RELATIVE_PATH)
    args = parser.parse_args(argv)
    write_report(args.root.resolve(), args.input, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
