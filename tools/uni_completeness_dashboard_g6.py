"""Build a deterministic global completeness dashboard for UniCostraction.

The dashboard is an observational aggregate of the university pack/card
filesystem, the G4 pack/exam map, and the G5 human-review queue.  It keeps
observed counts, alias signals, unmatched records, and human-pending records
in separate fields.  It never changes corpus content and never turns a
pending or unmatched record into a completed association.

Usage::

    python tools/uni_completeness_dashboard_g6.py
    python tools/uni_completeness_dashboard_g6.py --root . \
        --output docs/coordination/UNI_COMPLETENESS_DASHBOARD_G6.json
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Iterable

try:
    from tools.uni_pack_exam_map_g4 import build_report as build_g4_report
    from tools.uni_pack_exam_review_g5 import build_review_report
except ModuleNotFoundError:
    from uni_pack_exam_map_g4 import build_report as build_g4_report
    from uni_pack_exam_review_g5 import build_review_report


REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_COMPLETENESS_DASHBOARD_G6.json")
PACK_ROOT = Path("UNIVERSITA_EDILIZIA")
PACK_SUFFIX = "_PACK"
SCHEDE_RE = re.compile(r"^\s*schede\s*:\s*(\d+)\s*$", re.IGNORECASE)


def _corpus_pack_root(root: Path) -> Path:
    production_root = root / PACK_ROOT
    if production_root.is_dir() and (production_root / "ESAMI").is_dir():
        return production_root
    return root


def _declared_card_count(path: Path) -> int | None:
    if not path.is_file():
        return None
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        match = SCHEDE_RE.match(line)
        if match:
            return int(match.group(1))
    return None


def _jsonl_observation(path: Path) -> dict[str, int]:
    observation = {
        "observed_rows": 0,
        "malformed_json_rows": 0,
        "non_object_json_rows": 0,
    }
    if not path.is_file():
        return observation
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        observation["observed_rows"] += 1
        try:
            value = json.loads(line)
        except json.JSONDecodeError:
            observation["malformed_json_rows"] += 1
            continue
        if not isinstance(value, dict):
            observation["non_object_json_rows"] += 1
    return observation


def _pack_card_status(
    *,
    manifest_exists: bool,
    cards_exists: bool,
    declared_count: int | None,
    observed_rows: int,
    malformed_json_rows: int,
    non_object_json_rows: int,
) -> str:
    if not manifest_exists or not cards_exists:
        return "source_missing"
    if malformed_json_rows or non_object_json_rows:
        return "jsonl_invalid"
    if declared_count is None:
        return "declared_count_missing"
    if declared_count != observed_rows:
        return "declared_observed_mismatch"
    return "complete_observed"


def _pack_card_observations(
    root: Path, pack_entries: Iterable[dict[str, object]]
) -> list[dict[str, object]]:
    observations: list[dict[str, object]] = []
    for entry in pack_entries:
        pack_path = root / str(entry["pack_path"])
        manifest = pack_path / "COURSE.yaml"
        cards = pack_path / "schede" / "schede.jsonl"
        jsonl = _jsonl_observation(cards)
        declared = _declared_card_count(manifest)
        observations.append(
            {
                "pack_id": entry["pack_id"],
                "pack_path": entry["pack_path"],
                "manifest_path": manifest.relative_to(root).as_posix()
                if manifest.is_file()
                else None,
                "cards_path": cards.relative_to(root).as_posix()
                if cards.is_file()
                else None,
                "manifest_exists": manifest.is_file(),
                "cards_exists": cards.is_file(),
                "declared_schede": declared,
                **jsonl,
                "status": _pack_card_status(
                    manifest_exists=manifest.is_file(),
                    cards_exists=cards.is_file(),
                    declared_count=declared,
                    observed_rows=jsonl["observed_rows"],
                    malformed_json_rows=jsonl["malformed_json_rows"],
                    non_object_json_rows=jsonl["non_object_json_rows"],
                ),
            }
        )
    return observations


def _observed_pairs(g4: dict[str, object]) -> list[dict[str, str]]:
    pairs: dict[tuple[str, str], dict[str, str]] = {}
    for pack in g4["packs"]:  # type: ignore[index]
        for candidate in pack["candidate_exams"]:  # type: ignore[index]
            key = (str(pack["pack_id"]), str(candidate["exam_id"]))
            pairs[key] = {
                "pack_id": key[0],
                "exam_id": key[1],
                "relation": str(candidate["relation"]),
            }
    return [
        pairs[key]
        for key in sorted(pairs, key=lambda value: (value[0].casefold(), value[1].casefold()))
    ]


def _classification_counts(entries: Iterable[dict[str, object]]) -> dict[str, int]:
    counts = Counter(str(entry["classification"]) for entry in entries)
    return {
        name: counts.get(name, 0)
        for name in ("exact_name", "alias_observed", "unmatched_pack", "unmatched_exam", "ambiguous")
    }


def build_dashboard(root: Path) -> dict[str, object]:
    root = root.resolve()
    g4 = build_g4_report(root)
    g5 = build_review_report(root)
    pack_entries = [entry for entry in g4["packs"] if isinstance(entry, dict)]  # type: ignore[index]
    exam_entries = [entry for entry in g4["exams"] if isinstance(entry, dict)]  # type: ignore[index]
    card_observations = _pack_card_observations(root, pack_entries)
    pairs = _observed_pairs(g4)

    card_status_counts = Counter(str(item["status"]) for item in card_observations)
    observed_cards = sum(int(item["observed_rows"]) for item in card_observations)
    declared_cards = sum(
        int(item["declared_schede"])
        for item in card_observations
        if item["declared_schede"] is not None
    )
    alias_pairs = sum(item["relation"] == "alias_observed" for item in pairs)
    exact_pairs = sum(item["relation"] == "exact_name" for item in pairs)
    pack_classifications = _classification_counts(pack_entries)
    exam_classifications = _classification_counts(exam_entries)

    review_items = [item for item in g5["review_queue"] if isinstance(item, dict)]  # type: ignore[index]
    review_status_counts = Counter(str(item["review_status"]) for item in review_items)
    review_type_counts = Counter(str(item["item_type"]) for item in review_items)
    review_uncertainty_counts = Counter(str(item["uncertainty"]) for item in review_items)

    return {
        "schema_version": "g6a.v1",
        "tool": "tools/uni_completeness_dashboard_g6.py",
        "scope": {
            "university_pack_selector": "UNIVERSITA_EDILIZIA/*_PACK",
            "schede_selector": "UNIVERSITA_EDILIZIA/*_PACK/schede/schede.jsonl",
            "exam_source": "G4 pack/exam map built from the selected checkout filesystem",
            "review_source": "G5 review queue built from the selected checkout filesystem",
            "content_modified": False,
        },
        "sources": {
            "mapping": {
                "path": "docs/coordination/UNI_PACK_EXAM_MAP_G4.json",
                "schema_version": g4["schema_version"],
            },
            "review": {
                "path": "docs/coordination/UNI_PACK_EXAM_REVIEW_G5.json",
                "schema_version": g5["schema_version"],
            },
        },
        "observed": {
            "packs": len(pack_entries),
            "schede": {
                "jsonl_rows": observed_cards,
                "declared_total": declared_cards,
                "malformed_json_rows": sum(int(item["malformed_json_rows"]) for item in card_observations),
                "non_object_json_rows": sum(int(item["non_object_json_rows"]) for item in card_observations),
            },
            "exams": len(exam_entries),
            "exam_pack_pairs": len(pairs),
        },
        "pack_card_completeness": {
            "packs_with_course_manifest": sum(bool(item["manifest_exists"]) for item in card_observations),
            "packs_with_schede_jsonl": sum(bool(item["cards_exists"]) for item in card_observations),
            "packs_with_matching_declared_observed_schede": card_status_counts.get("complete_observed", 0),
            "status_counts": {
                status: card_status_counts.get(status, 0)
                for status in (
                    "complete_observed",
                    "source_missing",
                    "jsonl_invalid",
                    "declared_count_missing",
                    "declared_observed_mismatch",
                )
            },
        },
        "mapping": {
            "observed_pair_count": len(pairs),
            "pair_relation_counts": {
                "exact_name": exact_pairs,
                "alias_observed": alias_pairs,
            },
            "pack_classification_counts": pack_classifications,
            "exam_classification_counts": exam_classifications,
            "alias_observed": {
                "pair_count": alias_pairs,
                "pack_count": pack_classifications["alias_observed"],
                "exam_count": exam_classifications["alias_observed"],
            },
        },
        "unmatched": {
            "pack_count": pack_classifications["unmatched_pack"],
            "exam_count": exam_classifications["unmatched_exam"],
            "total_items": pack_classifications["unmatched_pack"]
            + exam_classifications["unmatched_exam"],
        },
        "pending_human_review": {
            "queue_item_count": len(review_items),
            "status_counts": {
                status: review_status_counts.get(status, 0)
                for status in ("pending", "decided")
            },
            "pending_count": review_status_counts.get("pending", 0),
            "item_type_counts": {
                item_type: review_type_counts.get(item_type, 0)
                for item_type in ("pack", "exam")
            },
            "uncertainty_counts": {
                uncertainty: review_uncertainty_counts.get(uncertainty, 0)
                for uncertainty in (
                    "ambiguous_observed_candidates",
                    "unmatched_legacy_domain",
                )
            },
        },
        "pack_card_observations": card_observations,
        "observed_exam_pack_pairs": pairs,
        "boundaries": [
            "Observed counts describe filesystem rows and records only; they do not certify educational or normative correctness.",
            "alias_observed is a bounded name/documentation signal, not proof of semantic coverage or equivalence.",
            "unmatched remains unmatched until explicit evidence is reviewed; no fallback association is created.",
            "pending_human_review remains pending and is not counted as decided or completed.",
            "Declared schede totals and observed JSONL rows are reported separately; a match is structural evidence only.",
            "No questions, answers, schede content, source files, or review decisions are edited by this tool.",
        ],
    }


def write_report(root: Path, output: Path) -> None:
    report = build_dashboard(root)
    output_path = output if output.is_absolute() else root / output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="checkout root (default: current directory)")
    parser.add_argument(
        "--output",
        type=Path,
        default=REPORT_RELATIVE_PATH,
        help=f"JSON report path relative to --root (default: {REPORT_RELATIVE_PATH.as_posix()})",
    )
    args = parser.parse_args(argv)
    write_report(args.root.resolve(), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
