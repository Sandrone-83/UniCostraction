"""Build a deterministic, non-semantic map between university packs and exams.

The report uses only directory names, the first simple ``corso:`` value in
``COURSE.yaml``, local README headings, exam headings, and the local exam
README's legacy note.  Name overlap is emitted as an observed signal, never
as proof that an exam tests a pack or that two domains are semantically equal.

Usage::

    python tools/uni_pack_exam_map_g4.py
    python tools/uni_pack_exam_map_g4.py --root . \
        --output docs/coordination/UNI_PACK_EXAM_MAP_G4.json
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path
from typing import Iterable


REPORT_RELATIVE_PATH = Path("docs/coordination/UNI_PACK_EXAM_MAP_G4.json")
PACK_ROOT = Path("UNIVERSITA_EDILIZIA")
EXAM_ROOT = PACK_ROOT / "ESAMI"
PACK_SUFFIX = "_PACK"
IGNORED_EXAM_DIRECTORIES = frozenset({"RISPOSTE_CANDIDATO"})
STOPWORDS = frozenset(
    {
        "a",
        "al",
        "alla",
        "all",
        "con",
        "da",
        "de",
        "del",
        "della",
        "delle",
        "di",
        "e",
        "ed",
        "gli",
        "i",
        "il",
        "in",
        "la",
        "le",
        "per",
        "un",
        "una",
    }
)
COURSE_RE = re.compile(r"^\s*corso\s*:\s*(.*?)\s*$", re.IGNORECASE)
HEADING_RE = re.compile(r"^\s{0,3}#\s+(.+?)\s*#*\s*$")
EXAM_HEADING_RE = re.compile(r"^\s*#\s+ESAME\s*-\s*(.+?)\s*$", re.IGNORECASE)
# Underscores separate directory-name words; they must not remain inside a token.
TOKEN_RE = re.compile(r"[^\W_]+", re.UNICODE)


def _ascii_casefold(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    return normalized.encode("ascii", "ignore").decode("ascii").casefold()


def _key(value: str) -> str:
    return "_".join(TOKEN_RE.findall(_ascii_casefold(value)))


def _tokens(value: str) -> list[str]:
    return [token for token in TOKEN_RE.findall(_ascii_casefold(value)) if token not in STOPWORDS]


def _root(token: str) -> str:
    """Apply only a bounded name-level suffix rule, not semantic matching."""

    for suffix in ("zioni", "zione", "iche", "ichi", "ica", "ico", "ale", "ali", "ire", "are", "ere"):
        if len(token) - len(suffix) >= 5 and token.endswith(suffix):
            return token[: -len(suffix)]
    if len(token) >= 6 and token[-1] in "aeiou":
        return token[:-1]
    return token


def _name_roots(values: Iterable[str]) -> set[str]:
    return {_root(token) for value in values for token in _tokens(value)}


def _quoted_scalar(value: str) -> str:
    value = value.strip().rstrip(",").strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1].strip()
    return value


def _first_course_title(path: Path) -> str | None:
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        match = COURSE_RE.match(line)
        if match:
            value = _quoted_scalar(match.group(1))
            return value or None
    return None


def _first_heading(path: Path) -> str | None:
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        match = HEADING_RE.match(line)
        if match:
            value = re.split(r"\s+[—–-]\s+", match.group(1).strip(), maxsplit=1)[0].strip()
            return value or None
    return None


def _exam_heading(path: Path) -> str | None:
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        match = EXAM_HEADING_RE.match(line)
        if match:
            value = re.sub(r"\s+\([^)]*\).*?$", "", match.group(1)).strip()
            return value or None
    return None


def _legacy_exam_ids(path: Path) -> set[str]:
    """Read only the explicit legacy rows from the local exam README."""

    if not path.is_file():
        return set()
    legacy: set[str] = set()
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if "legacy" not in line.casefold():
            continue
        cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        if cells and cells[0] and cells[0].upper() not in {"SETTORE", "NOTE"}:
            legacy.add(cells[0])
    return legacy


def _corpus_roots(root: Path) -> tuple[Path, Path]:
    """Resolve the production layout and the compact test-fixture layout."""

    production_pack_root = root / PACK_ROOT
    if production_pack_root.is_dir() and (production_pack_root / "ESAMI").is_dir():
        return production_pack_root, production_pack_root / "ESAMI"
    return root, root / "ESAMI"


def _pack_records(root: Path) -> list[dict[str, object]]:
    pack_root, _ = _corpus_roots(root)
    records: list[dict[str, object]] = []
    for path in sorted(pack_root.glob(f"*{PACK_SUFFIX}"), key=lambda current: current.name.casefold()):
        if not path.is_dir():
            continue
        manifest = path / "COURSE.yaml"
        readme = path / "README.md"
        title = _first_course_title(manifest) if manifest.is_file() else None
        heading = _first_heading(readme) if readme.is_file() else None
        stem = path.name[: -len(PACK_SUFFIX)]
        labels = [stem]
        if title:
            labels.append(title)
        if heading:
            labels.append(heading)
        records.append(
            {
                "pack_id": path.name,
                "pack_path": path.relative_to(root).as_posix(),
                "directory_name": path.name,
                "directory_key": _key(stem),
                "course_title": title,
                "readme_heading": heading,
                "source_files": [
                    item.relative_to(root).as_posix()
                    for item in (manifest, readme)
                    if item.is_file()
                ],
                "_labels": labels,
                "_roots": _name_roots(labels),
            }
        )
    return records


def _exam_records(root: Path) -> list[dict[str, object]]:
    _, exam_root = _corpus_roots(root)
    legacy_ids = _legacy_exam_ids(exam_root / "README.md")
    records: list[dict[str, object]] = []
    for path in sorted(exam_root.iterdir(), key=lambda current: current.name.casefold()):
        if not path.is_dir() or path.name in IGNORED_EXAM_DIRECTORIES:
            continue
        questions = path / "domande.md"
        if not questions.is_file():
            continue
        heading = _exam_heading(questions)
        labels = [path.name]
        if heading:
            labels.append(heading)
        records.append(
            {
                "exam_id": path.name,
                "exam_path": path.relative_to(root).as_posix(),
                "directory_name": path.name,
                "directory_key": _key(path.name),
                "exam_heading": heading,
                "legacy_observed": path.name in legacy_ids,
                "source_files": [
                    questions.relative_to(root).as_posix(),
                    (exam_root / "README.md").relative_to(root).as_posix(),
                ],
                "_labels": labels,
                "_roots": _name_roots(labels),
            }
        )
    return records


def _pair_evidence(pack: dict[str, object], exam: dict[str, object]) -> dict[str, object] | None:
    pack_key = str(pack["directory_key"])
    exam_key = str(exam["directory_key"])
    if pack_key == exam_key:
        return {
            "relation": "exact_name",
            "signal": "pack_stem_equals_exam_directory",
            "pack_value": pack_key,
            "exam_value": exam_key,
        }

    pack_labels = [str(value) for value in pack["_labels"]]  # type: ignore[index]
    exam_labels = [str(value) for value in exam["_labels"]]  # type: ignore[index]
    pack_roots = set(pack["_roots"])  # type: ignore[arg-type]
    exam_roots = set(exam["_roots"])  # type: ignore[arg-type]
    shared_roots = sorted(pack_roots & exam_roots)
    if not shared_roots:
        return None

    # A candidate is an observed name alias only when all non-stopword roots
    # from one exam label occur in at least one pack label, or vice versa.
    directional: list[dict[str, object]] = []
    for exam_label in exam_labels:
        wanted = {_root(token) for token in _tokens(exam_label)}
        if wanted and wanted <= pack_roots:
            directional.append({"exam_label": exam_label, "matched_roots": sorted(wanted)})
    for pack_label in pack_labels:
        wanted = {_root(token) for token in _tokens(pack_label)}
        if wanted and wanted <= exam_roots:
            directional.append({"pack_label": pack_label, "matched_roots": sorted(wanted)})
    if not directional:
        return None
    return {
        "relation": "alias_observed",
        "signal": "bounded_name_root_overlap",
        "shared_roots": shared_roots,
        "directional_matches": directional,
    }


def _public_record(record: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in record.items() if not key.startswith("_")}


def build_report(root: Path) -> dict[str, object]:
    root = root.resolve()
    packs = _pack_records(root)
    exams = _exam_records(root)
    pairs: list[dict[str, object]] = []
    for pack in packs:
        for exam in exams:
            evidence = _pair_evidence(pack, exam)
            if evidence is None:
                continue
            pairs.append(
                {
                    "pack_id": pack["pack_id"],
                    "exam_id": exam["exam_id"],
                    "relation": evidence["relation"],
                    "evidence": evidence,
                }
            )
    pairs.sort(key=lambda item: (str(item["pack_id"]), str(item["exam_id"])))

    pairs_by_pack: dict[str, list[dict[str, object]]] = {str(pack["pack_id"]): [] for pack in packs}
    pairs_by_exam: dict[str, list[dict[str, object]]] = {str(exam["exam_id"]): [] for exam in exams}
    for pair in pairs:
        pairs_by_pack[str(pair["pack_id"])].append(pair)
        pairs_by_exam[str(pair["exam_id"])].append(pair)

    def pack_classification(pack: dict[str, object]) -> str:
        candidates = pairs_by_pack[str(pack["pack_id"])]
        return (
            "unmatched_pack"
            if not candidates
            else "ambiguous"
            if len(candidates) > 1
            else "exact_name"
            if candidates[0]["relation"] == "exact_name"
            else "alias_observed"
        )

    def exam_classification(exam: dict[str, object]) -> str:
        candidates = pairs_by_exam[str(exam["exam_id"])]
        return (
            "unmatched_exam"
            if not candidates
            else "ambiguous"
            if len(candidates) > 1
            else "exact_name"
            if candidates[0]["relation"] == "exact_name"
            else "alias_observed"
        )

    pack_entries: list[dict[str, object]] = []
    for pack in packs:
        candidates = pairs_by_pack[str(pack["pack_id"])]
        pack_entries.append(
            {
                **_public_record(pack),
                "classification": pack_classification(pack),
                "candidate_exams": [
                    {
                        "exam_id": pair["exam_id"],
                        "relation": pair["relation"],
                        "evidence": pair["evidence"],
                    }
                    for pair in candidates
                ],
            }
        )

    exam_entries: list[dict[str, object]] = []
    for exam in exams:
        candidates = pairs_by_exam[str(exam["exam_id"])]
        exam_entries.append(
            {
                **_public_record(exam),
                "classification": exam_classification(exam),
                "candidate_packs": [
                    {
                        "pack_id": pair["pack_id"],
                        "relation": pair["relation"],
                        "evidence": pair["evidence"],
                    }
                    for pair in candidates
                ],
            }
        )

    counts = {
        "packs": len(packs),
        "exams": len(exams),
        "observed_pairs": len(pairs),
        "pack_classifications": {
            classification: sum(entry["classification"] == classification for entry in pack_entries)
            for classification in ("exact_name", "alias_observed", "unmatched_pack", "ambiguous")
        },
        "exam_classifications": {
            classification: sum(entry["classification"] == classification for entry in exam_entries)
            for classification in ("exact_name", "alias_observed", "unmatched_exam", "ambiguous")
        },
    }
    return {
        "schema_version": "g4.v1",
        "tool": "tools/uni_pack_exam_map_g4.py",
        "scope": {
            "pack_root": PACK_ROOT.as_posix(),
            "exam_root": EXAM_ROOT.as_posix(),
            "pack_selector": "UNIVERSITA_EDILIZIA/*_PACK",
            "exam_selector": "UNIVERSITA_EDILIZIA/ESAMI/*/domande.md",
            "included_evidence": [
                "pack and exam directory names",
                "COURSE.yaml first corso value",
                "pack README first heading",
                "exam domande.md first ESAME heading",
                "explicit legacy rows in UNIVERSITA_EDILIZIA/ESAMI/README.md",
            ],
            "source_of_truth": "selected checkout filesystem",
            "content_modified": False,
        },
        "method": {
            "exact_name": "pack directory stem without _PACK equals exam directory key",
            "alias_observed": "all non-stopword bounded name roots of one observed label occur in the other side's labels",
            "ambiguous": "more than one observed candidate remains for the item",
            "unmatched": "no observed name candidate; no semantic fallback is applied",
            "normalization": "Unicode NFKD, ASCII fold, casefold, tokenization; bounded Italian suffix stripping only for name signals",
            "semantic_inference": False,
        },
        "counts": counts,
        "packs": pack_entries,
        "exams": exam_entries,
        "boundaries": [
            "A candidate is a name/documentation signal, not proof of pack coverage or semantic equivalence.",
            "Legacy status is reported only when explicitly observed in the local exam README.",
            "No questions, answers, schede.jsonl records, or pack content are used to infer a mapping.",
            "No source content is edited, merged, moved, overwritten, or deleted.",
            "Ambiguous and unmatched items require human review before any canonical association is declared.",
        ],
    }


def write_report(root: Path, output: Path) -> None:
    report = build_report(root)
    output_path = output if output.is_absolute() else root / output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="checkout root (default: current directory)")
    parser.add_argument(
        "--output",
        type=Path,
        default=REPORT_RELATIVE_PATH,
        help=f"JSON report path relative to --root (default: {REPORT_RELATIVE_PATH.as_posix()})",
    )
    args = parser.parse_args(argv)
    write_report(args.root.resolve(), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
