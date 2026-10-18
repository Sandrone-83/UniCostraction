"""Deterministic, metadata-only checks for the G13-B pack coverage audit."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "docs/coordination/UNI_PACK_PROVENANCE_COVERAGE_G13_B_SCHEMA.json"
REPORT_PATH = ROOT / "docs/coordination/UNI_PACK_PROVENANCE_COVERAGE_G13_B.json"
sys.path.insert(0, str(ROOT))
from tools.audit_pack_provenance_g13_b import build_audit  # noqa: E402


class G13BPackProvenanceCoverageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    def test_schema_contract_and_base_commit_are_anchored(self) -> None:
        self.assertEqual(self.report["$schema"], "./UNI_PACK_PROVENANCE_COVERAGE_G13_B_SCHEMA.json")
        self.assertEqual(self.report["schema_version"], "G13-B-pack-provenance-coverage")
        self.assertEqual(self.schema["properties"]["base_commit"]["const"], "5563510cbf40c1e2a5476cb64be845947c68e710")
        self.assertEqual(self.report["base_commit"], "5563510cbf40c1e2a5476cb64be845947c68e710")
        self.assertTrue(self.report["metadata_only"])

    def test_all_71_courses_are_reported_once_in_sorted_order(self) -> None:
        rows = self.report["packs"]
        self.assertEqual(len(rows), 71)
        self.assertEqual([row["pack_path"] for row in rows], sorted(row["pack_path"] for row in rows))
        self.assertEqual(len({row["pack_path"] for row in rows}), 71)
        self.assertEqual(self.report["summary"]["pack_count"], 71)

    def test_matching_is_explicit_and_only_g3_pack_is_matched(self) -> None:
        matched = [row for row in self.report["packs"] if row["matched_source_records"]]
        self.assertEqual(len(matched), 1)
        row = matched[0]
        self.assertEqual(row["pack_path"], "UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK")
        self.assertEqual(row["source_record_present"], "observed_local")
        self.assertEqual(row["locator_present"], "observed_local")
        self.assertEqual(row["license_status"], "blocked")
        self.assertEqual(row["evidence_status"], "blocked")
        self.assertTrue(all(item["match_basis"] == "scope.package_exact" for item in row["matched_source_records"]))

    def test_unmatched_rows_are_conservative_and_never_semantically_linked(self) -> None:
        for row in self.report["packs"]:
            self.assertTrue(row["remediation_required"])
            self.assertNotIn("course_name", row["matching_note"])
            if not row["matched_source_records"]:
                self.assertEqual(row["source_record_present"], "blocked")
                self.assertEqual(row["locator_present"], "blocked")
                self.assertEqual(row["license_status"], "blocked")
                self.assertEqual(row["evidence_status"], "blocked")

    def test_report_is_reproducible(self) -> None:
        self.assertEqual(self.report, build_audit())


if __name__ == "__main__":
    unittest.main()
