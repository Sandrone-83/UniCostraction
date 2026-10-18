"""Deterministic metadata-only provenance checks for the G10-B source tranche."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "docs" / "coordination" / "UNI_SOURCE_RECORD_SCHEMA_G10_B.json"
MANIFEST_PATH = ROOT / "docs" / "coordination" / "UNI_CORPUS_LOTTO_G10_B.json"


class G10BOfficialSourceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    def test_manifest_and_schema_are_json_and_schema_anchored(self) -> None:
        self.assertEqual(self.manifest["$schema"], "./UNI_SOURCE_RECORD_SCHEMA_G10_B.json")
        self.assertEqual(self.schema["properties"]["schema_version"]["const"], "G10-B-source-metadata")
        self.assertEqual(self.manifest["schema_version"], "G10-B-source-metadata")
        self.assertEqual(self.manifest["manifest_id"], "G10-B-EU-EPBD-2024-1275")
        self.assertTrue(self.manifest["metadata_only"])

    def test_exactly_one_source_record_and_refs_are_disjoint(self) -> None:
        self.assertEqual(len(self.manifest["source_records"]), 1)
        source = self.manifest["source_records"][0]
        self.assertEqual(source["source_record_id"], "G10-B-001")
        self.assertEqual(source["source_kind"], "primary_official")
        self.assertEqual(source["source"]["url_status"], "verified_direct")
        self.assertEqual(source["source"]["local_payload_status"], "not_added")
        self.assertEqual(source["evidence_status"], "context_only")
        self.assertFalse(source["claim_ready"])
        self.assertEqual(source["interpretation_record_id"], self.manifest["interpretation_records"][0]["interpretation_record_id"])
        self.assertEqual(source["context_record_id"], self.manifest["official_context_records"][0]["context_record_id"])
        self.assertEqual(source["license_record_id"], self.manifest["license_records"][0]["license_record_id"])

    def test_source_interpretation_context_license_and_blocker_remain_separate(self) -> None:
        interpretation = self.manifest["interpretation_records"][0]
        context = self.manifest["official_context_records"][0]
        license_record = self.manifest["license_records"][0]
        blocker = self.manifest["related_blockers"][0]
        self.assertEqual(interpretation["scope"], "catalogue_selection_only")
        self.assertEqual(interpretation["status"], "non_normative")
        self.assertEqual(context["relationship"], "official_reuse_context_only")
        self.assertEqual(context["status"], "context_only")
        self.assertEqual(license_record["status"], "declared_context_only")
        self.assertTrue(license_record["not_a_source_specific_license"])
        self.assertEqual(blocker["state"], "blocked")

    def test_metadata_only_excludes_payloads_and_claim_promotion(self) -> None:
        serialized = json.dumps(self.manifest, ensure_ascii=False).lower()
        for forbidden_key in ('"text"', '"content"', '"question"', '"answer"', '"solution"', '"value"'):
            self.assertNotIn(forbidden_key, serialized)
        self.assertNotRegex(serialized, re.compile(r"/esami(?:/|\\\\)|\\besame\\b"))
        self.assertNotIn("interpretation", self.manifest["source_records"][0])
        self.assertNotIn("license", self.manifest["source_records"][0])

    def test_generation_is_deterministic_and_no_extra_records_are_present(self) -> None:
        second = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        self.assertEqual(self.manifest, second)
        self.assertEqual(len(self.manifest["source_records"]), 1)
        self.assertEqual(len(self.manifest["interpretation_records"]), 1)
        self.assertEqual(len(self.manifest["official_context_records"]), 1)
        self.assertEqual(len(self.manifest["license_records"]), 1)


if __name__ == "__main__":
    unittest.main()
