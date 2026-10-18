"""Audit deterministic regeneration and integrity of the G10-A to G14-A chain.

The audit stages the card/exam inputs and the G4 mapping in a temporary output
directory, reruns the applicable generators there, and compares their generated
reports with the published checkout.  Published reports, guides, schemas, cards,
and exams are read-only: no generator is pointed at the published output path.

Usage::

    python tools/uni_determinism_audit_g15_a.py --root .
    python tools/uni_determinism_audit_g15_a.py --root . --output path/to/g15.json

The command prints a machine-readable report and returns exit code 1 when a
published report, hash, count, cluster/packet invariant, or workflow state
drifts from the isolated regeneration.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import uuid
from pathlib import Path
from typing import Any, Iterable

try:
    from tools import (
        uni_cluster_review_g12_a as g12,
        uni_cluster_review_packet_g13_a as g13,
        uni_cluster_review_progress_g14_a as g14,
        uni_redundancy_audit_g10_a as g10,
        uni_redundancy_priority_g11_a as g11,
    )
except ModuleNotFoundError:  # Direct ``python tools/<script>.py`` execution.
    import uni_cluster_review_g12_a as g12
    import uni_cluster_review_packet_g13_a as g13
    import uni_cluster_review_progress_g14_a as g14
    import uni_redundancy_audit_g10_a as g10
    import uni_redundancy_priority_g11_a as g11


SCHEMA_VERSION = "g15a.v1"
TOOL_PATH = "tools/uni_determinism_audit_g15_a.py"

GENERATED_ARTIFACTS = {
    "g10_report": Path("docs/coordination/UNI_REDUNDANCY_AUDIT_G10_A.json"),
    "g11_report": Path("docs/coordination/UNI_REDUNDANCY_PRIORITY_G11_A.json"),
    "g12_report": Path("docs/coordination/UNI_CLUSTER_REVIEW_G12_A.json"),
    "g12_guide": Path("docs/coordination/UNI_CLUSTER_REVIEW_G12_A.md"),
    "g13_report": Path("docs/coordination/UNI_CLUSTER_REVIEW_PACKET_G13_A.json"),
    "g13_guide": Path("docs/coordination/UNI_CLUSTER_REVIEW_PACKET_G13_A.md"),
    "g14_report": Path("docs/coordination/UNI_CLUSTER_REVIEW_PROGRESS_G14_A.json"),
    "g14_guide": Path("docs/coordination/UNI_CLUSTER_REVIEW_PROGRESS_G14_A.md"),
}

PROTECTED_ARTIFACTS = tuple(
    dict.fromkeys(
        (
            *GENERATED_ARTIFACTS.values(),
            Path("docs/coordination/UNI_REDUNDANCY_AUDIT_G10_A.schema.json"),
            Path("docs/coordination/UNI_REDUNDANCY_PRIORITY_G11_A.schema.json"),
            Path("docs/coordination/UNI_CLUSTER_REVIEW_G12_A.schema.json"),
            Path("docs/coordination/UNI_CLUSTER_REVIEW_PACKET_G13_A.schema.json"),
            Path("docs/coordination/UNI_CLUSTER_REVIEW_PROGRESS_G14_A.schema.json"),
        )
    )
)

JSON_ARTIFACTS = {
    name for name in GENERATED_ARTIFACTS if name.endswith("_report")
}


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _copy_file(source: Path, destination_root: Path, source_root: Path) -> None:
    destination = destination_root / source.relative_to(source_root)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)


def _stage_inputs(source_root: Path, staging_root: Path) -> list[Path]:
    source_files = [
        *g10.discover_card_files(source_root),
        *g10.discover_exam_files(source_root),
    ]
    for source in source_files:
        _copy_file(source, staging_root, source_root)

    g4_path = source_root / g13.G4_RELATIVE_PATH
    if not g4_path.is_file():
        raise FileNotFoundError(f"required G4 report is missing: {g4_path}")
    _copy_file(g4_path, staging_root, source_root)
    return source_files


def _run_generators(staging_root: Path) -> None:
    """Run G10-A through G14-A using only the temporary root and outputs."""

    g10.write_report(staging_root, g10.REPORT_RELATIVE_PATH)
    g11.write_report(
        staging_root,
        g11.INPUT_RELATIVE_PATH,
        g11.REPORT_RELATIVE_PATH,
    )
    g12.write_reports(
        staging_root,
        g12.INPUT_RELATIVE_PATH,
        g12.REPORT_RELATIVE_PATH,
    )
    g13.write_reports(staging_root)
    g14.write_reports(staging_root)


def _snapshot(paths: Iterable[Path], root: Path) -> dict[str, bytes | None]:
    return {
        path.as_posix(): (root / path).read_bytes() if (root / path).is_file() else None
        for path in paths
    }


def _check(name: str, expected: Any, actual: Any) -> dict[str, Any]:
    return {
        "name": name,
        "expected": expected,
        "actual": actual,
        "ok": expected == actual,
    }


def _path_value(value: Any, path: tuple[str, ...]) -> Any:
    current = value
    for part in path:
        if not isinstance(current, dict):
            return None
        current = current.get(part)
    return current


def _invariant_checks(
    reports: dict[str, tuple[dict[str, Any], dict[str, Any]]]
) -> dict[str, list[dict[str, Any]]]:
    """Return explicit drift checks, with published values as the baseline."""

    checks: dict[str, list[dict[str, Any]]] = {}

    g10_published, g10_generated = reports["g10_report"]
    checks["g10"] = [
        _check(
            "file_counts_by_source_group",
            _path_value(g10_published, ("evidence", "file_counts_by_source_group")),
            _path_value(g10_generated, ("evidence", "file_counts_by_source_group")),
        ),
        _check(
            "unit_counts_by_source_group",
            _path_value(g10_published, ("evidence", "unit_counts_by_source_group")),
            _path_value(g10_generated, ("evidence", "unit_counts_by_source_group")),
        ),
        _check(
            "candidate_review_count",
            len(_path_value(g10_published, ("results", "candidate_review")) or []),
            len(_path_value(g10_generated, ("results", "candidate_review")) or []),
        ),
        _check(
            "exact_duplicate_group_count",
            len(_path_value(g10_published, ("results", "duplicate_exact")) or []),
            len(_path_value(g10_generated, ("results", "duplicate_exact")) or []),
        ),
        _check(
            "classification_counts",
            _path_value(g10_published, ("results", "classification_counts")),
            _path_value(g10_generated, ("results", "classification_counts")),
        ),
    ]

    g11_published, g11_generated = reports["g11_report"]
    checks["g11"] = [
        _check(
            "candidate_pair_count",
            _path_value(g11_published, ("results", "candidate_pair_count")),
            _path_value(g11_generated, ("results", "candidate_pair_count")),
        ),
        _check(
            "connected_component_count",
            _path_value(g11_published, ("results", "connected_component_count")),
            _path_value(g11_generated, ("results", "connected_component_count")),
        ),
        _check(
            "unit_count",
            _path_value(g11_published, ("results", "unit_count")),
            _path_value(g11_generated, ("results", "unit_count")),
        ),
        _check(
            "priority_ranks",
            [item.get("priority_rank") for item in g11_published["results"]["queue"]],
            [item.get("priority_rank") for item in g11_generated["results"]["queue"]],
        ),
    ]

    g12_published, g12_generated = reports["g12_report"]
    checks["g12"] = [
        _check(
            "component_count",
            _path_value(g12_published, ("coverage", "component_count")),
            _path_value(g12_generated, ("coverage", "component_count")),
        ),
        _check(
            "pending_count",
            _path_value(g12_published, ("coverage", "pending_count")),
            _path_value(g12_generated, ("coverage", "pending_count")),
        ),
        _check(
            "decided_count",
            _path_value(g12_published, ("coverage", "decided_count")),
            _path_value(g12_generated, ("coverage", "decided_count")),
        ),
        _check(
            "all_decisions_null",
            _path_value(g12_published, ("coverage", "all_decisions_null")),
            _path_value(g12_generated, ("coverage", "all_decisions_null")),
        ),
    ]

    g13_published, g13_generated = reports["g13_report"]
    checks["g13"] = [
        _check(
            "cluster_count",
            _path_value(g13_published, ("coverage", "cluster_count")),
            _path_value(g13_generated, ("coverage", "cluster_count")),
        ),
        _check(
            "batch_count",
            _path_value(g13_published, ("coverage", "batch_count")),
            _path_value(g13_generated, ("coverage", "batch_count")),
        ),
        _check(
            "pending_count",
            _path_value(g13_published, ("coverage", "pending_count")),
            _path_value(g13_generated, ("coverage", "pending_count")),
        ),
        _check(
            "cluster_ids",
            [item.get("cluster_id") for item in g13_published["clusters"]],
            [item.get("cluster_id") for item in g13_generated["clusters"]],
        ),
        _check(
            "batch_ids",
            [item.get("batch_id") for item in g13_published["batches"]],
            [item.get("batch_id") for item in g13_generated["batches"]],
        ),
    ]

    g14_published, g14_generated = reports["g14_report"]
    checks["g14"] = [
        _check(
            "cluster_count",
            _path_value(g14_published, ("coverage", "cluster_count")),
            _path_value(g14_generated, ("coverage", "cluster_count")),
        ),
        _check(
            "batch_count",
            _path_value(g14_published, ("coverage", "batch_count")),
            _path_value(g14_generated, ("coverage", "batch_count")),
        ),
        _check(
            "status_counts",
            _path_value(g14_published, ("coverage", "status_counts")),
            _path_value(g14_generated, ("coverage", "status_counts")),
        ),
        _check(
            "open_count",
            _path_value(g14_published, ("coverage", "open_count")),
            _path_value(g14_generated, ("coverage", "open_count")),
        ),
        _check(
            "in_review_count",
            _path_value(g14_published, ("coverage", "in_review_count")),
            _path_value(g14_generated, ("coverage", "in_review_count")),
        ),
        _check(
            "decided_count",
            _path_value(g14_published, ("coverage", "decided_count")),
            _path_value(g14_generated, ("coverage", "decided_count")),
        ),
        _check(
            "cluster_statuses",
            [item.get("status") for item in g14_published["clusters"]],
            [item.get("status") for item in g14_generated["clusters"]],
        ),
    ]
    return checks


def _write_output(path: Path, report: dict[str, Any], published_root: Path) -> None:
    resolved = path.resolve()
    protected = {
        (published_root / relative).resolve() for relative in PROTECTED_ARTIFACTS
    }
    if resolved in protected:
        raise ValueError(f"G15 output cannot overwrite a protected artifact: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run_audit(
    root: Path,
    *,
    published_root: Path | None = None,
    output_path: Path | None = None,
) -> dict[str, Any]:
    """Run G10-A through G14-A in temporary output and return the audit report."""

    source_root = root.resolve()
    published_root = (published_root or source_root).resolve()
    resolved_output = None
    if output_path is not None:
        resolved_output = output_path if output_path.is_absolute() else source_root / output_path
        protected = {
            (published_root / relative).resolve() for relative in PROTECTED_ARTIFACTS
        }
        if resolved_output.resolve() in protected:
            raise ValueError(f"G15 output cannot overwrite a protected artifact: {output_path}")
    published_before = _snapshot(PROTECTED_ARTIFACTS, published_root)
    source_files = [
        *g10.discover_card_files(source_root),
        *g10.discover_exam_files(source_root),
    ]
    source_before = _snapshot(
        [path.relative_to(source_root) for path in source_files], source_root
    )

    scratch_root = source_root / "work"
    scratch_root.mkdir(parents=True, exist_ok=True)
    staging_root = scratch_root / f"uni_g15_audit_{uuid.uuid4().hex}"
    staging_root.mkdir(parents=True)
    try:
        _stage_inputs(source_root, staging_root)
        _run_generators(staging_root)

        reports: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
        artifact_results: dict[str, dict[str, Any]] = {}
        drift: list[str] = []
        for name, relative in GENERATED_ARTIFACTS.items():
            published_path = published_root / relative
            generated_path = staging_root / relative
            published_exists = published_path.is_file()
            generated_exists = generated_path.is_file()
            published_bytes = published_path.read_bytes() if published_exists else None
            generated_bytes = generated_path.read_bytes() if generated_exists else None
            byte_match = (
                published_exists
                and generated_exists
                and published_bytes == generated_bytes
            )
            result = {
                "path": relative.as_posix(),
                "published_exists": published_exists,
                "generated_exists": generated_exists,
                "published_sha256": _sha256(published_bytes) if published_bytes is not None else None,
                "generated_sha256": _sha256(generated_bytes) if generated_bytes is not None else None,
                "byte_match": byte_match,
            }
            if name in JSON_ARTIFACTS and published_exists and generated_exists:
                published_json = json.loads(published_bytes.decode("utf-8"))
                generated_json = json.loads(generated_bytes.decode("utf-8"))
                result["json_match"] = published_json == generated_json
                if name in {"g10_report", "g11_report", "g12_report", "g13_report", "g14_report"}:
                    reports[name] = (published_json, generated_json)
            else:
                result["json_match"] = None
            artifact_results[name] = result
            if not byte_match:
                drift.append(f"{name}.report_or_guide")
            if result.get("json_match") is False:
                drift.append(f"{name}.json")

        required_reports = {name for name in GENERATED_ARTIFACTS if name.endswith("_report")}
        invariants = (
            _invariant_checks(reports)
            if required_reports.issubset(reports)
            else {group: [] for group in ("g10", "g11", "g12", "g13", "g14")}
        )
        for group, group_checks in invariants.items():
            for check in group_checks:
                if not check["ok"]:
                    drift.append(f"{group}.{check['name']}")
    finally:
        shutil.rmtree(staging_root)

    published_after = _snapshot(PROTECTED_ARTIFACTS, published_root)
    protected_unchanged = published_before == published_after
    if not protected_unchanged:
        drift.append("published_artifacts_modified")

    source_after = _snapshot(
        [path.relative_to(source_root) for path in source_files], source_root
    )
    source_unchanged = source_before == source_after
    if not source_unchanged:
        drift.append("card_or_exam_sources_modified")

    report = {
        "schema_version": SCHEMA_VERSION,
        "tool": TOOL_PATH,
        "scope": {
            "root": ".",
            "generators_rerun": ["G10-A", "G11-A", "G12-A", "G13-A", "G14-A"],
            "temporary_output": True,
            "published_artifacts_written": False,
            "cards_and_exams_written": False,
            "answers_read": False,
            "didactic_content_modified": False,
        },
        "artifacts": artifact_results,
        "invariants": invariants,
        "integrity": {
            "published_artifacts_unchanged": protected_unchanged,
            "card_and_exam_sources_unchanged": source_unchanged,
        },
        "drift": sorted(set(drift)),
        "passed": not drift,
    }
    if resolved_output is not None:
        _write_output(resolved_output, report, published_root)
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument(
        "--published-root",
        type=Path,
        help="checkout containing the baseline G10-G14 artifacts; defaults to --root",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="optional G15 report path; G10-G14 artifacts are always protected",
    )
    args = parser.parse_args(argv)
    report = run_audit(
        args.root,
        published_root=args.published_root,
        output_path=args.output,
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
