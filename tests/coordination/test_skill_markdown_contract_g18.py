"""G18 structural contract tests using temporary libraries only."""

from __future__ import annotations

import json
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.validate_skill_markdown_g18 import REPOSITORY_ROOT, validate_library


VALID_SKILL = """---
name: skill-cila-basics
description: Metadata-only CILA workflow fixture.
metadata:
  skill_id: skill-cila-basics
  category: edilizia
  version: 1
---

# CILA basics

## Purpose
Describe the original review workflow and its intended handoff.

## Inputs and Preconditions
Require the supplied project context and identify missing documents first.

## Operational Workflow
Inspect inputs, record provenance, and prepare a review note.

## Outputs and Handoff
Produce a draft checklist for human review.

## Sources and Provenance
Primary reference: https://example.invalid/source and register entry SRC-EXAMPLE.

## Rights and Use
The procedure is original; licence and redistribution rights require review and attribution.

## Professional and Legal Boundaries
Human review and professional review remain mandatory. No automatic execution or legal advice; factual correctness requires review.

## Verification and Escalation
Escalate unresolved facts to the responsible professional and record the decision.
"""


def _manifest(path: str = "edilizia/skill-cila-basics/SKILL.md", skill_id: str = "skill-cila-basics") -> dict:
    return {"schema_version": "g18", "skills": [{"id": skill_id, "category": "edilizia", "path": path}]}


class SkillMarkdownContractG18Tests(unittest.TestCase):
    ROOT = REPOSITORY_ROOT / "tools"

    def findings_for(
        self,
        skill_text: str = VALID_SKILL,
        manifest: dict | None = None,
        skill_paths: tuple[str, ...] = ("edilizia/skill-cila-basics/SKILL.md",),
        extra_files: tuple[str, ...] = (),
        read_error: BaseException | None = None,
        json_error: BaseException | None = None,
    ) -> list[str]:
        paths = tuple(self.ROOT / relative for relative in skill_paths)
        files = (self.ROOT / "manifest.json", *paths, *(self.ROOT / relative for relative in extra_files))

        def read_utf8(path: Path) -> str:
            if read_error is not None and path.name == "SKILL.md":
                raise read_error
            return skill_text

        def read_json(path: Path) -> dict:
            if json_error is not None:
                raise json_error
            return manifest or _manifest()

        with patch("tools.validate_skill_markdown_g18._library_files", return_value=files), patch(
            "tools.validate_skill_markdown_g18._read_json", side_effect=read_json
        ), patch("tools.validate_skill_markdown_g18._read_utf8", side_effect=read_utf8), patch.object(
            Path, "is_file", return_value=True
        ):
            return validate_library(self.ROOT)

    def test_valid_library_passes(self) -> None:
        self.assertEqual([], self.findings_for())

    def test_front_matter_and_operational_sections_are_required(self) -> None:
        text = VALID_SKILL.replace(
            "metadata:\n  skill_id: skill-cila-basics\n  category: edilizia\n  version: 1\n", ""
        ).replace("## Operational Workflow", "## Workflow")
        findings = self.findings_for(text)
        self.assertTrue(any("missing required front matter field metadata" in issue for issue in findings))
        self.assertTrue(any("metadata: non-empty mapping required" in issue for issue in findings))
        self.assertTrue(any("missing required section heading ## Operational Workflow" in issue for issue in findings))

    def test_source_rights_and_boundaries_fail_closed(self) -> None:
        text = VALID_SKILL.replace("https://example.invalid/source and register entry SRC-EXAMPLE", "no external reference")
        text = text.replace("licence and redistribution rights require review and attribution", "a statement")
        text = text.replace(
            "Human review and professional review remain mandatory. No automatic execution or legal advice; factual correctness requires review.",
            "This is descriptive only.",
        )
        findings = self.findings_for(text)
        self.assertTrue(any("source reference required" in issue for issue in findings))
        self.assertTrue(any("rights or licence statement required" in issue for issue in findings))
        for boundary in ("human review", "professional review", "automatic execution", "legal advice", "factual correctness"):
            self.assertTrue(any(boundary in issue for issue in findings), boundary)

    def test_manifest_and_path_consistency_are_required(self) -> None:
        findings = self.findings_for(manifest=_manifest("urbanistica/other/SKILL.md", "other"))
        self.assertTrue(any("missing entry for edilizia/skill-cila-basics/SKILL.md" in issue for issue in findings))
        self.assertTrue(any("path does not exist" in issue for issue in findings))

    def test_duplicate_skill_ids_are_rejected(self) -> None:
        manifest = _manifest()
        manifest["skills"].append({"id": "skill-cila-basics", "category": "urbanistica", "path": "urbanistica/skill-cila-basics/SKILL.md"})
        findings = self.findings_for(
            manifest=manifest,
            skill_paths=("edilizia/skill-cila-basics/SKILL.md", "urbanistica/skill-cila-basics/SKILL.md"),
        )
        self.assertTrue(any("duplicate exact skill ID" in issue for issue in findings))

    def test_utf8_empty_and_duplicate_json_keys_fail_closed(self) -> None:
        findings = self.findings_for(json_error=ValueError("duplicate JSON key"))
        self.assertTrue(any("valid UTF-8 JSON object required" in issue for issue in findings))
        self.assertTrue(any("EMPTY.md: unsupported file" in issue for issue in self.findings_for(extra_files=("EMPTY.md",))))
        findings = self.findings_for(read_error=UnicodeDecodeError("utf-8", b"\xff", 0, 1, "invalid"))
        self.assertTrue(any("SKILL.md: file must be valid UTF-8" in issue for issue in findings))

    def test_missing_or_empty_library_is_invalid(self) -> None:
        missing = self.ROOT / "missing-g18-library"
        self.assertTrue(any("directory does not exist" in issue for issue in validate_library(missing)))
        with patch("tools.validate_skill_markdown_g18._library_files", return_value=(self.ROOT / "manifest.json",)), patch(
            "tools.validate_skill_markdown_g18._read_json", side_effect=ValueError("empty file")
        ), patch.object(Path, "is_file", return_value=True):
            findings = validate_library(self.ROOT)
        self.assertTrue(any("manifest.json: file must not be empty" in issue for issue in findings))

    def test_published_unicostraction_v01_layout_is_supported(self) -> None:
        """G18 must validate the real G17 layout, not only the future contract."""

        legacy_skill = """---
name: skill-cila-basics
description: Metadata-only legacy workflow fixture.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: edilizia
---

# Skill legacy

## Attivazione
Attiva con contesto sufficiente e assunzioni registrate.

## Input minimo
Raccogli documenti, località e obiettivo.

## Workflow
Controlla input, fonte, revisione e handoff.

## Output
Prepara una bozza tracciabile per revisione.

## Quality gates
Nessun output passa senza controllo umano.

## Evidenza e provenienza
Registra fonte, data, versione e hash quando possibile.

## Confini professionali e legali
Il risultato richiede professionista, verifica normativa e autorizzazione; non è consulenza legale.

## Failure modes
Blocca dati mancanti e fonti discordanti.

## Strumenti
Usa editor, registro e controlli di integrità.

## Fonti ufficiali e diritti
Fonte: https://example.invalid/source. Procedura originale; licenza e diritti di riuso richiedono verifica.
"""
        root = self.ROOT
        manifest_path = root / "manifest.json"
        skill_path = root / "skill-cila-basics" / "SKILL.md"
        manifest = {
            "library": "UniCostraction/AuraTrix-AulaFIX",
            "version": "0.1.0",
            "skills": [{"id": "skill-cila-basics", "path": "skill-cila-basics/SKILL.md"}],
        }
        with patch(
            "tools.validate_skill_markdown_g18._library_files",
            return_value=(manifest_path, skill_path),
        ), patch(
            "tools.validate_skill_markdown_g18._read_json",
            return_value=manifest,
        ), patch(
            "tools.validate_skill_markdown_g18._read_utf8",
            side_effect=lambda path: legacy_skill if path == skill_path else "{}",
        ), patch.object(Path, "is_file", return_value=True):
            self.assertEqual([], validate_library(root))


if __name__ == "__main__":
    unittest.main()
