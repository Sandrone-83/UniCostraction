"""Deterministic metadata-only checks for the G16-B coherence report."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "docs/coordination/UNI_PACK_SOURCE_COHERENCE_G16_B.json"
SCHEMA_PATH = ROOT / "docs/coordination/UNI_PACK_SOURCE_COHERENCE_G16_B_SCHEMA.json"
sys.path.insert(0, str(ROOT))
from tools.audit_pack_source_coherence_g16_b import BASE_COMMIT, build_report, validate_report  # noqa: E402


class G16BPackSourceCoherenceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
        self.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    def test_report_and_schema_are_anchored(self) -> None:
        validate_report(self.report)
        self.assertEqual(self.report["base_commit"], BASE_COMMIT)
        self.assertEqual(self.schema["properties"]["base_commit"]["const"], BASE_COMMIT)
        self.assertTrue(self.report["metadata_only"])

    def test_every_pack_appears_once_and_inputs_have_expected_cardinality(self) -> None:
        rows = self.report["packs"]
        self.assertEqual(len(rows), 71)
        self.assertEqual([row["pack_path"] for row in rows], sorted(row["pack_path"] for row in rows))
        self.assertEqual(len({row["pack_path"] for row in rows}), 71)
        self.assertEqual([item["report_id"] for item in self.report["input_reports"]], ["G13", "G14", "G15"])
        self.assertEqual(self.report["summary"]["g13_pack_count"], 71)
        self.assertEqual(self.report["summary"]["g14_queue_count"], 70)
        self.assertEqual(self.report["summary"]["g15_pack_count"], 71)

    def test_states_requests_and_remediation_references_are_coherent(self) -> None:
        queued = [row for row in self.report["packs"] if row["g14"]["status"] == "blocked"]
        not_queued = [row for row in self.report["packs"] if row["g14"]["status"] == "not_queued"]
        self.assertEqual(len(queued), 70)
        self.assertEqual(len(not_queued), 1)
        self.assertEqual(not_queued[0]["pack_id"], "ENERGETICA_INCENTIVI_PACK")
        for row in self.report["packs"]:
            self.assertIn(row["status"], {"blocked", "observed_local"})
            self.assertIn(row["states"]["source_record"], {"blocked", "observed_local"})
            self.assertIn(row["states"]["locator"], {"blocked", "observed_local"})
            self.assertIn(row["states"]["license"], {"blocked", "observed_local"})
            self.assertIn(row["states"]["evidence"], {"blocked", "observed_local"})
            self.assertEqual(row["evidence_request"]["status"], row["states"]["evidence"])
            self.assertGreater(len(row["evidence_request"]["request_refs"]), 0)
            self.assertTrue(row["remediation"]["open"])
            self.assertGreaterEqual(len(row["remediation"]["references"]), 3)

    def test_no_semantic_mapping_or_source_payload_is_introduced(self) -> None:
        self.assertIn("do not create source relationships", self.report["scope"]["no_semantic_mapping"])
        self.assertTrue(all("not used" in row["matching_note"] for row in self.report["packs"]))
        encoded = json.dumps(self.report, ensure_ascii=False).lower()
        for forbidden in ('"text"', '"content"', '"question"', '"answer"', '"solution"'):
            self.assertNotIn(forbidden, encoded)

    def test_report_generation_is_reproducible(self) -> None:
        self.assertEqual(self.report, build_report(ROOT))


if __name__ == "__main__":
    unittest.main()
