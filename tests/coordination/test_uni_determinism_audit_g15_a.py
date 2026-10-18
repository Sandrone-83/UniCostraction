from __future__ import annotations

import json
import shutil
import unittest
from pathlib import Path
from shutil import copyfile
from uuid import uuid4

from tools.uni_determinism_audit_g15_a import (
    GENERATED_ARTIFACTS,
    PROTECTED_ARTIFACTS,
    run_audit,
)
from tools.uni_redundancy_audit_g10_a import discover_card_files, discover_exam_files


class UniDeterminismAuditG15ATest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = Path(__file__).parents[2]

    def _snapshot(self, paths: list[Path]) -> dict[str, bytes]:
        return {path.as_posix(): path.read_bytes() for path in paths}

    def _temporary_directory(self, prefix: str) -> Path:
        directory = self.root / "work" / f"{prefix}{uuid4().hex}"
        directory.mkdir(parents=True)
        return directory

    def test_tracked_chain_regenerates_without_writing_published_or_didactic_files(self) -> None:
        source_files = [*discover_card_files(self.root), *discover_exam_files(self.root)]
        protected_files = [
            self.root / relative
            for relative in PROTECTED_ARTIFACTS
            if (self.root / relative).is_file()
        ]
        source_before = self._snapshot(source_files)
        protected_before = self._snapshot(protected_files)

        report = run_audit(self.root)

        self.assertTrue(report["passed"], report["drift"])
        self.assertEqual(report["drift"], [])
        self.assertTrue(report["integrity"]["published_artifacts_unchanged"])
        self.assertTrue(report["integrity"]["card_and_exam_sources_unchanged"])
        self.assertEqual(report["invariants"]["g10"][0]["actual"], {"cards": 71, "public_exams": 73})
        self.assertEqual(report["invariants"]["g13"][0]["actual"], 85)
        self.assertEqual(report["invariants"]["g14"][2]["actual"], {"open": 85, "in_review": 0, "decided": 0})
        self.assertEqual(source_before, self._snapshot(source_files))
        self.assertEqual(protected_before, self._snapshot(protected_files))

    def test_drift_in_temp_published_baseline_is_reported_by_category(self) -> None:
        baseline_root = self._temporary_directory("uni_g15_baseline_")
        try:
            for relative in PROTECTED_ARTIFACTS:
                source = self.root / relative
                if source.is_file():
                    destination = baseline_root / relative
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    copyfile(source, destination)

            g14_path = baseline_root / GENERATED_ARTIFACTS["g14_report"]
            g14_report = json.loads(g14_path.read_text(encoding="utf-8"))
            g14_report["coverage"]["status_counts"]["open"] = 84
            g14_path.write_text(json.dumps(g14_report, indent=2) + "\n", encoding="utf-8")

            report = run_audit(self.root, published_root=baseline_root)
        finally:
            shutil.rmtree(baseline_root)

        self.assertFalse(report["passed"])
        self.assertIn("g14_report.report_or_guide", report["drift"])
        self.assertIn("g14.status_counts", report["drift"])

    def test_optional_output_is_json_and_cannot_target_protected_artifact(self) -> None:
        output_root = self._temporary_directory("uni_g15_output_")
        try:
            output = output_root / "g15.json"
            report = run_audit(self.root, output_path=output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), report)
        finally:
            shutil.rmtree(output_root)

        with self.assertRaises(ValueError):
            run_audit(self.root, output_path=self.root / GENERATED_ARTIFACTS["g14_report"])


if __name__ == "__main__":
    unittest.main()
