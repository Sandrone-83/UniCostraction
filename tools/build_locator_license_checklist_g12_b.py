"""Build the deterministic, metadata-only G12-B locator/licence checklist."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "docs" / "coordination" / "UNI_LOCATOR_LICENSE_CHECKLIST_G12_B.json"
INPUT_MANIFESTS = (
    Path("docs/coordination/UNI_CORPUS_LOTTO_G5_ECFR.json"),
    Path("docs/coordination/UNI_CORPUS_LOTTO_G10_B.json"),
)
OBSERVED_AT = "2026-10-18"
SOURCE_COMMIT = "5609b4eb965e4b45d4520a563f2403b1f9fce980"


def _read_json(relative_path: Path) -> dict[str, Any]:
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


def _context_for(manifest: dict[str, Any], source_id: str) -> dict[str, Any] | None:
    return next(
        (item for item in manifest.get("official_context_records", []) if item.get("related_source_record_id") == source_id),
        None,
    )


def _license_for(manifest: dict[str, Any], source: dict[str, Any]) -> dict[str, Any] | None:
    if source.get("license_reuse") is not None:
        return source["license_reuse"]
    source_id = source["source_record_id"]
    return next(
        (item for item in manifest.get("license_records", []) if item.get("related_source_record_id") == source_id),
        None,
    )


def _locator(source: dict[str, Any]) -> str | None:
    source_data = source.get("source", {})
    return source_data.get("official_url") or source_data.get("url")


def _observation(*, state: str, value: bool | None, live_check: str, basis: str, refs: list[str]) -> dict[str, Any]:
    return {
        "state": state,
        "value": value,
        "live_check": live_check,
        "basis": basis,
        "evidence_refs": refs,
    }


def _row(manifest_path: Path, manifest: dict[str, Any], source: dict[str, Any]) -> dict[str, Any]:
    source_id = source["source_record_id"]
    locator = _locator(source)
    context = _context_for(manifest, source_id)
    context_url = context.get("url") if context else None
    license_record = _license_for(manifest, source)
    license_url = license_record.get("url") if license_record else None
    refs = list(dict.fromkeys(ref for ref in (locator, context_url, license_url) if ref))

    if source_id == "G5-001":
        locator_observation = _observation(
            state="observed_local",
            value=True,
            live_check="blocked",
            basis=(
                "Il locator esatto è presente nel record e nei registri locali; il controllo live del contenuto "
                "dell'endpoint è rimasto bloccato dalla dimensione della risposta."
            ),
            refs=refs,
        )
        context_observation = _observation(
            state="observed_local",
            value=True,
            live_check="blocked",
            basis=(
                "Il contesto ufficiale è registrato localmente sul locator eCFR; non è stata ottenuta una "
                "osservazione live completa della pagina esatta."
            ),
            refs=refs,
        )
        license_observation = _observation(
            state="observed_local",
            value=True,
            live_check="blocked",
            basis=(
                "La dichiarazione public-domain è associata localmente al record OSHA-1926 tramite il registro; "
                "non è una clearance legale indipendente e i termini source-specific non sono stati controllati live."
            ),
            refs=refs + ["Edilizia_Pack/licenze_audit.json", "Edilizia_Pack/manifest.json"],
        )
        blocker_codes = [
            "exact_locator_live_check_blocked",
            "official_context_live_check_blocked",
            "source_specific_license_terms_live_not_checked",
            "independent_legal_clearance_required",
            "claim_not_ready",
        ]
        blocker_reason = (
            "Il locator e la dichiarazione di licenza sono osservati localmente; la verifica live dell'endpoint "
            "e la clearance legale indipendente non sono disponibili, quindi non è consentita alcuna promozione."
        )
    else:
        locator_observation = _observation(
            state="observed_live",
            value=True,
            live_check="passed",
            basis="Il locator ELI ufficiale EUR-Lex è stato raggiunto e ha esposto il documento 32024L1275.",
            refs=refs,
        )
        context_observation = _observation(
            state="observed_live",
            value=True,
            live_check="passed",
            basis="La pagina ufficiale EUR-Lex di contesto riuso è stata raggiunta e osservata.",
            refs=refs,
        )
        license_observation = _observation(
            state="blocked",
            value=False,
            live_check="passed",
            basis=(
                "Il contesto live EUR-Lex richiama riuso gratuito soggetto a condizioni di copyright, ma non "
                "stabilisce una licenza source-specific per questo atto."
            ),
            refs=refs,
        )
        blocker_codes = [
            "source_specific_license_not_established",
            "official_context_is_not_source_license",
            "independent_legal_clearance_required",
            "claim_not_ready",
        ]
        blocker_reason = (
            "Il locator e il contesto ufficiale sono stati osservati live, ma il contesto di riuso non è una "
            "licenza source-specific; la clearance legale resta richiesta e il record non è claim-ready."
        )

    return {
        "record_key": f"{manifest_path.as_posix()}#{source_id}",
        "manifest_path": manifest_path.as_posix(),
        "manifest_id": manifest["manifest_id"],
        "source_record_id": source_id,
        "source_kind": source["source_kind"],
        "title": source["title"],
        "locator_reachable_observed": locator_observation,
        "official_context_observed": context_observation,
        "license_source_specific": license_observation,
        "legal_clearance_required": {
            "required": True,
            "state": "required",
            "basis": "La catalogazione metadata-only non sostituisce la verifica dei diritti e della clearance per l'uso previsto.",
        },
        "claim_ready": False,
        "blocker": {
            "state": "blocked",
            "codes": blocker_codes,
            "reason": blocker_reason,
            "promotion_forbidden": True,
        },
    }


def build_checklist() -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    for manifest_path in INPUT_MANIFESTS:
        manifest = _read_json(manifest_path)
        for source in manifest.get("source_records", []):
            records.append(_row(manifest_path, manifest, source))
    records.sort(key=lambda row: (row["manifest_path"], row["source_record_id"]))

    def count_state(field: str, state: str) -> int:
        return sum(item[field]["state"] == state for item in records)

    return {
        "$schema": "./UNI_LOCATOR_LICENSE_CHECKLIST_G12_B_SCHEMA.json",
        "schema_version": "G12-B-locator-license-checklist",
        "checklist_id": "G12-B-locator-license",
        "metadata_only": True,
        "observed_at": OBSERVED_AT,
        "source_commit": SOURCE_COMMIT,
        "scope": {
            "input_manifests": [path.as_posix() for path in INPUT_MANIFESTS],
            "record_scope": "Ogni elemento source_records dei manifest G5 e G10 presenti nel checkout G11.",
            "excluded_payloads": [
                "testo XML/HTML/PDF e altri payload delle fonti",
                "schede, domande, risposte e soluzioni d'esame",
                "qualsiasi trasformazione o modifica dei file sorgente",
            ],
            "live_verification_policy": "Registrare solo esiti live effettivamente osservati; se il controllo non è disponibile, conservare blocked o observed_local.",
            "promotion_policy": "Nessun campo claim_ready può diventare true; contesto ufficiale e raggiungibilità non sono licenza né clearance legale.",
        },
        "summary": {
            "record_count": len(records),
            "claim_ready_count": sum(item["claim_ready"] for item in records),
            "legal_clearance_required_count": sum(item["legal_clearance_required"]["required"] for item in records),
            "by_locator_reachable_state": {state: count_state("locator_reachable_observed", state) for state in ("observed_live", "observed_local", "blocked")},
            "by_official_context_state": {state: count_state("official_context_observed", state) for state in ("observed_live", "observed_local", "blocked")},
            "by_license_source_specific_state": {state: count_state("license_source_specific", state) for state in ("observed_live", "observed_local", "blocked")},
            "blocker_count": len(records),
        },
        "records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()
    args.output.write_text(json.dumps(build_checklist(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
