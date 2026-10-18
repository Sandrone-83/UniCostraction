import copy
import json
import unittest
from pathlib import Path

from tools.uni_cluster_review_packet_g13_a import (
    ALLOWED_DECISIONS,
    build_packet,
    load_json,
    validate_packet,
)


class UniClusterReviewPacketG13ATest(unittest.TestCase):
    def _fixture_reports(self) -> tuple[dict, dict, dict]:
        g11 = {
            "schema_version": "g11a.v1",
            "results": {
                "queue": [
                    {
                        "component_id": "component-0001",
                        "priority_rank": 1,
                        "priority_key": {"collision_count": 3, "component_id": "component-0001"},
                        "source_group": "public_exams",
                        "unit_ids": ["exam:EXAM_ONE/domande.md#question-0001"],
                        "coverage": {"exam_paths": ["ROOT/ESAMI/EXAM_ONE/domande.md"]},
                        "collision_count": 3,
                    },
                    {
                        "component_id": "component-0002",
                        "priority_rank": 2,
                        "priority_key": {"collision_count": 1, "component_id": "component-0002"},
                        "source_group": "public_exams",
                        "unit_ids": [
                            "exam:EXAM_TWO/domande.md#question-0002",
                            "exam:EXAM_TWO/domande.md#question-0003",
                        ],
                        "coverage": {"exam_paths": ["ROOT/ESAMI/EXAM_TWO/domande.md"]},
                        "collision_count": 1,
                    },
                ]
            },
        }
        g12 = {
            "schema_version": "g12a.v1",
            "scope": {
                "initial_decision": None,
                "allowed_decisions": ALLOWED_DECISIONS,
            },
            "review_policy": {
                "evidence_ref_required_for_non_null_decision": True,
                "reviewer_required": True,
                "rationale_required": True,
                "decision_is_not_an_action": True,
            },
            "review_queue": [
                {"component_id": f"component-{index:04d}", "review": {field: None for field in ("decision", "evidence_ref", "reviewer", "rationale")}}
                for index in (1, 2)
            ],
        }
        g4 = {
            "schema_version": "g4.v1",
            "exams": [
                {
                    "exam_id": "EXAM_ONE",
                    "exam_path": "ROOT/ESAMI/EXAM_ONE",
                    "classification": "alias_observed",
                    "legacy_observed": False,
                    "source_files": ["ROOT/ESAMI/EXAM_ONE/domande.md"],
                    "candidate_packs": [
                        {"pack_id": "PACK_ONE", "relation": "alias_observed"}
                    ],
                },
                {
                    "exam_id": "EXAM_TWO",
                    "exam_path": "ROOT/ESAMI/EXAM_TWO",
                    "classification": "ambiguous",
                    "legacy_observed": False,
                    "source_files": ["ROOT/ESAMI/EXAM_TWO/domande.md"],
                    "candidate_packs": [
                        {"pack_id": "PACK_ONE", "relation": "alias_observed"},
                        {"pack_id": "PACK_TWO", "relation": "alias_observed"},
                    ],
                },
            ],
            "packs": [
                {"pack_id": "PACK_ONE", "pack_path": "ROOT/PACK_ONE", "classification": "alias_observed", "source_files": ["ROOT/PACK_ONE/COURSE.yaml"]},
                {"pack_id": "PACK_TWO", "pack_path": "ROOT/PACK_TWO", "classification": "alias_observed", "source_files": ["ROOT/PACK_TWO/COURSE.yaml"]},
            ],
        }
        return g11, g12, g4

    def test_fixture_is_deterministic_and_preserves_ambiguous_candidates(self) -> None:
        reports = self._fixture_reports()
        first = build_packet(*reports, expected_cluster_count=2, batch_size=1)
        second = build_packet(*copy.deepcopy(reports), expected_cluster_count=2, batch_size=1)
        self.assertEqual(first, second)
        self.assertEqual(first["coverage"]["pending_count"], 2)
        self.assertEqual(first["clusters"][1]["references"]["exam_refs"][0]["classification"], "ambiguous")
        self.assertEqual(
            [item["pack_id"] for item in first["clusters"][1]["references"]["pack_refs"]],
            ["PACK_ONE", "PACK_TWO"],
        )
        self.assertTrue(all(item["review"] == {field: None for field in ("decision", "evidence_ref", "reviewer", "rationale")} for item in first["clusters"]))

    def test_pending_packet_rejects_any_pre_decision_value(self) -> None:
        packet = build_packet(*self._fixture_reports(), expected_cluster_count=2)
        packet["clusters"][0]["review"]["reviewer"] = "human"
        with self.assertRaises(ValueError):
            validate_packet(packet, expected_cluster_count=2)

    def test_tracked_packet_has_85_clusters_without_didactic_fields(self) -> None:
        root = Path(__file__).resolve().parents[2]
        g11, g11_sha = load_json(root / "docs/coordination/UNI_REDUNDANCY_PRIORITY_G11_A.json")
        g12, g12_sha = load_json(root / "docs/coordination/UNI_CLUSTER_REVIEW_G12_A.json")
        g4, g4_sha = load_json(root / "docs/coordination/UNI_PACK_EXAM_MAP_G4.json")
        generated = build_packet(g11, g12, g4, g11_sha256=g11_sha, g12_sha256=g12_sha, g4_sha256=g4_sha)
        tracked = json.loads((root / "docs/coordination/UNI_CLUSTER_REVIEW_PACKET_G13_A.json").read_text(encoding="utf-8"))
        self.assertEqual(tracked, generated)
        self.assertEqual(generated["coverage"]["cluster_count"], 85)
        self.assertEqual(generated["coverage"]["pending_count"], 85)
        self.assertTrue(generated["coverage"]["all_decisions_null"])
        self.assertTrue(all(item["review"]["decision"] is None for item in generated["clusters"]))
        self.assertTrue(all(item["review"]["reviewer"] is None for item in generated["clusters"]))
        encoded = json.dumps(generated, ensure_ascii=False).lower()
        self.assertNotIn("answer_key", encoded)
        self.assertNotIn("question_body", encoded)


if __name__ == "__main__":
    unittest.main()
