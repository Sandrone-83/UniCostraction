"""Build the G12-A human decision contract for the 85 G11 components.

The output is a metadata-only review queue.  It carries component identifiers,
priority metadata and provenance paths from G11, but never copies card or exam
text and never changes those source files.  A decision is intentionally null
until a human reviewer records an allowed outcome with evidence, identity and
rationale.

Usage::

    python tools/uni_cluster_review_g12_a.py
    python tools/uni_cluster_review_g12_a.py --root . \
        --input docs/coordination/UNI_REDUNDANCY_PRIORITY_G11_A.json
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable


INPUT_RELATIVE_PATH = Path("docs/coordination/UNI_REDUNDANCY_PRIORITY_G11_A.json")
REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_CLUSTER_REVIEW_G12_A.json")
MARKDOWN_RELATIVE_PATH = Path("docs/coordination/UNI_CLUSTER_REVIEW_G12_A.md")
TOOL_PATH = "tools/uni_cluster_review_g12_a.py"
SCHEMA_VERSION = "g12a.v1"
INPUT_SCHEMA_VERSION = "g11a.v1"
EXPECTED_COMPONENT_COUNT = 85
ALLOWED_DECISIONS = [
    "distinct",
    "merge_candidate",
    "reject_candidate",
    "needs_source_review",
]
REVIEW_FIELDS = ("decision", "evidence_ref", "reviewer", "rationale")


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _component_ids_sha256(components: Iterable[dict[str, Any]]) -> str:
    component_ids = [str(component["component_id"]) for component in components]
    return _sha256(_canonical_json(component_ids).encode("utf-8"))


def load_report(path: Path) -> tuple[dict[str, Any], str]:
    """Load a JSON report and return it with the exact input byte hash."""

    raw = path.read_bytes()
    return json.loads(raw.decode("utf-8")), _sha256(raw)


def _validate_g11_queue(input_report: dict[str, Any]) -> list[dict[str, Any]]:
    if input_report.get("schema_version") != INPUT_SCHEMA_VERSION:
        raise ValueError("G12-A requires a g11a.v1 input report")
    queue = input_report.get("results", {}).get("queue")
    if not isinstance(queue, list):
        raise ValueError("G11 results.queue must be an array")

    seen_ids: set[str] = set()
    seen_ranks: set[int] = set()
    for component in queue:
        if not isinstance(component, dict):
            raise ValueError("every G11 queue item must be an object")
        component_id = str(component.get("component_id", ""))
        if not component_id or component_id in seen_ids:
            raise ValueError(f"duplicate or empty G11 component_id: {component_id}")
        rank = component.get("priority_rank")
        if not isinstance(rank, int) or isinstance(rank, bool) or rank < 1:
            raise ValueError(f"invalid G11 priority_rank: {component_id}")
        if rank in seen_ranks:
            raise ValueError(f"duplicate G11 priority_rank: {rank}")
        if not isinstance(component.get("unit_ids"), list) or not component["unit_ids"]:
            raise ValueError(f"G11 component has no unit_ids: {component_id}")
        if not isinstance(component.get("coverage"), dict):
            raise ValueError(f"G11 component has no coverage object: {component_id}")
        if component.get("source_group") not in {"cards", "public_exams"}:
            raise ValueError(f"invalid G11 source_group: {component_id}")
        seen_ids.add(component_id)
        seen_ranks.add(rank)

    expected_ranks = set(range(1, len(queue) + 1))
    if seen_ranks != expected_ranks:
        raise ValueError("G11 priority ranks must be consecutive from 1")
    return sorted(queue, key=lambda item: (int(item["priority_rank"]), str(item["component_id"])))


def _review_placeholder() -> dict[str, None]:
    return {
        "decision": None,
        "evidence_ref": None,
        "reviewer": None,
        "rationale": None,
    }


def _component_review_record(component: dict[str, Any]) -> dict[str, Any]:
    """Copy only G11 metadata needed to locate and prioritize the review."""

    return {
        "component_id": str(component["component_id"]),
        "priority_rank": int(component["priority_rank"]),
        "priority_key": copy.deepcopy(component["priority_key"]),
        "source_group": str(component["source_group"]),
        "unit_ids": [str(unit_id) for unit_id in component["unit_ids"]],
        "coverage": copy.deepcopy(component["coverage"]),
        "collision_count": int(component["collision_count"]),
        "review": _review_placeholder(),
    }


def validate_review_report(
    report: dict[str, Any],
    *,
    expected_component_count: int | None = EXPECTED_COMPONENT_COUNT,
) -> None:
    """Validate the G12 decision invariants without using a schema package."""

    if report.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("unexpected G12 schema_version")
    queue = report.get("review_queue")
    if not isinstance(queue, list):
        raise ValueError("review_queue must be an array")
    if expected_component_count is not None and len(queue) != expected_component_count:
        raise ValueError(
            f"expected {expected_component_count} components, got {len(queue)}"
        )

    seen_ids: set[str] = set()
    for item in queue:
        if not isinstance(item, dict):
            raise ValueError("review_queue items must be objects")
        component_id = str(item.get("component_id", ""))
        if not component_id or component_id in seen_ids:
            raise ValueError(f"duplicate or empty review component_id: {component_id}")
        seen_ids.add(component_id)
        review = item.get("review")
        if not isinstance(review, dict) or any(field not in review for field in REVIEW_FIELDS):
            raise ValueError(f"review must contain {REVIEW_FIELDS}: {component_id}")
        decision = review["decision"]
        if decision is not None and decision not in ALLOWED_DECISIONS:
            raise ValueError(f"unsupported decision for {component_id}: {decision}")
        if decision is not None:
            for field in ("evidence_ref", "reviewer", "rationale"):
                value = review[field]
                if not isinstance(value, str) or not value.strip():
                    raise ValueError(f"{field} is required for non-null decision: {component_id}")

    decisions = [item["review"]["decision"] for item in queue]
    expected_pending = sum(decision is None for decision in decisions)
    coverage = report.get("coverage", {})
    if coverage.get("component_count") != len(queue):
        raise ValueError("coverage.component_count does not match review_queue")
    if coverage.get("pending_count") != expected_pending:
        raise ValueError("coverage.pending_count does not match review_queue")
    if coverage.get("decided_count") != len(queue) - expected_pending:
        raise ValueError("coverage.decided_count does not match review_queue")
    if coverage.get("all_decisions_null") != (expected_pending == len(queue)):
        raise ValueError("coverage.all_decisions_null does not match review_queue")


def build_report(
    input_report: dict[str, Any],
    *,
    input_path: str = INPUT_RELATIVE_PATH.as_posix(),
    input_report_sha256: str | None = None,
    expected_component_count: int | None = EXPECTED_COMPONENT_COUNT,
) -> dict[str, Any]:
    components = _validate_g11_queue(input_report)
    if expected_component_count is not None and len(components) != expected_component_count:
        raise ValueError(
            f"expected {expected_component_count} G11 components, got {len(components)}"
        )

    review_queue = [_component_review_record(component) for component in components]
    report = {
        "schema_version": SCHEMA_VERSION,
        "tool": TOOL_PATH,
        "input": {
            "path": input_path,
            "schema_version": input_report.get("schema_version"),
            "component_count": len(review_queue),
            "component_ids_sha256": _component_ids_sha256(review_queue),
            "report_sha256": input_report_sha256,
        },
        "scope": {
            "decision_level": "connected_component",
            "initial_decision": None,
            "allowed_decisions": ALLOWED_DECISIONS,
            "human_review_required": True,
            "answers_read": False,
            "didactic_content_copied": False,
            "didactic_content_modified": False,
            "automatic_card_modification": False,
            "automatic_exam_modification": False,
            "automatic_merge_or_reject": False,
            "files_deleted": False,
            "source_of_truth": "G11 priority queue component metadata",
        },
        "review_policy": {
            "evidence_ref_required_for_non_null_decision": True,
            "reviewer_required": True,
            "rationale_required": True,
            "null_initial_state_is_pending": True,
            "decision_is_not_an_action": True,
        },
        "coverage": {
            "component_count": len(review_queue),
            "pending_count": len(review_queue),
            "decided_count": 0,
            "all_decisions_null": True,
        },
        "review_queue": review_queue,
        "boundaries": [
            "The queue contains one human-review record per G11 connected component.",
            "A component is a review unit, not proof of semantic, didactic, factual, normative or licensing equivalence.",
            "Only the four declared decisions are allowed; null means pending and is the initial state.",
            "A non-null decision requires a non-empty evidence_ref, reviewer and rationale.",
            "No card or exam file may be modified, merged, rejected or deleted automatically by this contract.",
            "The contract contains identifiers, metrics and provenance metadata only; it contains no exam answers or didactic bodies.",
        ],
    }
    validate_review_report(report, expected_component_count=expected_component_count)
    return report


def render_markdown(report: dict[str, Any]) -> str:
    coverage = report["coverage"]
    input_data = report["input"]
    return "\n".join(
        [
            "# UniCostraction — contratto decisioni umane sui cluster G12-A",
            "",
            "Questo contratto machine-readable prepara la revisione umana dei",
            f"**{coverage['component_count']} componenti** della coda G11-A.",
            "Ogni componente ha una sola registrazione `review`; la decisione iniziale",
            "è `null` e non implica alcuna fusione, rigetto o approvazione.",
            "",
            "## Input e rigenerazione",
            "",
            f"- input: `{input_data['path']}` (`{input_data['schema_version']}`)",
            f"- componenti: **{input_data['component_count']}**",
            f"- hash ID componenti: `{input_data['component_ids_sha256']}`",
            "",
            "```powershell",
            "python tools/uni_cluster_review_g12_a.py",
            "```",
            "",
            "## Campi della decisione",
            "",
            "Ogni record contiene sempre `decision`, `evidence_ref`, `reviewer` e",
            "`rationale`. I valori iniziali sono tutti `null` come placeholder di",
            "revisione. Prima di registrare una decisione non-null, il revisore deve",
            "compilare tutti e tre i campi di audit; `evidence_ref` deve puntare a",
            "un'evidenza verificabile.",
            "",
            "Decisioni ammesse: `distinct`, `merge_candidate`, `reject_candidate`,",
            "`needs_source_review`.",
            "",
            "## Confini",
            "",
            "- la coda è a livello di componente connesso, non di singola risposta;",
            "- non vengono lette, copiate o generate risposte d'esame;",
            "- card ed esami restano immutati: il contratto non esegue azioni automatiche;",
            "- `merge_candidate` e `reject_candidate` sono esiti di revisione, non comandi esecutivi;",
            "- la decisione umana non certifica correttezza didattica, normativa, legale o fattuale.",
            "",
        ]
    )


def write_reports(root: Path, input_path: Path, output_path: Path) -> dict[str, Any]:
    resolved_input = input_path if input_path.is_absolute() else root / input_path
    resolved_output = output_path if output_path.is_absolute() else root / output_path
    input_report, input_sha256 = load_report(resolved_input)
    report = build_report(
        input_report,
        input_path=input_path.as_posix(),
        input_report_sha256=input_sha256,
    )
    resolved_output.parent.mkdir(parents=True, exist_ok=True)
    resolved_output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    markdown_path = root / MARKDOWN_RELATIVE_PATH
    markdown_path.write_text(render_markdown(report), encoding="utf-8")
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--input", type=Path, default=INPUT_RELATIVE_PATH)
    parser.add_argument("--output", type=Path, default=REPORT_RELATIVE_PATH)
    args = parser.parse_args(argv)
    report = write_reports(args.root.resolve(), args.input, args.output)
    print(
        f"components={report['coverage']['component_count']} "
        f"pending={report['coverage']['pending_count']} "
        f"decided={report['coverage']['decided_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
