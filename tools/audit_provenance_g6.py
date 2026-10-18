"""Build a deterministic, metadata-only provenance audit for the G6-B tranche.

The input catalog is intentionally explicit.  This tool reads only JSON
manifests and their metadata; it does not open PDFs, XML, course cards, or
exam payloads.  It never upgrades a source state: ``verified`` is emitted
only when an input manifest explicitly says ``verified`` or ``verificato``.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


REPORT_SCHEMA_VERSION = "G6-provenance-audit"
ALLOWED_STATES = ("verified", "observed_local", "context_only", "blocked")
PROTECTED_KEYS = {"text", "content", "question", "answer", "solution"}

MANIFEST_SPECS = (
    {
        "path": "docs/coordination/UNI_CORPUS_LOTTO_G1.json",
        "collections": (("records", "source"),),
    },
    {
        "path": "Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json",
        "collections": (("records", "source"),),
    },
    {
        "path": (
            "UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/fonti/"
            "PROVENANCE_MANIFEST_G3_GSE_CT3.json"
        ),
        "collections": (("records", "source_or_context"),),
    },
    {
        "path": "docs/coordination/UNI_CORPUS_LOTTO_G5_ECFR.json",
        "collections": (
            ("source_records", "source"),
            ("official_context_records", "context"),
            ("related_blockers", "blocker"),
        ),
    },
)


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


def source_id(record: dict[str, Any], kind: str, index: int) -> str:
    existing = first_nonempty(
        record.get("source_record_id"),
        record.get("record_id"),
        record.get("context_record_id"),
    )
    if existing:
        return str(existing)
    if kind == "blocker":
        return f"BLOCKER-{index:03d}"
    raise ValueError(f"Record has no source_record_id/record_id: {record}")


def state_for(record: dict[str, Any], kind: str) -> str:
    if kind == "blocker":
        return "blocked"
    explicit = ((record.get("verification_status") or {}).get("state"))
    if explicit in ("verified", "verificato"):
        return "verified"
    if explicit in ALLOWED_STATES:
        return explicit
    if kind == "context" or record.get("source_kind") in {
        "official_context_page",
        "official_context",
    }:
        return "context_only"
    raise ValueError(f"Unsupported or missing verification state: {explicit!r}")


def record_url(record: dict[str, Any]) -> tuple[str | None, str | None]:
    locator = record.get("locator") or {}
    source = record.get("source") or {}
    url = first_nonempty(locator.get("url"), source.get("url"), record.get("url"))
    basis = None
    if locator.get("url") not in (None, ""):
        basis = "locator.url"
    elif source.get("url") not in (None, ""):
        basis = "source.url"
    elif record.get("url") not in (None, ""):
        basis = "url"
    return (str(url) if url is not None else None, basis)


def record_local_path(record: dict[str, Any]) -> str | None:
    locator = record.get("locator") or {}
    source = record.get("source") or {}
    return first_nonempty(
        locator.get("path"),
        source.get("local_path"),
        record.get("raw_file"),
    )


def license_info(record: dict[str, Any]) -> dict[str, Any]:
    license_data = record.get("license")
    if isinstance(license_data, dict):
        label = first_nonempty(license_data.get("label"), license_data.get("local_statement"))
        status = "declared" if label else "not_declared"
        return {
            "status": status,
            "label": label,
            "basis_path": license_data.get("basis_path"),
            "basis_selector": license_data.get("basis_selector"),
        }

    reuse = record.get("license_reuse")
    if isinstance(reuse, dict):
        label = first_nonempty(reuse.get("label"), reuse.get("local_statement"))
        declared = reuse.get("status") not in (None, "not_declared", "not_assessed_separately")
        return {
            "status": "declared" if declared and label else "not_declared",
            "label": label,
            "basis_path": reuse.get("basis_path"),
            "basis_selector": reuse.get("basis_selector"),
        }

    return {
        "status": "not_declared",
        "label": None,
        "basis_path": None,
        "basis_selector": None,
    }


def raw_residuals(record: dict[str, Any]) -> list[str]:
    limitations = record.get("limitations") or []
    verification = record.get("verification_status") or {}
    not_checked = verification.get("not_checked") or []
    context_relation = record.get("context_relation") or {}
    values: list[str] = []
    values.extend(f"not_checked:{item}" for item in not_checked)
    values.extend(f"limitation:{item}" for item in limitations)
    if context_relation:
        values.append("context_relation:" + json.dumps(context_relation, ensure_ascii=False, sort_keys=True))
    return values


def derived_residuals(
    record: dict[str, Any], state: str, url: str | None, license_data: dict[str, Any]
) -> list[str]:
    verification = record.get("verification_status") or {}
    not_checked = set(verification.get("not_checked") or [])
    result: list[str] = []

    if url is None:
        result.append("exact_url_not_declared")
    elif "external_url_availability" in not_checked:
        result.append("external_url_availability_not_checked")

    if license_data["status"] == "not_declared":
        result.append("license_or_reuse_terms_not_declared")
    if {"current_license_terms", "independent_legal_clearance"} & not_checked:
        result.append("independent_license_clearance_not_checked")

    if {
        "current_content_as_of_observed_at",
        "current_regulatory_applicability",
        "current_version_or_vigency",
    } & not_checked:
        result.append("current_version_or_vigency_not_checked")

    if {
        "technical_accuracy_or_completeness",
        "content_accuracy_or_completeness",
        "independent_legal_clearance",
    } & not_checked:
        result.append("content_or_legal_accuracy_not_checked")

    if state == "context_only":
        result.append("context_does_not_prove_source_vigency_or_reuse")
    if state == "blocked":
        result.append("blocked_until_missing_metadata_or_evidence_is_supplied")

    return list(dict.fromkeys(result))


def normalize_record(
    manifest_path: str,
    manifest: dict[str, Any],
    record: dict[str, Any],
    kind: str,
    index: int,
) -> dict[str, Any]:
    if not isinstance(record, dict):
        raise ValueError(f"Non-object record in {manifest_path}: {record!r}")

    state = state_for(record, kind)
    url, url_basis = record_url(record)
    license_data = license_info(record)
    identifier = source_id(record, kind, index)
    manifest_id = first_nonempty(manifest.get("manifest_id"), manifest.get("lot_id"))
    if not manifest_id:
        raise ValueError(f"Manifest has no manifest_id: {manifest_path}")

    blocker_evidence = record.get("evidence") if kind == "blocker" else None
    raw_residue = raw_residuals(record)
    if kind == "blocker":
        raw_residue.extend(
            [
                "blocker_reason:" + str(record.get("reason", "")),
                *["blocker_evidence:" + str(item) for item in (blocker_evidence or [])],
            ]
        )

    result: dict[str, Any] = {
        "record_key": f"{manifest_path}#{identifier}",
        "manifest_path": manifest_path,
        "manifest_id": manifest_id,
        "record_id": identifier,
        "record_kind": kind,
        "title": first_nonempty(record.get("title"), record.get("candidate")),
        "entity": record.get("entity"),
        "source_kind": record.get("source_kind"),
        "local_path": record_local_path(record),
        "url": {
            "status": "declared" if url is not None else "not_declared",
            "value": url,
            "basis": url_basis,
        },
        "license": license_data,
        "proof_state": state,
        "hash": record.get("hash"),
        "residual_codes": derived_residuals(record, state, url, license_data),
        "residuals": raw_residue,
    }
    if kind == "blocker":
        result["blocker"] = {
            "reason": record.get("reason"),
            "evidence": blocker_evidence or [],
        }
    if "metadata_only" not in manifest:
        result["residual_codes"].append("manifest_metadata_only_flag_not_declared")
    if "manifest_id" not in manifest and "lot_id" in manifest:
        result["residual_codes"].append("manifest_id_not_declared_lot_id_used_as_reference")
    return result


def validate_input_manifest(path: str, manifest: dict[str, Any]) -> None:
    if manifest.get("metadata_only") is False:
        raise ValueError(f"metadata_only must be true: {path}")
    if not first_nonempty(manifest.get("manifest_id"), manifest.get("lot_id")):
        raise ValueError(f"manifest_id or lot_id is required: {path}")


def collect_records(root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    all_records: list[dict[str, Any]] = []
    manifests: list[dict[str, Any]] = []
    blocker_index = 0
    for spec in MANIFEST_SPECS:
        relative_path = str(spec["path"])
        path = root / relative_path
        manifest = load_json(path)
        validate_input_manifest(relative_path, manifest)
        manifest_entry = {
            "path": relative_path,
            "manifest_id": first_nonempty(manifest.get("manifest_id"), manifest.get("lot_id")),
            "manifest_id_source": (
                "manifest_id" if "manifest_id" in manifest else "lot_id_fallback"
            ),
            "schema_version": manifest.get("schema_version"),
            "metadata_only": manifest.get("metadata_only"),
            "metadata_only_flag": (
                "declared_true"
                if manifest.get("metadata_only") is True
                else "not_declared"
            ),
            "collection_counts": {},
        }
        for collection_name, kind in spec["collections"]:
            records = manifest.get(collection_name, [])
            if not isinstance(records, list):
                raise ValueError(f"Expected array {collection_name} in {relative_path}")
            manifest_entry["collection_counts"][collection_name] = len(records)
            for item in records:
                if kind == "blocker":
                    blocker_index += 1
                normalized_kind = kind
                if kind == "source_or_context":
                    normalized_kind = "context" if item.get("source_kind") == "official_context_page" else "source"
                all_records.append(
                    normalize_record(
                        relative_path,
                        manifest,
                        item,
                        normalized_kind,
                        blocker_index,
                    )
                )
        manifests.append(manifest_entry)
    return all_records, manifests


def alias_groups(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[str]] = defaultdict(list)
    for record in records:
        if record["record_kind"] == "blocker":
            continue
        local_path = record.get("local_path")
        digest = (record.get("hash") or {}).get("value")
        if local_path and digest:
            grouped[(str(local_path), str(digest).upper())].append(record["record_key"])
    result = []
    for (local_path, digest), record_keys in sorted(grouped.items()):
        if len(record_keys) < 2:
            continue
        result.append(
            {
                "local_path": local_path,
                "hash_sha256": digest,
                "record_keys": sorted(record_keys),
                "representation_count": len(record_keys),
                "residual_code": "cross_manifest_alias_review_required",
            }
        )
    return result


def validate_report(report: dict[str, Any]) -> None:
    required = {
        "$schema",
        "schema_version",
        "audit_id",
        "metadata_only",
        "scope",
        "summary",
        "manifests",
        "records",
        "alias_groups",
    }
    missing = required - set(report)
    if missing:
        raise ValueError(f"Report missing required keys: {sorted(missing)}")
    if report["schema_version"] != REPORT_SCHEMA_VERSION:
        raise ValueError("Unexpected G6 report schema_version")
    if report["metadata_only"] is not True:
        raise ValueError("G6 report must be metadata-only")
    if any(state not in ALLOWED_STATES for state in report["summary"]["by_proof_state"]):
        raise ValueError("Unsupported proof state in summary")
    if report["summary"]["record_count"] != len(report["records"]):
        raise ValueError("Summary record_count does not match records")
    for record in report["records"]:
        if record["proof_state"] not in ALLOWED_STATES:
            raise ValueError(f"Unsupported proof state: {record['proof_state']}")
        if set(record).intersection(PROTECTED_KEYS):
            raise ValueError(f"Protected payload key in audit record: {record['record_key']}")


def build_report(root: Path) -> dict[str, Any]:
    records, manifests = collect_records(root)
    state_counts = Counter(record["proof_state"] for record in records)
    url_counts = Counter(record["url"]["status"] for record in records)
    license_counts = Counter(record["license"]["status"] for record in records)
    residual_counts = Counter(
        code for record in records for code in record["residual_codes"]
    )
    observed_dates = []
    for manifest in manifests:
        source_manifest = load_json(root / manifest["path"])
        if source_manifest.get("observed_at"):
            observed_dates.append(source_manifest["observed_at"])
        source_lot = source_manifest.get("source_lot") or {}
        if source_lot.get("observed_at"):
            observed_dates.append(source_lot["observed_at"])

    report = {
        "$schema": "./UNI_PROVENANCE_AUDIT_G6_SCHEMA.json",
        "schema_version": REPORT_SCHEMA_VERSION,
        "audit_id": "G6-B-provenance",
        "metadata_only": True,
        "observed_at": max(observed_dates) if observed_dates else None,
        "scope": {
            "manifest_count": len(manifests),
            "input_manifests": [manifest["path"] for manifest in manifests],
            "excluded_payloads": [
                "PDF bytes/content",
                "XML bytes/content",
                "course cards and values",
                "exam questions, answers, and solutions",
            ],
            "state_policy": (
                "No state is promoted. verified is emitted only when explicitly present "
                "in an input manifest; observed_local remains observed_local."
            ),
        },
        "summary": {
            "record_count": len(records),
            "by_proof_state": {state: state_counts.get(state, 0) for state in ALLOWED_STATES},
            "by_url_status": {
                "declared": url_counts.get("declared", 0),
                "not_declared": url_counts.get("not_declared", 0),
            },
            "by_license_status": {
                "declared": license_counts.get("declared", 0),
                "not_declared": license_counts.get("not_declared", 0),
            },
            "residual_code_counts": dict(sorted(residual_counts.items())),
        },
        "manifests": manifests,
        "records": sorted(records, key=lambda item: item["record_key"]),
        "alias_groups": alias_groups(records),
    }
    validate_report(report)
    return report


def render_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# G6-B — audit deterministico di provenienza",
        "",
        "Audit metadata-only dei record/manifests di provenienza già presenti al commit G5.",
        "Non è stata letta o modificata la sostanza di PDF, XML, schede, valori o contenuti d'esame.",
        "",
        "## Perimetro e regola di prova",
        "",
        f"- Manifest inclusi: {summary['record_count']} record normalizzati da {len(report['manifests'])} manifest.",
        "- `verified` non viene assegnato per inferenza: compare solo se dichiarato esplicitamente in ingresso.",
        "- `observed_local` indica controlli locali già dichiarati dai manifest, non disponibilità URL, licenza corrente o validazione legale indipendente.",
        "- `context_only` non viene trattato come fonte primaria; `blocked` resta bloccato.",
        "",
        "## Quadro sintetico",
        "",
        "| Dimensione | Esito |",
        "| --- | ---: |",
        f"| Record totali | {summary['record_count']} |",
    ]
    for state in ALLOWED_STATES:
        lines.append(f"| Stato `{state}` | {summary['by_proof_state'][state]} |")
    lines.extend(
        [
            f"| URL dichiarato | {summary['by_url_status']['declared']} |",
            f"| URL non dichiarato | {summary['by_url_status']['not_declared']} |",
            f"| Licenza/riuso dichiarato | {summary['by_license_status']['declared']} |",
            f"| Licenza/riuso non dichiarato | {summary['by_license_status']['not_declared']} |",
            "",
            "## Copertura dei manifest",
            "",
            "| Manifest | ID | Collezioni |",
            "| --- | --- | --- |",
        ]
    )
    for manifest in report["manifests"]:
        collections = ", ".join(
            f"`{name}`={count}" for name, count in manifest["collection_counts"].items()
        )
        lines.append(f"| `{manifest['path']}` | `{manifest['manifest_id']}` | {collections} |")

    lines.extend(
        [
            "",
            "## Record auditati",
            "",
            "| Record | Manifest | Stato | URL | Licenza/riuso | Residui |",
            "| --- | --- | --- | --- | --- | ---: |",
        ]
    )
    for record in report["records"]:
        lines.append(
            f"| `{record['record_id']}` | `{record['manifest_id']}` | `"
            f"{record['proof_state']}` | {record['url']['status']} | "
            f"{record['license']['status']} | {len(record['residual_codes']) + len(record['residuals'])} |"
        )

    lines.extend(["", "## Residui visibili", ""])
    for record in report["records"]:
        if not record["residual_codes"] and not record["residuals"]:
            continue
        lines.append(f"### `{record['record_key']}`")
        if record["residual_codes"]:
            lines.append("- Codici: " + ", ".join(f"`{code}`" for code in record["residual_codes"]))
        for residual in record["residuals"]:
            lines.append(f"- {residual}")
        lines.append("")

    lines.extend(["## Alias tra manifest", ""])
    if not report["alias_groups"]:
        lines.append("Nessun alias hash/path rilevato.")
    else:
        lines.append("Le righe seguenti sono rappresentazioni dello stesso path+SHA-256 in manifest diversi; non sono deduplicate automaticamente.")
        lines.append("")
        for group in report["alias_groups"]:
            lines.append(
                f"- `{group['local_path']}` — `{group['hash_sha256']}`: "
                + ", ".join(f"`{key}`" for key in group["record_keys"])
            )
    lines.extend(
        [
            "",
            "## Limiti",
            "",
            "Questo audit rende leggibili gli stati e i residui dichiarati; non prova accuratezza tecnica, vigenza normativa, disponibilità esterna degli URL, titolarità/licenza indipendente o correttezza didattica.",
            "",
        ]
    )
    return "\n".join(lines)


def write_outputs(root: Path, report_path: Path, markdown_path: Path) -> None:
    report = build_report(root)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )
    markdown_path.write_text(render_markdown(report), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--output-json",
        type=Path,
        default=Path("docs/coordination/UNI_PROVENANCE_AUDIT_G6.json"),
    )
    parser.add_argument(
        "--output-md",
        type=Path,
        default=Path("docs/coordination/UNI_PROVENANCE_AUDIT_G6.md"),
    )
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    report = build_report(root)
    if args.validate_only:
        print(json.dumps(report["summary"], ensure_ascii=False, sort_keys=True))
        return 0
    output_json = args.output_json if args.output_json.is_absolute() else root / args.output_json
    output_md = args.output_md if args.output_md.is_absolute() else root / args.output_md
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )
    output_md.write_text(render_markdown(report), encoding="utf-8")
    print(f"wrote {output_json}")
    print(f"wrote {output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
