import json
import unittest
from pathlib import Path

from tools.uni_inventory_g1 import build_report


class UniInventoryG1Test(unittest.TestCase):
    def test_report_is_deterministic_and_separates_candidate_signals(self) -> None:
        root = Path(__file__).parent / "fixtures" / "uni_inventory_g1"
        first = build_report(root)
        second = build_report(root)
        self.assertEqual(first, second)
        json.dumps(first, ensure_ascii=False)

        files = first["evidence"]["files"]
        self.assertEqual([entry["path"] for entry in files], sorted(entry["path"] for entry in files))
        self.assertNotIn("ignored.txt", [entry["path"] for entry in files])
        self.assertEqual(first["scope"]["deduplicated"], False)

        groups = first["interpretation"]["possible_duplicate_groups"]
        signals = {group["signal"] for group in groups}
        self.assertIn("exact_sha256_match", signals)
        self.assertIn("course_title_match", signals)

        exam_entries = [entry for entry in files if entry["path"].endswith("domande.md")]
        self.assertEqual({entry["category"] for entry in exam_entries}, {"exam_questions"})
        self.assertTrue(all(entry["signals"] for entry in exam_entries))


if __name__ == "__main__":
    unittest.main()
