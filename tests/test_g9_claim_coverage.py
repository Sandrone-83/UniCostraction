"""Deterministic checks for the G9-B provenance index and claim coverage."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from audit_claim_coverage_g9 import (  # noqa: E402
    REPORT_SCHEMA_VERSION,
    build_report,
    validate_report,
)


REPORT_PATH = ROOT / "docs" / "coordination" / "UNI_CLAIM_COVERAGE_G9_B.json"
SCHEMA_PATH = ROOT / "docs" / "coordination" / "UNI_CLAIM_COVERAGE_G9_B_SCHEMA.json"


class G9ClaimCoverageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    def test_report_is_deterministic_and_schema_anchored(self) -> None:
        validate_report(self.report)
        self.assertEqual(self.report["schema_version"], REPORT_SCHEMA_VERSION)
        self.assertEqual(self.report["$schema"], "./UNI_CLAIM_COVERAGE_G9_B_SCHEMA.json")
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["schema_version"]["const"], REPORT_SCHEMA_VERSION)
        self.assertEqual(self.report, build_report(ROOT))

    def test_presence_fields_are_distinct_and_counts_are_explicit(self) -> None:
        self.assertEqual(self.report["summary"]["record_count"], 33)
        self.assertEqual(self.report["summary"]["source_record_present_count"], 30)
        self.assertEqual(self.report["summary"]["url_present_count"], 31)
        self.assertEqual(self.report["summary"]["license_present_count"], 29)
        self.assertEqual(self.report["summary"]["by_evidence_status"], {
            "verified": 0,
            "observed_local": 29,
            "context_only": 2,
            "blocked": 2,
        })

    def test_no_claim_is_promoted_to_ready_without_explicit_evidence(self) -> None:
        self.assertEqual(self.report["summary"]["claim_ready_count"], 0)
        self.assertEqual(self.report["summary"]["remediation_claim_ready_count"], 0)
        self.assertTrue(all(not record["claim_ready"] for record in self.report["records"]))
        self.assertTrue(all(not item["coverage"]["claim_ready"] for item in self.report["remediation_coverage"]))
        self.assertTrue(all("explicit_claim_ready_evidence_missing" in record["residual_codes"] for record in self.report["records"]))

    def test_all_48_queue_items_are_linked_without_payloads(self) -> None:
        self.assertEqual(len(self.report["remediation_coverage"]), 48)
        self.assertEqual(self.report["summary"]["remediation_open_item_count"], 48)
        self.assertTrue(all(item["status"] == "open" for item in self.report["remediation_coverage"]))
        self.assertTrue(all(item["record_keys"] for item in self.report["remediation_coverage"]))
        serialized = json.dumps(self.report, ensure_ascii=False).lower()
        for forbidden_key in ('"text"', '"content"', '"question"', '"answer"', '"solution"'):
            self.assertNotIn(forbidden_key, serialized)

    def test_context_and_blocked_records_remain_distinct(self) -> None:
        context = [record for record in self.report["records"] if record["evidence_status"] == "context_only"]
        blocked = [record for record in self.report["records"] if record["evidence_status"] == "blocked"]
        self.assertEqual(len(context), 2)
        self.assertEqual(len(blocked), 2)
        self.assertTrue(all(not record["source_record_present"] for record in context))
        self.assertTrue(all(not record["claim_ready"] for record in context + blocked))


if __name__ == "__main__":
    unittest.main()
