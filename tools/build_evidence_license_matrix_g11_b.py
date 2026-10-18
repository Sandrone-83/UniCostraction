"""Build the deterministic, metadata-only G11-B evidence/licence matrix."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "docs" / "coordination" / "UNI_EVIDENCE_LICENSE_MATRIX_G11_B_SCHEMA.json"
OUTPUT_PATH = ROOT / "docs" / "coordination" / "UNI_EVIDENCE_LICENSE_MATRIX_G11_B.json"
INPUT_MANIFESTS = (
    Path("docs/coordination/UNI_CORPUS_LOTTO_G5_ECFR.json"),
    Path("docs/coordination/UNI_CORPUS_LOTTO_G10_B.json"),
)
OBSERVED_AT = "2026-10-18"


def _read_json(relative_path: Path) -> dict[str, Any]:
    path = ROOT / relative_path
    return json.loads(path.read_text(encoding="utf-8"))


def _context_for(manifest: dict[str, Any], source_id: str) -> dict[str, Any] | None:
    for context in manifest.get("official_context_records", []):
        if context.get("related_source_record_id") == source_id:
            return context
    return None


def _license_for(manifest: dict[str, Any], source: dict[str, Any]) -> dict[str, Any] | None:
    embedded = source.get("license_reuse")
    if embedded is not None:
        return embedded
    source_id = source["source_record_id"]
    for license_record in manifest.get("license_records", []):
        if license_record.get("related_source_record_id") == source_id:
            return license_record
    return None


def _locator(source: dict[str, Any]) -> str | None:
    source_data = source.get("source", {})
    return source_data.get("official_url") or source_data.get("url")


def _row(manifest_path: Path, manifest: dict[str, Any], source: dict[str, Any]) -> dict[str, Any]:
    source_id = source["source_record_id"]
    context = _context_for(manifest, source_id)
    license_record = _license_for(manifest, source)
    locator = _locator(source)
    context_url = context.get("url") if context else None
    license_url = license_record.get("url") if license_record else None

    is_g5_local = source_id == "G5-001"
    if is_g5_local:
        locator_status = "observed_local"
        official_context_status = "observed_local" if context_url else "blocked"
        license_status = (
            "observed_local"
            if license_record and license_record.get("status") == "observed_local"
            else "blocked"
        )
        evidence_status = (
            "observed_local"
            if source.get("verification_status", {}).get("state") == "observed_local"
            else "blocked"
        )
        blocker_codes = [
            "live_locator_not_checked",
            "current_license_terms_not_checked",
            "independent_legal_clearance_not_checked",
            "current_content_or_regulatory_status_not_checked",
        ]
        blocker_reason = (
            "Il record è supportato da osservazioni locali (file, registri, hash e locator), "
            "ma non da una verifica live dell'URL, dei termini correnti o della clearance legale indipendente."
        )
    else:
        locator_status = "observed_local" if locator else "blocked"
        official_context_status = "observed_local" if context_url else "blocked"
        license_status = "blocked"
        evidence_status = "blocked"
        blocker_codes = [
            "live_locator_recheck_not_performed",
            "source_specific_license_not_established",
            "official_context_is_not_source_license",
            "claim_ready_not_allowed",
        ]
        blocker_reason = (
            "Il locator e il contesto EUR-Lex sono registrati come metadati osservati localmente; "
            "non è stata stabilita una licenza specifica per l'atto e il record non è claim-ready."
        )

    evidence_refs: list[str] = []
    for ref in (locator, context_url, license_url):
        if ref and ref not in evidence_refs:
            evidence_refs.append(ref)

    return {
        "record_key": f"{manifest_path.as_posix()}#{source_id}",
        "manifest_path": manifest_path.as_posix(),
        "manifest_id": manifest["manifest_id"],
        "source_record_id": source_id,
        "source_kind": source.get("source_kind"),
        "title": source["title"],
        "locator_status": locator_status,
        "official_context_status": official_context_status,
        "license_status": license_status,
        "evidence_status": evidence_status,
        "verification_date": manifest["observed_at"],
        "claim_ready": False,
        "blocker": {
            "state": "blocked",
            "codes": blocker_codes,
            "reason": blocker_reason,
            "evidence_refs": evidence_refs,
            "live_verification": False,
        },
    }


def build_matrix() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for manifest_path in INPUT_MANIFESTS:
        manifest = _read_json(manifest_path)
        for source in manifest.get("source_records", []):
            rows.append(_row(manifest_path, manifest, source))
    rows.sort(key=lambda row: (row["manifest_path"], row["source_record_id"]))

    def count(field: str, value: str) -> int:
        return sum(row[field] == value for row in rows)

    return {
        "$schema": "./UNI_EVIDENCE_LICENSE_MATRIX_G11_B_SCHEMA.json",
        "schema_version": "G11-B-evidence-license-matrix",
        "matrix_id": "G11-B-evidence-license",
        "metadata_only": True,
        "observed_at": OBSERVED_AT,
        "scope": {
            "input_manifests": [path.as_posix() for path in INPUT_MANIFESTS],
            "record_scope": "Ogni elemento source_records dei manifest G5 e G10 presenti nel checkout.",
            "excluded_payloads": [
                "testo XML/HTML/PDF e altri payload delle fonti",
                "schede, domande, risposte e soluzioni d'esame",
                "record normalizzati con chiave records che non sono source_records",
            ],
            "verification_policy": "Questa matrice non esegue richieste live: lo stato massimo è observed_local; le lacune restano blocked.",
            "claim_policy": "Nessun record della matrice è claim-ready; la Direttiva (UE) 2024/1275 resta metadata-only.",
        },
        "summary": {
            "record_count": len(rows),
            "claim_ready_count": sum(row["claim_ready"] for row in rows),
            "by_locator_status": {"observed_local": count("locator_status", "observed_local"), "blocked": count("locator_status", "blocked")},
            "by_official_context_status": {"observed_local": count("official_context_status", "observed_local"), "blocked": count("official_context_status", "blocked")},
            "by_license_status": {"observed_local": count("license_status", "observed_local"), "blocked": count("license_status", "blocked")},
            "by_evidence_status": {"observed_local": count("evidence_status", "observed_local"), "blocked": count("evidence_status", "blocked")},
            "blocker_count": len(rows),
        },
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()
    report = build_matrix()
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
