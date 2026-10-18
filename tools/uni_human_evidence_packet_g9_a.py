"""Build the traceable G9-A human-evidence packet for open G5 review.

The packet is a metadata-only companion to the G5 queue, G8 ledger, and G7
readiness gate.  It carries references to observed files and review contracts
without copying didactic content or making an association decision.

Usage::

    python tools/uni_human_evidence_packet_g9_a.py
    python tools/uni_human_evidence_packet_g9_a.py --root .
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

try:
    from tools.uni_completeness_ledger_g8 import (
        MARKDOWN_RELATIVE_PATH as G8_MARKDOWN_PATH,
        REPORT_RELATIVE_PATH as G8_REPORT_PATH,
        build_ledger,
    )
    from tools.uni_pack_exam_review_g5 import (
        REPORT_RELATIVE_PATH as G5_REPORT_PATH,
        build_review_report,
    )
    from tools.uni_release_readiness_g7 import (
        MARKDOWN_RELATIVE_PATH as G7_MARKDOWN_PATH,
        REPORT_RELATIVE_PATH as G7_REPORT_PATH,
        build_release_readiness,
    )
except ModuleNotFoundError:
    from uni_completeness_ledger_g8 import (  # type: ignore[no-redef]
        MARKDOWN_RELATIVE_PATH as G8_MARKDOWN_PATH,
        REPORT_RELATIVE_PATH as G8_REPORT_PATH,
        build_ledger,
    )
    from uni_pack_exam_review_g5 import (  # type: ignore[no-redef]
        REPORT_RELATIVE_PATH as G5_REPORT_PATH,
        build_review_report,
    )
    from uni_release_readiness_g7 import (  # type: ignore[no-redef]
        MARKDOWN_RELATIVE_PATH as G7_MARKDOWN_PATH,
        REPORT_RELATIVE_PATH as G7_REPORT_PATH,
        build_release_readiness,
    )


REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_HUMAN_EVIDENCE_PACKET_G9_A.json")
MARKDOWN_RELATIVE_PATH = Path("docs/coordination/UNI_HUMAN_EVIDENCE_PACKET_G9_A.md")
SCHEMA_RELATIVE_PATH = Path("docs/coordination/UNI_HUMAN_EVIDENCE_PACKET_G9_A.schema.json")


def _sorted_unique(values: Iterable[object]) -> list[str]:
    return sorted({str(value) for value in values}, key=str.casefold)


def _record_by_id(ledger: dict[str, Any]) -> dict[str, dict[str, Any]]:
    entries = [
        entry
        for group in (ledger.get("packs", []), ledger.get("exams", []))
        for entry in group
        if isinstance(entry, dict)
    ]
    return {str(entry["record_id"]): entry for entry in entries}


def _evidence_requirements(item: dict[str, Any]) -> list[dict[str, Any]]:
    if item["uncertainty"] == "unmatched_legacy_domain":
        return [
            {
                "evidence_id": "explicit_association_or_disposition",
                "description": (
                    "A source or project-maintained record that either names one existing "
                    "pack for this exam or explicitly records why it remains unmatched."
                ),
                "required": True,
            },
            {
                "evidence_id": "legacy_scope_provenance",
                "description": (
                    "Metadata establishing the legacy record's origin, scope, and applicable "
                    "version or time context."
                ),
                "required": True,
            },
            {
                "evidence_id": "review_audit",
                "description": (
                    "Reviewer identity, date, cited evidence paths, and a note explaining "
                    "the selected allowed outcome."
                ),
                "required": True,
            },
        ]
    return [
        {
            "evidence_id": "explicit_candidate_association",
            "description": (
                "A source or project-maintained record that names exactly one candidate "
                "association for this pack or exam."
            ),
            "required": True,
        },
        {
            "evidence_id": "candidate_scope_disambiguation",
            "description": (
                "Evidence identifying the candidate's scope, version, or ownership and "
                "addressing the competing observed candidates."
            ),
            "required": True,
        },
        {
            "evidence_id": "review_audit",
            "description": (
                "Reviewer identity, date, cited evidence paths, and a note explaining "
                "the selected allowed outcome."
            ),
            "required": True,
        },
    ]


def _allowed_decisions(item: dict[str, Any]) -> list[str]:
    if item["uncertainty"] == "unmatched_legacy_domain":
        return ["associate_with_explicit_evidence", "keep_unmatched", "defer"]
    return ["associate_with_explicit_evidence", "keep_unresolved", "defer"]


def _g7_check_ids(item: dict[str, Any]) -> list[str]:
    checks = [
        "cross_report.pending_count",
        "review_safety.all_items_pending",
        "review_safety.all_decisions_null",
    ]
    if item["uncertainty"] == "unmatched_legacy_domain":
        checks.extend(
            [
                "cross_report.legacy_unmatched_count",
                "review_safety.legacy_items_have_no_candidates",
                "review_safety.legacy_items_pending",
            ]
        )
    return checks


def _packet_item(
    root: Path,
    item: dict[str, Any],
    ledger_entry: dict[str, Any],
    readiness: dict[str, Any],
) -> dict[str, Any]:
    queue_id = str(item["queue_id"])
    record_id = str(ledger_entry["record_id"])
    if item["uncertainty"] == "unmatched_legacy_domain":
        block_reason = (
            "The exam is explicitly legacy and has no observed pack candidate; "
            "the current metadata cannot establish an association."
        )
    else:
        block_reason = (
            "Observed naming or documentation signals leave multiple candidates; "
            "no canonical association has been established."
        )
    return {
        "identifier": {
            "queue_id": queue_id,
            "record_id": record_id,
            "item_type": item["item_type"],
            "item_id": item["item_id"],
            "classification": item["classification"],
            "uncertainty": item["uncertainty"],
            "legacy_observed": bool(item.get("legacy_observed", False)),
        },
        "observed_files": _sorted_unique(
            [*item.get("source_files", []), *ledger_entry.get("source_files", [])]
        ),
        "block_reason": block_reason,
        "evidence_to_collect": _evidence_requirements(item),
        "allowed_decisions": _allowed_decisions(item),
        "no_auto_resolution": {
            "forbidden": True,
            "required_actor": "human_reviewer",
            "prohibited_basis": [
                "name_only_overlap",
                "bounded_root_overlap",
                "directory_proximity",
                "legacy_flag_alone",
                "didactic_content_or_answer_inference",
            ],
            "required_condition": (
                "An allowed decision needs explicit cited evidence and a reviewer note; "
                "otherwise the item remains open."
            ),
        },
        "linkage": {
            "g5": {
                "report_path": G5_REPORT_PATH.as_posix(),
                "queue_id": queue_id,
                "review_status": item["review_status"],
            },
            "g8": {
                "report_path": G8_REPORT_PATH.as_posix(),
                "record_id": record_id,
                "evidence_state": ledger_entry["evidence_state"],
            },
            "g7": {
                "report_path": G7_REPORT_PATH.as_posix(),
                "status": readiness["status"],
                "relevant_check_ids": _g7_check_ids(item),
            },
        },
    }


def build_packet(root: Path) -> dict[str, Any]:
    """Build the G9-A packet from the current checkout's G5/G8/G7 builders."""

    root = root.resolve()
    review = build_review_report(root)
    ledger = build_ledger(root)
    readiness = build_release_readiness(root)
    ledger_by_id = _record_by_id(ledger)
    pending = [
        item
        for item in review["review_queue"]
        if isinstance(item, dict) and item.get("review_status") == "pending"
    ]
    legacy = [
        item
        for item in pending
        if item.get("uncertainty") == "unmatched_legacy_domain"
    ]
    packet_items = []
    for item in pending:
        record_id = f"{item['item_type']}:{item['item_id']}"
        if record_id not in ledger_by_id:
            raise ValueError(f"missing G8 ledger record for {record_id}")
        packet_items.append(_packet_item(root, item, ledger_by_id[record_id], readiness))
    packet_items.sort(key=lambda entry: str(entry["identifier"]["queue_id"]).casefold())

    queue_ids = [str(entry["identifier"]["queue_id"]) for entry in packet_items]
    legacy_queue_ids = [str(item["queue_id"]) for item in legacy]
    return {
        "schema_version": "g9a.v1",
        "tool": "tools/uni_human_evidence_packet_g9_a.py",
        "scope": {
            "source_of_truth": "selected checkout through G5 review, G8 ledger, and G7 readiness builders",
            "didactic_content_reviewed": False,
            "didactic_content_copied": False,
            "semantic_association_inferred": False,
            "content_modified": False,
            "automatic_resolution": False,
        },
        "source_reports": {
            "g5_review": {
                "path": G5_REPORT_PATH.as_posix(),
                "schema_version": review["schema_version"],
            },
            "g8_ledger": {
                "path": G8_REPORT_PATH.as_posix(),
                "markdown_path": G8_MARKDOWN_PATH.as_posix(),
                "schema_version": ledger["schema_version"],
            },
            "g7_readiness": {
                "path": G7_REPORT_PATH.as_posix(),
                "markdown_path": G7_MARKDOWN_PATH.as_posix(),
                "schema_version": readiness["schema_version"],
                "status": readiness["status"],
                "release_ready": readiness["release_ready"],
                "mismatch_count": readiness["mismatch_count"],
            },
        },
        "coverage": {
            "pending_g5": len(pending),
            "legacy_unmatched_exams": len(legacy),
            "unique_item_count": len(packet_items),
            "pending_queue_ids": queue_ids,
            "legacy_unmatched_queue_ids": sorted(legacy_queue_ids, key=str.casefold),
            "legacy_is_subset_of_pending": set(legacy_queue_ids).issubset(queue_ids),
            "duplicate_entries": False,
        },
        "items": packet_items,
        "boundaries": [
            "The two legacy unmatched exams are represented once each because they are already part of the six pending G5 items.",
            "Observed files are metadata references; no question, answer, schede, or source content is copied into this packet.",
            "Allowed decisions do not constitute educational, normative, legal, or semantic approval.",
            "No item may be auto-resolved; unresolved or deferred items remain open in G5/G8/G7.",
        ],
    }


def render_markdown(packet: dict[str, Any]) -> str:
    coverage = packet["coverage"]
    reports = packet["source_reports"]
    lines = [
        "# UniCostraction — packet evidenze revisione umana tracciabile G9-A",
        "",
        "Il packet è un indice metadata-only per la revisione umana dei sei item G5 pending.",
        "I due esami legacy unmatched sono già inclusi in quei sei item e quindi compaiono",
        "una sola volta, con copertura esplicita nel campo `coverage`.",
        "",
        "Si rigenera dal checkout selezionato con:",
        "",
        "```powershell",
        "python tools/uni_human_evidence_packet_g9_a.py",
        "```",
        "",
        "## Collegamenti machine-readable",
        "",
        f"- G5 review: [`{reports['g5_review']['path']}`]({reports['g5_review']['path']})",
        f"- G8 ledger: [`{reports['g8_ledger']['path']}`]({reports['g8_ledger']['path']}) e [`{reports['g8_ledger']['markdown_path']}`]({reports['g8_ledger']['markdown_path']})",
        f"- G7 readiness: [`{reports['g7_readiness']['path']}`]({reports['g7_readiness']['path']}) e [`{reports['g7_readiness']['markdown_path']}`]({reports['g7_readiness']['markdown_path']}); stato **{reports['g7_readiness']['status'].upper()}**",
        "",
        "## Copertura",
        "",
        f"- G5 pending: **{coverage['pending_g5']}**",
        f"- esami legacy unmatched: **{coverage['legacy_unmatched_exams']}**",
        f"- record unici nel packet: **{coverage['unique_item_count']}**",
        "- auto-risoluzione: **vietata**",
        "",
        "La cardinalità non è 6+2 record: i due legacy sono il sottoinsieme `exam:IMPIANTI_FV_EOLICO` e `exam:MATERIALEDILE` della coda G5, non una seconda copia.",
        "",
        "## Item",
        "",
    ]
    for entry in packet["items"]:
        identifier = entry["identifier"]
        lines.extend(
            [
                f"### `{identifier['queue_id']}`",
                "",
                f"- Identificativo record G8: `{identifier['record_id']}`",
                f"- Classificazione: `{identifier['classification']}`; incertezza: `{identifier['uncertainty']}`",
                f"- File osservati: {', '.join(f'`{path}`' for path in entry['observed_files'])}",
                f"- Motivo del blocco: {entry['block_reason']}",
                "- Evidenze da raccogliere:",
            ]
        )
        lines.extend(f"  - `{req['evidence_id']}`: {req['description']}" for req in entry["evidence_to_collect"])
        lines.append(f"- Decisioni ammesse: {', '.join(f'`{decision}`' for decision in entry['allowed_decisions'])}")
        lines.append("- Divieto di auto-risoluzione: **sì**; nessuna decisione su nome, radice, prossimità, flag legacy o contenuto didattico.")
        lines.append("")
    lines.extend(
        [
            "## Confini",
            "",
            "- il packet non copia contenuti didattici e non modifica corpus, domande, risposte, schede o decisioni G5;",
            "- una decisione `associate_with_explicit_evidence` richiede evidenza esplicita citata e nota del revisore;",
            "- `keep_unresolved`, `keep_unmatched` e `defer` mantengono aperta la revisione;",
            "- il packet non trasforma una revisione umana in approvazione didattica, normativa, legale o semantica.",
            "",
        ]
    )
    return "\n".join(lines)


def write_reports(root: Path) -> dict[str, Any]:
    root = root.resolve()
    packet = build_packet(root)
    json_path = root / REPORT_RELATIVE_PATH
    markdown_path = root / MARKDOWN_RELATIVE_PATH
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(packet), encoding="utf-8")
    return packet


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args(argv)
    packet = write_reports(args.root)
    print(
        f"pending_g5={packet['coverage']['pending_g5']} "
        f"legacy_unmatched={packet['coverage']['legacy_unmatched_exams']} "
        f"unique_items={packet['coverage']['unique_item_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
