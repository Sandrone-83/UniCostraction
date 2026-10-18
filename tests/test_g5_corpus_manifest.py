"""Structural and coherence checks for the G5 metadata-only source tranche."""

from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "docs" / "coordination" / "UNI_SOURCE_RECORD_SCHEMA_G5.json"
MANIFEST_PATH = ROOT / "docs" / "coordination" / "UNI_CORPUS_LOTTO_G5_ECFR.json"
SOURCE_PATH = ROOT / "Edilizia_Pack" / "raw" / "ecfr" / "29CFR1926_construction.xml"
AUDIT_PATH = ROOT / "Edilizia_Pack" / "licenze_audit.json"
PACKAGE_MANIFEST_PATH = ROOT / "Edilizia_Pack" / "manifest.json"


class G5CorpusManifestTest(unittest.TestCase):
    def setUp(self) -> None:
        self.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        self.record = self.manifest["source_records"][0]

    def test_manifest_json_shape_and_schema_contract(self) -> None:
        self.assertEqual(self.manifest["$schema"], "./UNI_SOURCE_RECORD_SCHEMA_G5.json")
        self.assertEqual(self.schema["properties"]["schema_version"]["const"], "G5-source-metadata")
        self.assertEqual(self.manifest["schema_version"], "G5-source-metadata")
        self.assertTrue(self.manifest["metadata_only"])
        self.assertEqual(self.manifest["manifest_id"], "G5-ECFR-OSHA-1926")
        self.assertEqual(self.manifest["scope"]["source_path"], "Edilizia_Pack/raw/ecfr/29CFR1926_construction.xml")
        self.assertEqual(len(self.manifest["source_records"]), 1)
        self.assertEqual(self.record["source_record_id"], "G5-001")
        self.assertEqual(self.record["source_kind"], "primary_official")

    def test_local_source_hash_and_registry_coherence(self) -> None:
        self.assertTrue(SOURCE_PATH.is_file(), SOURCE_PATH)
        self.assertEqual(SOURCE_PATH.stat().st_size, self.record["document_metadata"]["file_size_bytes"])
        digest = hashlib.sha256(SOURCE_PATH.read_bytes()).hexdigest().upper()
        self.assertEqual(digest, self.record["hash"]["value"])
        self.assertEqual(self.record["hash"]["algorithm"], "SHA-256")

        audit = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))
        audit_record = next(item for item in audit["fonti"] if item["id"] == "OSHA-1926")
        package_manifest = json.loads(PACKAGE_MANIFEST_PATH.read_text(encoding="utf-8"))
        package_record = next(item for item in package_manifest if item["doc"] == "29 CFR 1926 OSHA Construction")
        self.assertEqual(self.record["source"]["url"], audit_record["url"])
        self.assertEqual(self.record["source"]["url"], package_record["url"])
        self.assertEqual(self.record["license_reuse"]["label"], audit_record["licenza"])
        self.assertEqual(self.record["source"]["local_path"], "Edilizia_Pack/raw/ecfr/29CFR1926_construction.xml")

    def test_source_interpretation_and_context_are_separate(self) -> None:
        self.assertEqual(self.manifest["interpretation_records"], [])
        self.assertNotIn("interpretation", self.record)
        self.assertNotIn("official_context", self.record)

        contexts = self.manifest["official_context_records"]
        self.assertEqual(len(contexts), 1)
        context = contexts[0]
        self.assertEqual(context["related_source_record_id"], self.record["source_record_id"])
        self.assertEqual(context["relationship"], "official_locator_context_only")
        self.assertEqual(context["url"], self.record["source"]["url"])

    def test_metadata_only_and_structured_blocker_contract(self) -> None:
        serialized = json.dumps(self.manifest, ensure_ascii=False).lower()
        for forbidden_key in ("text", "content", "question", "answer", "solution", "incentive_values"):
            self.assertNotIn(f'"{forbidden_key}"', serialized)
        self.assertNotRegex(serialized, re.compile(r"/esami(?:/|\\\\)|\\besame\\b"))

        blocker = self.manifest["related_blockers"][0]
        self.assertEqual(blocker["state"], "blocked")
        self.assertIn("PROVENANCE_MANIFEST_G3_GSE_CT3.json", blocker["evidence"][0])
        self.assertIn("verification_status.state=blocked", blocker["evidence"])

    def test_source_status_does_not_overclaim(self) -> None:
        self.assertEqual(self.record["verification_status"]["state"], "observed_local")
        not_checked = set(self.record["verification_status"]["not_checked"])
        self.assertIn("external_url_availability", not_checked)
        self.assertIn("independent_legal_clearance", not_checked)
        self.assertIn("current_regulatory_applicability", not_checked)
        self.assertEqual(self.record["version"]["value"], None)


if __name__ == "__main__":
    unittest.main()
