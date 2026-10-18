import copy
import json
import unittest
from pathlib import Path

from tools.uni_cluster_review_batch_g16_a import (
    build_batch_template,
    import_batch_review,
    validate_batch_payload,
)
from tools.uni_cluster_review_progress_g14_a import build_progress_register


class UniClusterReviewBatchG16ATest(unittest.TestCase):
    def _packet(self) -> dict:
        path = Path(__file__).parent / "fixtures" / "uni_cluster_review_batch_g16_a" / "packet.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def _sources(self) -> tuple[dict, dict]:
        packet = self._packet()
        progress = build_progress_register(packet, expected_cluster_count=3, expected_batch_count=2)
        return packet, progress

    def _template(self) -> dict:
        packet, progress = self._sources()
        return build_batch_template(
            packet,
            progress,
            "batch-01",
            g13_sha256="a" * 64,
            g14_sha256="b" * 64,
            expected_cluster_count=3,
            expected_batch_count=2,
        )

    def test_export_is_single_batch_and_all_review_fields_are_null(self) -> None:
        template = self._template()
        validate_batch_payload(template, expected_batch_id="batch-01", expected_mode="template")
        self.assertEqual(template["mode"], "template")
        self.assertEqual(template["batch"]["cluster_ids"], ["component-0001", "component-0002"])
        for entry in template["entries"]:
            self.assertEqual(entry["review"], {"decision": None, "evidence_ref": None, "reviewer": None, "rationale": None})

    def test_import_accepts_only_a_complete_human_decision(self) -> None:
        template = self._template()
        template["entries"][0]["review"] = {
            "decision": "distinct",
            "evidence_ref": "synthetic/evidence/component-0001",
            "reviewer": "human-placeholder",
            "rationale": "Synthetic placeholder review is complete.",
        }
        packet, progress = self._sources()
        reviewed = import_batch_review(
            template,
            packet,
            progress,
            g13_sha256="a" * 64,
            g14_sha256="b" * 64,
            expected_cluster_count=3,
            expected_batch_count=2,
        )
        self.assertEqual(reviewed["mode"], "reviewed")
        self.assertTrue(reviewed["scope"]["import_validated"])
        validate_batch_payload(reviewed, expected_batch_id="batch-01", expected_mode="reviewed")

    def test_partial_review_is_rejected_even_when_decision_is_null(self) -> None:
        template = self._template()
        template["entries"][0]["review"]["reviewer"] = "human-placeholder"
        with self.assertRaisesRegex(ValueError, "partial human review"):
            validate_batch_payload(template, expected_mode="template")

    def test_decision_without_any_required_field_is_rejected(self) -> None:
        template = self._template()
        for field in ("evidence_ref", "reviewer", "rationale"):
            invalid = copy.deepcopy(template)
            invalid["entries"][0]["review"] = {
                "decision": "distinct",
                "evidence_ref": "synthetic/evidence/component-0001",
                "reviewer": "human-placeholder",
                "rationale": "Synthetic placeholder review is complete.",
            }
            invalid["entries"][0]["review"][field] = None
            with self.subTest(field=field):
                with self.assertRaisesRegex(ValueError, "requires evidence_ref, reviewer and rationale"):
                    validate_batch_payload(invalid, expected_mode="template")

    def test_import_rejects_changed_canonical_metadata(self) -> None:
        template = self._template()
        template["entries"][0]["g11"]["unit_refs"] = ["synthetic:tampered"]
        packet, progress = self._sources()
        with self.assertRaisesRegex(ValueError, "non-review metadata changed"):
            import_batch_review(
                template,
                packet,
                progress,
                g13_sha256="a" * 64,
                g14_sha256="b" * 64,
                expected_cluster_count=3,
                expected_batch_count=2,
            )

    def test_canonical_sources_remain_unchanged(self) -> None:
        packet, progress = self._sources()
        packet_before = copy.deepcopy(packet)
        progress_before = copy.deepcopy(progress)
        template = build_batch_template(
            packet,
            progress,
            "batch-02",
            g13_sha256=None,
            g14_sha256=None,
            expected_cluster_count=3,
            expected_batch_count=2,
        )
        template["entries"][0]["review"] = {
            "decision": "needs_source_review",
            "evidence_ref": "synthetic/evidence/component-0003",
            "reviewer": "human-placeholder",
            "rationale": "Synthetic placeholder requires source review.",
        }
        import_batch_review(
            template,
            packet,
            progress,
            expected_cluster_count=3,
            expected_batch_count=2,
        )
        self.assertEqual(packet, packet_before)
        self.assertEqual(progress, progress_before)
        self.assertTrue(all(item["review"]["decision"] is None for item in packet["clusters"]))


if __name__ == "__main__":
    unittest.main()
