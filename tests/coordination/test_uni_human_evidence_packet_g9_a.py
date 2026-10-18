import json
import unittest
from pathlib import Path

from tools.uni_human_evidence_packet_g9_a import build_packet


ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = ROOT / "docs" / "coordination" / "UNI_HUMAN_EVIDENCE_PACKET_G9_A.json"
SCHEMA_PATH = ROOT / "docs" / "coordination" / "UNI_HUMAN_EVIDENCE_PACKET_G9_A.schema.json"


class UniHumanEvidencePacketG9ATest(unittest.TestCase):
    def test_packet_is_deterministic_and_tracks_current_open_review(self) -> None:
        first = build_packet(ROOT)
        second = build_packet(ROOT)
        tracked = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

        self.assertEqual(first, second)
        self.assertEqual(tracked, first)
        self.assertEqual(first["schema_version"], "g9a.v1")
        self.assertEqual(first["coverage"]["pending_g5"], 6)
        self.assertEqual(first["coverage"]["legacy_unmatched_exams"], 2)
        self.assertEqual(first["coverage"]["unique_item_count"], 6)
        self.assertTrue(first["coverage"]["legacy_is_subset_of_pending"])
        self.assertFalse(first["coverage"]["duplicate_entries"])
        self.assertEqual(
            [item["identifier"]["queue_id"] for item in first["items"]],
            [
                "exam:IMPIANTI_FV_EOLICO",
                "exam:INFRASTRUTTURE",
                "exam:MATERIALEDILE",
                "exam:STRUTTURE",
                "pack:AEROPORTI_E_INFRASTRUTTURE_DI_VOLO_PACK",
                "pack:FORMULARIO_STRUTTURE_PACK",
            ],
        )

    def test_legacy_items_are_not_duplicated_and_have_stricter_disposition(self) -> None:
        packet = build_packet(ROOT)
        legacy = [
            item
            for item in packet["items"]
            if item["identifier"]["uncertainty"] == "unmatched_legacy_domain"
        ]

        self.assertEqual(len(legacy), 2)
        self.assertEqual(
            packet["coverage"]["legacy_unmatched_queue_ids"],
            ["exam:IMPIANTI_FV_EOLICO", "exam:MATERIALEDILE"],
        )
        for item in legacy:
            self.assertEqual(item["identifier"]["item_type"], "exam")
            self.assertTrue(item["identifier"]["legacy_observed"])
            self.assertIn("keep_unmatched", item["allowed_decisions"])
            self.assertNotIn("keep_unresolved", item["allowed_decisions"])
            self.assertTrue(item["no_auto_resolution"]["forbidden"])
            self.assertEqual(item["linkage"]["g8"]["evidence_state"], "human_review_required")

    def test_every_item_has_traceable_files_and_g7_g8_links(self) -> None:
        packet = build_packet(ROOT)
        self.assertEqual(packet["source_reports"]["g8_ledger"]["schema_version"], "g8a.v1")
        self.assertEqual(packet["source_reports"]["g7_readiness"]["schema_version"], "g7a.v1")
        self.assertEqual(packet["source_reports"]["g7_readiness"]["status"], "blocked")
        for item in packet["items"]:
            identifier = item["identifier"]
            self.assertTrue(item["observed_files"])
            self.assertEqual(item["linkage"]["g5"]["queue_id"], identifier["queue_id"])
            self.assertEqual(item["linkage"]["g8"]["record_id"], identifier["record_id"])
            self.assertEqual(item["linkage"]["g7"]["status"], "blocked")
            self.assertTrue(item["evidence_to_collect"])
            self.assertTrue(item["no_auto_resolution"]["forbidden"])
            self.assertIn("didactic_content_or_answer_inference", item["no_auto_resolution"]["prohibited_basis"])

    def test_schema_is_anchored_to_metadata_only_boundaries(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["schema_version"]["const"], "g9a.v1")
        self.assertEqual(schema["properties"]["scope"]["properties"]["content_modified"]["const"], False)
        self.assertEqual(schema["properties"]["coverage"]["properties"]["duplicate_entries"]["const"], False)
        self.assertEqual(
            schema["$defs"]["packetItem"]["properties"]["no_auto_resolution"]["properties"]["forbidden"]["const"],
            True,
        )


if __name__ == "__main__":
    unittest.main()
