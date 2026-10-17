import json
import unittest
from pathlib import Path

from tools.uni_inventory_g1 import build_report


ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = ROOT / "docs" / "coordination" / "UNI_DUPLICATE_MATRIX_G1.json"


class UniInventoryG2Test(unittest.TestCase):
    def test_tracked_matrix_matches_clean_checkout_without_duplicate_signals(self) -> None:
        generated = build_report(ROOT)
        tracked = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

        self.assertEqual(tracked, generated)
        self.assertEqual(generated["interpretation"]["possible_duplicate_groups"], [])

        files = generated["evidence"]["files"]
        self.assertEqual(len(files), len({entry["sha256"] for entry in files}))

        normalized_hashes = [
            entry["normalized_text_sha256"]
            for entry in files
            if "normalized_text_sha256" in entry
        ]
        self.assertEqual(len(normalized_hashes), len(set(normalized_hashes)))

        course_title_keys = [
            entry["course_title_key"]
            for entry in files
            if "course_title_key" in entry
        ]
        self.assertEqual(len(course_title_keys), len(set(course_title_keys)))
        self.assertTrue(all(not entry["signals"] for entry in files))


if __name__ == "__main__":
    unittest.main()
