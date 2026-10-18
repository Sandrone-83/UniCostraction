# UniCostraction G19 — skill-library release checklist

## Scope and decision

This checklist governs the scoped G19 coverage matrix in [`UNI_SKILL_COVERAGE_MATRIX_G19.json`](UNI_SKILL_COVERAGE_MATRIX_G19.json):

- 16 skill-library IDs with implementation evidence in the local `codex/uni-corpus` reference at `43f1286bc5b401d5015cc33ef5ee694325f73c45`;
- 36 canonical G17 skill IDs defined by the inventory taxonomy;
- 8 G18 family IDs defined as curriculum/dependency-graph proposals.

The inventory checkout observed for this artifact is `codex/uni-inventory` at `b0e0dc46761582db8ee2a696e955c6a2c00f708d`. The 16 implementation files are not present in that HEAD; the matrix records their separate local reference explicitly. No catalog, pack, exam, fixture, tool, test or corpus file is in scope for modification.

Current release decision: **BLOCKED**.

This is a release-control record, not a completeness claim. A path, manifest entry, taxonomy node, static check or passing structural test does not establish factual, technical, legal, educational, licensing, runtime or professional correctness.

## Cohort posture

| Cohort | Count | What the repository evidence supports | What it does not support | Current posture |
| --- | ---: | --- | --- | --- |
| Implemented skill-library IDs | 16 | A manifest entry and `SKILL.md` are observed in the recorded `codex/uni-corpus` reference | Presence in the inventory HEAD, authoritative knowledge, current source correctness, runtime behavior or professional suitability | `implementation` / `reference-only` / `needs-review` / `blocked` |
| G17 canonical skills | 36 | Canonical IDs, branch ownership and reference-only source posture are recorded in the G17 taxonomy and G18 graph | Semantic completeness, per-skill factual coverage, licensing clearance or promotion to verified knowledge | `reference-only` / `needs-review` / `blocked` |
| G18 proposed families | 8 | Proposed family IDs, boundaries and evaluation-gate concepts are recorded in the G18 graph/curriculum | Any implementation, content completeness, runtime capability or release authorization | `future` / `needs-review` / `blocked` |

## Mandatory release gates

Every gate applies to the scoped release, and a gate is not passed merely because another gate is green. `BLOCKED` is fail-closed: the release cannot be promoted or used as authoritative/professional content while it remains open.

| Gate | Required evidence to pass | Evidence currently available | Current state | Required owner/sign-off |
| --- | --- | --- | --- | --- |
| G19-PROV — provenance and context | Each item has source/interpretation/example/hypothesis separation, source version or snapshot, geography/jurisdiction and period/effective date where material, plus an auditable reviewer record | G17 defines the provenance contract; G18 proposes provenance/context families; the 16-item manifest contains source references and rights states, but not a completed per-item release packet for this checkout | **BLOCKED**; retain `needs-review` records | Provenance curator plus domain reviewer |
| G19-LIC — license and rights | Every external source, standard, dataset, image, media asset and derivative has verified terms, attribution, permitted use and publication/training decision | The 16-item manifest explicitly says references do not confer redistribution rights and several rights states require version/currentness verification; G17 records licensing review as incomplete | **BLOCKED**; no blanket license clearance inferred | Rights/licensing reviewer |
| G19-RUN — runtime and interoperability | Relevant CAD/BIM/coding/data/media workflow is exercised in its target environment with reproducible inputs/outputs; failures are retained with environment data | G18 defines runtime gate G18-E06, but this inventory artifact supplies no runtime result and no production-compatibility evidence | **BLOCKED**; static presence is insufficient | Runtime/QA owner and tool specialist |
| G19-LSF — legal, safety and financial review | Current-law, contract, procurement, tax, valuation, calculation, safety and risk-bearing claims have jurisdiction/time scope, explicit stop conditions and qualified review | G17 and the implemented skill documents state professional boundaries; the repository does not record completed qualified review for the scoped release | **BLOCKED**; no advice, certification, design approval, valuation or safety authorization | Qualified legal, safety, engineering and financial reviewers as applicable |
| G19-EVAL — evaluation and protected exam integrity | Reproducible evaluation exists without exposing protected answers; answer correctness, educational validity, semantic separation and source rights are reviewed independently | Existing structural/provenance QA separates public exams and does not prove answer-key correctness; G17 reports 6 G5 pending items and 85 open G14 clusters | **BLOCKED**; evaluation remains incomplete for release | Evaluation owner plus educational reviewer |
| G19-HUMAN — human sign-off and release record | Named reviewers decide scope, exceptions, limitations and release status; unresolved blockers remain visible; no automatic external action is implied | No completed sign-off packet exists in this G19 artifact; G18 explicitly requires professional review/release boundaries | **BLOCKED**; sign-off fields must be completed before promotion | Release owner with all applicable domain signatories |

## Gate acceptance rules

### Provenance

- [ ] The matrix row has a stable ID and an evidence reference.
- [ ] Source, interpretation, example and hypothesis are separate in the downstream record.
- [ ] Jurisdiction/geography, period/effective date and lifecycle are recorded when the claim depends on them.
- [ ] The evidence snapshot is reproducible from a named ref and commit; an uncommitted working-tree observation is not enough.
- [ ] The reviewer records what was checked and what remains unknown.

### License and rights

- [ ] Every external source has a verified rights decision for the intended use.
- [ ] Paid/restricted standards and manuals are treated as references; their text is not assumed redistributable.
- [ ] Public availability is not treated as commercial, training, publication or derivative-use permission.
- [ ] Images, media, marks, datasets and generated derivatives have separate rights/attribution decisions.
- [ ] A missing or ambiguous rights decision keeps the affected item `blocked`.

### Runtime and interoperability

- [ ] The route-specific tool is executed in its target environment, not only inspected statically.
- [ ] Inputs, versions, environment, outputs and failure modes are retained.
- [ ] CAD/BIM/data interchange claims have a reproducible sample and an explicit limitation statement.
- [ ] A runtime pass is not treated as proof of production safety, engineering adequacy or professional conformity.
- [ ] If no relevant runtime applies, the exception and responsible reviewer are recorded rather than inferred.

### Legal, safety and financial review

- [ ] Current-law and administrative claims carry jurisdiction and effective-date controls.
- [ ] Structural, MEP, calculation, construction and safety routes stop at qualified human review.
- [ ] Procurement, tax, contract, valuation, insurance and investment claims are bounded and reviewed by the appropriate professional.
- [ ] The record does not authorize filing, certification, payment, contract execution, safety clearance or professional sign-off automatically.
- [ ] Open risks and missing evidence are visible in the release decision.

### Evaluation

- [ ] The evaluation set and answer material are separated and access-controlled.
- [ ] Structural tests are reported separately from answer correctness, educational quality and source/licensing review.
- [ ] Duplicate or semantic-similarity signals create a human review queue; they do not trigger autonomous merge, deletion or rewriting.
- [ ] Evaluation results identify the exact snapshot, rubric, environment and reviewer.
- [ ] Failed, pending or unreviewed items remain blocked or explicitly excluded from the release scope.

### Human sign-off

- [ ] A named release owner confirms the exact scope and snapshot.
- [ ] Each applicable domain reviewer records a decision, date, limits and unresolved issues.
- [ ] The final record distinguishes `reference-only`, `needs-review`, `blocked` and `future` from any future `verified_knowledge` state.
- [ ] The release packet contains no claim of global completeness or professional certification.
- [ ] No external publication, message, filing, payment or execution is performed by this checklist.

## Promotion rule

No row may move from `reference-only` or `future` to authoritative/verified knowledge from this matrix alone. Promotion requires all applicable G19 gates, reproducible evidence and qualified human sign-off. For legal, safety, financial, calculation, rights and professional-document routes, an explicit reviewer decision and a use boundary are mandatory.

The 16 implementation records remain structurally implemented in their recorded local reference, but their `knowledge_status` stays `reference-only`. The 36 G17 records remain canonical taxonomy records, not a claim that every semantic subtopic is covered. The 8 G18 records remain proposed families and are not implementation counts.

## Structural and delivery checks for this commit

- [ ] JSON parses as one document.
- [ ] Matrix contains exactly 16 + 36 + 8 = 60 unique row IDs.
- [ ] Matrix order is deterministic and matches `matrix_contract.row_order`.
- [ ] Every G17 ID resolves to `UNI_SKILL_TAXONOMY_G17.json`/`UNI_SKILL_DEPENDENCY_GRAPH_G18.json`.
- [ ] Every G18 ID resolves to `g18_family_nodes` in `UNI_SKILL_DEPENDENCY_GRAPH_G18.json`.
- [ ] Candidate links are visibly marked `needs-review`; no link is presented as an approved equivalence.
- [ ] `git diff --check` passes.
- [ ] `git status --short` contains only these two G19 files before commit.
- [ ] Commit includes only these two G19 files.
- [ ] No push is performed by this task.

## Sign-off record

| Role | Name | Decision | Date | Notes |
| --- | --- | --- | --- | --- |
| Release owner | — | `pending` | — | Scope is currently blocked by open gates. |
| Provenance/domain reviewer | — | `pending` | — | Per-item source and context review not recorded here. |
| Rights/licensing reviewer | — | `pending` | — | Manifest rights states are not blanket clearance. |
| Runtime/QA reviewer | — | `pending` | — | No runtime evidence is asserted by this artifact. |
| Legal/safety/financial reviewers | — | `pending` | — | Apply only to relevant routes; no professional authorization implied. |
| Evaluation/education reviewer | — | `pending` | — | Structural exam QA is not answer correctness or didactic approval. |
