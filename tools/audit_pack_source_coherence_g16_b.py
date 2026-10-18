"""Build the deterministic, metadata-only G16-B pack/source coherence report.

G16-B reconciles the explicit pack rows from G13-B, the evidence requests
queued by G14-B, and the pack reconciliation rows from G15-B.  It does not
read or modify source payloads and never performs semantic matching.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = Path("docs/coordination/UNI_PACK_SOURCE_COHERENCE_G16_B.json")
SCHEMA_REF = "./UNI_PACK_SOURCE_COHERENCE_G16_B_SCHEMA.json"
SCHEMA_VERSION = "G16-B-pack-source-coherence"
COHERENCE_ID = SCHEMA_VERSION
BASE_COMMIT = "6d0f5920d253a09491e739aadcd705cde0539212"
OBSERVED_AT = "2026-10-18"

G13_PATH = Path("docs/coordination/UNI_PACK_PROVENANCE_COVERAGE_G13_B.json")
G14_PATH = Path("docs/coordination/UNI_PACK_EVIDENCE_QUEUE_G14_B.json")
G15_PATH = Path("docs/coordination/UNI_MANIFEST_RECONCILIATION_G15_B.json")
G13_COMMIT = "5563510cbf40c1e2a5476cb64be845947c68e710"
G14_COMMIT = "7bdaa0a33260fb5380f02f0a8b41ec6e625a1b44"
G15_COMMIT = "8567297743ea5e4c94c1c0b6a0f18c7886ebc6fc"

STATES = {"blocked", "observed_local"}
REMEDIATION_STATUS = {"blocked", "observed_local"}


def load_json(root: Path, relative_path: Path) -> dict[str, Any]:
    path = root / relative_path
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"JSON root must be an object: {relative_path}")
    return value


def _indexed(rows: list[dict[str, Any]], key: str, label: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        value = row.get(key)
        if not isinstance(value, str) or not value:
            raise ValueError(f"{label} row has no non-empty {key}")
        if value in result:
            raise ValueError(f"{label} contains duplicate {key}: {value}")
        result[value] = row
    return result


def _input_inventory(g13: dict[str, Any], g14: dict[str, Any], g15: dict[str, Any]) -> list[dict[str, Any]]:
    expected = (
        ("G13", G13_PATH, "G13-B-pack-provenance-coverage", G13_COMMIT, g13, "packs"),
        ("G14", G14_PATH, "G14-B-pack-evidence-queue", G14_COMMIT, g14, "items"),
        ("G15", G15_PATH, "G15-B-manifest-reconciliation", G15_COMMIT, g15, "pack_reconciliation"),
    )
    inventory: list[dict[str, Any]] = []
    for report_id, path, schema_version, source_commit, report, collection in expected:
        if report.get("schema_version") != schema_version:
            raise ValueError(f"Unexpected {report_id} schema_version")
        if report_id == "G13" and report.get("base_commit") != source_commit:
            raise ValueError("G13 base commit changed")
        if report_id == "G14" and report.get("source_commit") != source_commit:
            raise ValueError("G14 source commit changed")
        if report_id == "G15" and report.get("base_commit") != source_commit:
            raise ValueError("G15 base commit changed")
        rows = report.get(collection)
        if not isinstance(rows, list):
            raise ValueError(f"{report_id} collection is not an array")
        identity = next(
            (report.get(field) for field in ("audit_id", "queue_id", "reconciliation_id") if report.get(field)),
            None,
        )
        inventory.append(
            {
                "report_id": report_id,
                "path": path.as_posix(),
                "schema_version": schema_version,
                "artifact_id": identity,
                "observed_at": report.get("observed_at"),
                "source_commit": source_commit,
                "row_count": len(rows),
            }
        )
    return inventory


def _requirement_refs(item: dict[str, Any]) -> list[str]:
    queue_id = item["queue_item_id"]
    return [
        f"{queue_id}#source.evidence_required",
        f"{queue_id}#source.locator_required",
        f"{queue_id}#source.license_proof_required",
        f"{queue_id}#closure_checklist",
    ]


def _g13_only_request(pack: dict[str, Any]) -> dict[str, Any]:
    codes = sorted(set(pack["remediation_codes"]))
    refs = [f"G13-B:{pack['pack_id']}#remediation_codes:{code}" for code in codes]
    return {
        "status": "blocked",
        "origin_report": "G13",
        "queue_item_id": None,
        "request_refs": refs,
        "requirements": {
            "evidence": [
                "Resolve the G13-B evidence_not_observed_local_for_all_matched_records remediation before promoting evidence status."
            ],
            "locator": [],
            "license_proof": [
                "Resolve the G13-B source_specific_license_not_declared remediation before promoting licence status."
            ],
        },
    }


def _evidence_request(g13: dict[str, Any], g14: dict[str, Any] | None) -> dict[str, Any]:
    if g14 is None:
        return _g13_only_request(g13)
    return {
        "status": g13["evidence_status"],
        "origin_report": "G14",
        "queue_item_id": g14["queue_item_id"],
        "request_refs": _requirement_refs(g14),
        "requirements": {
            "evidence": list(g14["source"]["evidence_required"]),
            "locator": list(g14["source"]["locator_required"]),
            "license_proof": list(g14["source"]["license_proof_required"]),
        },
    }


def _pack_row(g13: dict[str, Any], g14: dict[str, Any] | None, g15: dict[str, Any]) -> dict[str, Any]:
    g13_statuses = {
        "source_record": g13["source_record_present"],
        "locator": g13["locator_present"],
        "license": g13["license_status"],
        "evidence": g13["evidence_status"],
    }
    if any(value not in STATES for value in g13_statuses.values()):
        raise ValueError(f"G13 has an invalid state for {g13['pack_id']}")
    if g15["g13_source_record_status"] != g13_statuses["source_record"]:
        raise ValueError(f"G15/G13 source state mismatch for {g13['pack_id']}")
    if g15["g13_license_status"] != g13_statuses["license"]:
        raise ValueError(f"G15/G13 licence state mismatch for {g13['pack_id']}")
    if g15["g13_evidence_status"] != g13_statuses["evidence"]:
        raise ValueError(f"G15/G13 evidence state mismatch for {g13['pack_id']}")

    if g14 is not None and g14["status"] != "blocked":
        raise ValueError(f"G14 queue item is not blocked for {g13['pack_id']}")
    overall = "blocked" if any(value == "blocked" for value in g13_statuses.values()) else "observed_local"
    remediation_refs = [
        f"G13-B:{g13['pack_id']}#remediation_codes",
        f"G15-B:{g13['pack_id']}#remediation_open",
    ]
    if g14 is not None:
        remediation_refs.append(f"{g14['queue_item_id']}#blocked.codes")
    else:
        remediation_refs.append(f"G13-B:{g13['pack_id']}#evidence_request")

    return {
        "pack_id": g13["pack_id"],
        "pack_path": g13["pack_path"],
        "course_yaml": g13["course_yaml"],
        "status": overall,
        "states": g13_statuses,
        "g13": {
            "source_record_present": g13["source_record_present"],
            "locator_present": g13["locator_present"],
            "license_status": g13["license_status"],
            "evidence_status": g13["evidence_status"],
            "remediation_codes": sorted(g13["remediation_codes"]),
        },
        "g14": {
            "queue_item_id": g14["queue_item_id"] if g14 is not None else None,
            "status": g14["status"] if g14 is not None else "not_queued",
            "blocker_codes": sorted(g14["blocked"]["codes"]) if g14 is not None else [],
        },
        "g15": {
            "package_scope_status": g15["package_scope_status"],
            "source_record_keys": list(g15["source_record_keys"]),
            "remediation_open": g15["remediation_open"],
        },
        "evidence_request": _evidence_request(g13, g14),
        "remediation": {
            "status": "blocked" if g15["remediation_open"] else "observed_local",
            "open": g15["remediation_open"],
            "references": remediation_refs,
        },
        "matching_note": "Pack identity is reconciled only by exact pack_path and explicit report keys; course names, COURSE.yaml fonti, titles, topics, and text similarity are not used.",
    }


def validate_report(report: dict[str, Any]) -> None:
    if report.get("$schema") != SCHEMA_REF:
        raise ValueError("G16 report has an unexpected schema reference")
    if report.get("schema_version") != SCHEMA_VERSION or report.get("coherence_id") != COHERENCE_ID:
        raise ValueError("G16 report identity is invalid")
    if report.get("metadata_only") is not True or report.get("base_commit") != BASE_COMMIT:
        raise ValueError("G16 report is not anchored to the requested metadata-only base")
    rows = report.get("packs")
    if not isinstance(rows, list) or len(rows) != 71:
        raise ValueError("G16 must contain exactly 71 pack rows")
    paths = [row.get("pack_path") for row in rows]
    if paths != sorted(paths) or len(set(paths)) != 71:
        raise ValueError("G16 pack rows are not unique and sorted")
    for row in rows:
        if row.get("status") not in STATES:
            raise ValueError(f"Invalid overall status for {row.get('pack_id')}")
        states = row.get("states", {})
        if set(states) != {"source_record", "locator", "license", "evidence"} or any(value not in STATES for value in states.values()):
            raise ValueError(f"Invalid state matrix for {row.get('pack_id')}")
        if row["status"] != ("blocked" if "blocked" in states.values() else "observed_local"):
            raise ValueError(f"Overall status is incoherent for {row.get('pack_id')}")
        request = row.get("evidence_request", {})
        if request.get("status") != states["evidence"] or not request.get("request_refs"):
            raise ValueError(f"Evidence request is incoherent for {row.get('pack_id')}")
        if row.get("g14", {}).get("status") == "blocked" and not row["g14"].get("queue_item_id"):
            raise ValueError(f"Blocked G14 row has no queue item for {row.get('pack_id')}")
        remediation = row.get("remediation", {})
        if not remediation.get("open") or not remediation.get("references"):
            raise ValueError(f"Remediation reference is missing for {row.get('pack_id')}")
        if remediation.get("status") not in REMEDIATION_STATUS:
            raise ValueError(f"Invalid remediation status for {row.get('pack_id')}")
    summary = report.get("summary", {})
    if summary.get("pack_count") != len(rows) or summary.get("unique_pack_count") != len(set(paths)):
        raise ValueError("G16 summary pack count mismatch")
    if summary.get("coherence_blocked_count") != sum(row["status"] == "blocked" for row in rows):
        raise ValueError("G16 blocked count mismatch")
    if summary.get("evidence_request_count") != len(rows):
        raise ValueError("G16 evidence request count mismatch")
    if summary.get("remediation_reference_count") != sum(len(row["remediation"]["references"]) for row in rows):
        raise ValueError("G16 remediation reference count mismatch")
    encoded = json.dumps(report, ensure_ascii=False).lower()
    for forbidden in ('"text"', '"content"', '"question"', '"answer"', '"solution"'):
        if forbidden in encoded:
            raise ValueError(f"Protected payload key found in G16 report: {forbidden}")


def build_report(root: Path = ROOT) -> dict[str, Any]:
    g13 = load_json(root, G13_PATH)
    g14 = load_json(root, G14_PATH)
    g15 = load_json(root, G15_PATH)
    inventory = _input_inventory(g13, g14, g15)
    g13_by_path = _indexed(g13["packs"], "pack_path", "G13")
    g14_by_path = _indexed(g14["items"], "pack_path", "G14")
    g15_by_path = _indexed(g15["pack_reconciliation"], "pack_path", "G15")
    if set(g13_by_path) != set(g15_by_path):
        raise ValueError("G13 and G15 pack identities differ")
    if not set(g14_by_path) < set(g13_by_path) or len(g14_by_path) != 70:
        raise ValueError("G14 queue is not the exact 70-pack subset of G13")
    rows = [
        _pack_row(g13_by_path[path], g14_by_path.get(path), g15_by_path[path])
        for path in sorted(g13_by_path)
    ]
    report = {
        "$schema": SCHEMA_REF,
        "schema_version": SCHEMA_VERSION,
        "coherence_id": COHERENCE_ID,
        "metadata_only": True,
        "observed_at": OBSERVED_AT,
        "base_commit": BASE_COMMIT,
        "scope": {
            "input_reports": [entry["path"] for entry in inventory],
            "matching_policy": "Only exact pack_path identity and explicit report keys are admissible across G13-B, G14-B, and G15-B.",
            "state_policy": "Copy blocked or observed_local states conservatively; no state is promoted by G16.",
            "evidence_request_policy": "Every pack receives an open evidence request reference; queued packs copy G14-B requirements and the non-queued matched pack retains G13-B remediation references.",
            "remediation_policy": "Every pack retains G13-B and G15-B remediation references; G14-B blocker references are added when a queue item exists.",
            "no_semantic_mapping": "Course names, COURSE.yaml fonti, titles, topics, and text similarity are not matching bases and do not create source relationships.",
            "excluded_payloads": [
                "Source files, source text, PDFs, XML, HTML, manuals, standards, prices, manufacturer data, schede JSONL, exams, answers, and solutions",
                "Independent legal, technical, factual, licence, or regulatory conclusions",
            ],
        },
        "summary": {
            "pack_count": len(rows),
            "unique_pack_count": len({row["pack_path"] for row in rows}),
            "g13_pack_count": len(g13_by_path),
            "g14_queue_count": len(g14_by_path),
            "g15_pack_count": len(g15_by_path),
            "g14_blocked_count": sum(row["g14"]["status"] == "blocked" for row in rows),
            "coherence_blocked_count": sum(row["status"] == "blocked" for row in rows),
            "coherence_observed_local_count": sum(row["status"] == "observed_local" for row in rows),
            "g13_source_observed_local_count": sum(row["states"]["source_record"] == "observed_local" for row in rows),
            "g13_locator_observed_local_count": sum(row["states"]["locator"] == "observed_local" for row in rows),
            "evidence_request_count": sum(bool(row["evidence_request"]["request_refs"]) for row in rows),
            "remediation_reference_count": sum(len(row["remediation"]["references"]) for row in rows),
        },
        "input_reports": inventory,
        "packs": rows,
        "limitations": [
            "G16 reconciles declared metadata only; it does not prove source accuracy, current URL availability, licence clearance, legal status, or regulatory vigency.",
            "The report does not create semantic source mappings and does not modify source or pack content.",
            "An observed_local state is a local observation only and is not a claim-ready, legally cleared, or commercially reusable state.",
        ],
    }
    validate_report(report)
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / OUTPUT_PATH)
    args = parser.parse_args()
    report = build_report(ROOT)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
