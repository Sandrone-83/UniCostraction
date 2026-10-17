"""Package-level provenance checks for the G1 raw source lot.

The test compares metadata only. It never loads raw educational payloads,
parsed lessons, schede, or examination material.
"""

from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
G1_PATH = ROOT / "docs" / "coordination" / "UNI_CORPUS_LOTTO_G1.json"
G2_PATH = ROOT / "Fondamenti_Pack" / "PROVENANCE_MANIFEST_G2.json"


class G2ProvenanceManifestTest(unittest.TestCase):
    def setUp(self) -> None:
        self.g1 = json.loads(G1_PATH.read_text(encoding="utf-8"))
        self.g2 = json.loads(G2_PATH.read_text(encoding="utf-8"))

    def test_package_manifest_matches_g1_metadata(self) -> None:
        self.assertEqual(self.g2["schema_version"], "G2-package-metadata")
        self.assertEqual(self.g2["package"], "Fondamenti_Pack")
        self.assertTrue(self.g2["metadata_only"])
        self.assertEqual(self.g2["source_lot"]["lot_id"], self.g1["lot_id"])
        self.assertEqual(self.g2["source_lot"]["manifest_path"], "docs/coordination/UNI_CORPUS_LOTTO_G1.json")
        self.assertEqual(self.g2["source_lot"]["raw_root"], self.g1["scope"]["root_path"])
        self.assertEqual(self.g2["source_lot"]["record_count"], 14)
        self.assertEqual(len(self.g2["records"]), len(self.g1["records"]))

        g1_by_id = {record["record_id"]: record for record in self.g1["records"]}
        self.assertEqual(
            {record["source_record_id"] for record in self.g2["records"]},
            set(g1_by_id),
        )
        compared_fields = (
            "source_kind",
            "title",
            "author",
            "version_date",
            "locator",
            "hash",
            "license",
            "attribution",
            "transformation",
            "verification_status",
            "limitations",
        )
        for package_record in self.g2["records"]:
            source_id = package_record["source_record_id"]
            g1_record = g1_by_id[source_id]
            self.assertEqual(package_record["raw_file"], g1_record["locator"]["path"])
            for field in compared_fields:
                self.assertEqual(package_record[field], g1_record[field], f"{source_id}: {field}")

    def test_package_manifest_hashes_and_license_locators(self) -> None:
        for record in self.g2["records"]:
            relative_path = Path(record["raw_file"])
            self.assertEqual(relative_path.parts[:3], ("Fondamenti_Pack", "raw", "gutenberg"))
            self.assertEqual(relative_path.suffix, ".txt")
            source_path = ROOT / relative_path
            self.assertTrue(source_path.is_file(), source_path)
            digest = hashlib.sha256(source_path.read_bytes()).hexdigest().upper()
            self.assertEqual(digest, record["hash"]["value"], relative_path)
            license_basis = ROOT / record["license"]["basis_path"]
            self.assertTrue(license_basis.is_file(), license_basis)

    def test_package_manifest_is_metadata_only(self) -> None:
        serialized = json.dumps(self.g2, ensure_ascii=False).lower()
        for forbidden_key in ("text", "content", "question", "answer", "solution"):
            self.assertNotIn(f'"{forbidden_key}"', serialized)
        self.assertNotRegex(serialized, re.compile(r"/esami(?:/|\\\\)|\\besame\\b"))


if __name__ == "__main__":
    unittest.main()
