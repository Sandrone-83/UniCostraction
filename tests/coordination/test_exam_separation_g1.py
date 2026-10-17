"""QA limitato per la separazione tra domande pubbliche e chiavi d'esame.

Questo test non contiene né ricostruisce una risposta corretta. I due campioni
pubblici sono sigillati tramite metadati (formato, conteggio e SHA-256), così
una sostituzione silenziosa del fixture fa fallire il controllo senza esporre la
chiave esterna.

Il controllo verifica solo l'assenza di campi espliciti di risposta nei blocchi
di domanda e la documentazione del percorso esterno/protetto della chiave. Non
prova la correttezza didattica, normativa o fattuale delle domande, né la
completezza o l'accuratezza della chiave riservata.
"""

from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
PUBLIC_EXAMS_ROOT = REPOSITORY_ROOT / "UNIVERSITA_EDILIZIA" / "ESAMI"


# Metadati pubblici attesi: non sono una answer key. Il digest rileva una
# sostituzione del campione, mentre il formato/conteggio verifica il parser
# corretto per entrambi i formati presenti nel repository.
EXPECTED_PUBLIC_FIXTURES = (
    {
        "relative_path": Path("UNIVERSITA_EDILIZIA/ESAMI/ACUSTICA/domande.md"),
        "format": "standard",
        "question_pattern": re.compile(r"(?m)^## Domanda (\d+)\s*$"),
        "question_count": 220,
        "sha256": "62adc576fa153ad830c81833251d2e184e232bb022e5d9aafc927a1745265a30",
    },
    {
        "relative_path": Path("UNIVERSITA_EDILIZIA/ESAMI/MATERIALEDILE/domande.md"),
        "format": "legacy",
        "question_pattern": re.compile(r"(?m)^\*\*D(\d+)\.\*\*"),
        "question_count": 1000,
        "sha256": "b2437654343ed576de4e7c98eda63cb0148116c4ab9b78412342bf4c9879ee92",
    },
)


# Sono ammessi gli avvisi di riservatezza nella premessa del file pubblico.
# La ricerca è limitata ai blocchi di domanda per intercettare invece un
# eventuale campo esplicito aggiunto al payload della domanda.
EXPLICIT_ANSWER_FIELD_PATTERNS = (
    re.compile(
        r"(?im)^\s*(?:[-*]\s*)?(?:lettera|risposta_corretta|"
        r"risposta\s+(?:corretta|esatta)|correct_answer|answer_key)\s*[:=]"
    ),
    re.compile(r"(?im)^\s*[\"']?(?:lettera|risposta_corretta|answer_key)[\"']?\s*:") ,
)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _question_blocks(text: str, pattern: re.Pattern[str]) -> list[str]:
    matches = list(pattern.finditer(text))
    return [
        text[match.end() : (matches[index + 1].start() if index + 1 < len(matches) else len(text))]
        for index, match in enumerate(matches)
    ]


class ExamSeparationG1Tests(unittest.TestCase):
    def test_public_sample_metadata_is_sealed(self) -> None:
        """The sampled public files and their parsable formats are stable."""
        for fixture in EXPECTED_PUBLIC_FIXTURES:
            path = REPOSITORY_ROOT / fixture["relative_path"]
            self.assertTrue(path.is_file(), path)
            self.assertEqual(fixture["sha256"], _sha256(path), path)

            text = path.read_text(encoding="utf-8")
            matches = fixture["question_pattern"].findall(text)
            self.assertEqual(fixture["question_count"], len(matches), path)
            self.assertEqual(
                list(range(1, fixture["question_count"] + 1)),
                [int(number) for number in matches],
                path,
            )

    def test_public_question_blocks_have_no_explicit_answer_fields(self) -> None:
        """Public question payloads expose options, not answer fields."""
        for fixture in EXPECTED_PUBLIC_FIXTURES:
            path = REPOSITORY_ROOT / fixture["relative_path"]
            text = path.read_text(encoding="utf-8")
            blocks = _question_blocks(text, fixture["question_pattern"])
            self.assertEqual(fixture["question_count"], len(blocks), path)

            for number, block in enumerate(blocks, start=1):
                for field_pattern in EXPLICIT_ANSWER_FIELD_PATTERNS:
                    self.assertIsNone(
                        field_pattern.search(block),
                        f"campo di risposta esplicito nella domanda {number} di {path}",
                    )

    def test_docs_identify_external_protected_key(self) -> None:
        """The public protocol points to the external key and keeps it out of git."""
        readme = (PUBLIC_EXAMS_ROOT / "README.md").read_text(encoding="utf-8")
        protocol = (PUBLIC_EXAMS_ROOT / "PROTOCOLLO_VALUTAZIONE.md").read_text(
            encoding="utf-8"
        )
        gitignore = (REPOSITORY_ROOT / ".gitignore").read_text(encoding="utf-8")

        for document in (readme, protocol):
            self.assertIn("ESAMI_RISPOSTE/", document)
        self.assertRegex(readme, r"(?i)fuori repository|archivio riservato")
        self.assertRegex(protocol, r"(?i)NON committare mai|non vanno mai.*repository")
        self.assertIn("ESAMI_RISPOSTE/", gitignore)
        self.assertFalse((REPOSITORY_ROOT / "ESAMI_RISPOSTE").exists())


if __name__ == "__main__":
    unittest.main()
