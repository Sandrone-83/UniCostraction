import json
import unittest
from pathlib import Path

from tools.uni_pack_exam_map_g4 import build_report


ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = ROOT / "docs" / "coordination" / "UNI_PACK_EXAM_MAP_G4.json"


class UniPackExamMapG4Test(unittest.TestCase):
    def test_fixture_is_deterministic_and_keeps_ambiguous_and_unmatched_states(self) -> None:
        root = Path(__file__).parent / "fixtures" / "uni_pack_exam_map_g4"
        first = build_report(root)
        second = build_report(root)

        self.assertEqual(first, second)
        self.assertEqual(first["schema_version"], "g4.v1")
        self.assertEqual(first["counts"]["packs"], 4)
        self.assertEqual(first["counts"]["exams"], 5)
        self.assertFalse(first["method"]["semantic_inference"])

        packs = {entry["pack_id"]: entry for entry in first["packs"]}
        exams = {entry["exam_id"]: entry for entry in first["exams"]}
        self.assertEqual(packs["ONE_PACK"]["classification"], "exact_name")
        self.assertEqual(packs["SHARED_ALPHA_PACK"]["classification"], "ambiguous")
        self.assertEqual(packs["SHARED_BETA_PACK"]["classification"], "alias_observed")
        self.assertEqual(packs["ORPHAN_PACK"]["classification"], "unmatched_pack")
        self.assertEqual(exams["ONE"]["classification"], "exact_name")
        self.assertEqual(exams["SHARED"]["classification"], "ambiguous")
        self.assertEqual(exams["EXAM_ONLY"]["classification"], "unmatched_exam")
        self.assertTrue(exams["LEGACY"]["legacy_observed"])
        json.dumps(first, ensure_ascii=False)

    def test_tracked_report_matches_selected_checkout(self) -> None:
        generated = build_report(ROOT)
        tracked = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(tracked, generated)
        self.assertEqual(generated["counts"]["packs"], 71)
        self.assertEqual(generated["counts"]["exams"], 73)
        self.assertTrue(all("classification" in item for item in generated["packs"]))
        self.assertTrue(all("classification" in item for item in generated["exams"]))


if __name__ == "__main__":
    unittest.main()
