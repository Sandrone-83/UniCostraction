"""Deterministic, metadata-only checks for the G12-B locator/licence checklist."""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "docs" / "coordination" / "UNI_LOCATOR_LICENSE_CHECKLIST_G12_B_SCHEMA.json"
REPORT_PATH = ROOT / "docs" / "coordination" / "UNI_LOCATOR_LICENSE_CHECKLIST_G12_B.json"
sys.path.insert(0, str(ROOT))
from tools.build_locator_license_checklist_g12_b import INPUT_MANIFESTS, build_checklist  # noqa: E402


class G12BLocatorLicenseChecklistTest(unittest.TestCase):
    def setUp(self) -> None:
        self.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    def test_schema_contract_and_commit_are_anchored(self) -> None:
        self.assertEqual(self.report["$schema"], "./UNI_LOCATOR_LICENSE_CHECKLIST_G12_B_SCHEMA.json")
        self.assertEqual(self.schema["properties"]["schema_version"]["const"], "G12-B-locator-license-checklist")
        self.assertEqual(self.report["schema_version"], "G12-B-locator-license-checklist")
        self.assertEqual(self.report["source_commit"], "5609b4eb965e4b45d4520a563f2403b1f9fce980")
        self.assertTrue(self.report["metadata_only"])

    def test_every_source_record_is_present_once_and_sorted(self) -> None:
        expected: list[tuple[str, str]] = []
        for manifest_path in INPUT_MANIFESTS:
            manifest = json.loads((ROOT / manifest_path).read_text(encoding="utf-8"))
            expected.extend((manifest_path.as_posix(), item["source_record_id"]) for item in manifest["source_records"])
        expected.sort()
        actual = [(item["manifest_path"], item["source_record_id"]) for item in self.report["records"]]
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), len(set(actual)))

    def test_required_checklist_dimensions_are_conservative(self) -> None:
        by_id = {item["source_record_id"]: item for item in self.report["records"]}
        g5 = by_id["G5-001"]
        self.assertEqual(g5["locator_reachable_observed"]["state"], "observed_local")
        self.assertEqual(g5["locator_reachable_observed"]["live_check"], "blocked")
        self.assertEqual(g5["official_context_observed"]["state"], "observed_local")
        self.assertEqual(g5["license_source_specific"]["state"], "observed_local")
        self.assertTrue(g5["legal_clearance_required"]["required"])
        self.assertFalse(g5["claim_ready"])

        directive = by_id["G10-B-001"]
        self.assertEqual(directive["locator_reachable_observed"]["state"], "observed_live")
        self.assertEqual(directive["official_context_observed"]["state"], "observed_live")
        self.assertEqual(directive["license_source_specific"]["state"], "blocked")
        self.assertFalse(directive["license_source_specific"]["value"])
        self.assertTrue(directive["legal_clearance_required"]["required"])
        self.assertFalse(directive["claim_ready"])

    def test_no_verified_or_payload_promotion(self) -> None:
        serialized = json.dumps(self.report, ensure_ascii=False).lower()
        for forbidden_key in ('"text"', '"content"', '"question"', '"answer"', '"solution"'):
            self.assertNotIn(forbidden_key, serialized)
        self.assertNotIn('"claim_ready": true', serialized)
        self.assertNotRegex(serialized, re.compile(r'"state"\s*:\s*"verified"'))
        self.assertIn("metadata-only", serialized)
        self.assertIn("promotion_forbidden", serialized)

    def test_report_is_reproducible(self) -> None:
        self.assertEqual(self.report, build_checklist())
        self.assertEqual(self.report["summary"]["record_count"], 2)
        self.assertEqual(self.report["summary"]["claim_ready_count"], 0)
        self.assertEqual(self.report["summary"]["legal_clearance_required_count"], 2)


if __name__ == "__main__":
    unittest.main()
