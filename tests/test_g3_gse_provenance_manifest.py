"""Metadata-only checks for the local GSE Conto Termico 3.0 source."""

from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = (
    ROOT
    / "UNIVERSITA_EDILIZIA"
    / "ENERGETICA_INCENTIVI_PACK"
    / "fonti"
    / "PROVENANCE_MANIFEST_G3_GSE_CT3.json"
)
SOURCE_PATH = (
    ROOT
    / "UNIVERSITA_EDILIZIA"
    / "ENERGETICA_INCENTIVI_PACK"
    / "fonti"
    / "Regole_Applicative_CT_3_0_GSE.pdf"
)
README_PATH = SOURCE_PATH.with_name("README.md")


class G3GseProvenanceManifestTest(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        self.record = self.manifest["records"][0]

    def test_manifest_records_observed_metadata_and_local_locator(self) -> None:
        self.assertEqual(self.manifest["schema_version"], "G3-source-metadata")
        self.assertEqual(self.manifest["manifest_id"], "G3-2-ENERGETICA-GSE-CT3")
        self.assertTrue(self.manifest["metadata_only"])
        self.assertEqual(len(self.manifest["records"]), 2)
        self.assertEqual(self.record["source_record_id"], "G3-2-001")
        self.assertEqual(self.record["source_kind"], "primary_official")
        self.assertIn("Regole Applicative del D.M. 7 agosto 2025", self.record["title"])
        self.assertEqual(self.record["entity"], "GSE (Gestore dei Servizi Energetici)")
        self.assertEqual(self.record["version_date"]["value"], "5 dicembre 2025")
        self.assertEqual(self.record["document_reference"]["value"], "D.M. 7 agosto 2025")
        self.assertEqual(self.record["observed_pdf_metadata"]["page_count"], 172)
        self.assertEqual(self.record["observed_pdf_metadata"]["author"], "Di Giamberardino Luciana (GSE)")
        self.assertEqual(self.record["locator"]["path"], SOURCE_PATH.relative_to(ROOT).as_posix())
        self.assertIsNone(self.record["locator"]["url"])
        self.assertEqual(self.record["locator"]["url_status"], "not_recorded_in_local_metadata")

    def test_manifest_records_gse_page_as_context_only(self) -> None:
        context = self.manifest["records"][1]
        self.assertEqual(context["source_record_id"], "G3-2-002")
        self.assertEqual(context["source_kind"], "official_context_page")
        self.assertEqual(context["entity"], "GSE (Gestore dei Servizi Energetici)")
        self.assertIsNone(context["locator"]["path"])
        self.assertEqual(
            context["locator"]["url"],
            "https://www.gse.it/servizi-per-te/efficienza-energetica/conto-termico-3-0/modulistica-ct-2",
        )
        self.assertEqual(context["locator"]["url_status"], "observed_exact_url")
        self.assertEqual(context["context_relation"]["related_source_record_id"], "G3-2-001")
        self.assertEqual(context["context_relation"]["relationship"], "institutional_context_only")
        self.assertEqual(context["verification_status"]["state"], "context_only")
        self.assertEqual(context["license_reuse"]["status"], "not_declared")
        self.assertEqual(context["observed_page_metadata"]["section_heading"], "Conto Termico 3.0")
        self.assertEqual(context["observed_page_metadata"]["navigation_label"], "MODULISTICA CT 2.0")

        relation_text = json.dumps(context["context_relation"], ensure_ascii=False).lower()
        self.assertIn("non", relation_text)
        self.assertIn("vigenza", relation_text)
        self.assertIn("riuso", relation_text)

    def test_manifest_hash_matches_pdf_and_supporting_readme_exists(self) -> None:
        self.assertTrue(SOURCE_PATH.is_file(), SOURCE_PATH)
        self.assertTrue(README_PATH.is_file(), README_PATH)
        digest = hashlib.sha256(SOURCE_PATH.read_bytes()).hexdigest().upper()
        self.assertEqual(digest, self.record["hash"]["value"])
        self.assertEqual(self.record["hash"]["algorithm"], "SHA-256")

    def test_manifest_is_explicitly_blocked_without_invented_url_or_reuse_claim(self) -> None:
        self.assertEqual(self.record["verification_status"]["state"], "blocked")
        self.assertIsNone(self.record["locator"]["url"])
        self.assertEqual(self.record["license_reuse"]["status"], "not_declared")
        self.assertIn("URL GSE", self.record["limitations"][0])
        self.assertIn("Non inventare", self.manifest["blocking_notes"][0])

        serialized = json.dumps(self.record, ensure_ascii=False).lower()
        for forbidden_key in ("text", "content", "question", "answer", "solution", "incentive_values"):
            self.assertNotIn(f'"{forbidden_key}"', serialized)
        self.assertNotIn("https://", serialized)


if __name__ == "__main__":
    unittest.main()
