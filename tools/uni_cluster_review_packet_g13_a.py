"""Build the deterministic G13-A review packet for the 85 G11 clusters.

The packet is an index, not a content export and not a deduplication action.  It
joins the G11 priority queue, the G12 human decision contract, and the G4
pack/exam mapping metadata.  Exam anchors and source paths are retained, but
question bodies, answers, pairs, and card content are never copied.

Usage::

    python tools/uni_cluster_review_packet_g13_a.py
    python tools/uni_cluster_review_packet_g13_a.py --root . --batch-size 10
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


G11_RELATIVE_PATH = Path("docs/coordination/UNI_REDUNDANCY_PRIORITY_G11_A.json")
G12_RELATIVE_PATH = Path("docs/coordination/UNI_CLUSTER_REVIEW_G12_A.json")
G4_RELATIVE_PATH = Path("docs/coordination/UNI_PACK_EXAM_MAP_G4.json")
REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_CLUSTER_REVIEW_PACKET_G13_A.json")
GUIDE_RELATIVE_PATH = Path("docs/coordination/UNI_CLUSTER_REVIEW_PACKET_G13_A.md")
TOOL_PATH = "tools/uni_cluster_review_packet_g13_a.py"
SCHEMA_VERSION = "g13a.v1"
EXPECTED_CLUSTER_COUNT = 85
DEFAULT_BATCH_SIZE = 10
G12_SCHEMA_VERSION = "g12a.v1"
G11_SCHEMA_VERSION = "g11a.v1"
G4_SCHEMA_VERSION = "g4.v1"
ALLOWED_DECISIONS = [
    "distinct",
    "merge_candidate",
    "reject_candidate",
    "needs_source_review",
]
REVIEW_FIELDS = ("decision", "evidence_ref", "reviewer", "rationale")
BASE_COMMIT = "6db979d69d924bf191637354c91949009d010967"


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


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


def _validate_g11(g11: dict[str, Any], expected_count: int | None) -> list[dict[str, Any]]:
    if g11.get("schema_version") != G11_SCHEMA_VERSION:
        raise ValueError("G13-A requires a g11a.v1 priority report")
    queue = _require_dict(g11.get("results"), "G11 results").get("queue")
    if not isinstance(queue, list):
        raise ValueError("G11 results.queue must be an array")
    if expected_count is not None and len(queue) != expected_count:
        raise ValueError(f"expected {expected_count} G11 clusters, got {len(queue)}")

    seen_ids: set[str] = set()
    seen_ranks: set[int] = set()
    for item in queue:
        component = _require_dict(item, "G11 queue item")
        component_id = str(component.get("component_id", ""))
        rank = component.get("priority_rank")
        if not component_id or component_id in seen_ids:
            raise ValueError(f"duplicate or empty G11 component_id: {component_id}")
        if not isinstance(rank, int) or isinstance(rank, bool) or rank < 1:
            raise ValueError(f"invalid G11 priority_rank: {component_id}")
        if rank in seen_ranks:
            raise ValueError(f"duplicate G11 priority_rank: {rank}")
        if not isinstance(component.get("unit_ids"), list) or not component["unit_ids"]:
            raise ValueError(f"G11 component has no unit_ids: {component_id}")
        if not isinstance(component.get("coverage"), dict):
            raise ValueError(f"G11 component has no coverage: {component_id}")
        if component.get("source_group") not in {"cards", "public_exams"}:
            raise ValueError(f"invalid G11 source_group: {component_id}")
        seen_ids.add(component_id)
        seen_ranks.add(rank)
    if seen_ranks != set(range(1, len(queue) + 1)):
        raise ValueError("G11 priority ranks must be consecutive from 1")
    return sorted(queue, key=lambda item: (int(item["priority_rank"]), str(item["component_id"])))


def _validate_g12(g12: dict[str, Any], g11_queue: list[dict[str, Any]]) -> dict[str, Any]:
    if g12.get("schema_version") != G12_SCHEMA_VERSION:
        raise ValueError("G13-A requires the g12a.v1 decision contract")
    queue = g12.get("review_queue")
    if not isinstance(queue, list):
        raise ValueError("G12 review_queue must be an array")
    by_id = {str(item["component_id"]): item for item in queue if isinstance(item, dict)}
    expected_ids = [str(item["component_id"]) for item in g11_queue]
    if list(by_id) and set(by_id) != set(expected_ids):
        raise ValueError("G11 and G12 component IDs do not match")
    contract = {
        "source": G12_RELATIVE_PATH.as_posix(),
        "schema_version": g12["schema_version"],
        "initial_decision": g12.get("scope", {}).get("initial_decision"),
        "allowed_decisions": g12.get("scope", {}).get("allowed_decisions"),
        "evidence_ref_required_for_non_null_decision": g12.get("review_policy", {}).get(
            "evidence_ref_required_for_non_null_decision"
        ),
        "reviewer_required": g12.get("review_policy", {}).get("reviewer_required"),
        "rationale_required": g12.get("review_policy", {}).get("rationale_required"),
        "decision_is_not_an_action": g12.get("review_policy", {}).get(
            "decision_is_not_an_action"
        ),
    }
    if contract["initial_decision"] is not None:
        raise ValueError("G12 initial decision must remain null")
    if contract["allowed_decisions"] != ALLOWED_DECISIONS:
        raise ValueError("G12 allowed decisions changed unexpectedly")
    for field in (
        "evidence_ref_required_for_non_null_decision",
        "reviewer_required",
        "rationale_required",
        "decision_is_not_an_action",
    ):
        if contract[field] is not True:
            raise ValueError(f"G12 contract flag is not true: {field}")
    for item in queue:
        if not isinstance(item, dict):
            raise ValueError("G12 review_queue items must be objects")
        review = item.get("review")
        if not isinstance(review, dict) or any(field not in review for field in REVIEW_FIELDS):
            raise ValueError(f"G12 review placeholder is incomplete: {item.get('component_id')}")
        if any(review[field] is not None for field in REVIEW_FIELDS):
            raise ValueError("G12 source contract is not in its initial pending state")
    return contract


def _index_g4(g4: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    if g4.get("schema_version") != G4_SCHEMA_VERSION:
        raise ValueError("G13-A requires a g4.v1 pack/exam map")
    exams = g4.get("exams")
    packs = g4.get("packs")
    if not isinstance(exams, list) or not isinstance(packs, list):
        raise ValueError("G4 exams and packs must be arrays")
    exams_by_path: dict[str, dict[str, Any]] = {}
    packs_by_id: dict[str, dict[str, Any]] = {}
    for exam in exams:
        exam = _require_dict(exam, "G4 exam")
        exams_by_path[str(exam["exam_path"])] = exam
    for pack in packs:
        pack = _require_dict(pack, "G4 pack")
        packs_by_id[str(pack["pack_id"])] = pack
    return exams_by_path, packs_by_id


def _exam_path_from_source_path(source_path: str) -> str:
    suffix = "/domande.md"
    return source_path[: -len(suffix)] if source_path.endswith(suffix) else source_path


def _exam_ref(exam: dict[str, Any]) -> dict[str, Any]:
    return {
        "exam_id": str(exam["exam_id"]),
        "exam_path": str(exam["exam_path"]),
        "classification": str(exam["classification"]),
        "legacy_observed": bool(exam.get("legacy_observed", False)),
        "source_files": [str(path) for path in exam.get("source_files", [])],
    }


def _pack_ref(candidate: dict[str, Any], pack: dict[str, Any]) -> dict[str, Any]:
    return {
        "pack_id": str(pack["pack_id"]),
        "pack_path": str(pack["pack_path"]),
        "classification": str(pack["classification"]),
        "mapping_relation": str(candidate["relation"]),
        "source_files": [str(path) for path in pack.get("source_files", [])],
    }


def _review_placeholder() -> dict[str, None]:
    return {field: None for field in REVIEW_FIELDS}


def _batch_for_rank(rank: int, batch_size: int) -> tuple[str, int]:
    batch_number = ((rank - 1) // batch_size) + 1
    batch_rank = ((rank - 1) % batch_size) + 1
    return f"batch-{batch_number:02d}", batch_rank


def _build_batches(clusters: list[dict[str, Any]], batch_size: int) -> list[dict[str, Any]]:
    batches: list[dict[str, Any]] = []
    for offset in range(0, len(clusters), batch_size):
        group = clusters[offset : offset + batch_size]
        number = (offset // batch_size) + 1
        batches.append(
            {
                "batch_id": f"batch-{number:02d}",
                "priority_rank_start": int(group[0]["priority_rank"]),
                "priority_rank_end": int(group[-1]["priority_rank"]),
                "cluster_count": len(group),
                "cluster_ids": [str(item["cluster_id"]) for item in group],
                "pending_count": len(group),
            }
        )
    return batches


def build_packet(
    g11: dict[str, Any],
    g12: dict[str, Any],
    g4: dict[str, Any],
    *,
    g11_sha256: str | None = None,
    g12_sha256: str | None = None,
    g4_sha256: str | None = None,
    expected_cluster_count: int | None = EXPECTED_CLUSTER_COUNT,
    batch_size: int = DEFAULT_BATCH_SIZE,
    base_commit: str = BASE_COMMIT,
) -> dict[str, Any]:
    if batch_size < 1:
        raise ValueError("batch_size must be positive")
    g11_queue = _validate_g11(g11, expected_cluster_count)
    g12_contract = _validate_g12(g12, g11_queue)
    exams_by_path, packs_by_id = _index_g4(g4)

    clusters: list[dict[str, Any]] = []
    for component in g11_queue:
        component_id = str(component["component_id"])
        rank = int(component["priority_rank"])
        coverage = _require_dict(component["coverage"], f"G11 coverage {component_id}")
        exam_refs: list[dict[str, Any]] = []
        pack_refs: list[dict[str, Any]] = []
        for source_path in coverage.get("exam_paths", []):
            exam_path = _exam_path_from_source_path(str(source_path))
            exam = exams_by_path.get(exam_path)
            if exam is None:
                raise ValueError(f"G4 has no exam reference for {exam_path}")
            exam_refs.append(_exam_ref(exam))
            for candidate in exam.get("candidate_packs", []):
                candidate = _require_dict(candidate, f"G4 candidate pack {exam_path}")
                pack_id = str(candidate["pack_id"])
                pack = packs_by_id.get(pack_id)
                if pack is None:
                    raise ValueError(f"G4 has no pack reference for {pack_id}")
                pack_refs.append(_pack_ref(candidate, pack))
        if not exam_refs:
            raise ValueError(f"cluster has no exam reference: {component_id}")
        batch_id, batch_rank = _batch_for_rank(rank, batch_size)
        clusters.append(
            {
                "cluster_id": component_id,
                "priority_rank": rank,
                "priority_key": json.loads(json.dumps(component["priority_key"])),
                "g11": {
                    "source_group": str(component["source_group"]),
                    "collision_count": int(component["collision_count"]),
                    "unit_count": len(component["unit_ids"]),
                    "unit_refs": [str(unit_id) for unit_id in component["unit_ids"]],
                },
                "references": {
                    "exam_refs": exam_refs,
                    "pack_refs": pack_refs,
                    "pack_reference_mode": "observed_g4_candidates_preserved",
                },
                "batch": {"batch_id": batch_id, "batch_rank": batch_rank},
                "g12_contract_ref": f"{G12_RELATIVE_PATH.as_posix()}#{component_id}",
                "review": _review_placeholder(),
            }
        )

    batches = _build_batches(clusters, batch_size)
    report = {
        "schema_version": SCHEMA_VERSION,
        "tool": TOOL_PATH,
        "base_commit": base_commit,
        "source_reports": {
            "g11_priority": {
                "path": G11_RELATIVE_PATH.as_posix(),
                "schema_version": G11_SCHEMA_VERSION,
                "sha256": g11_sha256,
            },
            "g12_decision_contract": {
                "path": G12_RELATIVE_PATH.as_posix(),
                "schema_version": G12_SCHEMA_VERSION,
                "sha256": g12_sha256,
            },
            "g4_pack_exam_map": {
                "path": G4_RELATIVE_PATH.as_posix(),
                "schema_version": G4_SCHEMA_VERSION,
                "sha256": g4_sha256,
            },
        },
        "scope": {
            "index_level": "g11_connected_component",
            "human_review_required": True,
            "answers_read": False,
            "didactic_content_copied": False,
            "didactic_content_modified": False,
            "deduplication_performed": False,
            "automatic_merge_or_reject": False,
            "decision_made": False,
            "source_of_truth": "G11 priority + G12 decision contract + G4 observed pack/exam metadata",
        },
        "review_contract": g12_contract,
        "coverage": {
            "cluster_count": len(clusters),
            "batch_count": len(batches),
            "pending_count": len(clusters),
            "decided_count": 0,
            "all_decisions_null": True,
            "all_reviewers_null": True,
            "all_rationales_null": True,
            "all_evidence_refs_null": True,
        },
        "batches": batches,
        "clusters": clusters,
        "boundaries": [
            "One packet record is emitted for each G11 connected component; records are not deduplicated.",
            "G11 priority, unit anchors, and collision metrics are copied as metadata only.",
            "G4 pack/exam mappings are observed candidates and remain unmatched or ambiguous when the source says so.",
            "No exam answers, question bodies, card bodies, or didactic text are included.",
            "G12 decision, evidence_ref, reviewer, and rationale remain null until human review.",
            "A non-null G12 decision requires verifiable evidence_ref, reviewer, and rationale; it is not an execution command.",
            "The packet does not modify, merge, reject, or delete any card or exam file.",
        ],
    }
    validate_packet(report, expected_cluster_count=expected_cluster_count, batch_size=batch_size)
    return report


def validate_packet(
    report: dict[str, Any],
    *,
    expected_cluster_count: int | None = EXPECTED_CLUSTER_COUNT,
    batch_size: int = DEFAULT_BATCH_SIZE,
) -> None:
    if report.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("unexpected G13 schema_version")
    clusters = report.get("clusters")
    if not isinstance(clusters, list):
        raise ValueError("clusters must be an array")
    if expected_cluster_count is not None and len(clusters) != expected_cluster_count:
        raise ValueError(f"expected {expected_cluster_count} clusters, got {len(clusters)}")
    seen_ids: set[str] = set()
    ranks: list[int] = []
    for cluster in clusters:
        cluster = _require_dict(cluster, "cluster")
        cluster_id = str(cluster.get("cluster_id", ""))
        rank = cluster.get("priority_rank")
        if not cluster_id or cluster_id in seen_ids:
            raise ValueError(f"duplicate or empty cluster_id: {cluster_id}")
        if not isinstance(rank, int) or isinstance(rank, bool) or rank < 1:
            raise ValueError(f"invalid priority_rank: {cluster_id}")
        review = cluster.get("review")
        if not isinstance(review, dict) or any(field not in review for field in REVIEW_FIELDS):
            raise ValueError(f"review placeholder incomplete: {cluster_id}")
        if any(review[field] is not None for field in REVIEW_FIELDS):
            raise ValueError(f"review is not pending: {cluster_id}")
        refs = _require_dict(cluster.get("references"), f"references {cluster_id}")
        if not isinstance(refs.get("exam_refs"), list) or not refs["exam_refs"]:
            raise ValueError(f"cluster has no exam refs: {cluster_id}")
        if not isinstance(_require_dict(cluster.get("g11"), f"g11 {cluster_id}").get("unit_refs"), list):
            raise ValueError(f"cluster has no unit refs: {cluster_id}")
        seen_ids.add(cluster_id)
        ranks.append(rank)
    if ranks != list(range(1, len(clusters) + 1)):
        raise ValueError("G13 priority ranks must be consecutive and ordered")
    batches = report.get("batches")
    if not isinstance(batches, list) or not batches:
        raise ValueError("batches must be a non-empty array")
    if sum(int(batch["cluster_count"]) for batch in batches) != len(clusters):
        raise ValueError("batch counts do not cover clusters")
    coverage = _require_dict(report.get("coverage"), "coverage")
    expected_coverage = {
        "cluster_count": len(clusters),
        "batch_count": len(batches),
        "pending_count": len(clusters),
        "decided_count": 0,
        "all_decisions_null": True,
        "all_reviewers_null": True,
        "all_rationales_null": True,
        "all_evidence_refs_null": True,
    }
    if coverage != expected_coverage:
        raise ValueError("coverage does not describe the pending packet")
    if batch_size < 1:
        raise ValueError("batch_size must be positive")


def render_guide(report: dict[str, Any]) -> str:
    lines = [
        "# UniCostraction — guida di revisione a lotti G13-A",
        "",
        "Questo documento accompagna `UNI_CLUSTER_REVIEW_PACKET_G13_A.json`.",
        "È un indice metadata-only dei 85 cluster G11, ordinato per priorità,",
        "con riferimenti osservati a esami e candidati pack. Non contiene testo",
        "didattico, risposte, né una decisione di revisione.",
        "",
        "## Regole del packet",
        "",
        "- Ogni cluster compare una sola volta nell'indice perché è una unità di lavoro G11; non vengono deduplicati né riscritti gli anchor `unit_refs`.",
        "- Le associazioni pack/esame sono riportate come osservate da G4: `ambiguous` e `unmatched_exam` restano tali e non diventano associazioni canoniche.",
        "- Il contratto decisionale è quello G12: `distinct`, `merge_candidate`, `reject_candidate`, `needs_source_review`.",
        "- Prima di una decisione non-null, compilare `evidence_ref`, `reviewer` e `rationale`; `evidence_ref` deve puntare a un'evidenza verificabile.",
        "- `merge_candidate` e `reject_candidate` sono esiti da sottoporre a revisione, non comandi esecutivi; non modificare o cancellare card/esami durante questa fase.",
        "- La decisione umana non certifica correttezza didattica, normativa, legale, fattuale o di licenza.",
        "",
        "## Sequenza per ogni lotto",
        "",
        "1. Aprire il lotto in ordine di `priority_rank` e controllare gli identificativi e gli anchor, senza copiare il testo delle domande.",
        "2. Verificare separatamente i riferimenti `exam_refs` e i candidati `pack_refs`; conservare eventuali stati unmatched o ambiguous.",
        "3. Raccogliere l'evidenza esterna necessaria e registrare il riferimento verificabile nel record del cluster.",
        "4. Solo dopo l'intervento umano, valorizzare decisione, reviewer e rationale; fino ad allora tutti i quattro campi `review` devono restare `null`.",
        "5. Rieseguire la validazione strutturale del packet e lasciare ogni azione sui contenuti a un flusso esplicitamente autorizzato e successivo.",
        "",
        "## Lotti deterministici",
        "",
        "| Lotto | Priorità G11 | Cluster | Stato iniziale |",
        "| --- | ---: | --- | --- |",
    ]
    for batch in report["batches"]:
        lines.append(
            f"| `{batch['batch_id']}` | {batch['priority_rank_start']}–{batch['priority_rank_end']} | "
            f"{', '.join(f'`{cluster_id}`' for cluster_id in batch['cluster_ids'])} | "
            f"{batch['pending_count']} pending |"
        )
    lines.extend(
        [
            "",
            "## Gate di chiusura del lotto",
            "",
            "- nessun campo `review` valorizzato senza evidenza, reviewer e rationale;",
            "- nessun testo didattico o risposta inseriti nel packet;",
            "- nessuna deduplicazione o modifica automatica di card/esami;",
            "- ordine e copertura dei cluster invariati rispetto a G11;",
            "- eventuali decisioni umane restano tracciate come contratto G12 e non come azioni eseguite.",
            "",
        ]
    )
    return "\n".join(lines)


def write_reports(root: Path, *, batch_size: int = DEFAULT_BATCH_SIZE) -> dict[str, Any]:
    g11, g11_sha = load_json(root / G11_RELATIVE_PATH)
    g12, g12_sha = load_json(root / G12_RELATIVE_PATH)
    g4, g4_sha = load_json(root / G4_RELATIVE_PATH)
    report = build_packet(
        g11,
        g12,
        g4,
        g11_sha256=g11_sha,
        g12_sha256=g12_sha,
        g4_sha256=g4_sha,
        batch_size=batch_size,
    )
    (root / REPORT_RELATIVE_PATH).write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (root / GUIDE_RELATIVE_PATH).write_text(render_guide(report), encoding="utf-8")
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    args = parser.parse_args(argv)
    report = write_reports(args.root.resolve(), batch_size=args.batch_size)
    print(
        f"clusters={report['coverage']['cluster_count']} "
        f"batches={report['coverage']['batch_count']} "
        f"pending={report['coverage']['pending_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
