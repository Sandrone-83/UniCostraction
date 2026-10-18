"""Build and validate the G14-A cluster-review progress register.

The register is a metadata-only workflow ledger derived from the G13 packet. It
tracks one status per cluster and one aggregate status view per batch without
copying, modifying, merging, rejecting, or deleting any card or exam content.

Usage::

    python tools/uni_cluster_review_progress_g14_a.py
    python tools/uni_cluster_review_progress_g14_a.py --root .
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

try:
    from tools.uni_cluster_review_packet_g13_a import validate_packet
except ModuleNotFoundError:  # Direct ``python tools/<script>.py`` execution.
    from uni_cluster_review_packet_g13_a import validate_packet


INPUT_RELATIVE_PATH = Path("docs/coordination/UNI_CLUSTER_REVIEW_PACKET_G13_A.json")
REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_CLUSTER_REVIEW_PROGRESS_G14_A.json")
GUIDE_RELATIVE_PATH = Path("docs/coordination/UNI_CLUSTER_REVIEW_PROGRESS_G14_A.md")
TOOL_PATH = "tools/uni_cluster_review_progress_g14_a.py"
SCHEMA_VERSION = "g14a.v1"
INPUT_SCHEMA_VERSION = "g13a.v1"
EXPECTED_CLUSTER_COUNT = 85
EXPECTED_BATCH_COUNT = 9
ALLOWED_STATUSES = ["open", "in_review", "decided"]
AUDIT_FIELDS = ("evidence_ref", "reviewer", "rationale")


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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


def _placeholder() -> dict[str, None]:
    return {field: None for field in AUDIT_FIELDS}


def _non_empty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _status_counts(records: list[dict[str, Any]]) -> dict[str, int]:
    counts = Counter(str(record["status"]) for record in records)
    return {status: counts.get(status, 0) for status in ALLOWED_STATUSES}


def _validate_source_packet(packet: dict[str, Any], expected_cluster_count: int | None) -> None:
    if packet.get("schema_version") != INPUT_SCHEMA_VERSION:
        raise ValueError("G14-A requires a g13a.v1 packet")
    validate_packet(packet, expected_cluster_count=expected_cluster_count)
    for cluster in packet["clusters"]:
        review = _require_dict(cluster.get("review"), f"G13 review {cluster.get('cluster_id')}")
        if any(review.get(field) is not None for field in ("decision", *AUDIT_FIELDS)):
            raise ValueError("G13 packet must remain in its initial all-null state")


def _build_records(packet: dict[str, Any]) -> list[dict[str, Any]]:
    batch_rank_by_cluster: dict[str, int] = {}
    batch_id_by_cluster: dict[str, str] = {}
    for batch in packet["batches"]:
        for batch_rank, cluster_id in enumerate(batch["cluster_ids"], start=1):
            batch_rank_by_cluster[str(cluster_id)] = batch_rank
            batch_id_by_cluster[str(cluster_id)] = str(batch["batch_id"])

    records: list[dict[str, Any]] = []
    for cluster in packet["clusters"]:
        cluster_id = str(cluster["cluster_id"])
        records.append(
            {
                "cluster_id": cluster_id,
                "priority_rank": int(cluster["priority_rank"]),
                "batch": {
                    "batch_id": batch_id_by_cluster[cluster_id],
                    "batch_rank": batch_rank_by_cluster[cluster_id],
                },
                "status": "open",
                **_placeholder(),
            }
        )
    return records


def _build_batches(packet: dict[str, Any], records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_id = {record["cluster_id"]: record for record in records}
    batches: list[dict[str, Any]] = []
    for batch in packet["batches"]:
        batch_records = [by_id[str(cluster_id)] for cluster_id in batch["cluster_ids"]]
        batches.append(
            {
                "batch_id": str(batch["batch_id"]),
                "priority_rank_start": int(batch["priority_rank_start"]),
                "priority_rank_end": int(batch["priority_rank_end"]),
                "cluster_count": len(batch_records),
                "cluster_ids": [record["cluster_id"] for record in batch_records],
                "status_counts": _status_counts(batch_records),
                "decided_count": 0,
            }
        )
    return batches


def _coverage(records: list[dict[str, Any]], batch_count: int) -> dict[str, Any]:
    counts = _status_counts(records)
    return {
        "cluster_count": len(records),
        "batch_count": batch_count,
        "status_counts": counts,
        "open_count": counts["open"],
        "in_review_count": counts["in_review"],
        "decided_count": counts["decided"],
        "pending_count": counts["open"] + counts["in_review"],
        "all_evidence_refs_null": all(record["evidence_ref"] is None for record in records),
        "all_reviewers_null": all(record["reviewer"] is None for record in records),
        "all_rationales_null": all(record["rationale"] is None for record in records),
    }


def validate_progress_register(
    report: dict[str, Any],
    *,
    expected_cluster_count: int | None = EXPECTED_CLUSTER_COUNT,
    expected_batch_count: int | None = EXPECTED_BATCH_COUNT,
) -> None:
    """Validate status transitions and audit-field invariants for G14-A."""

    if report.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("unexpected G14 schema_version")
    records = report.get("clusters")
    if not isinstance(records, list):
        raise ValueError("clusters must be an array")
    if expected_cluster_count is not None and len(records) != expected_cluster_count:
        raise ValueError(f"expected {expected_cluster_count} clusters, got {len(records)}")

    seen_ids: set[str] = set()
    seen_ranks: set[int] = set()
    for record in records:
        record = _require_dict(record, "cluster progress record")
        cluster_id = str(record.get("cluster_id", ""))
        rank = record.get("priority_rank")
        if not cluster_id or cluster_id in seen_ids:
            raise ValueError(f"duplicate or empty cluster_id: {cluster_id}")
        if not isinstance(rank, int) or isinstance(rank, bool) or rank < 1:
            raise ValueError(f"invalid priority_rank: {cluster_id}")
        batch = _require_dict(record.get("batch"), f"batch reference {cluster_id}")
        if not _non_empty(batch.get("batch_id")) or not isinstance(batch.get("batch_rank"), int):
            raise ValueError(f"invalid batch reference: {cluster_id}")
        status = record.get("status")
        if status not in ALLOWED_STATUSES:
            raise ValueError(f"unsupported status for {cluster_id}: {status}")
        if any(field not in record for field in AUDIT_FIELDS):
            raise ValueError(f"audit fields are incomplete: {cluster_id}")

        evidence_ref = record["evidence_ref"]
        reviewer = record["reviewer"]
        rationale = record["rationale"]
        if status == "open":
            if any(value is not None for value in (evidence_ref, reviewer, rationale)):
                raise ValueError(f"open cluster must keep audit fields null: {cluster_id}")
        else:
            if not _non_empty(reviewer):
                raise ValueError(f"reviewer is required for {status}: {cluster_id}")
            if not _non_empty(rationale):
                raise ValueError(f"rationale is required for {status}: {cluster_id}")
            if status == "decided" and not _non_empty(evidence_ref):
                raise ValueError(f"evidence_ref is required to close cluster: {cluster_id}")
            if evidence_ref is not None and not _non_empty(evidence_ref):
                raise ValueError(f"evidence_ref must be non-empty or null: {cluster_id}")

        seen_ids.add(cluster_id)
        seen_ranks.add(rank)

    if seen_ranks != set(range(1, len(records) + 1)):
        raise ValueError("cluster priority ranks must be consecutive from 1")

    batches = report.get("batches")
    if not isinstance(batches, list):
        raise ValueError("batches must be an array")
    if expected_batch_count is not None and len(batches) != expected_batch_count:
        raise ValueError(f"expected {expected_batch_count} batches, got {len(batches)}")

    by_id = {record["cluster_id"]: record for record in records}
    seen_batch_ids: set[str] = set()
    batch_cluster_ids: list[str] = []
    for batch in batches:
        batch = _require_dict(batch, "batch progress record")
        batch_id = str(batch.get("batch_id", ""))
        if not batch_id or batch_id in seen_batch_ids:
            raise ValueError(f"duplicate or empty batch_id: {batch_id}")
        seen_batch_ids.add(batch_id)
        cluster_ids = batch.get("cluster_ids")
        if not isinstance(cluster_ids, list) or not cluster_ids:
            raise ValueError("batch cluster_ids must be a non-empty array")
        if batch.get("cluster_count") != len(cluster_ids):
            raise ValueError(f"batch cluster_count mismatch: {batch.get('batch_id')}")
        if any(str(cluster_id) not in by_id for cluster_id in cluster_ids):
            raise ValueError(f"batch contains an unknown cluster: {batch.get('batch_id')}")
        expected_counts = _status_counts([by_id[str(cluster_id)] for cluster_id in cluster_ids])
        for cluster_id in cluster_ids:
            cluster = by_id[str(cluster_id)]
            if cluster["batch"]["batch_id"] != batch_id:
                raise ValueError(f"cluster batch reference mismatch: {cluster_id}")
        if batch.get("status_counts") != expected_counts:
            raise ValueError(f"batch status_counts mismatch: {batch.get('batch_id')}")
        if batch.get("decided_count") != expected_counts["decided"]:
            raise ValueError(f"batch decided_count mismatch: {batch.get('batch_id')}")
        batch_cluster_ids.extend(str(cluster_id) for cluster_id in cluster_ids)

    if len(batch_cluster_ids) != len(records) or set(batch_cluster_ids) != seen_ids:
        raise ValueError("batches do not cover each cluster exactly once")

    coverage = _require_dict(report.get("coverage"), "coverage")
    expected_coverage = _coverage(records, len(batches))
    if coverage != expected_coverage:
        raise ValueError("coverage does not match cluster statuses")


def build_progress_register(
    packet: dict[str, Any],
    *,
    packet_sha256: str | None = None,
    input_path: str = INPUT_RELATIVE_PATH.as_posix(),
    expected_cluster_count: int | None = EXPECTED_CLUSTER_COUNT,
    expected_batch_count: int | None = EXPECTED_BATCH_COUNT,
) -> dict[str, Any]:
    _validate_source_packet(packet, expected_cluster_count)
    if expected_batch_count is not None and len(packet["batches"]) != expected_batch_count:
        raise ValueError(f"expected {expected_batch_count} G13 batches, got {len(packet['batches'])}")

    records = _build_records(packet)
    batches = _build_batches(packet, records)
    report = {
        "schema_version": SCHEMA_VERSION,
        "tool": TOOL_PATH,
        "input": {
            "path": input_path,
            "schema_version": packet["schema_version"],
            "cluster_count": len(records),
            "batch_count": len(batches),
            "packet_sha256": packet_sha256,
        },
        "scope": {
            "tracking_level": "g13_cluster",
            "initial_status": "open",
            "human_review_required": True,
            "answers_read": False,
            "didactic_content_copied": False,
            "didactic_content_modified": False,
            "automatic_card_modification": False,
            "automatic_exam_modification": False,
            "source_of_truth": "G13 cluster review packet metadata",
        },
        "workflow": {
            "allowed_statuses": ALLOWED_STATUSES,
            "evidence_ref_required_for_decided": True,
            "reviewer_required_for_in_review_or_decided": True,
            "rationale_required_for_in_review_or_decided": True,
            "decided_is_not_an_action": True,
        },
        "coverage": _coverage(records, len(batches)),
        "batches": batches,
        "clusters": records,
        "boundaries": [
            "The register tracks one workflow status for each G13 cluster and aggregate counts for each G13 batch.",
            "The initial register uses status=open and null evidence_ref, reviewer and rationale for every cluster.",
            "in_review requires a non-empty reviewer and rationale; evidence_ref may remain null until closure.",
            "decided requires a non-empty evidence_ref, reviewer and rationale; a cluster cannot be closed without evidence.",
            "The register never changes, merges, rejects or deletes card or exam files.",
            "The G13 packet remains the initial all-null review packet and is not rewritten by this tool.",
        ],
    }
    validate_progress_register(
        report,
        expected_cluster_count=expected_cluster_count,
        expected_batch_count=expected_batch_count,
    )
    return report


def render_guide(report: dict[str, Any]) -> str:
    coverage = report["coverage"]
    lines = [
        "# UniCostraction — registro avanzamento review cluster G14-A",
        "",
        "Questo registro accompagna `UNI_CLUSTER_REVIEW_PACKET_G13_A.json` e non lo modifica.",
        f"Copre {coverage['cluster_count']} cluster in {coverage['batch_count']} lotti.",
        "Lo stato iniziale è `open` per ogni cluster; i tre campi di audit sono placeholder `null`.",
        "",
        "## Stati e gate",
        "",
        "- `open`: nessun audit field valorizzato; il cluster è ancora in coda.",
        "- `in_review`: `reviewer` e `rationale` non vuoti; `evidence_ref` può restare `null` durante il lavoro.",
        "- `decided`: `evidence_ref`, `reviewer` e `rationale` non vuoti; senza evidenza il cluster non si può chiudere.",
        "",
        "Il validatore applica il gate a ogni record, quindi non è possibile chiudere nemmeno un cluster — e a maggior ragione più di uno — senza `evidence_ref`.",
        "Le decisioni restano esiti di review umana: non sono comandi per modificare, fondere, rigettare o cancellare card ed esami.",
        "",
        "## Avanzamento iniziale",
        "",
        "| Lotto | Cluster | Open | In review | Decided |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for batch in report["batches"]:
        counts = batch["status_counts"]
        lines.append(
            f"| `{batch['batch_id']}` | {batch['cluster_count']} | {counts['open']} | "
            f"{counts['in_review']} | {counts['decided']} |"
        )
    lines.extend(
        [
            "",
            "## Rigenerazione",
            "",
            "```powershell",
            "python tools/uni_cluster_review_progress_g14_a.py",
            "```",
            "",
            "Il comando legge soltanto il packet G13 e scrive il registro G14 e questa guida.",
            "",
        ]
    )
    return "\n".join(lines)


def write_reports(root: Path) -> dict[str, Any]:
    packet, packet_sha256 = load_json(root / INPUT_RELATIVE_PATH)
    report = build_progress_register(packet, packet_sha256=packet_sha256)
    (root / REPORT_RELATIVE_PATH).write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (root / GUIDE_RELATIVE_PATH).write_text(render_guide(report), encoding="utf-8")
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args(argv)
    report = write_reports(args.root.resolve())
    print(
        f"clusters={report['coverage']['cluster_count']} "
        f"batches={report['coverage']['batch_count']} "
        f"open={report['coverage']['open_count']} "
        f"in_review={report['coverage']['in_review_count']} "
        f"decided={report['coverage']['decided_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
