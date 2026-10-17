"""QA globale e limitato per la separazione dei file pubblici d'esame.

Il test copre tutti i ``ESAMI/*/domande.md`` pubblici compatibili con il
contratto del repository. Mantiene distinti il formato standard e il formato
legacy: non tenta di convertirli in un unico schema.

Il verdetto riguarda esclusivamente invarianti di formato e l'assenza di
campi espliciti di risposta nei blocchi di domanda. Non contiene né ricostruisce
answer key, lettere corrette, spiegazioni o giudizi sulle domande.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path
from typing import Pattern


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
PUBLIC_EXAMS_ROOT = REPOSITORY_ROOT / "UNIVERSITA_EDILIZIA" / "ESAMI"

# Il conteggio è un controllo di copertura dell'inventario pubblico presente
# alla base G2. Non è un conteggio di domande corrette o di esiti d'esame.
EXPECTED_PUBLIC_EXAM_FILE_COUNT = 73
EXPECTED_FORMAT_COUNTS = {"standard": 71, "legacy": 2}


# I due parser restano separati perché i generatori legacy hanno intestazioni
# diverse. Le regex riconoscono solo le intestazioni, non il contenuto delle
# domande o delle opzioni.
FORMAT_PATTERNS: dict[str, Pattern[str]] = {
    "standard": re.compile(r"(?m)^## Domanda (\d+)\s*$"),
    "legacy": re.compile(r"(?m)^\*\*D(\d+)\.\*\*"),
}


# Il controllo è strutturale: intercetta un campo nominato in testa a una
# riga, non parole simili dentro il testo della domanda o di un'opzione.
EXPLICIT_ANSWER_FIELD_PATTERN = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?(?:[*_`\"']*\s*)?"
    r"(?:lettera|risposta(?:\s+(?:corretta|esatta))?|risposta_corretta|"
    r"correct(?:_answer|_option)?|answer(?:_key)?|solution|soluzione)"
    r"(?:[*_`\"']*\s*)?[:=]"
)


def _public_exam_files() -> list[Path]:
    """Return only the public exam payloads defined by the repository contract."""
    return sorted(PUBLIC_EXAMS_ROOT.glob("*/domande.md"))


def _matching_formats(text: str) -> dict[str, list[re.Match[str]]]:
    return {
        format_name: list(pattern.finditer(text))
        for format_name, pattern in FORMAT_PATTERNS.items()
    }


def _question_blocks(text: str, matches: list[re.Match[str]]) -> list[str]:
    return [
        text[
            match.end() : (
                matches[index + 1].start()
                if index + 1 < len(matches)
                else len(text)
            )
        ]
        for index, match in enumerate(matches)
    ]


class ExamSeparationG2Tests(unittest.TestCase):
    def test_all_public_exam_files_use_one_supported_format(self) -> None:
        """Every public payload is covered by exactly one parser."""
        files = _public_exam_files()
        self.assertEqual(EXPECTED_PUBLIC_EXAM_FILE_COUNT, len(files))

        observed_format_counts = {format_name: 0 for format_name in FORMAT_PATTERNS}
        for path in files:
            self.assertTrue(path.is_file(), path)
            text = path.read_text(encoding="utf-8")
            self.assertTrue(text.strip(), path)

            matches_by_format = _matching_formats(text)
            matching_formats = [
                format_name
                for format_name, matches in matches_by_format.items()
                if matches
            ]
            self.assertEqual(
                1,
                len(matching_formats),
                f"formato pubblico non univoco o non riconosciuto: {path}",
            )
            observed_format_counts[matching_formats[0]] += 1

        self.assertEqual(EXPECTED_FORMAT_COUNTS, observed_format_counts)

    def test_all_public_exam_numbering_is_consecutive(self) -> None:
        """Each supported parser sees a complete 1..N sequence."""
        for path in _public_exam_files():
            text = path.read_text(encoding="utf-8")
            matches_by_format = _matching_formats(text)
            matching_formats = [
                format_name
                for format_name, matches in matches_by_format.items()
                if matches
            ]
            self.assertEqual(1, len(matching_formats), path)

            format_name = matching_formats[0]
            matches = matches_by_format[format_name]
            numbers = [int(match.group(1)) for match in matches]
            self.assertEqual(list(range(1, len(numbers) + 1)), numbers, path)

    def test_all_public_question_blocks_have_no_explicit_answer_fields(self) -> None:
        """Question blocks do not expose named response fields."""
        for path in _public_exam_files():
            text = path.read_text(encoding="utf-8")
            matches_by_format = _matching_formats(text)
            matching_formats = [
                format_name
                for format_name, matches in matches_by_format.items()
                if matches
            ]
            self.assertEqual(1, len(matching_formats), path)

            matches = matches_by_format[matching_formats[0]]
            for number, block in enumerate(_question_blocks(text, matches), start=1):
                self.assertIsNone(
                    EXPLICIT_ANSWER_FIELD_PATTERN.search(block),
                    f"campo di risposta esplicito nella domanda {number} di {path}",
                )


if __name__ == "__main__":
    unittest.main()
