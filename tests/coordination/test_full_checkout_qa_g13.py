"""G13-C full-checkout QA using metadata-only fixtures.

The negative fixtures intentionally contain only ``None`` and ``placeholder``.
They do not contain a real answer, option letter, explanation, solution,
response, grade, or score.
"""

from __future__ import annotations

import unittest
from pathlib import Path

from tools.validate_full_checkout_g13 import (
    ALLOWED_STATES,
    EXPECTED_PUBLIC_EXAM_PAYLOAD_COUNT,
    REQUIRED_COORDINATION_ARTIFACTS,
    REPOSITORY_ROOT,
    _contract_issues,
    _text_structure_issues,
    forbidden_structure_issues,
    scoped_paths,
    validate_checkout,
)


class FullCheckoutQAG13Tests(unittest.TestCase):
    def test_full_checkout_scope_contains_all_protected_domains(self) -> None:
        paths = scoped_paths(REPOSITORY_ROOT)
        path_text = [path.as_posix() for path in paths]
        self.assertTrue(any(path.startswith("UNIVERSITA_EDILIZIA/ESAMI/") for path in path_text))
        self.assertTrue(any(path.startswith("docs/coordination/") for path in path_text))
        self.assertTrue(any("manifest" in Path(path).name.casefold() for path in path_text))
        self.assertTrue(any("audit" in Path(path).name.casefold() for path in path_text))
        self.assertTrue(any("ledger" in Path(path).name.casefold() for path in path_text))
        coordination_names = {
            Path(path).name for path in path_text if path.startswith("docs/coordination/")
        }
        self.assertTrue(REQUIRED_COORDINATION_ARTIFACTS <= coordination_names)

    def test_full_checkout_passes_protected_contract(self) -> None:
        self.assertEqual([], validate_checkout(REPOSITORY_ROOT))
        payload_count = sum(
            1
            for path in scoped_paths(REPOSITORY_ROOT)
            if path.as_posix().startswith("UNIVERSITA_EDILIZIA/ESAMI/")
            and path.name == "domande.md"
        )
        self.assertEqual(EXPECTED_PUBLIC_EXAM_PAYLOAD_COUNT, payload_count)

    def test_none_placeholder_structures_are_rejected_by_shape_only(self) -> None:
        self.assertTrue(forbidden_structure_issues({"correct option": None}))
        self.assertTrue(forbidden_structure_issues({"answer_key": "placeholder"}))
        self.assertTrue(forbidden_structure_issues({"1": None, "2": None, "3": None}))
        self.assertTrue(_text_structure_issues("correct option: placeholder"))
        self.assertTrue(_text_structure_issues("score: None"))
        self.assertEqual([], _text_structure_issues("Risposte NON presenti: placeholder."))

    def test_states_and_evidence_refs_are_coherent(self) -> None:
        valid = {
            "report_contract": {
                "limitations": ["placeholder"],
                "allowed_states": sorted(ALLOWED_STATES),
                "required_unresolved_states": ["blocked", "pending", "open"],
                "resolved_requires": ["evidence_ref"],
            },
            "entries": [
                {"id": "placeholder", "state": "pending", "evidence_ref": None},
                {"id": "placeholder", "state": "resolved", "evidence_ref": "placeholder"},
            ],
        }
        self.assertEqual([], _contract_issues(valid))

        missing_ref = {
            "report_contract": {
                "limitations": ["placeholder"],
                "allowed_states": sorted(ALLOWED_STATES),
            },
            "entries": [{"id": "placeholder", "state": "resolved", "evidence_ref": None}],
        }
        self.assertTrue(_contract_issues(missing_ref))


if __name__ == "__main__":
    unittest.main()
