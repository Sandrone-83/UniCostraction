"""Build the deterministic, metadata-only G13-B pack provenance coverage audit."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
COURSE_ROOT = Path("UNIVERSITA_EDILIZIA")
COURSE_GLOB = "COURSE.yaml"
OUTPUT_PATH = ROOT / "docs" / "coordination" / "UNI_PACK_PROVENANCE_COVERAGE_G13_B.json"
INPUT_MANIFESTS = (
    Path("docs/coordination/UNI_CORPUS_LOTTO_G1.json"),
    Path("Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json"),
    Path("UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/fonti/PROVENANCE_MANIFEST_G3_GSE_CT3.json"),
    Path("docs/coordination/UNI_CORPUS_LOTTO_G5_ECFR.json"),
    Path("docs/coordination/UNI_CORPUS_LOTTO_G10_B.json"),
)
OBSERVED_AT = "2026-10-18"
BASE_COMMIT = "5563510cbf40c1e2a5476cb64be845947c68e710"

OBSERVED_LOCAL = "observed_local"
BLOCKED = "blocked"


def _read_json(relative_path: Path) -> dict[str, Any]:
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


def _normalise_path(value: str | None) -> str | None:
    if not value:
        return None
    return value.replace("\\", "/").strip("/")


def _yaml_scalar(text: str) -> str | None:
    value = text.strip()
    if not value:
        return None
    if value[0] in {'"', "'"} and value[-1:] == value[0]:
        return value[1:-1]
    return value


def _read_course_metadata(path: Path) -> dict[str, Any]:
    course_name: str | None = None
    sources_present = False
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\s*corso\s*:\s*(.*?)\s*$", line)
        if match:
            course_name = _yaml_scalar(match.group(1))
        if re.match(r"^\s*fonti\s*:", line):
            sources_present = True
    if not course_name:
        raise ValueError(f"COURSE.yaml lacks a scalar corso field: {path}")
    return {
        "course_name": course_name,
        "fonti_field_present": sources_present,
    }


def _record_container(manifest: dict[str, Any]) -> tuple[str, list[dict[str, Any]]]:
    if isinstance(manifest.get("source_records"), list):
        return "source_records", manifest["source_records"]
    if isinstance(manifest.get("records"), list):
        return "records", manifest["records"]
    return "none", []


def _record_id(record: dict[str, Any]) -> str | None:
    return record.get("source_record_id") or record.get("record_id")


def _record_paths(record: dict[str, Any]) -> list[str]:
    values: list[str] = []
    locator = record.get("locator")
    if isinstance(locator, dict) and isinstance(locator.get("path"), str):
        values.append(locator["path"])
    source = record.get("source")
    if isinstance(source, dict):
        for key in ("local_path", "source_path"):
            if isinstance(source.get(key), str):
                values.append(source[key])
    return [normalised for value in values if (normalised := _normalise_path(value))]


def _matches_pack(manifest: dict[str, Any], record: dict[str, Any], pack_path: str) -> tuple[bool, str | None]:
    scope = manifest.get("scope")
    if isinstance(scope, dict):
        package = _normalise_path(scope.get("package"))
        if package == pack_path:
            return True, "scope.package_exact"
        source_path = _normalise_path(scope.get("source_path"))
        if source_path and (source_path == pack_path or source_path.startswith(f"{pack_path}/")):
            return True, "scope.source_path_under_pack"
    for path in _record_paths(record):
        if path == pack_path or path.startswith(f"{pack_path}/"):
            return True, "record.locator.path_under_pack"
    return False, None


def _has_locator(record: dict[str, Any]) -> bool:
    locator = record.get("locator")
    if isinstance(locator, dict):
        return any(isinstance(locator.get(key), str) and locator[key].strip() for key in ("path", "url"))
    source = record.get("source")
    return isinstance(source, dict) and any(
        isinstance(source.get(key), str) and source[key].strip()
        for key in ("local_path", "official_url", "url")
    )


def _license_is_declared(record: dict[str, Any]) -> bool:
    license_data = record.get("license_reuse") or record.get("license")
    if not isinstance(license_data, dict):
        return False
    status = license_data.get("status")
    return status not in {None, "not_declared", "blocked"} and any(
        isinstance(license_data.get(key), str) and license_data[key].strip()
        for key in ("label", "local_statement", "basis_path", "url")
    )


def _evidence_is_observed_local(record: dict[str, Any]) -> bool:
    verification = record.get("verification_status")
    return isinstance(verification, dict) and verification.get("state") == OBSERVED_LOCAL


def _status_for_matches(matches: list[dict[str, Any]], predicate: Any) -> str:
    return OBSERVED_LOCAL if matches and all(predicate(item["record"]) for item in matches) else BLOCKED


def _load_manifest_records() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    records: list[dict[str, Any]] = []
    inventory: list[dict[str, Any]] = []
    for manifest_path in INPUT_MANIFESTS:
        manifest = _read_json(manifest_path)
        container, manifest_records = _record_container(manifest)
        manifest_id = manifest.get("manifest_id") or manifest.get("lot_id")
        inventory.append(
            {
                "manifest_path": manifest_path.as_posix(),
                "manifest_id": manifest_id,
                "record_container": container,
                "record_count": len(manifest_records),
                "scope_package": (
                    _normalise_path(manifest.get("scope", {}).get("package"))
                    if isinstance(manifest.get("scope"), dict)
                    else None
                ),
            }
        )
        for record in manifest_records:
            source_id = _record_id(record)
            if not source_id:
                raise ValueError(f"Manifest record without source_record_id/record_id: {manifest_path}")
            records.append(
                {
                    "manifest_path": manifest_path.as_posix(),
                    "manifest_id": manifest_id,
                    "source_record_id": source_id,
                    "record": record,
                }
            )
    return records, inventory


def _pack_row(course_path: Path, manifest_records: list[dict[str, Any]]) -> dict[str, Any]:
    relative_course = course_path.relative_to(ROOT).as_posix()
    pack_path = course_path.parent.relative_to(ROOT).as_posix()
    metadata = _read_course_metadata(course_path)
    matches: list[dict[str, Any]] = []
    for item in manifest_records:
        matched, basis = _matches_pack(item["record"].get("_manifest", {}), item["record"], pack_path)
        if matched:
            matches.append({**item, "match_basis": basis})

    source_record_present = OBSERVED_LOCAL if matches else BLOCKED
    locator_present = _status_for_matches(matches, _has_locator)
    license_status = _status_for_matches(matches, _license_is_declared)
    evidence_status = _status_for_matches(matches, _evidence_is_observed_local)

    remediation_codes: list[str] = []
    if source_record_present == BLOCKED:
        remediation_codes.append("source_record_missing_for_pack")
    if locator_present == BLOCKED:
        remediation_codes.append("locator_missing_or_not_present_for_all_matched_records")
    if license_status == BLOCKED:
        remediation_codes.append("source_specific_license_not_declared")
    if evidence_status == BLOCKED:
        remediation_codes.append("evidence_not_observed_local_for_all_matched_records")

    return {
        "pack_id": course_path.parent.name,
        "pack_path": pack_path,
        "course_yaml": relative_course,
        "course_name": metadata["course_name"],
        "fonti_field_present": metadata["fonti_field_present"],
        "source_record_present": source_record_present,
        "locator_present": locator_present,
        "license_status": license_status,
        "evidence_status": evidence_status,
        "remediation_required": bool(remediation_codes),
        "remediation_codes": remediation_codes,
        "matched_source_records": [
            {
                "manifest_path": item["manifest_path"],
                "manifest_id": item["manifest_id"],
                "source_record_id": item["source_record_id"],
                "match_basis": item["match_basis"],
            }
            for item in sorted(matches, key=lambda value: (value["manifest_path"], value["source_record_id"]))
        ],
        "matching_note": (
            "Match uses only explicit manifest scope/local path metadata; COURSE.yaml fonti, titles, and text similarity "
            "are not used to establish provenance."
        ),
    }


def _count(rows: list[dict[str, Any]], field: str, value: str) -> int:
    return sum(row[field] == value for row in rows)


def build_audit() -> dict[str, Any]:
    courses = sorted((ROOT / COURSE_ROOT).rglob(COURSE_GLOB), key=lambda path: path.relative_to(ROOT).as_posix())
    manifest_records, manifest_inventory = _load_manifest_records()
    manifest_records_with_context: list[dict[str, Any]] = []
    manifests_by_path = {item["manifest_path"]: _read_json(Path(item["manifest_path"])) for item in manifest_inventory}
    for item in manifest_records:
        manifest_records_with_context.append({**item, "record": {**item["record"], "_manifest": manifests_by_path[item["manifest_path"]]}})
    rows = [_pack_row(course, manifest_records_with_context) for course in courses]
    rows.sort(key=lambda row: row["pack_path"])
    matched_pack_count = sum(bool(row["matched_source_records"]) for row in rows)
    return {
        "$schema": "./UNI_PACK_PROVENANCE_COVERAGE_G13_B_SCHEMA.json",
        "schema_version": "G13-B-pack-provenance-coverage",
        "audit_id": "G13-B-pack-provenance-coverage",
        "metadata_only": True,
        "observed_at": OBSERVED_AT,
        "base_commit": BASE_COMMIT,
        "scope": {
            "course_root": COURSE_ROOT.as_posix(),
            "course_glob": f"{COURSE_ROOT.as_posix()}/**/{COURSE_GLOB}",
            "expected_course_count": 71,
            "input_manifests": [path.as_posix() for path in INPUT_MANIFESTS],
            "manifest_record_scope": "Manifest records and source_records explicitly present in the listed local manifests.",
            "matching_policy": "Only exact manifest scope.package, scope.source_path, or record locator/local path under the pack path establishes a match.",
            "no_semantic_matching": "COURSE.yaml fonti, course names, titles, document topics, and text similarity are never used for matching.",
            "excluded_payloads": [
                "COURSE.yaml source text beyond the observed fonti-field presence",
                "schede JSONL and course-card payloads",
                "PDF, XML, HTML, source text, exam questions, answers, and solutions",
                "live URL requests or current license/legal verification",
            ],
            "state_policy": "The audit emits only observed_local or blocked; missing or insufficient evidence is never promoted.",
        },
        "manifest_inventory": manifest_inventory,
        "summary": {
            "pack_count": len(rows),
            "manifest_record_count": len(manifest_records),
            "matched_pack_count": matched_pack_count,
            "unmatched_pack_count": len(rows) - matched_pack_count,
            "by_source_record_present": {OBSERVED_LOCAL: _count(rows, "source_record_present", OBSERVED_LOCAL), BLOCKED: _count(rows, "source_record_present", BLOCKED)},
            "by_locator_present": {OBSERVED_LOCAL: _count(rows, "locator_present", OBSERVED_LOCAL), BLOCKED: _count(rows, "locator_present", BLOCKED)},
            "by_license_status": {OBSERVED_LOCAL: _count(rows, "license_status", OBSERVED_LOCAL), BLOCKED: _count(rows, "license_status", BLOCKED)},
            "by_evidence_status": {OBSERVED_LOCAL: _count(rows, "evidence_status", OBSERVED_LOCAL), BLOCKED: _count(rows, "evidence_status", BLOCKED)},
            "remediation_required_count": sum(row["remediation_required"] for row in rows),
        },
        "packs": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()
    report = build_audit()
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
