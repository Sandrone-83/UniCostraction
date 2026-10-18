import json
import unittest
from pathlib import Path

from tools.uni_completeness_ledger_g8 import build_ledger


ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = ROOT / "docs" / "coordination" / "UNI_COMPLETENESS_LEDGER_G8.json"
SCHEMA_PATH = ROOT / "docs" / "coordination" / "UNI_COMPLETENESS_LEDGER_G8.schema.json"


class UniCompletenessLedgerG8Test(unittest.TestCase):
    def test_current_ledger_is_deterministic_and_keeps_review_open(self) -> None:
        first = build_ledger(ROOT)
        second = build_ledger(ROOT)
        tracked = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

        self.assertEqual(first, second)
        self.assertEqual(tracked, first)
        self.assertEqual(first["counts"]["records"], {"packs": 71, "exams": 73})
        self.assertEqual(
            first["dashboard_counts"]["observed"],
            {
                "packs": 71,
                "schede": {
                    "jsonl_rows": 963,
                    "declared_total": 963,
                    "malformed_json_rows": 0,
                    "non_object_json_rows": 0,
                },
                "exams": 73,
                "exam_pack_pairs": 73,
            },
        )
        self.assertEqual(
            first["counts"]["evidence_state"],
            {
                "packs": {"evidence_present": 69, "human_review_required": 2},
                "exams": {"evidence_present": 69, "human_review_required": 4},
                "total": {"evidence_present": 138, "human_review_required": 6},
            },
        )
        self.assertEqual(first["open_review"]["pending_g5"], 6)
        self.assertEqual(first["open_review"]["legacy_unmatched_exams"], 2)
        self.assertFalse(first["open_review"]["pending_or_unmatched_closed"])

        pack = next(item for item in first["packs"] if item["item_id"] == "FORMULARIO_STRUTTURE_PACK")
        self.assertEqual(pack["evidence_state"], "human_review_required")
        self.assertIn(
            "UNIVERSITA_EDILIZIA/FORMULARIO_STRUTTURE_PACK/schede/schede.jsonl",
            pack["source_files"],
        )
        self.assertEqual(
            pack["dashboard_reference"]["count_paths"]["observed_schede_rows"],
            "pack_card_observations[pack_id=FORMULARIO_STRUTTURE_PACK].observed_rows",
        )

        legacy = next(item for item in first["exams"] if item["item_id"] == "MATERIALEDILE")
        self.assertEqual(legacy["evidence_state"], "human_review_required")
        self.assertTrue(legacy["human_review"]["legacy_unmatched"])
        self.assertFalse(first["scope"]["semantic_association_inferred"])

    def test_incomplete_pack_is_not_promoted_to_evidence_present(self) -> None:
        root = Path(__file__).parent / "fixtures" / "uni_completeness_g6"
        report = build_ledger(root)

        self.assertEqual(report["counts"]["records"]["packs"], 1)
        self.assertEqual(report["counts"]["evidence_state"]["packs"], {
            "evidence_present": 0,
            "human_review_required": 1,
        })
        self.assertEqual(report["packs"][0]["observed"]["card_status"], "jsonl_invalid")

    def test_schema_declares_the_two_evidence_states_and_review_boundary(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["schema_version"]["const"], "g8a.v1")
        self.assertEqual(
            schema["$defs"]["ledgerEntry"]["properties"]["evidence_state"]["enum"],
            ["evidence_present", "human_review_required"],
        )
        self.assertEqual(
            schema["properties"]["open_review"]["properties"]["pending_or_unmatched_closed"]["const"],
            False,
        )


if __name__ == "__main__":
    unittest.main()
