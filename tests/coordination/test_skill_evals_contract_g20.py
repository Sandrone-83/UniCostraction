"""G20 skill-evaluation contract tests using only in-memory fixtures."""

from __future__ import annotations

import unittest

from tools.validate_skill_evals_g20 import validate_evals


def _manifest(*skill_ids: str) -> dict:
    return {"schema_version": "g18", "skills": [{"id": skill_id} for skill_id in skill_ids]}


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

    def test_case_ids_and_skill_coverage_are_one_to_one(self) -> None:
        evaluations = [_case(), _case(case_id="case-cila-basics"), _case(skill_id="skill-unknown", case_id="case-unknown")]

        findings = validate_evals(_manifest("skill-cila-basics", "skill-urbanistica-basics"), evaluations)

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
