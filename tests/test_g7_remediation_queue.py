"""Deterministic checks for the G7-B provenance remediation queue."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

from build_remediation_queue_g7 import (  # noqa: E402
    CATEGORY_ORDER,
    QUEUE_SCHEMA_VERSION,
    build_queue,
    validate_queue,
)


REPORT_PATH = ROOT / "docs" / "coordination" / "UNI_REMEDIATION_QUEUE_G7_B.json"
SCHEMA_PATH = ROOT / "docs" / "coordination" / "UNI_REMEDIATION_QUEUE_G7_B_SCHEMA.json"
G6_PATH = ROOT / "docs" / "coordination" / "UNI_PROVENANCE_AUDIT_G6.json"


class G7RemediationQueueTest(unittest.TestCase):
    def setUp(self) -> None:
        self.report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
        self.g6 = json.loads(G6_PATH.read_text(encoding="utf-8"))

    def test_report_is_valid_metadata_only_and_schema_anchored(self) -> None:
        validate_queue(self.report)
        self.assertEqual(self.report["schema_version"], QUEUE_SCHEMA_VERSION)
        self.assertTrue(self.report["metadata_only"])
        self.assertEqual(self.report["$schema"], "./UNI_REMEDIATION_QUEUE_G7_B_SCHEMA.json")
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["schema_version"]["const"], QUEUE_SCHEMA_VERSION)

    def test_requested_gap_counts_are_explicit(self) -> None:
        self.assertEqual(
            self.report["summary"]["by_category"],
            {
                "missing_manifest_id": 14,
                "missing_metadata_only": 14,
                "license_missing": 4,
                "g3_pdf_blocked": 1,
                "gse_context_only": 1,
                "alias_not_deduplicated": 14,
            },
        )
        self.assertEqual(self.report["summary"]["item_count"], 48)
        self.assertEqual(self.report["summary"]["open_item_count"], 48)
        self.assertEqual(self.report["summary"]["by_status"], {"open": 48})
        self.assertEqual(self.report["scope"]["included_categories"], list(CATEGORY_ORDER))

    def test_each_item_points_to_g6_and_has_closure_contract(self) -> None:
        record_keys = {record["record_key"] for record in self.g6["records"]}
        alias_refs = {"alias:" + item["hash_sha256"] for item in self.g6["alias_groups"]}
        for item in self.report["items"]:
            self.assertEqual(item["source_audit"]["audit_id"], self.g6["audit_id"])
            self.assertIn(item["source_ref"], record_keys | alias_refs)
            self.assertEqual(item["status"], "open")
            self.assertFalse(item["closure_evidence"])
            self.assertGreater(len(item["closure_criteria"]), 0)
            self.assertIn("Do not modify source files or source payloads.", item["constraints"])

    def test_g1_g3_gse_and_alias_boundaries_are_preserved(self) -> None:
        manifest_ids = [item for item in self.report["items"] if item["category"] == "missing_manifest_id"]
        metadata_flags = [item for item in self.report["items"] if item["category"] == "missing_metadata_only"]
        self.assertTrue(all(item["record"]["manifest_path"].endswith("UNI_CORPUS_LOTTO_G1.json") for item in manifest_ids))
        self.assertTrue(all(item["record"]["manifest_path"].endswith("UNI_CORPUS_LOTTO_G1.json") for item in metadata_flags))
        pdf = next(item for item in self.report["items"] if item["category"] == "g3_pdf_blocked")
        self.assertEqual(pdf["record"]["proof_state"], "blocked")
        self.assertTrue(pdf["record"]["local_path"].endswith(".pdf"))
        gse = next(item for item in self.report["items"] if item["category"] == "gse_context_only")
        self.assertEqual(gse["record"]["proof_state"], "context_only")
        aliases = [item for item in self.report["items"] if item["category"] == "alias_not_deduplicated"]
        self.assertTrue(all(item["observed_gap"]["deduplication_performed"] is False for item in aliases))

    def test_generation_is_deterministic_and_does_not_contain_payload_keys(self) -> None:
        self.assertEqual(self.report, build_queue(ROOT))
        serialized = json.dumps(self.report, ensure_ascii=False).lower()
        for forbidden_key in ('"text"', '"content"', '"question"', '"answer"', '"solution"'):
            self.assertNotIn(forbidden_key, serialized)


if __name__ == "__main__":
    unittest.main()
