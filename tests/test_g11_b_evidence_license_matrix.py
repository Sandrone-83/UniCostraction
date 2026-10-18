"""Deterministic, metadata-only checks for the G11-B evidence/licence matrix."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "docs" / "coordination" / "UNI_EVIDENCE_LICENSE_MATRIX_G11_B_SCHEMA.json"
REPORT_PATH = ROOT / "docs" / "coordination" / "UNI_EVIDENCE_LICENSE_MATRIX_G11_B.json"
sys.path.insert(0, str(ROOT))
from tools.build_evidence_license_matrix_g11_b import INPUT_MANIFESTS, build_matrix  # noqa: E402


class G11BEvidenceLicenseMatrixTest(unittest.TestCase):
    def setUp(self) -> None:
        self.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    def test_json_and_schema_contract_are_anchored(self) -> None:
        self.assertEqual(self.report["$schema"], "./UNI_EVIDENCE_LICENSE_MATRIX_G11_B_SCHEMA.json")
        self.assertEqual(self.schema["properties"]["schema_version"]["const"], "G11-B-evidence-license-matrix")
        self.assertEqual(self.report["schema_version"], "G11-B-evidence-license-matrix")
        self.assertTrue(self.report["metadata_only"])
        self.assertEqual(self.report["summary"]["record_count"], 2)

    def test_every_source_record_is_present_once_and_sorted(self) -> None:
        expected: list[tuple[str, str]] = []
        for manifest_path in INPUT_MANIFESTS:
            manifest = json.loads((ROOT / manifest_path).read_text(encoding="utf-8"))
            expected.extend(
                (manifest_path.as_posix(), source["source_record_id"])
                for source in manifest["source_records"]
            )
        expected.sort()
        actual = [
            (row["manifest_path"], row["source_record_id"])
            for row in self.report["rows"]
        ]
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), len(set(actual)))

    def test_statuses_are_conservative_when_live_verification_is_absent(self) -> None:
        by_id = {row["source_record_id"]: row for row in self.report["rows"]}
        g5 = by_id["G5-001"]
        self.assertEqual(g5["locator_status"], "observed_local")
        self.assertEqual(g5["official_context_status"], "observed_local")
        self.assertEqual(g5["license_status"], "observed_local")
        self.assertEqual(g5["evidence_status"], "observed_local")
        self.assertFalse(g5["claim_ready"])
        self.assertFalse(g5["blocker"]["live_verification"])

        directive = by_id["G10-B-001"]
        self.assertIn("2024/1275", directive["title"])
        self.assertEqual(directive["locator_status"], "observed_local")
        self.assertEqual(directive["official_context_status"], "observed_local")
        self.assertEqual(directive["license_status"], "blocked")
        self.assertEqual(directive["evidence_status"], "blocked")
        self.assertFalse(directive["claim_ready"])
        self.assertIn("source_specific_license_not_established", directive["blocker"]["codes"])

    def test_report_is_reproducible_and_contains_no_payload(self) -> None:
        self.assertEqual(self.report, build_matrix())
        serialized = json.dumps(self.report, ensure_ascii=False).lower()
        for forbidden_key in ('"text"', '"content"', '"question"', '"answer"', '"solution"'):
            self.assertNotIn(forbidden_key, serialized)
        self.assertNotIn('"claim_ready": true', serialized)
        self.assertIn("metadata-only", self.report["scope"]["claim_policy"])


if __name__ == "__main__":
    unittest.main()
