"""Evaluate the deterministic G7-A release-readiness gate for the inventory.

The gate is deliberately narrower than a content or educational review.  It
recomputes the G6 dashboard and G5 review queue from the selected checkout,
compares them with the tracked JSON reports, and checks the corresponding
documentation markers.  Open human-review work remains open: a coherent
report can therefore still be ``blocked`` by pending or unmatched records.

Usage::

    python tools/uni_release_readiness_g7.py
    python tools/uni_release_readiness_g7.py --root .
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

try:
    from tools.uni_completeness_dashboard_g6 import build_dashboard
    from tools.uni_pack_exam_review_g5 import build_review_report
except ModuleNotFoundError:
    from uni_completeness_dashboard_g6 import build_dashboard
    from uni_pack_exam_review_g5 import build_review_report


REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_RELEASE_READINESS_G7.json")
MARKDOWN_RELATIVE_PATH = Path("docs/coordination/UNI_RELEASE_READINESS_G7.md")
G6_REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_COMPLETENESS_DASHBOARD_G6.json")
G5_REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_PACK_EXAM_REVIEW_G5.json")
G6_DOC_RELATIVE_PATH = Path("docs/coordination/UNI_COMPLETENESS_DASHBOARD_G6.md")
G5_DOC_RELATIVE_PATH = Path("docs/coordination/UNI_PACK_EXAM_REVIEW_G5.md")

EXPECTED_SNAPSHOT = {
    "dashboard": {
        "observed.packs": 71,
        "observed.schede.jsonl_rows": 963,
        "observed.schede.declared_total": 963,
        "observed.exams": 73,
        "observed.exam_pack_pairs": 73,
        "mapping.observed_pair_count": 73,
        "mapping.pair_relation_counts.exact_name": 14,
        "mapping.pair_relation_counts.alias_observed": 59,
        "unmatched.pack_count": 0,
        "unmatched.exam_count": 2,
        "unmatched.total_items": 2,
        "pending_human_review.queue_item_count": 6,
        "pending_human_review.pending_count": 6,
        "pending_human_review.status_counts.pending": 6,
        "pending_human_review.status_counts.decided": 0,
        "pending_human_review.item_type_counts.pack": 2,
        "pending_human_review.item_type_counts.exam": 4,
        "pending_human_review.uncertainty_counts.ambiguous_observed_candidates": 4,
        "pending_human_review.uncertainty_counts.unmatched_legacy_domain": 2,
    },
    "review": {
        "counts.queue_items": 6,
        "counts.ambiguous_pack": 2,
        "counts.ambiguous_exam": 2,
        "counts.legacy_unmatched_exam": 2,
        "counts.pending": 6,
    },
}

DASHBOARD_MARKER_RE = re.compile(
    r"<!--\s*G7-A observed:\s*"
    r"packs=(?P<packs>\d+);\s*"
    r"schede=(?P<schede>\d+);\s*"
    r"exams=(?P<exams>\d+);\s*"
    r"pairs=(?P<pairs>\d+)\s*-->"
)
REVIEW_MARKER_RE = re.compile(
    r"<!--\s*G7-A review:\s*"
    r"queue_items=(?P<queue_items>\d+);\s*"
    r"pending=(?P<pending>\d+);\s*"
    r"legacy_unmatched=(?P<legacy_unmatched>\d+)\s*-->"
)


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _path_value(value: dict[str, Any], dotted_path: str) -> Any:
    current: Any = value
    for part in dotted_path.split("."):
        if not isinstance(current, dict) or part not in current:
            return "<missing>"
        current = current[part]
    return current


def _add_check(
    checks: list[dict[str, Any]],
    mismatches: list[dict[str, Any]],
    *,
    check_id: str,
    path: str,
    expected: Any,
    observed: Any,
    source: str,
) -> None:
    matches = expected == observed
    check = {
        "check_id": check_id,
        "path": path,
        "source": source,
        "status": "pass" if matches else "mismatch",
        "expected": expected,
        "observed": observed,
    }
    checks.append(check)
    if not matches:
        mismatches.append(
            {
                "check_id": check_id,
                "path": path,
                "source": source,
                "expected": expected,
                "observed": observed,
                "status": "mismatch",
            }
        )


def _compare_snapshot(
    checks: list[dict[str, Any]],
    mismatches: list[dict[str, Any]],
    *,
    check_prefix: str,
    expected: dict[str, Any],
    observed: dict[str, Any],
    source: str,
) -> None:
    for path, expected_value in expected.items():
        _add_check(
            checks,
            mismatches,
            check_id=f"{check_prefix}.{path}",
            path=path,
            expected=expected_value,
            observed=observed[path] if path in observed else _path_value(observed, path),
            source=source,
        )


def _dashboard_snapshot(report: dict[str, Any]) -> dict[str, Any]:
    return {
        path: _path_value(report, path)
        for path in EXPECTED_SNAPSHOT["dashboard"]
    }


def _review_snapshot(report: dict[str, Any]) -> dict[str, Any]:
    return {path: _path_value(report, path) for path in EXPECTED_SNAPSHOT["review"]}


def _parse_marker(text: str, pattern: re.Pattern[str]) -> dict[str, int] | None:
    match = pattern.search(text)
    if match is None:
        return None
    return {name: int(value) for name, value in match.groupdict().items()}


def _review_invariants(review: dict[str, Any]) -> dict[str, Any]:
    queue = review.get("review_queue", [])
    if not isinstance(queue, list):
        return {
            "all_items_pending": False,
            "all_decisions_null": False,
            "legacy_items_have_no_candidates": False,
            "legacy_items_pending": False,
        }
    legacy_items = [
        item
        for item in queue
        if isinstance(item, dict)
        and item.get("uncertainty") == "unmatched_legacy_domain"
    ]
    return {
        "all_items_pending": all(
            isinstance(item, dict) and item.get("review_status") == "pending"
            for item in queue
        ),
        "all_decisions_null": all(
            isinstance(item, dict)
            and isinstance(item.get("decision"), dict)
            and all(item["decision"].get(key) is None for key in ("outcome", "selected_id", "reviewer_note"))
            for item in queue
        ),
        "legacy_items_have_no_candidates": all(
            isinstance(item, dict) and item.get("candidate_ids") == []
            for item in legacy_items
        ),
        "legacy_items_pending": all(
            isinstance(item, dict) and item.get("review_status") == "pending"
            for item in legacy_items
        ),
    }


def build_release_readiness(
    root: Path,
    *,
    dashboard_report_path: Path | None = None,
    review_report_path: Path | None = None,
    dashboard_doc_path: Path | None = None,
    review_doc_path: Path | None = None,
    dashboard_report: dict[str, Any] | None = None,
    review_report: dict[str, Any] | None = None,
    dashboard_doc: str | None = None,
    review_doc: str | None = None,
) -> dict[str, Any]:
    """Build a deterministic gate report without changing corpus or decisions."""

    root = root.resolve()
    dashboard_report_path = dashboard_report_path or root / G6_REPORT_RELATIVE_PATH
    review_report_path = review_report_path or root / G5_REPORT_RELATIVE_PATH
    dashboard_doc_path = dashboard_doc_path or root / G6_DOC_RELATIVE_PATH
    review_doc_path = review_doc_path or root / G5_DOC_RELATIVE_PATH

    recomputed_dashboard = build_dashboard(root)
    recomputed_review = build_review_report(root)
    tracked_dashboard = dashboard_report or _load_json(dashboard_report_path)
    tracked_review = review_report or _load_json(review_report_path)
    dashboard_doc = dashboard_doc if dashboard_doc is not None else dashboard_doc_path.read_text(encoding="utf-8")
    review_doc = review_doc if review_doc is not None else review_doc_path.read_text(encoding="utf-8")

    checks: list[dict[str, Any]] = []
    mismatches: list[dict[str, Any]] = []

    _compare_snapshot(
        checks,
        mismatches,
        check_prefix="recomputed_dashboard_contract",
        expected=EXPECTED_SNAPSHOT["dashboard"],
        observed=recomputed_dashboard,
        source="selected checkout filesystem via G6 builder",
    )
    _compare_snapshot(
        checks,
        mismatches,
        check_prefix="tracked_dashboard_matches_recomputed",
        expected=_dashboard_snapshot(recomputed_dashboard),
        observed=_dashboard_snapshot(tracked_dashboard),
        source=G6_REPORT_RELATIVE_PATH.as_posix(),
    )
    _compare_snapshot(
        checks,
        mismatches,
        check_prefix="recomputed_review_contract",
        expected=EXPECTED_SNAPSHOT["review"],
        observed=recomputed_review,
        source="selected checkout filesystem via G5 builder",
    )
    _compare_snapshot(
        checks,
        mismatches,
        check_prefix="tracked_review_matches_recomputed",
        expected=_review_snapshot(recomputed_review),
        observed=_review_snapshot(tracked_review),
        source=G5_REPORT_RELATIVE_PATH.as_posix(),
    )

    recomputed_dashboard_snapshot = _dashboard_snapshot(recomputed_dashboard)
    recomputed_review_snapshot = _review_snapshot(recomputed_review)
    _add_check(
        checks,
        mismatches,
        check_id="cross_report.pending_count",
        path="pending_human_review.pending_count == counts.pending",
        expected=recomputed_review_snapshot["counts.pending"],
        observed=recomputed_dashboard_snapshot["pending_human_review.pending_count"],
        source="G6 dashboard / G5 review report",
    )
    _add_check(
        checks,
        mismatches,
        check_id="cross_report.legacy_unmatched_count",
        path="unmatched.exam_count == counts.legacy_unmatched_exam",
        expected=recomputed_review_snapshot["counts.legacy_unmatched_exam"],
        observed=recomputed_dashboard_snapshot["unmatched.exam_count"],
        source="G6 dashboard / G5 review report",
    )

    invariants = _review_invariants(recomputed_review)
    for name, observed in invariants.items():
        _add_check(
            checks,
            mismatches,
            check_id=f"review_safety.{name}",
            path=name,
            expected=True,
            observed=observed,
            source="G5 review queue generated from selected checkout",
        )

    dashboard_marker = _parse_marker(dashboard_doc, DASHBOARD_MARKER_RE)
    review_marker = _parse_marker(review_doc, REVIEW_MARKER_RE)
    dashboard_doc_values = {
        "packs": recomputed_dashboard_snapshot["observed.packs"],
        "schede": recomputed_dashboard_snapshot["observed.schede.jsonl_rows"],
        "exams": recomputed_dashboard_snapshot["observed.exams"],
        "pairs": recomputed_dashboard_snapshot["observed.exam_pack_pairs"],
    }
    review_doc_values = {
        "queue_items": recomputed_review_snapshot["counts.queue_items"],
        "pending": recomputed_review_snapshot["counts.pending"],
        "legacy_unmatched": recomputed_review_snapshot["counts.legacy_unmatched_exam"],
    }
    for path, expected in dashboard_doc_values.items():
        _add_check(
            checks,
            mismatches,
            check_id=f"dashboard_documentation.{path}",
            path=path,
            expected=expected,
            observed=(dashboard_marker or {}).get(path, "<missing>"),
            source=G6_DOC_RELATIVE_PATH.as_posix(),
        )
    for path, expected in review_doc_values.items():
        _add_check(
            checks,
            mismatches,
            check_id=f"review_documentation.{path}",
            path=path,
            expected=expected,
            observed=(review_marker or {}).get(path, "<missing>"),
            source=G5_DOC_RELATIVE_PATH.as_posix(),
        )

    pending_count = recomputed_review_snapshot["counts.pending"]
    legacy_count = recomputed_review_snapshot["counts.legacy_unmatched_exam"]
    blocking_conditions: list[str] = []
    if pending_count:
        blocking_conditions.append(
            f"pending_human_review: {pending_count} G5 item remain pending"
        )
    if legacy_count:
        blocking_conditions.append(
            f"unmatched_legacy: {legacy_count} legacy exam remain unmatched"
        )
    if mismatches:
        blocking_conditions.append(f"coherence_mismatch: {len(mismatches)} explicit mismatch(es)")

    return {
        "schema_version": "g7a.v1",
        "tool": "tools/uni_release_readiness_g7.py",
        "status": "blocked" if blocking_conditions else "ready",
        "release_ready": not blocking_conditions,
        "review_state": "pending" if pending_count or legacy_count else "closed",
        "mismatch_count": len(mismatches),
        "source_reports": {
            "dashboard": G6_REPORT_RELATIVE_PATH.as_posix(),
            "review": G5_REPORT_RELATIVE_PATH.as_posix(),
            "dashboard_documentation": G6_DOC_RELATIVE_PATH.as_posix(),
            "review_documentation": G5_DOC_RELATIVE_PATH.as_posix(),
        },
        "observed_snapshot": {
            "dashboard": recomputed_dashboard_snapshot,
            "review": recomputed_review_snapshot,
        },
        "open_review": {
            "pending_g5": pending_count,
            "unmatched_legacy": legacy_count,
            "automatic_resolution": False,
        },
        "blocking_conditions": blocking_conditions,
        "checks": checks,
        "mismatches": mismatches,
        "scope": {
            "content_modified": False,
            "didactic_content_reviewed": False,
            "semantic_association_inferred": False,
            "pending_or_unmatched_closed": False,
        },
        "boundaries": [
            "The gate checks structural counts, report parity, documentation markers, and review-state invariants only.",
            "Six G5 pending items remain pending and require human review.",
            "Two legacy unmatched exams remain unmatched; no name-only fallback is accepted.",
            "A coherent gate is still blocked while open review work remains.",
            "No questions, answers, schede content, sources, mappings, or review decisions are edited.",
        ],
    }


def render_markdown(report: dict[str, Any]) -> str:
    snapshot = report["observed_snapshot"]
    dashboard = snapshot["dashboard"]
    review = snapshot["review"]
    return f"""# UniCostraction — gate release-readiness inventario G7-A

Stato gate: **{report['status'].upper()}**  
Release-ready: **{'sì' if report['release_ready'] else 'no'}**  
Stato revisione: **{report['review_state']}**  
Mismatch espliciti: **{report['mismatch_count']}**

<!-- G7-A gate: status={report['status']}; release_ready={str(report['release_ready']).lower()}; pending={review['counts.pending']}; unmatched_legacy={review['counts.legacy_unmatched_exam']} -->

## Snapshot strutturale osservato

| Indicatore | Valore |
| --- | ---: |
| Pack osservati | {dashboard['observed.packs']} |
| Righe JSONL `schede` osservate | {dashboard['observed.schede.jsonl_rows']} |
| Esami osservati | {dashboard['observed.exams']} |
| Coppie esame-pack osservate | {dashboard['observed.exam_pack_pairs']} |
| Item G5 in coda | {review['counts.queue_items']} |
| Item G5 pending | {review['counts.pending']} |
| Esami legacy unmatched | {review['counts.legacy_unmatched_exam']} |

## Gate

Il gate confronta il filesystem ricalcolato con i JSON G6/G5 tracciati e con i
marker numerici nella documentazione. Un mismatch non viene nascosto: è
riportato nel campo `mismatches` del JSON con percorso, atteso e osservato.

Condizioni correnti:

{chr(10).join(f"- {condition}" for condition in report['blocking_conditions']) or '- nessuna'}

I 6 item G5 restano `pending` e i 2 esami legacy restano `unmatched`. Il gate
non assegna associazioni canoniche, non chiude la coda e non legge né modifica
contenuto didattico.

Per rigenerare il report dal checkout selezionato:

```powershell
python tools/uni_release_readiness_g7.py
```
"""


def write_reports(root: Path) -> dict[str, Any]:
    root = root.resolve()
    report = build_release_readiness(root)
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
    print(f"status={report['status']} mismatches={report['mismatch_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
