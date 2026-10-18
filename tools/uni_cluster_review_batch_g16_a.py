"""Import and export one controlled G13/G14 cluster-review batch.

G16-A deliberately keeps human review outside the canonical G13 packet and
G14 progress register.  ``export`` creates a metadata-only template for one
batch with a completely null review.  ``import`` accepts only that template
with review fields changed atomically: a non-null decision requires a
non-empty ``evidence_ref``, ``reviewer`` and ``rationale``.  The imported
result is written to a separate output file; neither canonical input is ever
written.

Usage::

    python tools/uni_cluster_review_batch_g16_a.py --root . export \
        --batch-id batch-01 --output work/g16_batch-01.template.json
    python tools/uni_cluster_review_batch_g16_a.py --root . import \
        --input work/g16_batch-01.review.json \
        --output work/g16_batch-01.imported.json
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any

try:
    from tools.uni_cluster_review_packet_g13_a import (
        ALLOWED_DECISIONS,
        validate_packet,
    )
    from tools.uni_cluster_review_progress_g14_a import validate_progress_register
except ModuleNotFoundError:  # Direct ``python tools/<script>.py`` execution.
    from uni_cluster_review_packet_g13_a import ALLOWED_DECISIONS, validate_packet
    from uni_cluster_review_progress_g14_a import validate_progress_register


G13_RELATIVE_PATH = Path("docs/coordination/UNI_CLUSTER_REVIEW_PACKET_G13_A.json")
G14_RELATIVE_PATH = Path("docs/coordination/UNI_CLUSTER_REVIEW_PROGRESS_G14_A.json")
SCHEMA_RELATIVE_PATH = Path("docs/coordination/UNI_CLUSTER_REVIEW_BATCH_G16_A.schema.json")
TOOL_PATH = "tools/uni_cluster_review_batch_g16_a.py"
SCHEMA_VERSION = "g16a.v1"
G13_SCHEMA_VERSION = "g13a.v1"
G14_SCHEMA_VERSION = "g14a.v1"
EXPECTED_CLUSTER_COUNT = 85
EXPECTED_BATCH_COUNT = 9
REVIEW_FIELDS = ("decision", "evidence_ref", "reviewer", "rationale")
PROTECTED_INPUTS = (G13_RELATIVE_PATH, G14_RELATIVE_PATH)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _clone(value: Any) -> Any:
    return copy.deepcopy(value)


def load_json(path: Path) -> tuple[dict[str, Any], str]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value, _sha256(raw)


def _require_dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be an object")
    return value


def _non_empty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _placeholder() -> dict[str, None]:
    return {field: None for field in REVIEW_FIELDS}


def _source_report(path: Path, schema_version: str, sha256: str | None) -> dict[str, Any]:
    return {
        "path": path.as_posix(),
        "schema_version": schema_version,
        "sha256": sha256,
    }


def _validate_initial_sources(
    g13: dict[str, Any],
    g14: dict[str, Any],
    *,
    g13_sha256: str | None,
    expected_cluster_count: int | None,
    expected_batch_count: int | None,
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    validate_packet(g13, expected_cluster_count=expected_cluster_count)
    validate_progress_register(
        g14,
        expected_cluster_count=expected_cluster_count,
        expected_batch_count=expected_batch_count,
    )
    if g14.get("input", {}).get("schema_version") != G13_SCHEMA_VERSION:
        raise ValueError("G16-A requires G14 input schema g13a.v1")
    recorded_sha = g14.get("input", {}).get("packet_sha256")
    if recorded_sha is not None and recorded_sha != g13_sha256:
        raise ValueError("G14 does not reference the supplied G13 packet bytes")

    g13_by_id = {str(item["cluster_id"]): item for item in g13["clusters"]}
    g14_by_id = {str(item["cluster_id"]): item for item in g14["clusters"]}
    if set(g13_by_id) != set(g14_by_id):
        raise ValueError("G13 and G14 cluster IDs do not match")
    for cluster_id, cluster in g13_by_id.items():
        review = _require_dict(cluster.get("review"), f"G13 review {cluster_id}")
        if review != _placeholder():
            raise ValueError("G13 packet must remain in its initial all-null state")
        progress = g14_by_id[cluster_id]
        if progress.get("status") != "open":
            raise ValueError("G14 source must remain open while exporting a fresh template")
        if any(progress.get(field) is not None for field in ("evidence_ref", "reviewer", "rationale")):
            raise ValueError("G14 source must keep all audit fields null while exporting a fresh template")
        if progress.get("priority_rank") != cluster.get("priority_rank"):
            raise ValueError(f"G13/G14 priority mismatch: {cluster_id}")
        if progress.get("batch") != cluster.get("batch"):
            raise ValueError(f"G13/G14 batch mismatch: {cluster_id}")
    return g13_by_id, g14_by_id


def _batch_by_id(report: dict[str, Any], batch_id: str) -> dict[str, Any]:
    for batch in report.get("batches", []):
        if str(batch.get("batch_id")) == batch_id:
            return batch
    raise ValueError(f"unknown batch_id: {batch_id}")


def _entry_from_cluster(cluster: dict[str, Any]) -> dict[str, Any]:
    return {
        "cluster_id": str(cluster["cluster_id"]),
        "priority_rank": int(cluster["priority_rank"]),
        "batch_rank": int(cluster["batch"]["batch_rank"]),
        "g11": _clone(cluster["g11"]),
        "references": _clone(cluster["references"]),
        "g12_contract_ref": str(cluster["g12_contract_ref"]),
        "review": _placeholder(),
    }


def _batch_metadata(batch: dict[str, Any]) -> dict[str, Any]:
    return {
        "batch_id": str(batch["batch_id"]),
        "priority_rank_start": int(batch["priority_rank_start"]),
        "priority_rank_end": int(batch["priority_rank_end"]),
        "cluster_count": int(batch["cluster_count"]),
        "cluster_ids": [str(cluster_id) for cluster_id in batch["cluster_ids"]],
    }


def _scope(*, template: bool, imported: bool) -> dict[str, Any]:
    return {
        "batch_level": "single_g13_batch",
        "human_review_required": True,
        "template": template,
        "import_validated": imported,
        "human_fields_only": True,
        "answers_read": False,
        "didactic_content_copied": False,
        "didactic_content_modified": False,
        "canonical_packets_modified": False,
        "automatic_decision": False,
        "source_of_truth": "G13 packet + G14 progress register metadata",
    }


def _contract() -> dict[str, Any]:
    return {
        "initial_decision": None,
        "allowed_decisions": list(ALLOWED_DECISIONS),
        "evidence_ref_required_for_non_null_decision": True,
        "reviewer_required_for_non_null_decision": True,
        "rationale_required_for_non_null_decision": True,
        "decision_is_not_an_action": True,
    }


def build_batch_template(
    g13: dict[str, Any],
    g14: dict[str, Any],
    batch_id: str,
    *,
    g13_sha256: str | None = None,
    g14_sha256: str | None = None,
    g13_path: str = G13_RELATIVE_PATH.as_posix(),
    g14_path: str = G14_RELATIVE_PATH.as_posix(),
    expected_cluster_count: int | None = EXPECTED_CLUSTER_COUNT,
    expected_batch_count: int | None = EXPECTED_BATCH_COUNT,
) -> dict[str, Any]:
    g13_by_id, _ = _validate_initial_sources(
        g13,
        g14,
        g13_sha256=g13_sha256,
        expected_cluster_count=expected_cluster_count,
        expected_batch_count=expected_batch_count,
    )
    batch = _batch_by_id(g13, batch_id)
    entries = [_entry_from_cluster(g13_by_id[str(cluster_id)]) for cluster_id in batch["cluster_ids"]]
    payload = {
        "schema_version": SCHEMA_VERSION,
        "tool": TOOL_PATH,
        "mode": "template",
        "source_reports": {
            "g13_packet": _source_report(Path(g13_path), G13_SCHEMA_VERSION, g13_sha256),
            "g14_progress": _source_report(Path(g14_path), G14_SCHEMA_VERSION, g14_sha256),
        },
        "scope": _scope(template=True, imported=False),
        "review_contract": _contract(),
        "batch": _batch_metadata(batch),
        "entries": entries,
        "boundaries": [
            "This is a separate single-batch review envelope, not a canonical packet.",
            "The export contains metadata and source references only; it contains no exam or card text.",
            "The template starts with decision, evidence_ref, reviewer and rationale all null.",
            "A human decision is accepted only when evidence_ref, reviewer and rationale are all non-empty.",
            "Import writes a separate reviewed envelope and never rewrites G13, G14, cards or exams.",
            "A decision is a review outcome, not an instruction to merge, reject, delete or modify content.",
        ],
    }
    validate_batch_payload(payload, expected_batch_id=batch_id, expected_mode="template")
    return payload


def _validate_review(review: Any, *, entry_id: str) -> None:
    review = _require_dict(review, f"review {entry_id}")
    if set(review) != set(REVIEW_FIELDS):
        raise ValueError(f"review fields are incomplete or unexpected: {entry_id}")
    decision = review["decision"]
    audit = tuple(review[field] for field in REVIEW_FIELDS[1:])
    if decision is None:
        if any(value is not None for value in audit):
            raise ValueError(f"partial human review is not allowed: {entry_id}")
        return
    if decision not in ALLOWED_DECISIONS:
        raise ValueError(f"unsupported decision: {entry_id}")
    if not all(_non_empty(value) for value in audit):
        raise ValueError(f"decision requires evidence_ref, reviewer and rationale: {entry_id}")


def validate_batch_payload(
    payload: dict[str, Any],
    *,
    expected_batch_id: str | None = None,
    expected_mode: str | None = None,
) -> None:
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("unexpected G16 schema_version")
    if payload.get("tool") != TOOL_PATH:
        raise ValueError("unexpected G16 tool")
    if payload.get("mode") not in {"template", "reviewed"}:
        raise ValueError("mode must be template or reviewed")
    if expected_mode is not None and payload.get("mode") != expected_mode:
        raise ValueError(f"expected {expected_mode} payload")
    source_reports = _require_dict(payload.get("source_reports"), "source_reports")
    for name, schema_version in (("g13_packet", G13_SCHEMA_VERSION), ("g14_progress", G14_SCHEMA_VERSION)):
        source = _require_dict(source_reports.get(name), name)
        if source.get("schema_version") != schema_version or not _non_empty(source.get("path")):
            raise ValueError(f"invalid source report: {name}")
        if source.get("sha256") is not None and not (
            isinstance(source.get("sha256"), str) and len(source["sha256"]) == 64
        ):
            raise ValueError(f"invalid source hash: {name}")
    scope = _require_dict(payload.get("scope"), "scope")
    expected_scope = _scope(template=payload["mode"] == "template", imported=payload["mode"] == "reviewed")
    if scope != expected_scope:
        raise ValueError("scope does not describe the G16 workflow state")
    contract = _require_dict(payload.get("review_contract"), "review_contract")
    if contract != _contract():
        raise ValueError("review contract changed unexpectedly")
    batch = _require_dict(payload.get("batch"), "batch")
    batch_id = str(batch.get("batch_id", ""))
    if expected_batch_id is not None and batch_id != expected_batch_id:
        raise ValueError(f"unexpected batch_id: {batch_id}")
    cluster_ids = batch.get("cluster_ids")
    if not isinstance(cluster_ids, list) or not cluster_ids:
        raise ValueError("batch cluster_ids must be a non-empty array")
    if batch.get("cluster_count") != len(cluster_ids):
        raise ValueError("batch cluster_count mismatch")
    entries = payload.get("entries")
    if not isinstance(entries, list) or len(entries) != len(cluster_ids):
        raise ValueError("entries do not cover the selected batch")
    seen: list[str] = []
    for entry in entries:
        entry = _require_dict(entry, "batch entry")
        entry_id = str(entry.get("cluster_id", ""))
        if entry_id in seen or entry_id not in cluster_ids:
            raise ValueError(f"unexpected or duplicate cluster entry: {entry_id}")
        _validate_review(entry.get("review"), entry_id=entry_id)
        seen.append(entry_id)
    if seen != [str(cluster_id) for cluster_id in cluster_ids]:
        raise ValueError("entries must remain in canonical batch order")
    if not isinstance(payload.get("boundaries"), list) or not payload["boundaries"]:
        raise ValueError("boundaries must be a non-empty array")


def import_batch_review(
    template: dict[str, Any],
    g13: dict[str, Any],
    g14: dict[str, Any],
    *,
    g13_sha256: str | None = None,
    g14_sha256: str | None = None,
    expected_cluster_count: int | None = EXPECTED_CLUSTER_COUNT,
    expected_batch_count: int | None = EXPECTED_BATCH_COUNT,
) -> dict[str, Any]:
    validate_batch_payload(template, expected_mode="template")
    batch_id = str(template["batch"]["batch_id"])
    expected = build_batch_template(
        g13,
        g14,
        batch_id,
        g13_sha256=g13_sha256,
        g14_sha256=g14_sha256,
        g13_path=str(template["source_reports"]["g13_packet"]["path"]),
        g14_path=str(template["source_reports"]["g14_progress"]["path"]),
        expected_cluster_count=expected_cluster_count,
        expected_batch_count=expected_batch_count,
    )
    if template["source_reports"] != expected["source_reports"]:
        raise ValueError("template source reports do not match supplied canonical inputs")
    for actual, canonical in zip(template["entries"], expected["entries"]):
        if {key: value for key, value in actual.items() if key != "review"} != {
            key: value for key, value in canonical.items() if key != "review"
        }:
            raise ValueError(f"non-review metadata changed for cluster {actual.get('cluster_id')}")

    reviewed = _clone(template)
    reviewed["mode"] = "reviewed"
    reviewed["scope"] = _scope(template=False, imported=True)
    validate_batch_payload(reviewed, expected_batch_id=batch_id, expected_mode="reviewed")
    return reviewed


def _write_json(path: Path, payload: dict[str, Any], *, root: Path) -> None:
    resolved = path.resolve()
    protected = {(root / relative).resolve() for relative in PROTECTED_INPUTS}
    if resolved in protected:
        raise ValueError(f"G16 output cannot overwrite canonical input: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _root_path(root: Path, path: Path) -> Path:
    return path if path.is_absolute() else root / path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    subparsers = parser.add_subparsers(dest="command", required=True)

    export_parser = subparsers.add_parser("export", help="export one null review template")
    export_parser.add_argument("--batch-id", required=True)
    export_parser.add_argument("--output", type=Path, required=True)

    import_parser = subparsers.add_parser("import", help="validate and export a reviewed batch")
    import_parser.add_argument("--input", type=Path, required=True)
    import_parser.add_argument("--output", type=Path, required=True)

    args = parser.parse_args(argv)
    root = args.root.resolve()
    g13, g13_sha256 = load_json(root / G13_RELATIVE_PATH)
    g14, g14_sha256 = load_json(root / G14_RELATIVE_PATH)
    if args.command == "export":
        payload = build_batch_template(
            g13,
            g14,
            args.batch_id,
            g13_sha256=g13_sha256,
            g14_sha256=g14_sha256,
        )
    else:
        template, _ = load_json(_root_path(root, args.input))
        payload = import_batch_review(
            template,
            g13,
            g14,
            g13_sha256=g13_sha256,
            g14_sha256=g14_sha256,
        )
    output = _root_path(root, args.output)
    _write_json(output, payload, root=root)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
