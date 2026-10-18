"""Emit a deterministic JSON report for the G18 Markdown skill validator.

This runner is a structural QA adapter only.  A passing report does not prove
factual, educational, technical, normative, safety, professional, or legal
correctness, and it does not clear a source or licence for use.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence

if __package__:
    from . import validate_skill_markdown_g18 as markdown_validator
else:
    # ``python tools/run_skill_library_qa_g19.py`` puts only ``tools`` on
    # sys.path; add the repository root so the validator is still imported as
    # the existing ``tools`` module rather than duplicated as a top-level one.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from tools import validate_skill_markdown_g18 as markdown_validator


def build_report(library: Path) -> dict[str, Any]:
    """Run G18 and return the stable report contract for ``library``."""

    root = Path(library).resolve()
    findings = sorted(set(markdown_validator.validate_library(root)))
    count = sum(
        1
        for path in markdown_validator._library_files(root)
        if path.name == markdown_validator.SKILL_FILENAME
    )
    return {
        "count": count,
        "findings": findings,
        "exit_status": 1 if findings else 0,
    }


def render_report(report: dict[str, Any]) -> str:
    """Serialize a report without path, timestamp, or formatting drift."""

    return json.dumps(report, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("library", type=Path, help="G18 Markdown skill-library directory")
    args = parser.parse_args(argv)

    report = build_report(args.library)
    print(render_report(report))
    return int(report["exit_status"])


if __name__ == "__main__":
    raise SystemExit(main())
