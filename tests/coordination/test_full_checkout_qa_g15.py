"""G15-C deterministic full-checkout and report-cardinality QA.

All negative fixtures contain only ``None`` or ``placeholder``.  They never
contain an answer, option letter, explanation, solution, response, grade, or
score value.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools.validate_full_checkout_g13 import (
    ALLOWED_STATES,
    EXPECTED_PUBLIC_EXAM_FILE_COUNT,
    EXPECTED_PUBLIC_EXAM_PAYLOAD_COUNT,
    G15_REPORT_SPECS,
    REPOSITORY_ROOT,
    _manifest_issues,
    _text_structure_issues,
    determinism_issues,
    forbidden_structure_issues,
    report_state_count_issues,
    scoped_paths,
    validate_checkout,
)


class FullCheckoutQAG15Tests(unittest.TestCase):
    def test_full_checkout_is_deterministic_and_has_frozen_exam_counts(self) -> None:
        paths = scoped_paths(REPOSITORY_ROOT)
        self.assertEqual([], determinism_issues(REPOSITORY_ROOT, paths))
        exam_files = [
            path
            for path in paths
            if path.as_posix().startswith("UNIVERSITA_EDILIZIA/ESAMI/")
        ]
        exam_payloads = [path for path in exam_files if path.name == "domande.md"]
        self.assertEqual(EXPECTED_PUBLIC_EXAM_FILE_COUNT, len(exam_files))
        self.assertEqual(EXPECTED_PUBLIC_EXAM_PAYLOAD_COUNT, len(exam_payloads))

    def test_g10_to_g14_report_states_and_counts_are_frozen(self) -> None:
        self.assertEqual([], report_state_count_issues(REPOSITORY_ROOT))
        for filename, spec in G15_REPORT_SPECS.items():
            self.assertTrue((REPOSITORY_ROOT / "docs/coordination" / filename).is_file())
            self.assertTrue(spec["state_paths"])

    def test_manifest_paths_and_hashes_are_tracked_and_valid(self) -> None:
        manifest = REPOSITORY_ROOT / "docs/coordination/PUBLIC_EXAM_FIXTURE_MANIFEST_G3.json"
        payload = json.loads(manifest.read_text(encoding="utf-8"))
        self.assertEqual([], _manifest_issues(payload, REPOSITORY_ROOT, "$"))

    def test_manifest_rejects_placeholder_path_and_invalid_digest_shape(self) -> None:
        payload = {
            "algorithm": "sha256",
            "file_count": 3,
            "files": [
                {"path": "../placeholder", "sha256": "placeholder"},
                {
                    "path": "docs/coordination/UNI_QA_WORKFLOW_EVIDENCE_G14.md",
                    "sha256": "placeholder",
                },
                {"path": "placeholder", "sha256": "placeholder"},
            ],
        }
        findings = _manifest_issues(payload, REPOSITORY_ROOT, "$", frozenset())
        self.assertTrue(any("normalized repository-relative" in issue for issue in findings))
        self.assertTrue(any("64-hex digest" in issue for issue in findings))

    def test_full_checkout_guard_and_protected_blocks_remain_active(self) -> None:
        self.assertEqual([], validate_checkout(REPOSITORY_ROOT))
        for payload in (
            {"answer_key": None},
            {"response": "placeholder"},
            {"grade": None},
            {"solution": "placeholder"},
            {"score": None},
            {"correct option": "placeholder"},
            {"1": None, "2": "placeholder", "3": None},
        ):
            with self.subTest(payload=payload):
                self.assertTrue(forbidden_structure_issues(payload))
        self.assertTrue(_text_structure_issues("answer_key: None"))
        self.assertTrue(_text_structure_issues("1: None\n2: placeholder\n3: None"))
        self.assertEqual({"blocked", "pending", "open", "resolved"}, ALLOWED_STATES)


if __name__ == "__main__":
    unittest.main()
