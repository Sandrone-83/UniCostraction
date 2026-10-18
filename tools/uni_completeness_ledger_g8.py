"""Build a deterministic evidence ledger for the UniCostraction inventory.

The G8-A ledger is an index of observed files and G6 dashboard counts.  It
does not decide whether an exam belongs to a pack and it does not inspect
didactic content.  Records with an open G5 review item, or with an incomplete
pack/card observation, are explicitly marked ``human_review_required``;
everything else observed by the selected filesystem is marked
``evidence_present``.

Usage::

    python tools/uni_completeness_ledger_g8.py
    python tools/uni_completeness_ledger_g8.py --root .
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

try:
    from tools.uni_completeness_dashboard_g6 import build_dashboard
    from tools.uni_pack_exam_map_g4 import build_report as build_g4_report
    from tools.uni_pack_exam_review_g5 import build_review_report
except ModuleNotFoundError:
    from uni_completeness_dashboard_g6 import build_dashboard
    from uni_pack_exam_map_g4 import build_report as build_g4_report
    from uni_pack_exam_review_g5 import build_review_report


REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_COMPLETENESS_LEDGER_G8.json")
MARKDOWN_RELATIVE_PATH = Path("docs/coordination/UNI_COMPLETENESS_LEDGER_G8.md")
SCHEMA_RELATIVE_PATH = Path("docs/coordination/UNI_COMPLETENESS_LEDGER_G8.schema.json")
G6_REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_COMPLETENESS_DASHBOARD_G6.json")
G5_REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_PACK_EXAM_REVIEW_G5.json")
EVIDENCE_STATES = ("evidence_present", "human_review_required")


def _sorted_unique(values: Iterable[str]) -> list[str]:
    return sorted(set(values), key=lambda value: value.casefold())


def _existing_paths(root: Path, values: Iterable[object]) -> list[str]:
    paths = []
    for value in values:
        relative = str(value)
        if (root / Path(relative)).is_file():
            paths.append(relative)
    return _sorted_unique(paths)


def _review_items_by_key(review: dict[str, Any]) -> dict[tuple[str, str], list[dict[str, Any]]]:
    indexed: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for item in review.get("review_queue", []):
        if not isinstance(item, dict):
            continue
        key = (str(item.get("item_type")), str(item.get("item_id")))
        indexed.setdefault(key, []).append(item)
    return indexed


def _review_summary(items: list[dict[str, Any]]) -> dict[str, Any]:
    pending = [item for item in items if item.get("review_status") == "pending"]
    return {
        "required": bool(pending),
        "queue_ids": [str(item["queue_id"]) for item in pending],
        "uncertainties": _sorted_unique(str(item["uncertainty"]) for item in pending),
        "legacy_unmatched": any(bool(item.get("legacy_observed")) for item in pending),
    }


def _pack_dashboard_reference(
    dashboard: dict[str, Any],
    observation: dict[str, Any],
) -> dict[str, Any]:
    pack_id = str(observation["pack_id"])
    status = str(observation["status"])
    prefix = f"pack_card_observations[pack_id={pack_id}]"
    status_counts = dashboard["pack_card_completeness"]["status_counts"]
    return {
        "report_path": G6_REPORT_RELATIVE_PATH.as_posix(),
        "count_paths": {
            "total_packs": "observed.packs",
            "declared_schede": f"{prefix}.declared_schede",
            "observed_schede_rows": f"{prefix}.observed_rows",
            "card_status": f"{prefix}.status",
            "card_status_count": f"pack_card_completeness.status_counts.{status}",
        },
        "counts": {
            "total_packs": dashboard["observed"]["packs"],
            "declared_schede": observation["declared_schede"],
            "observed_schede_rows": observation["observed_rows"],
            "card_status": status,
            "card_status_count": status_counts[status],
        },
    }


def _exam_dashboard_reference(
    dashboard: dict[str, Any],
    exam: dict[str, Any],
) -> dict[str, Any]:
    classification = str(exam["classification"])
    return {
        "report_path": G6_REPORT_RELATIVE_PATH.as_posix(),
        "count_paths": {
            "total_exams": "observed.exams",
            "total_exam_pack_pairs": "observed.exam_pack_pairs",
            "classification_count": f"mapping.exam_classification_counts.{classification}",
            "unmatched_exam_count": "unmatched.exam_count",
            "pending_human_review_count": "pending_human_review.pending_count",
        },
        "counts": {
            "total_exams": dashboard["observed"]["exams"],
            "total_exam_pack_pairs": dashboard["observed"]["exam_pack_pairs"],
            "classification_count": dashboard["mapping"]["exam_classification_counts"][classification],
            "unmatched_exam_count": dashboard["unmatched"]["exam_count"],
            "pending_human_review_count": dashboard["pending_human_review"]["pending_count"],
        },
    }


def _pack_entry(
    root: Path,
    dashboard: dict[str, Any],
    review_by_key: dict[tuple[str, str], list[dict[str, Any]]],
    record: dict[str, Any],
) -> dict[str, Any]:
    pack_id = str(record["pack_id"])
    observation = next(
        item for item in dashboard["pack_card_observations"] if item["pack_id"] == pack_id
    )
    review = _review_summary(review_by_key.get(("pack", pack_id), []))
    card_complete = observation["status"] == "complete_observed"
    state = "human_review_required" if review["required"] or not card_complete else "evidence_present"
    source_files = _existing_paths(
        root,
        [*record.get("source_files", []), observation.get("cards_path")],
    )
    return {
        "record_id": f"pack:{pack_id}",
        "item_type": "pack",
        "item_id": pack_id,
        "evidence_state": state,
        "classification": record["classification"],
        "source_files": source_files,
        "dashboard_reference": _pack_dashboard_reference(dashboard, observation),
        "observed": {
            "pack_path": record["pack_path"],
            "manifest_exists": observation["manifest_exists"],
            "cards_exists": observation["cards_exists"],
            "card_status": observation["status"],
            "candidate_exam_count": len(record.get("candidate_exams", [])),
        },
        "human_review": review,
    }


def _exam_entry(
    root: Path,
    dashboard: dict[str, Any],
    review_by_key: dict[tuple[str, str], list[dict[str, Any]]],
    record: dict[str, Any],
) -> dict[str, Any]:
    exam_id = str(record["exam_id"])
    review = _review_summary(review_by_key.get(("exam", exam_id), []))
    state = "human_review_required" if review["required"] else "evidence_present"
    source_files = _existing_paths(root, record.get("source_files", []))
    return {
        "record_id": f"exam:{exam_id}",
        "item_type": "exam",
        "item_id": exam_id,
        "evidence_state": state,
        "classification": record["classification"],
        "source_files": source_files,
        "dashboard_reference": _exam_dashboard_reference(dashboard, record),
        "observed": {
            "exam_path": record["exam_path"],
            "legacy_observed": bool(record.get("legacy_observed", False)),
            "candidate_pack_count": len(record.get("candidate_packs", [])),
        },
        "human_review": review,
    }


def _state_counts(entries: list[dict[str, Any]]) -> dict[str, int]:
    counts = Counter(str(entry["evidence_state"]) for entry in entries)
    return {state: counts.get(state, 0) for state in EVIDENCE_STATES}


def build_ledger(root: Path) -> dict[str, Any]:
    """Build the ledger from the selected checkout without changing corpus data."""

    root = root.resolve()
    dashboard = build_dashboard(root)
    review = build_review_report(root)
    review_by_key = _review_items_by_key(review)
    # G6 derives its pack observations from G4, so recover the complete G4
    # records rather than inventing associations from the card filesystem.
    g4 = build_g4_report(root)
    packs = [item for item in g4["packs"] if isinstance(item, dict)]
    exams = [item for item in g4["exams"] if isinstance(item, dict)]
    pack_entries = [
        _pack_entry(root, dashboard, review_by_key, record) for record in packs
    ]
    exam_entries = [
        _exam_entry(root, dashboard, review_by_key, record) for record in exams
    ]

    pack_entries.sort(key=lambda item: str(item["item_id"]).casefold())
    exam_entries.sort(key=lambda item: str(item["item_id"]).casefold())
    all_entries = [*pack_entries, *exam_entries]
    pending_items = [
        item
        for item in review.get("review_queue", [])
        if isinstance(item, dict) and item.get("review_status") == "pending"
    ]
    legacy_pending = [
        item
        for item in pending_items
        if item.get("uncertainty") == "unmatched_legacy_domain"
    ]

    dashboard_counts = {
        "observed": dashboard["observed"],
        "pack_card_completeness": dashboard["pack_card_completeness"],
        "mapping": dashboard["mapping"],
        "unmatched": dashboard["unmatched"],
        "pending_human_review": dashboard["pending_human_review"],
    }
    return {
        "schema_version": "g8a.v1",
        "tool": "tools/uni_completeness_ledger_g8.py",
        "scope": {
            "source_of_truth": "selected checkout filesystem through G4/G5/G6 builders",
            "didactic_content_reviewed": False,
            "semantic_association_inferred": False,
            "content_modified": False,
        },
        "source_reports": {
            "dashboard": {
                "path": G6_REPORT_RELATIVE_PATH.as_posix(),
                "schema_version": dashboard["schema_version"],
            },
            "review": {
                "path": G5_REPORT_RELATIVE_PATH.as_posix(),
                "schema_version": review["schema_version"],
            },
        },
        "dashboard_counts": dashboard_counts,
        "counts": {
            "records": {"packs": len(pack_entries), "exams": len(exam_entries)},
            "evidence_state": {
                "packs": _state_counts(pack_entries),
                "exams": _state_counts(exam_entries),
                "total": _state_counts(all_entries),
            },
        },
        "open_review": {
            "pending_g5": len(pending_items),
            "legacy_unmatched_exams": len(legacy_pending),
            "pending_queue_ids": [str(item["queue_id"]) for item in pending_items],
            "automatic_resolution": False,
            "pending_or_unmatched_closed": False,
        },
        "packs": pack_entries,
        "exams": exam_entries,
        "boundaries": [
            "evidence_present means only that the referenced filesystem evidence and structural observations are present; it is not educational, normative, legal, or semantic approval.",
            "human_review_required is assigned to open G5 items and incomplete pack/card observations.",
            "Alias, ambiguous, and unmatched classifications remain observations and are never promoted to canonical associations.",
            "The six pending G5 items and two legacy unmatched exams remain open; this ledger does not resolve or close them.",
            "No questions, answers, schede content, source files, mappings, or review decisions are edited.",
        ],
    }


def render_markdown(report: dict[str, Any]) -> str:
    counts = report["counts"]
    dashboard = report["dashboard_counts"]["observed"]
    review = report["open_review"]
    pack_states = counts["evidence_state"]["packs"]
    exam_states = counts["evidence_state"]["exams"]
    return f"""# UniCostraction — ledger evidenza completezza G8-A

Il report deterministico è [`UNI_COMPLETENESS_LEDGER_G8.json`](UNI_COMPLETENESS_LEDGER_G8.json) ed è accompagnato dallo schema [`UNI_COMPLETENESS_LEDGER_G8.schema.json`](UNI_COMPLETENESS_LEDGER_G8.schema.json). Si rigenera dal checkout selezionato con:

```powershell
python tools/uni_completeness_ledger_g8.py
```

## Snapshot osservato

| Indicatore | Valore |
| --- | ---: |
| Pack | {dashboard['packs']} |
| Righe JSONL `schede` | {dashboard['schede']['jsonl_rows']} |
| Esami | {dashboard['exams']} |
| Coppie esame-pack | {dashboard['exam_pack_pairs']} |
| G5 pending | {review['pending_g5']} |
| Esami legacy unmatched | {review['legacy_unmatched_exams']} |

Ogni record `pack:*` e `exam:*` elenca i `source_files` osservati e un
`dashboard_reference` con i percorsi dei conteggi nel dashboard G6 e i valori
osservati. `evidence_present` descrive evidenza strutturale presente; non è una
certificazione didattica, normativa, legale o semantica.

| Tipo | `evidence_present` | `human_review_required` |
| --- | ---: | ---: |
| Pack | {pack_states['evidence_present']} | {pack_states['human_review_required']} |
| Esame | {exam_states['evidence_present']} | {exam_states['human_review_required']} |

La coda G5 resta aperta: i {review['pending_g5']} item sono ancora `pending` e
i {review['legacy_unmatched_exams']} esami legacy restano unmatched. Il ledger
non assegna associazioni canoniche e non chiude alcun item.

## Confini

- alias, ambiguità e unmatched restano classificazioni osservate;
- nessun contenuto didattico viene letto per inferire associazioni;
- nessun file di domande, risposte, schede o decisione di revisione viene modificato;
- il ledger indica dove guardare e cosa il dashboard conta, non sostituisce la revisione umana.
"""


def write_reports(root: Path) -> dict[str, Any]:
    root = root.resolve()
    report = build_ledger(root)
    json_path = root / REPORT_RELATIVE_PATH
    markdown_path = root / MARKDOWN_RELATIVE_PATH
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(report), encoding="utf-8")
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args(argv)
    report = write_reports(args.root)
    states = report["counts"]["evidence_state"]["total"]
    print(
        f"packs={report['counts']['records']['packs']} "
        f"exams={report['counts']['records']['exams']} "
        f"evidence_present={states['evidence_present']} "
        f"human_review_required={states['human_review_required']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
