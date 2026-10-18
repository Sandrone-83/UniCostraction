"""Deterministic checks for the metadata-only G14-B pack evidence queue."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "docs/coordination/UNI_PACK_EVIDENCE_QUEUE_G14_B_SCHEMA.json"
REPORT_PATH = ROOT / "docs/coordination/UNI_PACK_EVIDENCE_QUEUE_G14_B.json"
sys.path.insert(0, str(ROOT))
from tools.build_pack_evidence_queue_g14_b import SOURCE_COMMIT, build_queue  # noqa: E402


class G14BPackEvidenceQueueTest(unittest.TestCase):
    def setUp(self) -> None:
        self.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    def test_schema_and_source_commit_are_anchored(self) -> None:
        self.assertEqual(self.report["$schema"], "./UNI_PACK_EVIDENCE_QUEUE_G14_B_SCHEMA.json")
        self.assertEqual(self.report["schema_version"], "G14-B-pack-evidence-queue")
        self.assertEqual(self.report["queue_id"], "G14-B-pack-evidence-queue")
        self.assertTrue(self.report["metadata_only"])
        self.assertEqual(self.report["source_commit"], SOURCE_COMMIT)
        self.assertEqual(self.schema["properties"]["source_commit"]["const"], SOURCE_COMMIT)

    def test_exactly_70_unmatched_packs_are_queued_once(self) -> None:
        items = self.report["items"]
        self.assertEqual(len(items), 70)
        self.assertEqual(self.report["summary"]["item_count"], 70)
        self.assertEqual(self.report["summary"]["blocked_count"], 70)
        self.assertEqual(self.report["summary"]["closure_ready_count"], 0)
        self.assertEqual([item["pack_path"] for item in items], sorted(item["pack_path"] for item in items))
        self.assertEqual(len({item["pack_id"] for item in items}), 70)
        self.assertEqual(len({item["pack_path"] for item in items}), 70)

    def test_separation_and_mapping_prohibition_are_explicit(self) -> None:
        scope = self.report["scope"]
        self.assertEqual(scope["separation_policy"]["automatic_semantic_mapping"], "prohibited")
        self.assertIn("fonti", scope["no_semantic_mapping"])
        for item in self.report["items"]:
            self.assertTrue(item["automatic_semantic_mapping_prohibited"])
            self.assertTrue(item["interpretation"]["automatic_semantic_mapping_prohibited"])
            self.assertTrue(item["interpretation"]["human_review_required"])
            self.assertEqual(item["context"]["status"], "separate_and_pending")
            self.assertEqual(item["legal_clearance"]["status"], "required")
            self.assertTrue(item["legal_clearance"]["independent_review_required"])

    def test_every_item_has_all_four_blocked_gates_and_closure_criteria(self) -> None:
        for item in self.report["items"]:
            self.assertEqual(item["status"], "blocked")
            self.assertEqual(item["source"]["source_record_status"], "missing_explicit_record")
            self.assertGreater(len(item["source"]["evidence_required"]), 0)
            self.assertGreater(len(item["source"]["locator_required"]), 0)
            self.assertGreater(len(item["source"]["license_proof_required"]), 0)
            self.assertEqual(item["blocked"]["state"], "blocked")
            self.assertTrue(item["blocked"]["promotion_forbidden"])
            self.assertIsNone(item["closure_criteria"][0]["evidence_ref"])
            self.assertTrue(all(row["status"] == "pending" for row in item["closure_criteria"]))

    def test_no_source_payload_or_content_fields_are_queued(self) -> None:
        forbidden = {"text", "content", "question", "answer", "solution", "schede"}
        encoded = json.dumps(self.report, ensure_ascii=False).lower()
        for field in forbidden:
            self.assertNotIn(f'"{field}"', encoded)

    def test_report_is_reproducible(self) -> None:
        self.assertEqual(self.report, build_queue())


if __name__ == "__main__":
    unittest.main()
