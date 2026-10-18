"""Build the deterministic G9-B provenance index and claim-coverage audit.

This audit consumes the metadata-only G6 provenance report and the G7-B
remediation queue.  It indexes observations; it does not read or rewrite PDF,
XML, course-card, exam, or other source payloads.  In particular, a declared
URL or license is not independently cleared, and an observed local record is
not promoted to ``verified`` or ``claim_ready``.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


REPORT_SCHEMA_VERSION = "G9-B-claim-coverage"
AUDIT_ID = "G9-B-claim-coverage"
G6_REPORT = Path("docs/coordination/UNI_PROVENANCE_AUDIT_G6.json")
G7_REPORT = Path("docs/coordination/UNI_REMEDIATION_QUEUE_G7_B.json")
REPORT_PATH = Path("docs/coordination/UNI_CLAIM_COVERAGE_G9_B.json")
MARKDOWN_PATH = Path("docs/coordination/UNI_CLAIM_COVERAGE_G9_B.md")
SCHEMA_PATH = Path("docs/coordination/UNI_CLAIM_COVERAGE_G9_B_SCHEMA.json")

EVIDENCE_STATUSES = ("verified", "observed_local", "context_only", "blocked")
QUEUE_STATUSES = ("open", "resolved")
PROTECTED_KEYS = {"text", "content", "question", "answer", "solution"}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return value


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _source_record_present(record: dict[str, Any]) -> bool:
    """Return true only for an explicit normalized G6 source record."""
    return record.get("record_kind") == "source" and _nonempty(record.get("record_id"))


def _url_present(record: dict[str, Any]) -> bool:
    url = record.get("url") or {}
    return url.get("status") == "declared" and _nonempty(url.get("value"))


def _license_present(record: dict[str, Any]) -> bool:
    license_data = record.get("license") or {}
    return license_data.get("status") == "declared" and _nonempty(license_data.get("label"))


def _explicit_claim_ready(record: dict[str, Any]) -> bool:
    """Read an explicit input claim-ready flag without deriving one.

    G6 currently does not emit this field.  Keeping the check explicit makes
    future use fail closed: even a verified record is not claim-ready merely
    because its URL and license fields are present.
    """
    return record.get("claim_ready") is True


def _claim_ready(record: dict[str, Any], source_record_present: bool, url_present: bool, license_present: bool) -> bool:
    return (
        _explicit_claim_ready(record)
        and record.get("proof_state") == "verified"
        and source_record_present
        and url_present
        and license_present
    )


def _record_residuals(
    record: dict[str, Any],
    source_record_present: bool,
    url_present: bool,
    license_present: bool,
    evidence_status: str,
    claim_ready: bool,
) -> list[str]:
    residuals = [f"g6:{code}" for code in record.get("residual_codes") or []]
    if not source_record_present:
        residuals.append("source_record_missing")
    if not url_present:
        residuals.append("url_missing")
    if not license_present:
        residuals.append("license_missing")
    if evidence_status != "verified":
        residuals.append("evidence_not_verified")
    if not _explicit_claim_ready(record):
        residuals.append("explicit_claim_ready_evidence_missing")
    if not claim_ready:
        residuals.append("claim_not_ready")
    return list(dict.fromkeys(residuals))


def _index_record(record: dict[str, Any]) -> dict[str, Any]:
    evidence_status = record.get("proof_state")
    if evidence_status not in EVIDENCE_STATUSES:
        raise ValueError(f"Unsupported G6 proof_state for {record.get('record_key')}: {evidence_status!r}")
    source_record_present = _source_record_present(record)
    url_present = _url_present(record)
    license_present = _license_present(record)
    claim_ready = _claim_ready(record, source_record_present, url_present, license_present)
    return {
        "record_key": record["record_key"],
        "manifest_path": record["manifest_path"],
        "manifest_id": record["manifest_id"],
        "record_id": record["record_id"],
        "record_kind": record["record_kind"],
        "title": record.get("title"),
        "local_path": record.get("local_path"),
        "source_record_present": source_record_present,
        "url_present": url_present,
        "license_present": license_present,
        "evidence_status": evidence_status,
        "claim_ready": claim_ready,
        "evidence_basis": {
            "source_record": "G6 record_kind and record_id; no source payload read",
            "url": "G6 url.status and url.value",
            "license": "G6 license.status and license.label",
            "evidence_status": "G6 proof_state copied without promotion",
            "claim_ready": (
                "explicit G6 claim_ready=true plus verified evidence and complete presence fields"
                if claim_ready
                else "not promoted; G6 has no explicit claim_ready=true evidence for this record"
            ),
        },
        "residual_codes": _record_residuals(
            record,
            source_record_present,
            url_present,
            license_present,
            evidence_status,
            claim_ready,
        ),
    }


def _record_lookup(index: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result = {record["record_key"]: record for record in index}
    if len(result) != len(index):
        raise ValueError("G6 record_key values are not unique")
    return result


def _item_record_keys(item: dict[str, Any]) -> list[str]:
    if item["source_ref"].startswith("alias:"):
        alias_group = item.get("alias_group") or {}
        return sorted(alias_group.get("record_keys") or [])
    return [item["source_ref"]]


def _remediation_coverage(
    item: dict[str, Any], records_by_key: dict[str, dict[str, Any]]
) -> dict[str, Any]:
    record_keys = _item_record_keys(item)
    if not record_keys:
        raise ValueError(f"Remediation item has no linked record: {item['item_id']}")
    missing = [key for key in record_keys if key not in records_by_key]
    if missing:
        raise ValueError(f"Remediation item {item['item_id']} references unknown records: {missing}")
    linked = [records_by_key[key] for key in record_keys]
    coverage = {
        "source_record_present": all(record["source_record_present"] for record in linked),
        "url_present": all(record["url_present"] for record in linked),
        "license_present": all(record["license_present"] for record in linked),
        "evidence_statuses": sorted({record["evidence_status"] for record in linked}),
        "claim_ready": (
            item["status"] == "resolved"
            and _nonempty(item.get("evidence_ref"))
            and all(record["claim_ready"] for record in linked)
        ),
    }
    residuals = ["remediation_open"] if item["status"] == "open" else []
    residuals.extend(
        code
        for record in linked
        for code in record["residual_codes"]
        if code not in residuals
    )
    if not coverage["claim_ready"]:
        residuals.append("claim_not_ready")
    return {
        "item_id": item["item_id"],
        "category": item["category"],
        "status": item["status"],
        "source_ref": item["source_ref"],
        "record_keys": record_keys,
        "record_count": len(record_keys),
        "coverage": coverage,
        "residual_codes": list(dict.fromkeys(residuals)),
    }


def _residual_summary(
    records: list[dict[str, Any]], remediation: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    record_refs: dict[str, set[str]] = {}
    item_refs: dict[str, set[str]] = {}
    for record in records:
        for code in record["residual_codes"]:
            record_refs.setdefault(code, set()).add(record["record_key"])
    for item in remediation:
        for code in item["residual_codes"]:
            item_refs.setdefault(code, set()).add(item["item_id"])
    codes = sorted(set(record_refs) | set(item_refs))
    return [
        {
            "code": code,
            "record_count": len(record_refs.get(code, set())),
            "item_count": len(item_refs.get(code, set())),
            "record_keys": sorted(record_refs.get(code, set())),
            "item_ids": sorted(item_refs.get(code, set())),
        }
        for code in codes
    ]


def build_report(root: Path) -> dict[str, Any]:
    g6 = load_json(root / G6_REPORT)
    g7 = load_json(root / G7_REPORT)
    if g6.get("audit_id") != "G6-B-provenance":
        raise ValueError(f"Unexpected G6 audit_id: {g6.get('audit_id')!r}")
    if g7.get("queue_id") != "G7-B-provenance-remediation":
        raise ValueError(f"Unexpected G7 queue_id: {g7.get('queue_id')!r}")
    if len(g7.get("items") or []) != 48:
        raise ValueError("G9-B requires the protected G7 queue of exactly 48 items")

    records = [_index_record(record) for record in sorted(g6["records"], key=lambda value: value["record_key"])]
    records_by_key = _record_lookup(records)
    remediation = [
        _remediation_coverage(item, records_by_key)
        for item in sorted(g7["items"], key=lambda value: value["item_id"])
    ]
    evidence_counts = Counter(record["evidence_status"] for record in records)
    residuals = _residual_summary(records, remediation)
    return {
        "$schema": "./UNI_CLAIM_COVERAGE_G9_B_SCHEMA.json",
        "schema_version": REPORT_SCHEMA_VERSION,
        "audit_id": AUDIT_ID,
        "metadata_only": True,
        "observed_at": g6.get("observed_at"),
        "scope": {
            "input_reports": [str(G6_REPORT).replace("\\", "/"), str(G7_REPORT).replace("\\", "/")],
            "record_scope": "All normalized G6 records; source_record_present distinguishes source from context/blocker.",
            "excluded_payloads": [
                "PDF bytes/content",
                "XML bytes/content",
                "course cards and values",
                "exam questions, answers, and solutions",
            ],
            "state_policy": (
                "evidence_status is copied from G6 proof_state. claim_ready requires explicit claim_ready=true evidence; "
                "no field is promoted from URL, license, hash, local presence, or queue status."
            ),
        },
        "summary": {
            "record_count": len(records),
            "source_record_present_count": sum(record["source_record_present"] for record in records),
            "url_present_count": sum(record["url_present"] for record in records),
            "license_present_count": sum(record["license_present"] for record in records),
            "claim_ready_count": sum(record["claim_ready"] for record in records),
            "by_evidence_status": {status: evidence_counts.get(status, 0) for status in EVIDENCE_STATUSES},
            "remediation_item_count": len(remediation),
            "remediation_open_item_count": sum(item["status"] == "open" for item in remediation),
            "remediation_claim_ready_count": sum(item["coverage"]["claim_ready"] for item in remediation),
            "residual_count": len(residuals),
        },
        "records": records,
        "remediation_coverage": remediation,
        "residuals": residuals,
    }


def _walk_keys(value: Any) -> set[str]:
    if isinstance(value, dict):
        return set(value) | set().union(*(_walk_keys(child) for child in value.values()))
    if isinstance(value, list):
        return set().union(*(_walk_keys(child) for child in value)) if value else set()
    return set()


def validate_report(report: dict[str, Any]) -> None:
    required = {
        "$schema", "schema_version", "audit_id", "metadata_only", "observed_at",
        "scope", "summary", "records", "remediation_coverage", "residuals",
    }
    missing = required - set(report)
    if missing:
        raise ValueError(f"G9-B report missing keys: {sorted(missing)}")
    if report["schema_version"] != REPORT_SCHEMA_VERSION or report["audit_id"] != AUDIT_ID:
        raise ValueError("Unexpected G9-B identity")
    if report["metadata_only"] is not True:
        raise ValueError("G9-B report must be metadata-only")
    if _walk_keys(report) & PROTECTED_KEYS:
        raise ValueError("G9-B report contains protected payload keys")
    records = report["records"]
    remediation = report["remediation_coverage"]
    if len(records) != report["summary"]["record_count"]:
        raise ValueError("G9-B record count mismatch")
    if len(remediation) != report["summary"]["remediation_item_count"]:
        raise ValueError("G9-B remediation count mismatch")
    if len(remediation) != 48:
        raise ValueError("G9-B must cover exactly 48 remediation items")
    record_keys = [record.get("record_key") for record in records]
    if any(not _nonempty(key) for key in record_keys) or len(set(record_keys)) != len(record_keys):
        raise ValueError("G9-B record keys must be unique and non-empty")
    for record in records:
        if record["evidence_status"] not in EVIDENCE_STATUSES:
            raise ValueError("Invalid evidence_status")
        expected_ready = (
            record["source_record_present"]
            and record["url_present"]
            and record["license_present"]
            and record["evidence_status"] == "verified"
            and record.get("evidence_basis", {}).get("claim_ready", "").startswith("explicit G6 claim_ready=true")
        )
        if record["claim_ready"] != expected_ready:
            raise ValueError(f"claim_ready was promoted or is inconsistent: {record['record_key']}")
        if record["claim_ready"] is False and "claim_not_ready" not in record["residual_codes"]:
            raise ValueError("Non-ready records must expose claim_not_ready residual")
    known_keys = set(record_keys)
    item_ids = [item.get("item_id") for item in remediation]
    if len(item_ids) != len(set(item_ids)) or any(not _nonempty(item_id) for item_id in item_ids):
        raise ValueError("G9-B remediation item ids must be unique and non-empty")
    for item in remediation:
        if item["status"] not in QUEUE_STATUSES:
            raise ValueError("Invalid remediation status")
        if not item["record_keys"] or not set(item["record_keys"]).issubset(known_keys):
            raise ValueError(f"Unresolved record reference in {item['item_id']}")
        if item["coverage"]["claim_ready"] and item["status"] != "resolved":
            raise ValueError("An open remediation item cannot be claim-ready")
        if not item["coverage"]["claim_ready"] and "claim_not_ready" not in item["residual_codes"]:
            raise ValueError("Non-ready remediation items must expose claim_not_ready residual")


def render_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# G9-B — Indice di provenienza e claim coverage",
        "",
        "Audit deterministico, metadata-only, costruito dai report G6 e G7-B. Non modifica PDF, XML, schede o contenuti.",
        "",
        "## Esito",
        "",
        f"- Record indicizzati: **{summary['record_count']}**; record di fonte espliciti: **{summary['source_record_present_count']}**.",
        f"- URL presenti: **{summary['url_present_count']}**; licenze dichiarate: **{summary['license_present_count']}**.",
        f"- Record claim-ready: **{summary['claim_ready_count']}**; item remediation coperti: **{summary['remediation_item_count']}**, aperti: **{summary['remediation_open_item_count']}**.",
        f"- Item claim-ready: **{summary['remediation_claim_ready_count']}**; residui distinti: **{summary['residual_count']}**.",
        "",
        "`evidence_status` copia il `proof_state` G6 senza promozioni. `claim_ready` richiede un’evidenza esplicita `claim_ready=true`; tale evidenza non è presente in G8, quindi nessun record o item è promosso a ready.",
        "",
        "## Copertura per stato di evidenza",
        "",
        "| evidence_status | record |",
        "| --- | ---: |",
    ]
    for status, count in report["summary"]["by_evidence_status"].items():
        lines.append(f"| `{status}` | {count} |")
    lines.extend(["", "## Residui", "", "| Codice | Record | Item remediation |", "| --- | ---: | ---: |"])
    for residual in report["residuals"]:
        lines.append(f"| `{residual['code']}` | {residual['record_count']} | {residual['item_count']} |")
    lines.extend(
        [
            "",
            "## Limiti e confini",
            "",
            "- La presenza di URL o licenza è una dichiarazione osservata nei metadati G6, non una verifica esterna o un parere sui diritti.",
            "- `observed_local`, `context_only` e `blocked` restano tali; non vengono trasformati in `verified`.",
            "- I 48 item G7-B sono collegati ai loro record G6, inclusi i gruppi alias, senza deduplicazione e senza chiusura automatica.",
            "- Il report non dimostra accuratezza tecnica, vigenza normativa, completezza dei contenuti o idoneità professionale dei claim.",
            "",
        ]
    )
    return "\n".join(lines)


def write_outputs(root: Path) -> None:
    report = build_report(root)
    validate_report(report)
    (root / REPORT_PATH).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (root / MARKDOWN_PATH).write_text(render_markdown(report), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true", help="write the deterministic JSON and Markdown outputs")
    args = parser.parse_args()
    report = build_report(args.root)
    validate_report(report)
    if args.write:
        write_outputs(args.root)
        print(args.root / REPORT_PATH)
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
