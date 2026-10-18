"""Deterministic, metadata-only checks for the G15-B reconciliation."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "docs/coordination/UNI_MANIFEST_RECONCILIATION_G15_B.json"
SCHEMA_PATH = ROOT / "docs/coordination/UNI_MANIFEST_RECONCILIATION_G15_B_SCHEMA.json"
sys.path.insert(0, str(ROOT / "tools"))

from reconcile_manifest_g15_b import (  # noqa: E402
    BASE_COMMIT,
    EXPECTED_REPORT_IDS,
    REPORT_SCHEMA_VERSION,
    build_report,
    validate_report,
)


class G15BManifestReconciliationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
        self.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    def test_report_and_schema_are_json_and_anchored(self) -> None:
        validate_report(self.report)
        self.assertEqual(self.report["$schema"], "./UNI_MANIFEST_RECONCILIATION_G15_B_SCHEMA.json")
        self.assertEqual(self.report["schema_version"], REPORT_SCHEMA_VERSION)
        self.assertEqual(self.schema["properties"]["schema_version"]["const"], REPORT_SCHEMA_VERSION)
        self.assertEqual(self.report["base_commit"], BASE_COMMIT)
        self.assertEqual(self.schema["properties"]["base_commit"]["const"], BASE_COMMIT)
        self.assertTrue(self.report["metadata_only"])

    def test_g5_to_g14_inventory_exposes_missing_g8(self) -> None:
        self.assertEqual(
            [item["report_id"] for item in self.report["input_reports"]],
            list(EXPECTED_REPORT_IDS),
        )
        self.assertEqual(self.report["scope"]["available_report_ids"], ["G5", "G6", "G7", "G9", "G10", "G11", "G12", "G13", "G14"])
        self.assertEqual(self.report["scope"]["missing_report_ids"], ["G8"])
        g8 = next(item for item in self.report["input_reports"] if item["report_id"] == "G8")
        self.assertFalse(g8["present"])
        self.assertEqual(g8["status"], "missing_in_checkout")

    def test_record_reconciliation_keeps_aliases_and_path_hash(self) -> None:
        self.assertEqual(self.report["summary"]["record_count"], 34)
        self.assertEqual(self.report["summary"]["alias_group_count"], 14)
        self.assertEqual(self.report["summary"]["record_rows_with_aliases"], 28)
        aliases = self.report["duplicate_alias_groups"]
        self.assertTrue(all(item["relation"] == "exact_path_hash_alias" for item in aliases))
        self.assertTrue(all(not item["deduplication_performed"] for item in aliases))
        self.assertTrue(all(not item["semantic_deduplication_performed"] for item in aliases))
        g1 = next(
            item
            for item in self.report["record_reconciliation"]
            if item["record_key"] == "Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-001"
        )
        self.assertEqual(g1["path_hash"]["hash_algorithm"], "SHA-256")
        self.assertTrue(g1["path_hash"]["identity_key"].endswith("#A68264A6537BB58B899ED68E25D1C7D8EA1BCB3E9544B4D1B464F74D99C3D059"))
        self.assertEqual(g1["package_scope"]["status"], "not_declared")
        self.assertIn("G7-B-ALIAS-2d05db44caa2", [item["item_id"] for item in g1["remediation"]["g7_items"]])
        self.assertIn("G7-B-ALIAS-2d05db44caa2", g1["remediation"]["g9_item_ids"])

    def test_license_evidence_and_pack_scope_are_conservative(self) -> None:
        g10 = next(item for item in self.report["record_reconciliation"] if item["record_id"] == "G10-B-001")
        self.assertEqual(g10["package_scope"]["declared"], "docs/coordination")
        self.assertEqual(g10["license_status"]["state"], "blocked")
        self.assertEqual(g10["evidence_status"]["state"], "blocked")
        self.assertFalse(g10["evidence_status"]["claim_ready"])
        energy_pack = next(item for item in self.report["pack_reconciliation"] if item["pack_id"] == "ENERGETICA_INCENTIVI_PACK")
        self.assertEqual(energy_pack["package_scope_status"], "exact_manifest_scope")
        self.assertEqual(energy_pack["g13_license_status"], "blocked")
        self.assertIsNone(energy_pack["g14_queue_item_id"])
        self.assertEqual(self.report["summary"]["g14_blocked_pack_count"], 70)

    def test_no_payload_or_state_promotion(self) -> None:
        serialized = json.dumps(self.report, ensure_ascii=False).lower()
        for forbidden in ('"text"', '"content"', '"question"', '"answer"', '"solution"'):
            self.assertNotIn(forbidden, serialized)
        self.assertNotIn('"claim_ready": true', serialized)
        self.assertNotIn('"deduplication_performed": true', serialized)

    def test_generation_is_reproducible(self) -> None:
        self.assertEqual(self.report, build_report(ROOT))


if __name__ == "__main__":
    unittest.main()
