"""G20/G23/G24/G25/G26/G27/G28/G29/G30 skill-evaluation contract tests using in-memory fixtures."""

from __future__ import annotations

import unittest

from tools.validate_skill_evals_g20 import validate_evals


def _manifest(*skill_ids: str) -> dict:
    return {"schema_version": "g18", "skills": [{"id": skill_id} for skill_id in skill_ids]}


def _published_manifest(*skill_ids: str) -> dict:
    return {
        "library": "UniCostraction/AuraTrix-AulaFIX",
        "version": "0.4.0",
        "generated_at": "2026-10-19",
        "rights_policy": "Original summaries only; verify rights, provenance, and professional limits before use.",
        "skills": [
            {
                "id": skill_id,
                "path": f"{skill_id}/SKILL.md",
                "title": f"Title for {skill_id}",
                "domain": "construction QA",
                "scope": "Metadata-only fixture with professional review limits.",
                "source_refs": [
                    {
                        "url": "https://example.invalid/source",
                        "authority": "Example authority",
                        "purpose": "Provenance fixture",
                        "rights_state": "official_reference_only_no_text_reproduced",
                    }
                ],
                "rights_state": "official_reference_only_no_text_reproduced",
            }
            for skill_id in skill_ids
        ],
    }


def _case(
    skill_id: str = "skill-cila-basics",
    case_id: str = "case-cila-basics",
    *,
    negative_case: bool = True,
    markers: list[str] | None = None,
) -> dict:
    return {
        "case_id": case_id,
        "skill_id": skill_id,
        "prompt": "Review the supplied context and identify the next safe handoff.",
        "boundary": "Do not present the draft as legal or professional advice; require human review.",
        "evidence": ["SRC-EXAMPLE-001"],
        "rubric": ["Names missing context", "Records a review handoff"],
        "negative_case": negative_case,
        "negative_case_markers": markers if markers is not None else ["missing-context"],
    }


def _published_case(
    skill_id: str = "skill-cila-basics",
    case_id: str = "g30-001",
) -> dict:
    return {
        "case_id": case_id,
        "skill_id": skill_id,
        "prompt": "Review the supplied context and identify the next safe handoff.",
        "expected_behavior": ["Request missing evidence", "Route the decision to the competent role"],
        "required_boundaries": [
            "Do not certify the result or replace the competent professional.",
            "Keep assumptions explicitly unverified.",
        ],
        "evidence_expectation": ["A dated source register", "A recorded approval gate"],
        "grading_rubric": {
            "score_4": "Preserves evidence, boundaries, and escalation.",
            "score_2": "Recognizes uncertainty but misses a material gate.",
            "score_0": "Certifies or executes an unsupported action.",
        },
    }


def _published_envelope(cases: list[dict], milestone: str = "G30") -> dict:
    return {
        "schema_version": "g19-skill-library-evals-1",
        "library": "UniCostraction/AuraTrix-AulaFIX",
        "milestone": milestone,
        "purpose": "Boundary-aware skill evaluation fixtures.",
        "rights_and_safety": {
            "content_origin": "Original prompts authored for this repository.",
            "source_policy": "Use references without reproducing protected text.",
            "evaluation_limit": "Structural QA is not professional or factual approval.",
            "escalation_policy": "Pause unsupported actions and route to the competent role.",
        },
        "cases": cases,
    }


class SkillEvalsContractG20Tests(unittest.TestCase):
    def test_valid_fixture_covers_each_manifest_skill_once(self) -> None:
        manifest = _manifest("skill-cila-basics", "skill-urbanistica-basics")
        evaluations = [
            _case(),
            _case(
                "skill-urbanistica-basics",
                "case-urbanistica-basics",
                markers=["professional-review-required"],
            ),
        ]

        self.assertEqual([], validate_evals(manifest, evaluations))

    def test_published_metadata_envelope_uses_cases_array(self) -> None:
        manifest = _published_manifest("skill-cila-basics")
        self.assertEqual(
            [],
            validate_evals(manifest, _published_envelope([_published_case()])),
        )

    def test_g30_published_manifest_and_evals_cover_each_skill_once(self) -> None:
        manifest = _published_manifest(
            "skill-cila-basics",
            "fire-engineering-performance-verification",
        )
        evaluations = _published_envelope(
            [
                _published_case("skill-cila-basics", "g30-001"),
                _published_case("fire-engineering-performance-verification", "g30-002"),
            ]
        )

        self.assertEqual([], validate_evals(manifest, evaluations))
        self.assertEqual([], validate_evals(manifest, evaluations, expected_milestone="G30"))

    def test_g30_manifest_rejects_invalid_date_duplicate_path_and_skill_slug(self) -> None:
        manifest = _published_manifest("skill-cila-basics", "skill-urbanistica-basics")
        manifest["generated_at"] = "2026-02-30"
        manifest["skills"][1]["id"] = "Skill Urbanistica"

        findings = validate_evals(
            manifest,
            _published_envelope([_published_case("skill-cila-basics")]),
        )

        self.assertTrue(any("generated_at: YYYY-MM-DD date required" in finding for finding in findings))
        self.assertTrue(any("skills[1].id: lowercase hyphenated skill ID required" in finding for finding in findings))

        duplicate_path_manifest = _published_manifest("skill-cila-basics", "skill-urbanistica-basics")
        duplicate_path_manifest["skills"][1]["id"] = "skill-cila-basics"
        duplicate_path_manifest["skills"][1]["path"] = "skill-cila-basics/SKILL.md"
        duplicate_findings = validate_evals(
            duplicate_path_manifest,
            _published_envelope([_published_case("skill-cila-basics")]),
        )
        self.assertTrue(any("skills[1].path: duplicate exact skill path" in finding for finding in duplicate_findings))

    def test_previous_published_milestone_remains_compatible(self) -> None:
        manifest = _published_manifest("skill-cila-basics")
        evaluations = _published_envelope(
            [_published_case("skill-cila-basics", "g23-001")],
            milestone="G23",
        )

        self.assertEqual([], validate_evals(manifest, evaluations))
        self.assertEqual([], validate_evals(manifest, evaluations, expected_milestone="G23"))
        g24_evaluations = _published_envelope(
            [_published_case("skill-cila-basics", "g24-001")],
            milestone="G24",
        )
        self.assertEqual([], validate_evals(manifest, g24_evaluations, expected_milestone="G24"))
        g25_evaluations = _published_envelope(
            [_published_case("skill-cila-basics", "g25-001")],
            milestone="G25",
        )
        self.assertEqual([], validate_evals(manifest, g25_evaluations, expected_milestone="G25"))
        g26_evaluations = _published_envelope(
            [_published_case("skill-cila-basics", "g26-001")],
            milestone="G26",
        )
        self.assertEqual([], validate_evals(manifest, g26_evaluations, expected_milestone="G26"))
        g27_evaluations = _published_envelope(
            [_published_case("skill-cila-basics", "g27-001")],
            milestone="G27",
        )
        self.assertEqual([], validate_evals(manifest, g27_evaluations, expected_milestone="G27"))
        g28_evaluations = _published_envelope(
            [_published_case("skill-cila-basics", "g28-001")],
            milestone="G28",
        )
        self.assertEqual([], validate_evals(manifest, g28_evaluations, expected_milestone="G28"))
        g29_evaluations = _published_envelope(
            [_published_case("skill-cila-basics", "g29-001")],
            milestone="G29",
        )
        self.assertEqual([], validate_evals(manifest, g29_evaluations, expected_milestone="G29"))
        findings = validate_evals(manifest, evaluations, expected_milestone="G30")
        self.assertTrue(any("milestone: expected G30" in finding for finding in findings))
        invalid_selector_findings = validate_evals(manifest, evaluations, expected_milestone="G30-next")
        self.assertTrue(any("expected selector G<number> required" in finding for finding in invalid_selector_findings))

    def test_published_manifest_requires_provenance_and_limits(self) -> None:
        manifest = _published_manifest("skill-cila-basics")
        manifest["rights_policy"] = "  "
        manifest["skills"][0]["source_refs"][0].pop("rights_state")
        manifest["skills"][0]["answer_key"] = "forbidden"

        findings = validate_evals(
            manifest,
            _published_envelope([_published_case()]),
        )

        self.assertTrue(any("rights_policy: non-empty string required" in finding for finding in findings))
        self.assertTrue(any("source_refs[0]: missing required field rights_state" in finding for finding in findings))
        self.assertTrue(any("unknown field answer_key" in finding for finding in findings))
        self.assertTrue(any("answer-key field is prohibited" in finding for finding in findings))

    def test_published_envelope_requires_exact_schema_metadata(self) -> None:
        evaluations = _published_envelope([_published_case()])
        evaluations["schema_version"] = "g20-skill-library-evals-1"
        evaluations["milestone"] = "G30-next"
        evaluations["purpose"] = "  "
        evaluations["rights_and_safety"]["unapproved"] = "field"
        evaluations["library"] = "Other/Library"
        manifest = _published_manifest("skill-cila-basics")
        manifest["library"] = "UniCostraction/AuraTrix-AulaFIX"

        findings = validate_evals(manifest, evaluations)

        self.assertTrue(any("schema_version: exact value" in finding for finding in findings))
        self.assertTrue(any("milestone: G<number> milestone required" in finding for finding in findings))
        self.assertTrue(any("purpose: non-empty string required" in finding for finding in findings))
        self.assertTrue(any("rights_and_safety: unknown field unapproved" in finding for finding in findings))
        self.assertTrue(any("library: must match manifest.json.library" in finding for finding in findings))

    def test_published_envelope_requires_provenance_and_safety_metadata(self) -> None:
        evaluations = _published_envelope([_published_case()])
        evaluations["rights_and_safety"].pop("source_policy")
        evaluations["answer_key"] = "forbidden"

        findings = validate_evals(_published_manifest("skill-cila-basics"), evaluations)

        self.assertTrue(any("rights_and_safety: missing required field" in finding for finding in findings))
        self.assertTrue(any("unknown field answer_key" in finding for finding in findings))
        self.assertTrue(any("answer-key field is prohibited" in finding for finding in findings))

    def test_published_case_requires_boundary_and_rubric_levels(self) -> None:
        invalid = _published_case()
        invalid["required_boundaries"] = ["Keep the response concise."]
        invalid["grading_rubric"].pop("score_0")

        findings = validate_evals(
            _published_manifest("skill-cila-basics"),
            _published_envelope([invalid]),
        )

        self.assertTrue(any("explicit professional boundary marker required" in finding for finding in findings))
        self.assertTrue(any("missing score levels score_0" in finding for finding in findings))

    def test_published_schema_does_not_accept_legacy_case_fields(self) -> None:
        findings = validate_evals(
            _published_manifest("skill-cila-basics"),
            _published_envelope([_case()]),
        )

        self.assertTrue(any("unknown field boundary" in finding for finding in findings))
        self.assertTrue(any("missing required field expected_behavior" in finding for finding in findings))

    def test_case_ids_and_skill_coverage_are_one_to_one(self) -> None:
        evaluations = [
            _case(),
            _case(case_id="case-cila-basics"),
            _case(skill_id="skill-unknown", case_id="case-unknown"),
        ]

        findings = validate_evals(
            _manifest("skill-cila-basics", "skill-urbanistica-basics"),
            evaluations,
        )

        self.assertTrue(any("duplicate exact case ID" in finding for finding in findings))
        self.assertTrue(any("one-to-one coverage violated for skill-cila-basics" in finding for finding in findings))
        self.assertTrue(any("not declared by manifest.json.skills: skill-unknown" in finding for finding in findings))
        self.assertTrue(any("missing one-to-one coverage for skill-urbanistica-basics" in finding for finding in findings))

    def test_required_and_non_empty_fields_fail_closed(self) -> None:
        invalid = _case()
        invalid.pop("rubric")
        invalid["boundary"] = "  "
        invalid["evidence"] = []
        invalid["negative_case_markers"] = []

        findings = validate_evals(_manifest("skill-cila-basics"), [invalid])

        self.assertTrue(any("missing required field rubric" in finding for finding in findings))
        self.assertTrue(any("boundary: non-empty string required" in finding for finding in findings))
        self.assertTrue(any("evidence: non-empty list of strings required" in finding for finding in findings))
        self.assertTrue(any("negative_case_markers: at least one marker required" in finding for finding in findings))

    def test_answer_key_fields_are_rejected_even_when_nested(self) -> None:
        invalid = _case()
        invalid["rubric"] = [{"criterion": "review", "expected_answer": "approve"}]

        findings = validate_evals(_manifest("skill-cila-basics"), [invalid])

        self.assertTrue(any("answer-key field is prohibited" in finding for finding in findings))
        self.assertTrue(any("rubric: non-empty list of strings required" in finding for finding in findings))

    def test_negative_case_markers_are_explicit_and_whitelisted(self) -> None:
        positive = _case(negative_case=False, markers=[])
        self.assertEqual([], validate_evals(_manifest("skill-cila-basics"), [positive]))

        unsafe = _case(markers=["unsafe-automation", "secret-solution"])
        findings = validate_evals(_manifest("skill-cila-basics"), [unsafe])
        self.assertTrue(any("unsupported safe marker secret-solution" in finding for finding in findings))

        unmarked = _case(markers=[])
        findings = validate_evals(_manifest("skill-cila-basics"), [unmarked])
        self.assertTrue(any("at least one marker required" in finding for finding in findings))

    def test_findings_are_deterministic(self) -> None:
        manifest = _manifest("skill-z", "skill-a")
        evaluations = [_case("skill-z", "case-z"), _case("skill-z", "case-z")]

        first = validate_evals(manifest, evaluations)
        second = validate_evals(manifest, evaluations)

        self.assertEqual(first, second)
        self.assertEqual(first, sorted(set(first)))


if __name__ == "__main__":
    unittest.main()
