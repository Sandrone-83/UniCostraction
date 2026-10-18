"""Tests for the deterministic G19 JSON adapter around the G18 validator."""

from __future__ import annotations

import json
import unittest
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from tools import run_skill_library_qa_g19 as runner


class SkillLibraryQARunnerG19Tests(unittest.TestCase):
    """Use mocked in-memory discovery instead of system temporary directories."""

    ROOT = Path("fixture-library")
    DISCOVERED = (ROOT / "edilizia" / "skill-cila-basics" / "SKILL.md",)

    def test_valid_fixture_emits_zero_exit_status_and_skill_count(self) -> None:
        with patch.object(runner.markdown_validator, "validate_library", return_value=[]) as validate, patch.object(
            runner.markdown_validator, "_library_files", return_value=self.DISCOVERED
        ):
            report = runner.build_report(self.ROOT)

        self.assertEqual(
            {"count": 1, "findings": [], "exit_status": 0},
            report,
        )
        validate.assert_called_once_with(self.ROOT.resolve())

    def test_findings_are_sorted_deduplicated_and_fail_closed(self) -> None:
        findings = ["zeta: finding", "alpha: finding", "zeta: finding"]
        with patch.object(runner.markdown_validator, "validate_library", return_value=findings), patch.object(
            runner.markdown_validator, "_library_files", return_value=()
        ):
            report = runner.build_report(self.ROOT)

        self.assertEqual(
            {"count": 0, "findings": ["alpha: finding", "zeta: finding"], "exit_status": 1},
            report,
        )

    def test_cli_output_is_stable_json_and_returns_report_exit_status(self) -> None:
        report = {"count": 1, "findings": ["fixture finding"], "exit_status": 1}
        output = StringIO()
        with patch.object(runner, "build_report", return_value=report), patch("sys.stdout", output):
            status = runner.main([self.ROOT.as_posix()])

        self.assertEqual(1, status)
        self.assertEqual(
            '{"count":1,"exit_status":1,"findings":["fixture finding"]}\n',
            output.getvalue(),
        )
        self.assertEqual(report, json.loads(output.getvalue()))


if __name__ == "__main__":
    unittest.main()
