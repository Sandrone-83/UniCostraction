"""QA G3 per integrita del fixture pubblico degli esami.

Il test confronta il manifest pubblico con il checkout corrente e controlla
che i file elencati non espongano campi espliciti di risposta. Gli hash sono
metadati di integrita del fixture: non sono una chiave di risposta e non
stabiliscono la correttezza delle domande o delle opzioni.
"""

from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path
from typing import Any


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
PUBLIC_EXAMS_ROOT = REPOSITORY_ROOT / "UNIVERSITA_EDILIZIA" / "ESAMI"
MANIFEST_PATH = (
    REPOSITORY_ROOT
    / "docs"
    / "coordination"
    / "PUBLIC_EXAM_FIXTURE_MANIFEST_G3.json"
)

EXPECTED_PUBLIC_EXAM_FILE_COUNT = 73
EXPECTED_MANIFEST_KEYS = {
    "manifest_version",
    "algorithm",
    "scope",
    "file_count",
    "files",
    "publication_contract",
}
EXPECTED_ENTRY_KEYS = {"path", "sha256"}

# Intercetta solo un campo nominato all'inizio di una riga. Non interpreta le
# frasi della domanda, delle opzioni o della premessa come dati strutturati.
EXPLICIT_ANSWER_FIELD_PATTERN = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?(?:[*_`\"']*\s*)?"
    r"(?:lettera|risposta(?:\s+(?:corretta|esatta))?|risposta_corretta|"
    r"correct(?:_answer|_option)?|answer(?:_key)?|solution|soluzione)"
    r"(?:[*_`\"']*\s*)?[:=]"
)


def _load_manifest() -> dict[str, Any]:
    with MANIFEST_PATH.open(encoding="utf-8") as manifest_file:
        manifest = json.load(manifest_file)
    if not isinstance(manifest, dict):
        raise TypeError("il manifest deve essere un oggetto JSON")
    return manifest


def _manifest_path(relative_path: str) -> Path:
    """Resolve a manifest path using its repository-relative slash form."""
    return REPOSITORY_ROOT.joinpath(*relative_path.split("/"))


class ExamProvenanceG3Tests(unittest.TestCase):
    def test_manifest_declares_only_public_fixture_integrity_metadata(self) -> None:
        """The public manifest has no answer-key or scoring fields."""
        manifest = _load_manifest()

        self.assertEqual(EXPECTED_MANIFEST_KEYS, set(manifest))
        self.assertEqual(1, manifest["manifest_version"])
        self.assertEqual("sha256", manifest["algorithm"])
        self.assertEqual(
            "UNIVERSITA_EDILIZIA/ESAMI/*/domande.md",
            manifest["scope"],
        )
        self.assertEqual(EXPECTED_PUBLIC_EXAM_FILE_COUNT, manifest["file_count"])
        self.assertIsInstance(manifest["files"], list)
        self.assertEqual(
            EXPECTED_PUBLIC_EXAM_FILE_COUNT,
            len(manifest["files"]),
        )

        for entry in manifest["files"]:
            self.assertIsInstance(entry, dict)
            self.assertEqual(EXPECTED_ENTRY_KEYS, set(entry))
            self.assertRegex(entry["path"], r"^UNIVERSITA_EDILIZIA/ESAMI/.+/domande\.md$")
            self.assertRegex(entry["sha256"], r"^[0-9a-f]{64}$")

        contract = manifest["publication_contract"]
        self.assertEqual("blocked", contract["state"])
        self.assertEqual({"pending", "blocked"}, set(contract["allowed_states"]))
        self.assertTrue(contract["limitations"])
        self.assertEqual("separate", contract["answer_key_separation"]["status"])
        self.assertFalse(contract["answer_key_separation"]["public"])

    def test_manifest_matches_public_exam_checkout(self) -> None:
        """Every public exam path and byte hash matches the checked-out fixture."""
        manifest = _load_manifest()
        entries = manifest["files"]
        manifest_paths = [entry["path"] for entry in entries]
        checkout_paths = sorted(
            path.relative_to(REPOSITORY_ROOT).as_posix()
            for path in PUBLIC_EXAMS_ROOT.glob("*/domande.md")
        )

        self.assertEqual(EXPECTED_PUBLIC_EXAM_FILE_COUNT, len(checkout_paths))
        self.assertEqual(checkout_paths, manifest_paths)

        for entry in entries:
            path = _manifest_path(entry["path"])
            self.assertTrue(path.is_file(), path)
            actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
            self.assertEqual(entry["sha256"], actual_hash, path)

    def test_public_fixture_files_have_no_explicit_answer_fields(self) -> None:
        """No public file listed by the manifest exposes a named answer field."""
        manifest = _load_manifest()

        for entry in manifest["files"]:
            path = _manifest_path(entry["path"])
            text = path.read_text(encoding="utf-8")
            self.assertIsNone(
                EXPLICIT_ANSWER_FIELD_PATTERN.search(text),
                f"campo di risposta esplicito in {path}",
            )


if __name__ == "__main__":
    unittest.main()
