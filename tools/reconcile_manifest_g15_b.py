"""Build the deterministic, metadata-only G15-B manifest reconciliation.

The reconciliation keeps every source-record representation visible.  It
reports exact path+SHA-256 aliases but never deduplicates them, performs no
semantic matching, and never promotes a licence, evidence, or claim state.
Only JSON manifests and JSON reports are read; source payloads are excluded.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
BASE_COMMIT = "8567297743ea5e4c94c1c0b6a0f18c7886ebc6fc"
REPORT_SCHEMA_VERSION = "G15-B-manifest-reconciliation"
RECONCILIATION_ID = "G15-B-manifest-reconciliation"
OUTPUT_PATH = Path("docs/coordination/UNI_MANIFEST_RECONCILIATION_G15_B.json")
SCHEMA_PATH = Path("docs/coordination/UNI_MANIFEST_RECONCILIATION_G15_B_SCHEMA.json")
SCHEMA_REF = "./UNI_MANIFEST_RECONCILIATION_G15_B_SCHEMA.json"

EXPECTED_REPORT_IDS = ("G5", "G6", "G7", "G8", "G9", "G10", "G11", "G12", "G13", "G14")

REPORT_SPECS: tuple[dict[str, Any], ...] = (
    {
        "report_id": "G5",
        "path": "docs/coordination/UNI_CORPUS_LOTTO_G5_ECFR.json",
        "kind": "manifest",
        "collection": "source_records",
    },
    {
        "report_id": "G6",
        "path": "docs/coordination/UNI_PROVENANCE_AUDIT_G6.json",
        "kind": "report",
        "collection": "records",
    },
    {
        "report_id": "G7",
        "path": "docs/coordination/UNI_REMEDIATION_QUEUE_G7_B.json",
        "kind": "report",
        "collection": "items",
    },
    {
        "report_id": "G8",
        "path": "docs/coordination/UNI_COMPLETENESS_LEDGER_G8.json",
        "kind": "report",
        "collection": "ledger",
        "missing_reason": "Report G8 is not present in the requested checkout at the G15-B base.",
    },
    {
        "report_id": "G9",
        "path": "docs/coordination/UNI_CLAIM_COVERAGE_G9_B.json",
        "kind": "report",
        "collection": "records",
    },
    {
        "report_id": "G10",
        "path": "docs/coordination/UNI_CORPUS_LOTTO_G10_B.json",
        "kind": "manifest",
        "collection": "source_records",
    },
    {
        "report_id": "G11",
        "path": "docs/coordination/UNI_EVIDENCE_LICENSE_MATRIX_G11_B.json",
        "kind": "report",
        "collection": "rows",
    },
    {
        "report_id": "G12",
        "path": "docs/coordination/UNI_LOCATOR_LICENSE_CHECKLIST_G12_B.json",
        "kind": "report",
        "collection": "records",
    },
    {
        "report_id": "G13",
        "path": "docs/coordination/UNI_PACK_PROVENANCE_COVERAGE_G13_B.json",
        "kind": "report",
        "collection": "packs",
    },
    {
        "report_id": "G14",
        "path": "docs/coordination/UNI_PACK_EVIDENCE_QUEUE_G14_B.json",
        "kind": "report",
        "collection": "items",
    },
)

MANIFEST_PATHS = (
    "docs/coordination/UNI_CORPUS_LOTTO_G1.json",
    "Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json",
    "UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/fonti/PROVENANCE_MANIFEST_G3_GSE_CT3.json",
    "docs/coordination/UNI_CORPUS_LOTTO_G5_ECFR.json",
    "docs/coordination/UNI_CORPUS_LOTTO_G10_B.json",
)

FORBIDDEN_KEYS = {"text", "content", "question", "answer", "solution"}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return value


def first_nonempty(*values: Any) -> Any:
    for value in values:
        if value not in (None, ""):
            return value
    return None


def record_key(manifest_path: str, record_id: str) -> str:
    return f"{manifest_path}#{record_id}"


def collection_count(report: dict[str, Any], collection: str) -> int | None:
    value = report.get(collection)
    return len(value) if isinstance(value, list) else None


def report_identity(report_id: str, report: dict[str, Any]) -> str | None:
    for field in ("audit_id", "queue_id", "matrix_id", "checklist_id", "manifest_id"):
        value = report.get(field)
        if value not in (None, ""):
            return str(value)
    return None


def build_input_inventory(root: Path) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    entries: list[dict[str, Any]] = []
    loaded: dict[str, dict[str, Any]] = {}
    for spec in REPORT_SPECS:
        relative_path = str(spec["path"])
        path = root / relative_path
        present = path.is_file()
        entry: dict[str, Any] = {
            "report_id": spec["report_id"],
            "path": relative_path,
            "kind": spec["kind"],
            "collection": spec["collection"],
            "present": present,
            "schema_version": None,
            "artifact_id": None,
            "observed_at": None,
            "item_count": 0,
            "status": "available" if present else "missing_in_checkout",
        }
        if present:
            report = load_json(path)
            loaded[spec["report_id"]] = report
            entry.update(
                {
                    "schema_version": report.get("schema_version"),
                    "artifact_id": report_identity(spec["report_id"], report),
                    "observed_at": report.get("observed_at"),
                    "item_count": collection_count(report, spec["collection"]),
                }
            )
        else:
            entry["absence_reason"] = spec.get("missing_reason", "Input is not present in the checkout.")
        entries.append(entry)
    return entries, loaded


def _manifest_record_container(manifest: dict[str, Any]) -> tuple[str, list[dict[str, Any]]]:
    for container in ("source_records", "records"):
        value = manifest.get(container)
        if isinstance(value, list):
            if not all(isinstance(item, dict) for item in value):
                raise ValueError(f"Manifest {container} must contain objects")
            return container, value
    raise ValueError("Manifest has no source_records or records array")


def _manifest_scope(manifest: dict[str, Any]) -> dict[str, Any]:
    scope = manifest.get("scope")
    if not isinstance(scope, dict):
        scope = {}
    package = scope.get("package")
    if package in (None, ""):
        return {
            "declared": None,
            "status": "not_declared",
            "basis": "not_declared",
            "root": first_nonempty(scope.get("root_path"), manifest.get("raw_root")),
        }
    return {
        "declared": str(package),
        "status": "declared",
        "basis": "manifest.scope.package",
        "root": first_nonempty(scope.get("root_path"), scope.get("source_path")),
    }


def build_manifest_inventory(root: Path) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    manifests: list[dict[str, Any]] = []
    loaded: dict[str, dict[str, Any]] = {}
    for relative_path in sorted(MANIFEST_PATHS):
        path = root / relative_path
        if not path.is_file():
            raise ValueError(f"Required manifest is missing: {relative_path}")
        manifest = load_json(path)
        loaded[relative_path] = manifest
        container, records = _manifest_record_container(manifest)
        scope = _manifest_scope(manifest)
        manifests.append(
            {
                "manifest_path": relative_path,
                "manifest_id": first_nonempty(manifest.get("manifest_id"), manifest.get("lot_id")),
                "schema_version": manifest.get("schema_version"),
                "metadata_only": manifest.get("metadata_only"),
                "record_container": container,
                "record_count": len(records),
                "declared_package_scope": scope["declared"],
                "package_scope_status": scope["status"],
                "package_scope_basis": scope["basis"],
                "scope_root": scope["root"],
            }
        )
    return manifests, loaded


def _g6_record_map(g6: dict[str, Any]) -> dict[str, dict[str, Any]]:
    records = g6.get("records")
    if not isinstance(records, list):
        raise ValueError("G6 report lacks records")
    result: dict[str, dict[str, Any]] = {}
    for record in records:
        key = record.get("record_key")
        if not isinstance(key, str) or key in result:
            raise ValueError(f"Invalid or duplicate G6 record_key: {key!r}")
        result[key] = record
    return result


def _direct_source_record_map(manifests: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for manifest_path in sorted(manifests):
        manifest = manifests[manifest_path]
        container, records = _manifest_record_container(manifest)
        if container != "source_records":
            continue
        for record in records:
            source_id = record.get("source_record_id")
            if not isinstance(source_id, str):
                raise ValueError(f"Source record lacks source_record_id: {manifest_path}")
            result[record_key(manifest_path, source_id)] = record
    return result


def _record_local_path(record: dict[str, Any]) -> str | None:
    source = record.get("source")
    if isinstance(source, dict):
        value = first_nonempty(source.get("local_path"), source.get("path"))
        if value is not None:
            return str(value)
    locator = record.get("locator")
    if isinstance(locator, dict):
        value = first_nonempty(locator.get("path"), locator.get("local_path"))
        if value is not None:
            return str(value)
    value = first_nonempty(record.get("local_path"), record.get("raw_file"))
    return str(value) if value is not None else None


def _record_hash(record: dict[str, Any]) -> dict[str, Any]:
    value = record.get("hash")
    if isinstance(value, dict):
        algorithm = first_nonempty(value.get("algorithm"), value.get("alg"))
        digest = first_nonempty(value.get("value"), value.get("digest"))
    else:
        algorithm = record.get("hash_algorithm")
        digest = value
    return {
        "algorithm": str(algorithm) if algorithm is not None else None,
        "value": str(digest).upper() if digest is not None else None,
        "status": "declared" if digest not in (None, "") else "not_declared",
    }


def _package_scope_for_manifest(manifest_rows: dict[str, dict[str, Any]], manifest_path: str) -> dict[str, Any]:
    row = manifest_rows[manifest_path]
    return {
        "declared": row["declared_package_scope"],
        "status": row["package_scope_status"],
        "basis": row["package_scope_basis"],
        "scope_root": row["scope_root"],
    }


def _raw_source_record(manifest: dict[str, Any], record_id: str) -> dict[str, Any] | None:
    _, records = _manifest_record_container(manifest)
    for record in records:
        if record.get("source_record_id") == record_id:
            return record
    return None


def _g6_alias_groups(g6: dict[str, Any]) -> list[dict[str, Any]]:
    groups = g6.get("alias_groups")
    if not isinstance(groups, list):
        raise ValueError("G6 report lacks alias_groups")
    result: list[dict[str, Any]] = []
    for index, group in enumerate(groups, start=1):
        if not isinstance(group, dict):
            raise ValueError("G6 alias group must be an object")
        path = group.get("local_path")
        digest = group.get("hash_sha256")
        keys = group.get("record_keys")
        if not isinstance(path, str) or not isinstance(digest, str) or not isinstance(keys, list):
            raise ValueError("G6 alias group lacks path, hash, or record_keys")
        result.append(
            {
                "alias_group_id": f"G15-B-ALIAS-{index:03d}",
                "relation": "exact_path_hash_alias",
                "local_path": path,
                "hash_sha256": digest.upper(),
                "record_keys": sorted(str(key) for key in keys),
                "representation_count": len(keys),
                "review_status": "open",
                "deduplication_performed": False,
                "semantic_deduplication_performed": False,
                "remediation_refs": [],
            }
        )
    result.sort(key=lambda item: (item["local_path"], item["hash_sha256"], item["record_keys"]))
    for index, group in enumerate(result, start=1):
        group["alias_group_id"] = f"G15-B-ALIAS-{index:03d}"
    return result


def _index_remediations(g7: dict[str, Any], g9: dict[str, Any], g14: dict[str, Any]) -> dict[str, Any]:
    g7_items = g7.get("items", [])
    g9_records = g9.get("records", [])
    g9_coverage = g9.get("remediation_coverage", [])
    g14_items = g14.get("items", [])
    if not all(isinstance(items, list) for items in (g7_items, g9_records, g9_coverage, g14_items)):
        raise ValueError("Remediation input arrays are malformed")
    g7_by_ref: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in g7_items:
        g7_by_ref[item["source_ref"]].append(item)
    g9_coverage_by_key: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in g9_coverage:
        for key in item.get("record_keys", []):
            g9_coverage_by_key[key].append(item)
    return {
        "g7_by_ref": dict(g7_by_ref),
        "g9_record_by_key": {item["record_key"]: item for item in g9_records},
        "g9_coverage_by_key": dict(g9_coverage_by_key),
        "g14_by_pack": {item["pack_id"]: item for item in g14_items},
        "g7_items": g7_items,
        "g9_coverage": g9_coverage,
        "g14_items": g14_items,
    }


def _g7_refs_for_record(record_key_value: str, alias_hashes: Iterable[str], indexes: dict[str, Any]) -> list[dict[str, Any]]:
    refs: list[dict[str, Any]] = []
    candidate_refs = [record_key_value, *(f"alias:{digest}" for digest in alias_hashes)]
    for source_ref in candidate_refs:
        for item in indexes["g7_by_ref"].get(source_ref, []):
            refs.append(
                {
                    "item_id": item["item_id"],
                    "category": item["category"],
                    "status": item["status"],
                    "source_ref": source_ref,
                }
            )
    return sorted(refs, key=lambda item: item["item_id"])


def _record_row(
    record: dict[str, Any],
    manifest_rows: dict[str, dict[str, Any]],
    direct_manifests: dict[str, dict[str, Any]],
    alias_by_key: dict[str, list[dict[str, Any]]],
    indexes: dict[str, Any],
) -> dict[str, Any]:
    key = record["record_key"]
    manifest_path = record["manifest_path"]
    record_id = record["record_id"]
    raw = record.get("_raw")
    if not isinstance(raw, dict):
        raw = _raw_source_record(direct_manifests.get(manifest_path, {}), record_id) or {}
    aliases = alias_by_key.get(key, [])
    alias_hashes = [group["hash_sha256"] for group in aliases]
    g9 = indexes["g9_record_by_key"].get(key)
    g11 = indexes["g11_by_key"].get(key)
    g12 = indexes["g12_by_key"].get(key)
    g7_refs = _g7_refs_for_record(key, alias_hashes, indexes)
    g9_coverage = indexes["g9_coverage_by_key"].get(key, [])
    local_path = first_nonempty(record.get("local_path"), _record_local_path(raw))
    declared_hash = record.get("hash") if isinstance(record.get("hash"), dict) else _record_hash(raw)
    if not isinstance(declared_hash, dict):
        declared_hash = _record_hash(raw)
    path_hash = {
        "local_path": local_path,
        "path_status": "declared" if local_path not in (None, "") else "not_declared",
        "hash_algorithm": first_nonempty(declared_hash.get("algorithm"), _record_hash(raw).get("algorithm")),
        "hash_sha256": first_nonempty(declared_hash.get("value"), _record_hash(raw).get("value")),
        "hash_status": "declared" if first_nonempty(declared_hash.get("value"), _record_hash(raw).get("value")) else "not_declared",
        "identity_key": (
            f"{local_path}#{str(first_nonempty(declared_hash.get('value'), _record_hash(raw).get('value'))).upper()}"
            if local_path and first_nonempty(declared_hash.get("value"), _record_hash(raw).get("value"))
            else None
        ),
    }
    license_status = record.get("license", {}).get("status") if isinstance(record.get("license"), dict) else "not_available"
    license_basis = "G6.provenance_audit" if key in indexes["g6_by_key"] else "manifest.source_record"
    source_specific = None
    if g11 is not None:
        license_status = g11.get("license_status", license_status)
        license_basis = "G11.evidence_license_matrix"
        source_specific = g11.get("license_status") != "blocked"
    evidence_state = record.get("proof_state") or first_nonempty(raw.get("evidence_status"), "not_available")
    evidence_basis = "G6.provenance_audit"
    if g11 is not None:
        evidence_state = g11.get("evidence_status", evidence_state)
        evidence_basis = "G11.evidence_license_matrix"
    if g12 is not None and g12.get("license_source_specific", {}).get("state") == "blocked":
        evidence_state = "blocked"
        evidence_basis = "G12.locator_license_checklist"
    claim_ready = bool(g9 and g9.get("claim_ready")) or bool(g11 and g11.get("claim_ready")) or bool(g12 and g12.get("claim_ready"))
    if claim_ready:
        raise ValueError(f"G15 must not promote claim_ready: {key}")
    source_reports: set[str] = set()
    if key in indexes["g6_by_key"]:
        source_reports.add("G6")
    if manifest_path.endswith("UNI_CORPUS_LOTTO_G5_ECFR.json"):
        source_reports.add("G5")
    if manifest_path.endswith("UNI_CORPUS_LOTTO_G10_B.json"):
        source_reports.add("G10")
    if g9 is not None:
        source_reports.add("G9")
    if g11 is not None:
        source_reports.add("G11")
    if g12 is not None:
        source_reports.add("G12")
    if g7_refs:
        source_reports.add("G7")
    remediation = {
        "g7_items": g7_refs,
        "g9_item_ids": sorted(
            {
                item_id
                for item in g9_coverage
                for item_id in ([item["item_id"]] if item.get("item_id") else item.get("item_ids", []))
            }
        ),
        "g9_residual_codes": sorted(g9.get("residual_codes", [])) if g9 else [],
        "g11_blocker_codes": sorted(g11.get("blocker", {}).get("codes", [])) if g11 else [],
        "g12_blocker_codes": sorted(g12.get("blocker", {}).get("codes", [])) if g12 else [],
        "open": bool(g7_refs or (g9 and not g9.get("claim_ready")) or (g11 and g11.get("blocker")) or (g12 and g12.get("blocker"))),
    }
    return {
        "record_key": key,
        "manifest_path": manifest_path,
        "manifest_id": record["manifest_id"],
        "record_id": record_id,
        "record_kind": record["record_kind"],
        "title": record.get("title"),
        "source_kind": record.get("source_kind"),
        "source_reports": sorted(source_reports),
        "path_hash": path_hash,
        "package_scope": _package_scope_for_manifest(manifest_rows, manifest_path),
        "license_status": {
            "state": license_status,
            "basis": license_basis,
            "source_specific": source_specific,
        },
        "evidence_status": {
            "state": evidence_state,
            "basis": evidence_basis,
            "g6_proof_state": record.get("proof_state"),
            "g9_status": g9.get("evidence_status") if g9 else None,
            "g11_status": g11.get("evidence_status") if g11 else None,
            "g12_license_state": g12.get("license_source_specific", {}).get("state") if g12 else None,
            "claim_ready": False,
            "promotion": "not_promoted",
        },
        "alias_group_ids": [group["alias_group_id"] for group in aliases],
        "remediation": remediation,
    }


def _pack_rows(g13: dict[str, Any], g14: dict[str, Any], manifest_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    g14_by_pack = {item["pack_id"]: item for item in g14.get("items", [])}
    scope_to_manifests: defaultdict[str, list[str]] = defaultdict(list)
    for manifest in manifest_rows:
        package = manifest.get("declared_package_scope")
        if package:
            scope_to_manifests[package].append(manifest["manifest_path"])
    rows: list[dict[str, Any]] = []
    for pack in sorted(g13.get("packs", []), key=lambda item: item["pack_path"]):
        pack_path = pack["pack_path"]
        queue_item = g14_by_pack.get(pack["pack_id"])
        matched = pack.get("matched_source_records", [])
        source_keys = sorted(
            record_key(item["manifest_path"], item["source_record_id"])
            for item in matched
        )
        rows.append(
            {
                "pack_id": pack["pack_id"],
                "pack_path": pack_path,
                "course_yaml": pack.get("course_yaml"),
                "package_scope_matches": sorted(scope_to_manifests.get(pack_path, [])),
                "package_scope_status": "exact_manifest_scope" if scope_to_manifests.get(pack_path) else "no_exact_manifest_scope",
                "source_record_keys": source_keys,
                "g13_source_record_status": pack["source_record_present"],
                "g13_license_status": pack["license_status"],
                "g13_evidence_status": pack["evidence_status"],
                "g13_remediation_codes": sorted(pack.get("remediation_codes", [])),
                "g14_queue_item_id": queue_item.get("queue_item_id") if queue_item else None,
                "g14_status": queue_item.get("status") if queue_item else "not_queued",
                "g14_blocker_codes": sorted(queue_item.get("blocked", {}).get("codes", [])) if queue_item else [],
                "remediation_open": bool(pack.get("remediation_required") or queue_item),
            }
        )
    return rows


def _index_aliases(alias_groups: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    result: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for group in alias_groups:
        for key in group["record_keys"]:
            result[key].append(group)
    return dict(result)


def _find_record_keys_from_g6(g6: dict[str, Any], direct_manifests: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    records = []
    for record in _g6_record_map(g6).values():
        records.append({**record, "_raw": None})
    known_keys = {item["record_key"] for item in records}
    for manifest_path, manifest in direct_manifests.items():
        if manifest_path != "docs/coordination/UNI_CORPUS_LOTTO_G10_B.json":
            continue
        for source in manifest.get("source_records", []):
            key = record_key(manifest_path, source["source_record_id"])
            if key in known_keys:
                continue
            hash_data = _record_hash(source)
            records.append(
                {
                    "record_key": key,
                    "manifest_path": manifest_path,
                    "manifest_id": manifest["manifest_id"],
                    "record_id": source["source_record_id"],
                    "record_kind": "source",
                    "title": source.get("title"),
                    "entity": source.get("entity"),
                    "source_kind": source.get("source_kind"),
                    "local_path": _record_local_path(source),
                    "url": {"status": "declared" if _record_local_path(source) else "declared", "value": first_nonempty((source.get("source") or {}).get("official_url"), (source.get("source") or {}).get("url")), "basis": "manifest.source"},
                    "license": {"status": "not_declared", "label": None},
                    "proof_state": source.get("evidence_status", "context_only"),
                    "hash": hash_data,
                    "residual_codes": [],
                    "residuals": [],
                    "_raw": source,
                }
            )
    return sorted(records, key=lambda item: item["record_key"])


def _set_report_indexes(indexes: dict[str, Any], g11: dict[str, Any] | None, g12: dict[str, Any] | None) -> None:
    indexes["g11_by_key"] = {row["record_key"]: row for row in (g11 or {}).get("rows", [])}
    indexes["g12_by_key"] = {row["record_key"]: row for row in (g12 or {}).get("records", [])}


def validate_report(report: dict[str, Any]) -> None:
    required = {
        "$schema",
        "schema_version",
        "reconciliation_id",
        "metadata_only",
        "observed_at",
        "base_commit",
        "scope",
        "summary",
        "input_reports",
        "manifest_inventory",
        "record_reconciliation",
        "duplicate_alias_groups",
        "pack_reconciliation",
        "limitations",
    }
    missing = required - set(report)
    if missing:
        raise ValueError(f"G15 report missing keys: {sorted(missing)}")
    if report["schema_version"] != REPORT_SCHEMA_VERSION:
        raise ValueError("Unexpected G15 schema_version")
    if report["$schema"] != SCHEMA_REF:
        raise ValueError("G15 report is not anchored to its schema")
    if report["metadata_only"] is not True:
        raise ValueError("G15 report must be metadata-only")
    if report["base_commit"] != BASE_COMMIT:
        raise ValueError("G15 report must remain anchored to the requested base commit")
    if report["scope"]["missing_report_ids"] != ["G8"]:
        raise ValueError("G15 expected only G8 to be missing from this checkout")
    if [item["report_id"] for item in report["input_reports"]] != list(EXPECTED_REPORT_IDS):
        raise ValueError("G15 input reports are not in deterministic G5-G14 order")
    record_rows = report["record_reconciliation"]
    if [item["record_key"] for item in record_rows] != sorted(item["record_key"] for item in record_rows):
        raise ValueError("G15 record rows are not sorted")
    if len({item["record_key"] for item in record_rows}) != len(record_rows):
        raise ValueError("G15 record rows contain duplicate keys")
    alias_keys = {key for group in report["duplicate_alias_groups"] for key in group["record_keys"]}
    record_keys = {item["record_key"] for item in record_rows}
    if not alias_keys <= record_keys:
        raise ValueError("G15 alias group references an unknown record")
    if any(group["deduplication_performed"] or group["semantic_deduplication_performed"] for group in report["duplicate_alias_groups"]):
        raise ValueError("G15 reports deduplication as performed")
    pack_rows = report["pack_reconciliation"]
    if [item["pack_path"] for item in pack_rows] != sorted(item["pack_path"] for item in pack_rows):
        raise ValueError("G15 pack rows are not sorted")
    if len({item["pack_path"] for item in pack_rows}) != len(pack_rows):
        raise ValueError("G15 pack rows contain duplicate paths")
    if any(item["evidence_status"].get("claim_ready") for item in record_rows):
        raise ValueError("G15 must not promote a record to claim-ready")
    if any(item["g14_status"] == "resolved" for item in pack_rows):
        raise ValueError("G15 must not promote a G14 item")
    serialized = json.dumps(report, ensure_ascii=False).lower()
    for forbidden in sorted(FORBIDDEN_KEYS):
        if f'"{forbidden}"' in serialized:
            raise ValueError(f"Protected payload key found in G15 report: {forbidden}")
    summary = report["summary"]
    if summary["record_count"] != len(record_rows):
        raise ValueError("G15 record count mismatch")
    if summary["alias_group_count"] != len(report["duplicate_alias_groups"]):
        raise ValueError("G15 alias count mismatch")
    if summary["pack_count"] != len(pack_rows):
        raise ValueError("G15 pack count mismatch")


def build_report(root: Path = ROOT) -> dict[str, Any]:
    input_reports, loaded_reports = build_input_inventory(root)
    manifest_rows, manifests = build_manifest_inventory(root)
    g6 = loaded_reports.get("G6")
    g7 = loaded_reports.get("G7")
    g9 = loaded_reports.get("G9")
    g11 = loaded_reports.get("G11")
    g12 = loaded_reports.get("G12")
    g13 = loaded_reports.get("G13")
    g14 = loaded_reports.get("G14")
    if not all(isinstance(item, dict) for item in (g6, g7, g9, g11, g12, g13, g14)):
        raise ValueError("G15 requires G6, G7, G9, G11, G12, G13, and G14")

    aliases = _g6_alias_groups(g6)
    alias_by_key = _index_aliases(aliases)
    indexes = _index_remediations(g7, g9, g14)
    indexes["g6_by_key"] = _g6_record_map(g6)
    _set_report_indexes(indexes, g11, g12)
    base_records = _find_record_keys_from_g6(g6, manifests)
    record_rows = [
        _record_row(record, {row["manifest_path"]: row for row in manifest_rows}, manifests, alias_by_key, indexes)
        for record in base_records
    ]
    record_rows.sort(key=lambda item: item["record_key"])

    g7_alias_refs = {item["source_ref"]: item["item_id"] for item in g7.get("items", []) if str(item.get("source_ref", "")).startswith("alias:")}
    for group in aliases:
        refs = [g7_alias_refs[f"alias:{group['hash_sha256']}"]] if f"alias:{group['hash_sha256']}" in g7_alias_refs else []
        group["remediation_refs"] = sorted(refs)

    pack_rows = _pack_rows(g13, g14, manifest_rows)
    observed_dates = [entry["observed_at"] for entry in input_reports if entry["observed_at"]]
    observed_at = max(observed_dates) if observed_dates else None
    available_ids = [entry["report_id"] for entry in input_reports if entry["present"]]
    missing_ids = [entry["report_id"] for entry in input_reports if not entry["present"]]
    g14_blocked = sum(item["g14_status"] == "blocked" for item in pack_rows)
    report = {
        "$schema": SCHEMA_REF,
        "schema_version": REPORT_SCHEMA_VERSION,
        "reconciliation_id": RECONCILIATION_ID,
        "metadata_only": True,
        "observed_at": observed_at,
        "base_commit": BASE_COMMIT,
        "scope": {
            "input_report_range": "G5-G14",
            "expected_report_ids": list(EXPECTED_REPORT_IDS),
            "available_report_ids": available_ids,
            "missing_report_ids": missing_ids,
            "current_checkout_only": True,
            "matching_policy": "Only explicit record keys, manifest paths, exact path+SHA-256 identity, and explicit manifest scope.package are admissible.",
            "deduplication_policy": "Exact path+SHA-256 aliases remain separate representations; no deduplication is performed.",
            "semantic_matching_policy": "Course names, titles, topics, COURSE.yaml fonti, text similarity, and presumed subject correspondence are not matching bases.",
            "promotion_policy": "Licence, evidence, vigency, legal clearance, and claim-ready state are copied or blocked conservatively; no state is promoted by this reconciliation.",
            "excluded_payloads": [
                "PDF, XML, HTML, manuals, standards, prices, manufacturer data, and source text",
                "COURSE.yaml content beyond report-provided pack identifiers and paths",
                "schede JSONL, exam questions, answers, and solutions",
                "live URL requests and independent legal or technical review",
            ],
        },
        "summary": {
            "input_report_count": len(input_reports),
            "available_report_count": len(available_ids),
            "missing_report_count": len(missing_ids),
            "manifest_count": len(manifest_rows),
            "record_count": len(record_rows),
            "alias_group_count": len(aliases),
            "record_rows_with_aliases": sum(bool(row["alias_group_ids"]) for row in record_rows),
            "record_rows_with_open_remediation": sum(row["remediation"]["open"] for row in record_rows),
            "pack_count": len(pack_rows),
            "pack_rows_with_exact_manifest_scope": sum(item["package_scope_status"] == "exact_manifest_scope" for item in pack_rows),
            "g14_blocked_pack_count": g14_blocked,
            "claim_ready_record_count": sum(row["evidence_status"]["claim_ready"] for row in record_rows),
        },
        "input_reports": input_reports,
        "manifest_inventory": manifest_rows,
        "record_reconciliation": record_rows,
        "duplicate_alias_groups": aliases,
        "pack_reconciliation": pack_rows,
        "limitations": [
            "G8 is explicitly absent from this checkout and is not imported from another branch or reconstructed.",
            "The report reconciles declared metadata and prior report states; it does not prove source accuracy, current URL availability, licence clearance, legal status, or regulatory vigency.",
            "An exact path+SHA-256 alias is reported as a review relationship, not as a destructive or semantic deduplication decision.",
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
