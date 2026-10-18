"""Deterministic metadata-only checks for the G6-B provenance audit."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

from audit_provenance_g6 import (  # noqa: E402
    ALLOWED_STATES,
    REPORT_SCHEMA_VERSION,
    build_report,
    validate_report,
)


REPORT_PATH = ROOT / "docs" / "coordination" / "UNI_PROVENANCE_AUDIT_G6.json"
SCHEMA_PATH = ROOT / "docs" / "coordination" / "UNI_PROVENANCE_AUDIT_G6_SCHEMA.json"


class G6ProvenanceAuditTest(unittest.TestCase):
    def setUp(self) -> None:
        self.report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    def test_report_is_valid_and_metadata_only(self) -> None:
        validate_report(self.report)
        self.assertEqual(self.report["schema_version"], REPORT_SCHEMA_VERSION)
        self.assertTrue(self.report["metadata_only"])
        self.assertEqual(self.report["$schema"], "./UNI_PROVENANCE_AUDIT_G6_SCHEMA.json")
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["schema_version"]["const"], REPORT_SCHEMA_VERSION)
        serialized = json.dumps(self.report, ensure_ascii=False).lower()
        for forbidden_key in ('"text"', '"content"', '"question"', '"answer"', '"solution"'):
            self.assertNotIn(forbidden_key, serialized)

    def test_current_state_distribution_is_not_promoted(self) -> None:
        self.assertEqual(
            self.report["summary"]["by_proof_state"],
            {"verified": 0, "observed_local": 29, "context_only": 2, "blocked": 2},
        )
        self.assertEqual(self.report["summary"]["record_count"], 33)

    def test_url_and_license_gaps_are_explicit(self) -> None:
        self.assertEqual(
            self.report["summary"]["by_url_status"],
            {"declared": 31, "not_declared": 2},
        )
        self.assertEqual(
            self.report["summary"]["by_license_status"],
            {"declared": 29, "not_declared": 4},
        )
        blocked = [record for record in self.report["records"] if record["proof_state"] == "blocked"]
        self.assertEqual(len(blocked), 2)
        self.assertTrue(all("exact_url_not_declared" in item["residual_codes"] for item in blocked))

    def test_manifest_aliases_are_reported_without_deduplication(self) -> None:
        aliases = self.report["alias_groups"]
        self.assertGreaterEqual(len(aliases), 1)
        g1_g2_alias = next(
            item for item in aliases if item["local_path"].startswith("Fondamenti_Pack/raw/gutenberg/")
        )
        self.assertEqual(g1_g2_alias["representation_count"], 2)
        self.assertEqual(len(self.report["records"]), 33)

    def test_legacy_g1_contract_gaps_are_visible(self) -> None:
        legacy_g1 = [
            record
            for record in self.report["records"]
            if record["manifest_id"] == "G1-FONDAMENTI-GUTENBERG-RAW"
        ]
        self.assertEqual(len(legacy_g1), 14)
        for record in legacy_g1:
            self.assertIn("manifest_metadata_only_flag_not_declared", record["residual_codes"])
            self.assertIn("manifest_id_not_declared_lot_id_used_as_reference", record["residual_codes"])

    def test_generation_is_deterministic(self) -> None:
        second = build_report(ROOT)
        self.assertEqual(self.report, second)
        self.assertEqual(set(self.report["summary"]["by_proof_state"]), set(ALLOWED_STATES))


if __name__ == "__main__":
    unittest.main()
