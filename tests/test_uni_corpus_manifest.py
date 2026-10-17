"""Structural checks for the G1 provenance manifest.

This test reads metadata and file hashes only. It does not load educational
payloads or examination material.
"""

from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "docs" / "coordination" / "UNI_SOURCE_RECORD_SCHEMA_G1.json"
MANIFEST_PATH = ROOT / "docs" / "coordination" / "UNI_CORPUS_LOTTO_G1.json"


class UniCorpusManifestTest(unittest.TestCase):
    def setUp(self) -> None:
        self.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    def test_manifest_has_g1_shape_and_required_fields(self) -> None:
        self.assertEqual(self.manifest["schema_version"], "G1")
        self.assertTrue(self.schema["$defs"]["source_record"]["properties"]["record_id"]["pattern"].startswith("^G1-"))
        self.assertEqual(self.manifest["$schema"], "./UNI_SOURCE_RECORD_SCHEMA_G1.json")
        self.assertEqual(self.manifest["scope"]["root_path"], "Fondamenti_Pack/raw/gutenberg")
        self.assertEqual(len(self.manifest["records"]), 14)

        required = {
            "record_id",
            "source_kind",
            "title",
            "locator",
            "version_date",
            "hash",
            "license",
            "attribution",
            "transformation",
            "verification_status",
            "limitations",
        }
        for record in self.manifest["records"]:
            self.assertTrue(required.issubset(record))
            self.assertRegex(record["record_id"], r"^G1-[0-9]{3}$")
            self.assertEqual(record["source_kind"], "public_domain_work")
            self.assertEqual(record["hash"]["algorithm"], "SHA-256")
            self.assertRegex(record["hash"]["value"], r"^[A-Fa-f0-9]{64}$")
            self.assertEqual(record["verification_status"]["state"], "observed_local")

    def test_manifest_paths_exist_and_hashes_match(self) -> None:
        for record in self.manifest["records"]:
            relative_path = Path(record["locator"]["path"])
            self.assertEqual(relative_path.parts[:2], ("Fondamenti_Pack", "raw"))
            self.assertEqual(relative_path.suffix, ".txt")
            source_path = ROOT / relative_path
            self.assertTrue(source_path.is_file(), source_path)
            digest = hashlib.sha256(source_path.read_bytes()).hexdigest().upper()
            self.assertEqual(digest, record["hash"]["value"], relative_path)

            license_basis = ROOT / record["license"]["basis_path"]
            self.assertTrue(license_basis.is_file(), license_basis)

    def test_manifest_contains_metadata_only(self) -> None:
        serialized = json.dumps(self.manifest, ensure_ascii=False).lower()
        for forbidden_key in ("text", "content", "question", "answer", "solution"):
            self.assertNotIn(f'"{forbidden_key}"', serialized)
        self.assertNotRegex(serialized, re.compile(r"/esami(?:/|\\\\)|\\besame\\b"))


if __name__ == "__main__":
    unittest.main()
