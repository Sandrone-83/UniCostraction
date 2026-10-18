"""Build the G7-B provenance remediation queue from the G6 audit only.

The queue is a metadata-only worklist.  It copies no source payloads, does not
decide licenses, does not promote proof states, and never deduplicates files.
Every item must be traceable to an observed G6 record or alias group.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


QUEUE_SCHEMA_VERSION = "G7-B-remediation-queue"
QUEUE_ID = "G7-B-provenance-remediation"
G6_AUDIT_ID = "G6-B-provenance"
G6_REPORT = Path("docs/coordination/UNI_PROVENANCE_AUDIT_G6.json")
QUEUE_REPORT = Path("docs/coordination/UNI_REMEDIATION_QUEUE_G7_B.json")
QUEUE_SCHEMA = Path("docs/coordination/UNI_REMEDIATION_QUEUE_G7_B_SCHEMA.json")

CATEGORY_ORDER = (
    "missing_manifest_id",
    "missing_metadata_only",
    "license_missing",
    "g3_pdf_blocked",
    "gse_context_only",
    "alias_not_deduplicated",
)

PROTECTED_KEYS = {"text", "content", "question", "answer", "solution"}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return value


def _record_map(audit: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {record["record_key"]: record for record in audit["records"]}


def _manifest_map(audit: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {manifest["path"]: manifest for manifest in audit["manifests"]}


def _category_code(category: str) -> str:
    return {
        "missing_manifest_id": "MANIFEST-ID",
        "missing_metadata_only": "METADATA-ONLY",
        "license_missing": "LICENSE",
        "g3_pdf_blocked": "G3-PDF",
        "gse_context_only": "GSE-CONTEXT",
        "alias_not_deduplicated": "ALIAS",
    }[category]


def _item_id(category: str, source_ref: str) -> str:
    digest = hashlib.sha256(source_ref.encode("utf-8")).hexdigest()[:12]
    return f"G7-B-{_category_code(category)}-{digest}"


def _base_item(category: str, source_ref: str, audit: dict[str, Any]) -> dict[str, Any]:
    return {
        "item_id": _item_id(category, source_ref),
        "category": category,
        "status": "open",
        "source_ref": source_ref,
        "source_audit": {
            "audit_id": audit["audit_id"],
            "audit_report": str(G6_REPORT).replace("\\", "/"),
        },
        "closure_evidence": [],
        "closure_criteria": [],
        "constraints": [
            "Do not modify source files or source payloads.",
            "Do not infer missing provenance, license, URL, or legal status.",
            "Do not promote a proof state from metadata alone.",
        ],
    }


def _record_item(
    category: str,
    record: dict[str, Any],
    audit: dict[str, Any],
    observed_gap: dict[str, Any],
    criteria: list[str],
) -> dict[str, Any]:
    item = _base_item(category, record["record_key"], audit)
    item["record"] = {
        "record_key": record["record_key"],
        "manifest_path": record["manifest_path"],
        "manifest_id": record["manifest_id"],
        "record_id": record["record_id"],
        "record_kind": record["record_kind"],
        "local_path": record["local_path"],
        "proof_state": record["proof_state"],
    }
    item["observed_gap"] = observed_gap
    item["closure_criteria"] = criteria
    return item


def _record_codes(record: dict[str, Any]) -> list[str]:
    return list(record.get("residual_codes") or [])


def _build_record_items(audit: dict[str, Any]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    manifests = _manifest_map(audit)
    for record in audit["records"]:
        codes = _record_codes(record)
        manifest = manifests[record["manifest_path"]]
        if "manifest_id_not_declared_lot_id_used_as_reference" in codes:
            items.append(
                _record_item(
                    "missing_manifest_id",
                    record,
                    audit,
                    {
                        "g6_residual_code": "manifest_id_not_declared_lot_id_used_as_reference",
                        "field": "manifest_id",
                        "g6_manifest_id_source": manifest["manifest_id_source"],
                        "g6_effective_reference": manifest["manifest_id"],
                    },
                    [
                        "The source manifest explicitly declares a stable manifest_id.",
                        "The chosen identifier is reviewed by the corpus owner; it is not inferred by this queue.",
                        "A regenerated G6 audit no longer reports the residual code for the affected records.",
                    ],
                )
            )
        if "manifest_metadata_only_flag_not_declared" in codes:
            items.append(
                _record_item(
                    "missing_metadata_only",
                    record,
                    audit,
                    {
                        "g6_residual_code": "manifest_metadata_only_flag_not_declared",
                        "field": "metadata_only",
                        "g6_manifest_metadata_only_flag": manifest["metadata_only_flag"],
                    },
                    [
                        "The source manifest explicitly declares the reviewed boolean metadata_only value.",
                        "The declared value and its scope are approved by the corpus owner; this queue does not choose it.",
                        "A regenerated G6 audit no longer reports the residual code for the affected records.",
                    ],
                )
            )
        if "license_or_reuse_terms_not_declared" in codes:
            license_data = record.get("license") or {}
            items.append(
                _record_item(
                    "license_missing",
                    record,
                    audit,
                    {
                        "g6_residual_code": "license_or_reuse_terms_not_declared",
                        "license_status": license_data.get("status"),
                        "license_label_observed_by_g6": license_data.get("label"),
                    },
                    [
                        "Exact license or reuse terms are supplied with a traceable basis.",
                        "Rights and reuse are reviewed independently where the terms require it.",
                        "A regenerated G6 audit no longer reports the missing-license residual code.",
                    ],
                )
            )
        if (
            record["manifest_path"].endswith("PROVENANCE_MANIFEST_G3_GSE_CT3.json")
            and record["record_kind"] == "source"
            and str(record.get("local_path") or "").lower().endswith(".pdf")
            and record["proof_state"] == "blocked"
            and "blocked_until_missing_metadata_or_evidence_is_supplied" in codes
        ):
            items.append(
                _record_item(
                    "g3_pdf_blocked",
                    record,
                    audit,
                    {
                        "g6_residual_codes": [
                            code
                            for code in codes
                            if code
                            in {
                                "exact_url_not_declared",
                                "license_or_reuse_terms_not_declared",
                                "blocked_until_missing_metadata_or_evidence_is_supplied",
                            }
                        ],
                        "proof_state": "blocked",
                        "local_path": record["local_path"],
                    },
                    [
                        "The exact locator for this local PDF is registered and identity-matched.",
                        "Reuse or distribution terms are evidenced for this specific PDF.",
                        "Current applicability and source identity are checked without editing the PDF.",
                        "A regenerated G6 audit no longer reports the blocked residual for this record.",
                    ],
                )
            )
        if (
            record["manifest_path"].endswith("PROVENANCE_MANIFEST_G3_GSE_CT3.json")
            and record["record_kind"] == "context"
            and record["proof_state"] == "context_only"
            and "context_does_not_prove_source_vigency_or_reuse" in codes
        ):
            items.append(
                _record_item(
                    "gse_context_only",
                    record,
                    audit,
                    {
                        "g6_residual_codes": [
                            "license_or_reuse_terms_not_declared",
                            "context_does_not_prove_source_vigency_or_reuse",
                        ],
                        "proof_state": "context_only",
                        "role": "institutional context; not a source locator for the local PDF",
                    },
                    [
                        "The record remains explicitly labeled context_only unless independently reassessed.",
                        "A primary source record for the local PDF is identified and assessed separately.",
                        "Context is not used as proof of PDF identity, vigency, license, or reuse.",
                        "The related G3 PDF blocker is closed separately under its own criteria.",
                    ],
                )
            )
    return items


def _build_alias_items(audit: dict[str, Any]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for alias in audit["alias_groups"]:
        source_ref = "alias:" + alias["hash_sha256"]
        item = _base_item("alias_not_deduplicated", source_ref, audit)
        item["alias_group"] = {
            "local_path": alias["local_path"],
            "hash_sha256": alias["hash_sha256"],
            "record_keys": alias["record_keys"],
            "representation_count": alias["representation_count"],
        }
        item["observed_gap"] = {
            "g6_residual_code": alias["residual_code"],
            "representation_count": alias["representation_count"],
            "deduplication_performed": False,
        }
        item["closure_criteria"] = [
            "The corpus owner records a canonical record and the intentional alias relationship.",
            "References are reconciled without deleting or rewriting source payloads.",
            "The hash and local path relationship is rechecked after the metadata-only change.",
            "A regenerated G6 audit no longer reports this unresolved alias review.",
        ]
        items.append(item)
    return items


def build_queue(root: Path) -> dict[str, Any]:
    audit = load_json(root / G6_REPORT)
    if audit.get("audit_id") != G6_AUDIT_ID:
        raise ValueError(f"Unexpected audit_id: {audit.get('audit_id')!r}")
    items = _build_record_items(audit) + _build_alias_items(audit)
    category_rank = {category: index for index, category in enumerate(CATEGORY_ORDER)}
    items.sort(key=lambda item: (category_rank[item["category"]], item["source_ref"]))
    categories = Counter(item["category"] for item in items)
    return {
        "$schema": "./UNI_REMEDIATION_QUEUE_G7_B_SCHEMA.json",
        "schema_version": QUEUE_SCHEMA_VERSION,
        "queue_id": QUEUE_ID,
        "metadata_only": True,
        "observed_at": audit.get("observed_at"),
        "source_audit": {
            "audit_id": audit["audit_id"],
            "report": str(G6_REPORT).replace("\\", "/"),
            "record_count": audit["summary"]["record_count"],
        },
        "scope": {
            "included_categories": list(CATEGORY_ORDER),
            "excluded_residual_codes": [
                "external_url_availability_not_checked",
                "independent_license_clearance_not_checked",
                "current_version_or_vigency_not_checked",
                "content_or_legal_accuracy_not_checked",
            ],
            "policy": "Only G6-observed gaps are queued; no gap is closed by this report.",
        },
        "summary": {
            "item_count": len(items),
            "open_item_count": len(items),
            "by_status": {"open": len(items)},
            "by_category": {category: categories.get(category, 0) for category in CATEGORY_ORDER},
        },
        "items": items,
    }


def _walk_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        keys.update(value)
        for child in value.values():
            keys.update(_walk_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.update(_walk_keys(child))
    return keys


def validate_queue(queue: dict[str, Any]) -> None:
    required = {
        "$schema",
        "schema_version",
        "queue_id",
        "metadata_only",
        "observed_at",
        "source_audit",
        "scope",
        "summary",
        "items",
    }
    missing = required - set(queue)
    if missing:
        raise ValueError(f"Queue missing keys: {sorted(missing)}")
    if queue["schema_version"] != QUEUE_SCHEMA_VERSION:
        raise ValueError("Unexpected queue schema_version")
    if queue["queue_id"] != QUEUE_ID or queue["metadata_only"] is not True:
        raise ValueError("Queue identity or metadata_only contract failed")
    expected_schema_ref = "./" + str(QUEUE_SCHEMA).replace("\\", "/").split("/")[-1]
    if queue["$schema"] != expected_schema_ref:
        raise ValueError("Queue schema reference failed")
    if set(queue["summary"]["by_category"]) != set(CATEGORY_ORDER):
        raise ValueError("Queue category summary failed")
    if queue["summary"]["item_count"] != len(queue["items"]):
        raise ValueError("Queue item count failed")
    if queue["summary"]["open_item_count"] != len(queue["items"]):
        raise ValueError("Queue contains a non-open item")
    if _walk_keys(queue) & PROTECTED_KEYS:
        raise ValueError("Queue contains protected payload keys")
    seen: set[str] = set()
    for item in queue["items"]:
        if item["item_id"] in seen:
            raise ValueError(f"Duplicate item_id: {item['item_id']}")
        seen.add(item["item_id"])
        if item["category"] not in CATEGORY_ORDER or item["status"] != "open":
            raise ValueError("Invalid item category or status")
        if not item["closure_criteria"] or not item["constraints"]:
            raise ValueError("Item closure contract is incomplete")


def write_queue(root: Path) -> Path:
    queue = build_queue(root)
    validate_queue(queue)
    path = root / QUEUE_REPORT
    path.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true", help="write the generated queue JSON")
    args = parser.parse_args()
    queue = build_queue(args.root)
    validate_queue(queue)
    if args.write:
        print(write_queue(args.root))
    else:
        print(json.dumps(queue, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
