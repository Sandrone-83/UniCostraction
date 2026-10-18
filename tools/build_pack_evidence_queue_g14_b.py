"""Build the deterministic, metadata-only G14-B pack evidence queue.

The queue is intentionally conservative: it contains only the G13-B packs
without an explicit source-record match.  It copies no source payloads, does
not infer provenance from course text or names, and does not grant legal
clearance.  Source, interpretation, context, and legal clearance remain
separate machine-readable sections in every item.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
G13_REPORT = Path("docs/coordination/UNI_PACK_PROVENANCE_COVERAGE_G13_B.json")
QUEUE_REPORT = Path("docs/coordination/UNI_PACK_EVIDENCE_QUEUE_G14_B.json")

QUEUE_SCHEMA_VERSION = "G14-B-pack-evidence-queue"
QUEUE_ID = "G14-B-pack-evidence-queue"
SOURCE_AUDIT_ID = "G13-B-pack-provenance-coverage"
SOURCE_COMMIT = "7bdaa0a33260fb5380f02f0a8b41ec6e625a1b44"
OBSERVED_AT = "2026-10-18"

EVIDENCE_REQUIRED = (
    "An explicit source record identifies the source_record_id, exact title, version or date, language, and rights holder.",
    "The source evidence artifact or an explicitly permitted local evidence reference is registered without copying protected payloads into this queue.",
    "The evidence identity is reproducible through a declared hash or equivalent immutable proof and an observation date/method.",
    "Each material claim has an explicit source-record relationship; evidence is not inferred from course text, titles, topics, or similarity.",
)
LOCATOR_REQUIRED = (
    "An exact official URL or exact local path is declared for the source evidence.",
    "A stable page, section, table, anchor, fragment, or record locator identifies the relevant evidence when the source format supports it.",
    "The locator has an observation/retrieval date and is tied to the declared source version and territory.",
    "A locator is not treated as proof of content accuracy, licence, or legal clearance by itself.",
)
LICENSE_PROOF_REQUIRED = (
    "Source-specific licence, terms, public-domain basis, or written permission is identified by an exact URL/path or retained proof reference.",
    "Rights holder, attribution, commercial use, modification, redistribution, scraping, ShareAlike/copyleft, NC/ND, and exclusions are recorded where applicable.",
    "A proof snapshot or hash makes the licence evidence reproducible and preserves its scope, version, territory, and observation date.",
    "Any unresolved rights question remains blocked and is not converted into a claim-ready or reuse-approved state.",
)

INTERPRETATION_REQUIREMENTS = (
    "Keep source wording and source metadata separate from interpretation, summaries, examples, hypotheses, and educational claims.",
    "Require a human-reviewed claim-to-source mapping based on explicit source-record metadata; semantic similarity is not an admissible mapping basis.",
)
CONTEXT_REQUIREMENTS = (
    "Record official context, jurisdiction/territory, version, date, vigency, and applicable domain separately from the source record.",
    "Context may explain provenance but cannot substitute for source evidence, an exact locator, licence proof, or legal clearance.",
)
LEGAL_CLEARANCE_REQUIREMENTS = (
    "Obtain an independent rights/legal review for the exact source, attachments, images, code, documentation, and data scope that may be retained or reused.",
    "Record the reviewer or approval authority, decision date, decision scope, and any attribution, exclusion, or use restriction.",
    "Do not mark the pack claim-ready, commercially reusable, or legally cleared from this queue alone.",
)

CLOSURE_CRITERIA = (
    ("source-record", "At least one explicit source record is supplied for every source actually used by the pack, with stable identity and pack relationship."),
    ("evidence", "Required evidence is supplied, identity-matched, hashable or otherwise reproducible, and observed without altering the source content."),
    ("locator", "Every source record has an exact URL or local path plus a stable locator and version/territory observation metadata."),
    ("license-proof", "Source-specific licence or permission proof is supplied with rights scope, restrictions, attribution, and reproducible proof reference."),
    ("interpretation", "Interpretation is stored separately and reviewed by a human; no semantic or similarity-based mapping is used."),
    ("context", "Official context is stored separately and does not replace source, locator, or licence evidence."),
    ("legal-clearance", "Independent legal clearance is recorded for the exact intended retention/reuse scope, or the material is explicitly reference-only."),
    ("queue-recheck", "Regenerating G13-B/G14-B from the resulting metadata removes this pack from the missing-source-record queue without modifying source/content files."),
)


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return value


def _source_audit(g13: dict[str, Any]) -> dict[str, Any]:
    if g13.get("audit_id") != SOURCE_AUDIT_ID:
        raise ValueError("G13 report has an unexpected audit_id")
    return {
        "audit_id": SOURCE_AUDIT_ID,
        "report": G13_REPORT.as_posix(),
        "report_base_commit": g13.get("base_commit"),
        "queue_source_commit": SOURCE_COMMIT,
    }


def _closure_rows() -> list[dict[str, Any]]:
    return [
        {
            "criterion_id": criterion_id,
            "requirement": requirement,
            "status": "pending",
            "evidence_ref": None,
        }
        for criterion_id, requirement in CLOSURE_CRITERIA
    ]


def _item(pack: dict[str, Any]) -> dict[str, Any]:
    if pack.get("matched_source_records"):
        raise ValueError(f"Pack is not eligible for the G14-B missing-record queue: {pack['pack_id']}")
    if pack.get("source_record_present") != "blocked":
        raise ValueError(f"Pack does not have blocked source-record state: {pack['pack_id']}")

    pack_id = pack["pack_id"]
    return {
        "queue_item_id": f"G14-B-{pack_id}",
        "pack_id": pack_id,
        "pack_path": pack["pack_path"],
        "course_yaml": pack["course_yaml"],
        "status": "blocked",
        "source": {
            "source_record_status": "missing_explicit_record",
            "evidence_required": list(EVIDENCE_REQUIRED),
            "locator_required": list(LOCATOR_REQUIRED),
            "license_proof_required": list(LICENSE_PROOF_REQUIRED),
        },
        "interpretation": {
            "status": "separate_and_pending",
            "human_review_required": True,
            "automatic_semantic_mapping_prohibited": True,
            "requirements": list(INTERPRETATION_REQUIREMENTS),
        },
        "context": {
            "status": "separate_and_pending",
            "requirements": list(CONTEXT_REQUIREMENTS),
        },
        "legal_clearance": {
            "status": "required",
            "independent_review_required": True,
            "requirements": list(LEGAL_CLEARANCE_REQUIREMENTS),
        },
        "blocked": {
            "state": "blocked",
            "reason": "G13-B has no explicit source record matched to this pack by exact manifest scope or local-path metadata; evidence, locator, source-specific licence proof, and legal clearance are therefore unproven.",
            "codes": [
                "source_record_missing_for_pack",
                "evidence_not_observed_for_pack",
                "locator_not_observed_for_pack",
                "license_proof_not_observed_for_pack",
                "interpretation_not_authorized",
                "context_not_substitutive",
                "legal_clearance_required",
            ],
            "promotion_forbidden": True,
        },
        "closure_criteria": _closure_rows(),
        "automatic_semantic_mapping_prohibited": True,
        "constraints": [
            "Do not modify source files, source payloads, course cards, exam files, or pack content.",
            "Do not create a source relationship from COURSE.yaml fonti, course names, titles, topics, or text similarity.",
            "Do not infer a licence, permission, current validity, factual accuracy, or legal status from availability or context.",
            "Do not promote any blocked field to observed, verified, claim-ready, commercially reusable, or legally cleared in this queue.",
        ],
    }


def build_queue() -> dict[str, Any]:
    g13 = load_json(ROOT / G13_REPORT)
    packs = g13.get("packs")
    if not isinstance(packs, list):
        raise ValueError("G13 report lacks a packs array")
    unmatched = [pack for pack in packs if not pack.get("matched_source_records")]
    unmatched.sort(key=lambda pack: pack["pack_path"])
    if len(unmatched) != 70:
        raise ValueError(f"Expected exactly 70 unmatched G13-B packs, found {len(unmatched)}")

    items = [_item(pack) for pack in unmatched]
    return {
        "$schema": "./UNI_PACK_EVIDENCE_QUEUE_G14_B_SCHEMA.json",
        "schema_version": QUEUE_SCHEMA_VERSION,
        "queue_id": QUEUE_ID,
        "metadata_only": True,
        "observed_at": OBSERVED_AT,
        "source_commit": SOURCE_COMMIT,
        "source_audit": _source_audit(g13),
        "scope": {
            "input_report": G13_REPORT.as_posix(),
            "included_pack_count": 70,
            "selection_rule": "Include exactly the G13-B pack rows whose matched_source_records array is empty; exclude the one explicitly matched pack.",
            "matching_policy": "Only an explicit source-record relationship from manifest scope or local-path metadata is admissible; this queue does not create one.",
            "no_semantic_mapping": "Automatic mapping by COURSE.yaml fonti, course name, title, topic, text similarity, or presumed subject correspondence is prohibited.",
            "excluded_payloads": [
                "COURSE.yaml content beyond the already observed pack identifiers and paths",
                "schede JSONL, course-card payloads, exam questions, answers, and solutions",
                "PDF, XML, HTML, manuals, standards, prices, manufacturer data, and source text",
                "live URL requests, current-vigency checks, and legal opinions",
            ],
            "separation_policy": {
                "source": "Source record and source evidence identify what the source is; they do not contain interpretation or legal clearance.",
                "interpretation": "Interpretation is a separate human-reviewed layer and never establishes provenance by semantic similarity.",
                "context": "Official context, territory, version, and vigency are recorded separately and do not prove licence or source accuracy.",
                "legal_clearance": "Legal clearance is an independent required decision for the exact intended use and is never implied by a source record, locator, or context.",
                "automatic_semantic_mapping": "prohibited",
            },
        },
        "summary": {
            "item_count": len(items),
            "blocked_count": len(items),
            "closure_ready_count": 0,
            "by_status": {"blocked": len(items)},
            "by_blocker_code": {code: len(items) for code in items[0]["blocked"]["codes"]},
        },
        "items": items,
        "closure_checklist": [
            {
                "criterion_id": criterion_id,
                "requirement": requirement,
                "status": "pending",
                "evidence_ref": None,
            }
            for criterion_id, requirement in CLOSURE_CRITERIA
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / QUEUE_REPORT)
    args = parser.parse_args()
    report = build_queue()
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
