"""G17-C structural QA for the future skill-library contract."""

from __future__ import annotations

import unittest
from pathlib import Path
from unittest.mock import patch

from tools.validate_skill_library_g17 import (
    DuplicateJSONKeyError,
    LICENSE_STATUS_VALUES,
    PROVENANCE_STATUS_VALUES,
    REPOSITORY_ROOT,
    validate_library,
)


def _skill(skill_id: str = "skill-cila-basics", category: str = "edilizia") -> dict:
    return {
        "id": skill_id,
        "title": "CILA basics",
        "summary": "Metadata-only workflow fixture.",
        "category": category,
        "path": f"{category}/{skill_id}.json",
        "workflow": [
            {
                "step_id": "inspect-input",
                "action": "Inspect the supplied project context.",
                "output": "A review note.",
            }
        ],
        "source_refs": [{"ref": "https://example.invalid/source", "kind": "official"}],
        "license_status": "pending",
        "safety_legal_boundary": {
            "human_review_required": True,
            "professional_review_required": True,
            "automatic_execution_prohibited": True,
            "legal_advice_prohibited": True,
            "factual_correctness_requires_review": True,
            "boundary_note": "Human and professional review remain mandatory.",
        },
        "provenance_status": "pending",
    }


class SkillLibraryContractG17Tests(unittest.TestCase):
    def findings_for(self, records: dict[str, dict]) -> list[str]:
        root = REPOSITORY_ROOT / "__g17_in_memory_library__"
        paths = tuple(root / relative for relative in sorted(records))
        with patch(
            "tools.validate_skill_library_g17._skill_files",
            return_value=(paths, []),
        ), patch(
            "tools.validate_skill_library_g17._read_json",
            side_effect=lambda path: records[path.relative_to(root).as_posix()],
        ):
            return validate_library(root)

    def test_valid_record_passes_and_status_domains_are_explicit(self) -> None:
        self.assertEqual([], self.findings_for({"edilizia/skill-cila-basics.json": _skill()}))
        self.assertEqual(
            {"unreviewed", "pending", "reviewed", "restricted", "not_applicable"},
            set(LICENSE_STATUS_VALUES),
        )
        self.assertEqual({"unreviewed", "pending", "verified", "blocked"}, set(PROVENANCE_STATUS_VALUES))

    def test_required_fields_and_unknown_fields_fail_closed(self) -> None:
        record = _skill()
        del record["source_refs"]
        record["unexpected"] = "hidden metadata"
        findings = self.findings_for({"edilizia/skill-cila-basics.json": record})
        self.assertTrue(any("missing required field source_refs" in issue for issue in findings))
        self.assertTrue(any("unknown field unexpected" in issue for issue in findings))

    def test_duplicate_exact_ids_are_rejected_across_files(self) -> None:
        first = _skill("skill-scia", "urbanistica")
        second = _skill("skill-scia", "catasto")
        findings = self.findings_for(
            {
                "urbanistica/skill-scia.json": first,
                "catasto/skill-scia.json": second,
            }
        )
        self.assertTrue(any("duplicate exact ID" in issue for issue in findings))

    def test_path_category_and_filename_mapping_is_required(self) -> None:
        record = _skill()
        record["path"] = "urbanistica/other-name.json"
        record["category"] = "urbanistica"
        record["id"] = "skill-other-name"
        findings = self.findings_for({"edilizia/skill-cila-basics.json": record})
        self.assertTrue(any("path: must match actual" in issue for issue in findings))
        self.assertTrue(any("category: must match path category" in issue for issue in findings))
        self.assertTrue(any("id: must match skill filename stem" in issue for issue in findings))

    def test_empty_workflow_and_empty_source_refs_are_rejected(self) -> None:
        record = _skill()
        record["workflow"] = []
        record["source_refs"] = []
        findings = self.findings_for({"edilizia/skill-cila-basics.json": record})
        self.assertTrue(any("non-empty workflow list required" in issue for issue in findings))
        self.assertTrue(any("non-empty source reference list required" in issue for issue in findings))

    def test_source_refs_license_and_provenance_statuses_are_structural(self) -> None:
        record = _skill()
        record["source_refs"] = [{"ref": "", "kind": "unknown"}]
        record["license_status"] = "cleared_for_use"
        record["provenance_status"] = "approved"
        findings = self.findings_for({"edilizia/skill-cila-basics.json": record})
        self.assertTrue(any("source_refs[0].ref" in issue for issue in findings))
        self.assertTrue(any("source_refs[0].kind" in issue for issue in findings))
        self.assertTrue(any("unsupported licence status" in issue for issue in findings))
        self.assertTrue(any("unsupported provenance status" in issue for issue in findings))

    def test_reviewed_and_verified_statuses_need_evidence_refs(self) -> None:
        record = _skill()
        record["license_status"] = "reviewed"
        record["provenance_status"] = "verified"
        findings = self.findings_for({"edilizia/skill-cila-basics.json": record})
        self.assertTrue(any("license_evidence_ref" in issue for issue in findings))
        self.assertTrue(any("provenance_evidence_ref" in issue for issue in findings))

    def test_safety_and_legal_boundaries_are_explicit_and_conservative(self) -> None:
        record = _skill()
        record["safety_legal_boundary"]["legal_advice_prohibited"] = False
        del record["safety_legal_boundary"]["boundary_note"]
        findings = self.findings_for({"edilizia/skill-cila-basics.json": record})
        self.assertTrue(any("legal_advice_prohibited" in issue for issue in findings))
        self.assertTrue(any("boundary_note" in issue for issue in findings))

    def test_utf8_invalid_json_duplicate_keys_and_unsupported_files_fail_closed(self) -> None:
        root = REPOSITORY_ROOT / "__g17_in_memory_library__"
        files = (
            root / "edilizia/skill-invalid-utf8.json",
            root / "edilizia/skill-duplicate-key.json",
        )

        def fake_read(path: Path) -> dict:
            if path.name == "skill-invalid-utf8.json":
                raise UnicodeDecodeError("utf-8", b"\xff", 0, 1, "invalid start byte")
            raise DuplicateJSONKeyError("duplicate JSON key: id")

        with patch(
            "tools.validate_skill_library_g17._skill_files",
            return_value=(files, ["README.md: unsupported file type; only UTF-8 JSON is allowed"]),
        ), patch("tools.validate_skill_library_g17._read_json", side_effect=fake_read):
            findings = validate_library(root)
        self.assertTrue(any("valid UTF-8" in issue for issue in findings))
        self.assertTrue(any("duplicate JSON object key" in issue for issue in findings))
        self.assertTrue(any("unsupported file type" in issue for issue in findings))

    def test_missing_or_empty_library_is_not_valid(self) -> None:
        self.assertTrue(
            any(
                "does not exist" in issue
                for issue in validate_library(REPOSITORY_ROOT / "__g17_missing_library__")
            )
        )
        with patch(
            "tools.validate_skill_library_g17._skill_files",
            return_value=((), ["library: no skill JSON files found"]),
        ):
            findings = validate_library(REPOSITORY_ROOT / "__g17_empty_library__")
        self.assertTrue(any("no skill JSON files found" in issue for issue in findings))

    def test_workflow_step_ids_and_fields_are_deterministic(self) -> None:
        record = _skill()
        record["workflow"] = [
            {"step_id": "same", "action": "one", "output": "out"},
            {"step_id": "same", "action": "", "output": "out"},
        ]
        findings = self.findings_for({"edilizia/skill-cila-basics.json": record})
        self.assertTrue(any("duplicate exact step ID" in issue for issue in findings))
        self.assertTrue(any("workflow[1].action" in issue for issue in findings))


if __name__ == "__main__":
    unittest.main()
