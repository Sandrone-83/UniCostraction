import copy
import json
import unittest
from pathlib import Path

from tools.uni_cluster_review_progress_g14_a import (
    ALLOWED_STATUSES,
    build_progress_register,
    load_json,
    validate_progress_register,
)


class UniClusterReviewProgressG14ATest(unittest.TestCase):
    def _fixture_packet(self) -> dict:
        path = Path(__file__).parent / "fixtures" / "uni_cluster_review_progress_g14_a" / "packet.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def test_fixture_starts_open_with_null_placeholders(self) -> None:
        packet = self._fixture_packet()
        report = build_progress_register(
            packet,
            packet_sha256=None,
            expected_cluster_count=3,
            expected_batch_count=2,
        )

        validate_progress_register(report, expected_cluster_count=3, expected_batch_count=2)
        self.assertEqual(report["workflow"]["allowed_statuses"], ALLOWED_STATUSES)
        self.assertEqual(report["coverage"]["status_counts"], {"open": 3, "in_review": 0, "decided": 0})
        self.assertTrue(report["coverage"]["all_evidence_refs_null"])
        for cluster in report["clusters"]:
            self.assertEqual(cluster["status"], "open")
            self.assertIsNone(cluster["evidence_ref"])
            self.assertIsNone(cluster["reviewer"])
            self.assertIsNone(cluster["rationale"])

    def test_build_is_deterministic(self) -> None:
        first = build_progress_register(self._fixture_packet(), expected_cluster_count=3, expected_batch_count=2)
        second = build_progress_register(copy.deepcopy(self._fixture_packet()), expected_cluster_count=3, expected_batch_count=2)
        self.assertEqual(first, second)

    def test_in_review_requires_reviewer_and_rationale(self) -> None:
        report = build_progress_register(self._fixture_packet(), expected_cluster_count=3, expected_batch_count=2)
        report["clusters"][0].update({"status": "in_review", "reviewer": "human-reviewer", "rationale": "Scope checked."})
        report["coverage"]["status_counts"] = {"open": 2, "in_review": 1, "decided": 0}
        report["coverage"]["open_count"] = 2
        report["coverage"]["in_review_count"] = 1
        report["coverage"]["pending_count"] = 3
        report["coverage"]["all_reviewers_null"] = False
        report["coverage"]["all_rationales_null"] = False
        report["batches"][0]["status_counts"] = {"open": 1, "in_review": 1, "decided": 0}
        invalid = copy.deepcopy(report)
        invalid["clusters"][0]["reviewer"] = None
        with self.assertRaises(ValueError):
            validate_progress_register(invalid, expected_cluster_count=3, expected_batch_count=2)
        validate_progress_register(report, expected_cluster_count=3, expected_batch_count=2)

    def test_decided_cluster_requires_evidence_reviewer_and_rationale(self) -> None:
        report = build_progress_register(self._fixture_packet(), expected_cluster_count=3, expected_batch_count=2)
        report["clusters"][0].update(
            {
                "status": "decided",
                "evidence_ref": "docs/evidence/component-0001.md#review",
                "reviewer": "human-reviewer",
                "rationale": "Evidence supports the recorded human decision.",
            }
        )
        report["coverage"] = {
            "cluster_count": 3,
            "batch_count": 2,
            "status_counts": {"open": 2, "in_review": 0, "decided": 1},
            "open_count": 2,
            "in_review_count": 0,
            "decided_count": 1,
            "pending_count": 2,
            "all_evidence_refs_null": False,
            "all_reviewers_null": False,
            "all_rationales_null": False,
        }
        report["batches"][0]["status_counts"] = {"open": 1, "in_review": 0, "decided": 1}
        report["batches"][0]["decided_count"] = 1
        validate_progress_register(report, expected_cluster_count=3, expected_batch_count=2)

        for field in ("evidence_ref", "reviewer", "rationale"):
            invalid = copy.deepcopy(report)
            invalid["clusters"][0][field] = None
            with self.assertRaises(ValueError):
                validate_progress_register(invalid, expected_cluster_count=3, expected_batch_count=2)

    def test_cannot_close_multiple_clusters_without_evidence(self) -> None:
        report = build_progress_register(self._fixture_packet(), expected_cluster_count=3, expected_batch_count=2)
        for cluster in report["clusters"][:2]:
            cluster.update({"status": "decided", "reviewer": "reviewer", "rationale": "Reviewed."})
        with self.assertRaisesRegex(ValueError, "evidence_ref is required"):
            validate_progress_register(report, expected_cluster_count=3, expected_batch_count=2)

    def test_tracked_register_covers_85_clusters_and_does_not_change_g13_packet(self) -> None:
        root = Path(__file__).resolve().parents[2]
        packet_path = root / "docs" / "coordination" / "UNI_CLUSTER_REVIEW_PACKET_G13_A.json"
        register_path = root / "docs" / "coordination" / "UNI_CLUSTER_REVIEW_PROGRESS_G14_A.json"
        packet, packet_sha256 = load_json(packet_path)
        generated = build_progress_register(packet, packet_sha256=packet_sha256)
        tracked = json.loads(register_path.read_text(encoding="utf-8"))

        self.assertEqual(tracked, generated)
        self.assertEqual(generated["coverage"]["cluster_count"], 85)
        self.assertEqual(generated["coverage"]["batch_count"], 9)
        self.assertEqual(generated["coverage"]["status_counts"], {"open": 85, "in_review": 0, "decided": 0})
        self.assertTrue(all(item["status"] == "open" for item in generated["clusters"]))
        self.assertTrue(all(item["evidence_ref"] is None for item in generated["clusters"]))
        self.assertTrue(all(item["reviewer"] is None for item in generated["clusters"]))
        self.assertTrue(all(item["rationale"] is None for item in generated["clusters"]))
        self.assertTrue(all(item["review"]["decision"] is None for item in packet["clusters"]))
        encoded = json.dumps(generated, ensure_ascii=False).lower()
        self.assertNotIn("answer_key", encoded)
        self.assertNotIn("question_body", encoded)


if __name__ == "__main__":
    unittest.main()
