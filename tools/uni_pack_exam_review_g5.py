"""Build a deterministic human-review queue from the G4 pack/exam map.

The queue is deliberately observational.  It carries G4's name/documentation
signals and uncertainty classifications into explicit review items, but never
chooses a canonical pack/exam association or infers semantic equivalence.

Usage::

    python tools/uni_pack_exam_review_g5.py
    python tools/uni_pack_exam_review_g5.py --root . \
        --output docs/coordination/UNI_PACK_EXAM_REVIEW_G5.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

try:
    from tools.uni_pack_exam_map_g4 import REPORT_RELATIVE_PATH as G4_REPORT_PATH
    from tools.uni_pack_exam_map_g4 import build_report as build_g4_report
except ModuleNotFoundError:
    from uni_pack_exam_map_g4 import REPORT_RELATIVE_PATH as G4_REPORT_PATH
    from uni_pack_exam_map_g4 import build_report as build_g4_report


REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_PACK_EXAM_REVIEW_G5.json")
QUEUE_CLASSIFICATIONS = {
    "pack": frozenset({"ambiguous"}),
    "exam": frozenset({"ambiguous", "unmatched_exam"}),
}


def _sorted_candidates(
    candidates: Iterable[dict[str, object]],
    identifier: str,
) -> list[dict[str, object]]:
    return sorted(candidates, key=lambda item: str(item[identifier]).casefold())


def _candidate_snapshot(
    candidate: dict[str, object],
    identifier: str,
    records_by_id: dict[str, dict[str, object]],
) -> dict[str, object]:
    candidate_id = str(candidate[identifier])
    source = records_by_id[candidate_id]
    return {
        identifier: candidate_id,
        "relation": candidate["relation"],
        "evidence": candidate["evidence"],
        "source_files": source["source_files"],
    }


def _queue_item(
    *,
    item_type: str,
    record: dict[str, object],
    records_by_id: dict[str, dict[str, object]],
) -> dict[str, object]:
    if item_type == "pack":
        identifier = "exam_id"
        item_id = str(record["pack_id"])
        candidates = _sorted_candidates(record["candidate_exams"], identifier)  # type: ignore[arg-type]
        candidate_ids = [str(item[identifier]) for item in candidates]
        is_legacy = False
        uncertainty = "ambiguous_observed_candidates"
        review_reason = "More than one observed exam candidate remains for this pack."
        review_prompt = (
            "Confirm one candidate only with explicit human/source evidence, "
            "or keep the pack unresolved; do not infer semantic equivalence."
        )
        allowed_outcomes = [
            "associate_with_explicit_evidence",
            "keep_unresolved",
            "defer",
        ]
        priority = 1
    else:
        identifier = "pack_id"
        item_id = str(record["exam_id"])
        candidates = _sorted_candidates(record["candidate_packs"], identifier)  # type: ignore[arg-type]
        candidate_ids = [str(item[identifier]) for item in candidates]
        is_legacy = bool(record.get("legacy_observed", False))
        if record["classification"] == "ambiguous":
            uncertainty = "ambiguous_observed_candidates"
            review_reason = "More than one observed pack candidate remains for this exam."
            review_prompt = (
                "Confirm one candidate only with explicit human/source evidence, "
                "or keep the exam unresolved; do not infer semantic equivalence."
            )
            allowed_outcomes = [
                "associate_with_explicit_evidence",
                "keep_unresolved",
                "defer",
            ]
            priority = 1
        else:
            uncertainty = "unmatched_legacy_domain"
            review_reason = "The exam is explicitly legacy and has no observed pack candidate."
            review_prompt = (
                "Locate explicit source/documentation evidence for an association, "
                "or retain it as unmatched; no name-only fallback is allowed."
            )
            allowed_outcomes = [
                "associate_with_explicit_evidence",
                "keep_unmatched",
                "defer",
            ]
            priority = 2

    return {
        "queue_id": f"{item_type}:{item_id}",
        "item_type": item_type,
        "item_id": item_id,
        "classification": record["classification"],
        "uncertainty": uncertainty,
        "legacy_observed": is_legacy,
        "review_priority": priority,
        "review_reason": review_reason,
        "review_prompt": review_prompt,
        "source_files": record["source_files"],
        "candidate_ids": candidate_ids,
        "observed_candidates": [
            _candidate_snapshot(item, identifier, records_by_id) for item in candidates
        ],
        "review_status": "pending",
        "allowed_outcomes": allowed_outcomes,
        "decision": {
            "outcome": None,
            "selected_id": None,
            "reviewer_note": None,
        },
    }


def build_review_report(root: Path) -> dict[str, object]:
    root = root.resolve()
    g4 = build_g4_report(root)
    packs = [entry for entry in g4["packs"] if isinstance(entry, dict)]  # type: ignore[index]
    exams = [entry for entry in g4["exams"] if isinstance(entry, dict)]  # type: ignore[index]
    packs_by_id = {str(entry["pack_id"]): entry for entry in packs}
    exams_by_id = {str(entry["exam_id"]): entry for entry in exams}

    queue: list[dict[str, object]] = []
    for record in packs:
        if record["classification"] in QUEUE_CLASSIFICATIONS["pack"]:
            queue.append(
                _queue_item(item_type="pack", record=record, records_by_id=exams_by_id)
            )
    for record in exams:
        if (
            record["classification"] in QUEUE_CLASSIFICATIONS["exam"]
            and (
                record["classification"] == "ambiguous"
                or bool(record.get("legacy_observed", False))
            )
        ):
            queue.append(
                _queue_item(item_type="exam", record=record, records_by_id=packs_by_id)
            )

    item_type_order = {"pack": 0, "exam": 1}
    queue.sort(
        key=lambda item: (
            int(item["review_priority"]),
            item_type_order[str(item["item_type"])],
            str(item["item_id"]).casefold(),
        )
    )
    for order, item in enumerate(queue, start=1):
        item["queue_order"] = order

    counts = {
        "queue_items": len(queue),
        "ambiguous_pack": sum(
            item["item_type"] == "pack" and item["classification"] == "ambiguous"
            for item in queue
        ),
        "ambiguous_exam": sum(
            item["item_type"] == "exam" and item["classification"] == "ambiguous"
            for item in queue
        ),
        "legacy_unmatched_exam": sum(
            item["item_type"] == "exam"
            and item["classification"] == "unmatched_exam"
            and item["legacy_observed"]
            for item in queue
        ),
        "pending": sum(item["review_status"] == "pending" for item in queue),
    }
    return {
        "schema_version": "g5.v1",
        "tool": "tools/uni_pack_exam_review_g5.py",
        "source_report": {
            "path": G4_REPORT_PATH.as_posix(),
            "schema_version": g4["schema_version"],
            "counts": g4["counts"],
        },
        "scope": {
            "queue_selection": [
                "pack records classified ambiguous by G4",
                "exam records classified ambiguous by G4",
                "exam records classified unmatched_exam with legacy_observed=true",
            ],
            "source_of_truth": "selected checkout filesystem through the G4 report",
            "content_modified": False,
        },
        "method": {
            "ordering": "review_priority ascending, item type pack before exam, then stable casefolded item_id",
            "pending_state": "every generated item starts with review_status=pending and null decision",
            "semantic_inference": False,
            "canonical_association": "never assigned by this tool",
        },
        "counts": counts,
        "review_queue": queue,
        "boundaries": [
            "Queue entries are review work items, not accepted pack/exam mappings.",
            "Candidate IDs and evidence are observed name/documentation signals only.",
            "Ambiguous records retain classification=ambiguous and list every observed candidate.",
            "Legacy unmatched records retain legacy_observed=true and candidate_ids=[].",
            "A decision.selected_id stays null until a human supplies explicit evidence.",
            "No semantic fallback, question content, answers, or source content is used.",
            "No corpus file is edited, merged, moved, overwritten, or deleted.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=REPORT_RELATIVE_PATH)
    args = parser.parse_args()

    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(build_review_report(root), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {output}")


if __name__ == "__main__":
    main()
