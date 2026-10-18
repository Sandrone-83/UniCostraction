# UniCostraction G20 — roadmap for six advanced facets

Status: `roadmap-only`, `release=blocked`, observed on 2026-10-18 in the
requested `codex/uni-inventory` worktree. This document defines controlled
follow-up work; it does not implement or promote any of the six facets.

## Evidence boundary

The G17 taxonomy says that a path, manifest or reference is structural
evidence only. Promotion requires provenance, version or date, rights,
qualified review and evaluation evidence. G18 adds explicit gates for
non-redundancy, document lifecycle, reproducible runtime checks and
professional review. G19 records the relevant reference-library rows as
`implementation`/`reference-only`/`needs-review`/`blocked`, while also saying
that their `SKILL.md` paths are not present in the inventory HEAD.

Accordingly, this roadmap uses the following vocabulary:

- `observed`: a path, file, script, manifest entry or statement was inspected
  in the selected checkout or in a G19 reference record;
- `proposed`: a capability, test or evidence packet to build; it is not an
  implementation claim;
- `needs-review`: a mapping, meaning, source, rights or scope decision still
  needs a human decision;
- `blocked`: the capability must not be promoted, used for professional output
  or automated external action until the named gate is satisfied.

No statement below certifies a CAD model, IFC exchange, render, PDF, SAL,
calculation, legal answer, licence, professional document or real-world
conformity.

## Canonical ownership and non-redundancy

The six items are lifecycle/runtime facets over existing canonical skills, not
six new copies of CAD, BIM, documents, accounting or law. The proposed
cross-cutting owners are:

| Facet | Canonical owner(s) to validate | Cross-cutting route | Non-redundancy decision |
|---|---|---|---|
| CAD API | `digital.cad_bim_and_interoperability`; possible `aec.design_representation` link | `g18.runtime_interoperability_validation`, `g18.evidence_document_control` | An API adapter tests or records operations; it does not create another CAD-domain skill or claim design authority. |
| IFC QA | `digital.cad_bim_and_interoperability`, `digital.asset_validation_and_data` | `g18.runtime_interoperability_validation`, `g18.evidence_document_control` | QA records schema, entity, property and geometry findings against a canonical model; it does not duplicate BIM teaching content. |
| Blender automation | `digital.asset_validation_and_data`; possible `media.visual_storytelling_and_content` link | `g18.runtime_interoperability_validation`, `g18.provenance_source_governance` | Automation is a reproducible asset/render workflow; it is not a second 3D, architecture or media curriculum. |
| PDF lifecycle | `documents.technical_records_and_reports`, `documents.evidence_provenance_and_audit`, `documents.templates_and_review_gates` | `g18.evidence_document_control`, `g18.provenance_source_governance` | Lifecycle state, hashes and review history govern a document; they do not duplicate its technical subject matter. |
| SAL reconciliation | Candidate links: `documents.technical_records_and_reports`, `business.enterprise_and_project_operations`, `science.explainable_calculation` | `g18.evidence_document_control`, `g18.professional_review_release` | Reconciliation compares supplied records and exposes differences; it does not become a new price-list, accounting or quantity-surveying skill. |
| Current-law lookup | `pa.italian_public_administration`, `pa.urban_building_procedures`, `pa.procurement_tax_safety_and_compliance` | `g18.context_jurisdiction_time`, `g18.provenance_source_governance`, `g18.professional_review_release` | Lookup supplies scoped sources and staleness signals; it does not create a second legal corpus or provide legal advice. |

Aliases, labels and lifecycle facets must resolve to one canonical ID. Similarity
or shared vocabulary is a review signal only: it never authorizes merge,
deletion, ownership transfer or answer-key exposure.

## Shared gates and deliverables

Every facet follows the same packet before any promotion:

1. **Scope packet** — canonical ID, intended task, artifact type, lifecycle,
   jurisdiction/period where material, risk class and explicit non-goals.
2. **Source/provenance register** — source path or URL, version or effective
   date, retrieval/observation date, checksum where applicable, source vs
   interpretation vs example vs hypothesis, attribution and rights state.
3. **Fixture and runtime record** — deterministic input, tool/runtime versions,
   command, output hashes or structured result, failure reproduction and
   environment notes. Static parsing or file presence is not runtime proof.
4. **Human review record** — named role, scope reviewed, decision, limitations,
   date and follow-up conditions. A document-shaped output is not an
   authorised filing, estimate, certification or professional opinion.
5. **Release decision** — `blocked` remains the default when a source, rights,
   runtime, semantic, safety, financial, legal or professional gate is open.

The six facet records below are intentionally written as acceptance contracts,
not as claims that the implementation already exists.

## 1. CAD API

**Non-redundancy rationale.** Keep API/tool invocation under the canonical
CAD/BIM interoperability owner. A command wrapper, importer, exporter or
geometry test is an execution facet and must not be catalogued as a new CAD
subject or as a substitute for a professional drawing review.

**Observed local evidence and limit.** `CAD_Library/training_corpus/README.md`
describes raw DXF/STEP/3DS material, parsed JSONL, a manifest with source and
licence fields, and parser tooling (`README.md:1-20, 35-60`). Its local
manifest distinguishes permissive MIT/BSD material from GPL research material
and records exclusions for undeclared or `NOASSERTION` sources
(`README.md:23-33, 45-50`). The repository also contains CAD build/analyse
scripts. No CAD API implementation, target application runtime, or live
AutoCAD/FreeCAD acceptance is established by this evidence.

**Prerequisites.**

- Choose the target API and version; record whether it is an offline parser,
  FreeCAD/other open tool, or a licensed desktop integration.
- Select only fixtures whose source and derivative rights are recorded; keep
  GPL/research fixtures out of a commercial or training route until separately
  cleared.
- Define the operation contract (read, create, transform, export) and the
  geometry invariants to preserve: units, coordinate frame, entity types,
  bounding box and object identity.
- Add a deterministic fixture, pinned environment and fail-closed error
  contract. Do not infer API success from a generated file alone.

**Expected evidence.** API/version manifest; input/output SHA-256; command log;
fixture licence and attribution; structured operation result; entity/type
counts and geometry invariant report; negative-case report; human review of
the resulting drawing/model when it is intended for a professional workflow.

**Runtime tests (proposed).** Run a read-only parse on a permissive DXF and a
STEP fixture; repeat it and compare structured output; run an export/import
round trip and compare declared invariants; reject malformed input and
unsupported versions; record timeout, missing dependency and licence-policy
failures. A passing parser test must not be reported as geometric or
professional conformity.

**Licensing gate.** The local CAD README labels MIT/BSD material as
`permissive` and LibreDWG test material as GPL-3.0/research. Preserve the
upstream notices and do not mix the classes in one release claim. Any target
application SDK, plug-in, font, block or derivative needs its own terms check.

**Professional review.** CAD technician/architect/engineer reviews units,
coordinates, layers, dimensions, topology and intended deliverable. The
reviewer must distinguish file integrity from geometric accuracy, regulatory
conformity and authorisation.

**Blocked states.** Target API/version unknown; runtime unavailable; fixture
rights unresolved; round-trip changes an invariant; malformed input is silently
accepted; output is presented as a professional drawing without review; or a
required licensed desktop/API integration cannot be used under its terms.

## 2. IFC QA

**Non-redundancy rationale.** IFC QA is a validation route over the existing
`digital.cad_bim_and_interoperability` and `digital.asset_validation_and_data`
owners. It records what a model contains and which checks passed; it does not
restate IFC/openBIM lessons or certify design adequacy.

**Observed local evidence and limit.** `Edilizia_Pack/manifest.json` records an
IFC index for six buildings with a MIT label and upstream URL. The raw folder
contains IFC files and a local MIT notice. `Edilizia_Pack/serialize_edilizia.py`
describes a proposed index operation that reads `FILE_SCHEMA`/`FILE_NAME`,
counts entity types in the first 60 KB and writes licence/attribution metadata
(`serialize_edilizia.py:194-221`). The generated
`Edilizia_Pack/parsed/ifc_bim_index.jsonl` is not present in this checkout, so
the index is not claimed as generated or validated here. G19 separately
records an IFC skill in `codex/uni-corpus`, but `head_presence_in_inventory_checkout`
is `false` (`UNI_SKILL_COVERAGE_MATRIX_G19.json:114-124`).

**Prerequisites.** Pin an IFC parser/schema profile; inventory every model and
checksum; define required entity/property/relationship checks; record whether
checks are lexical, schema-level, geometric or semantic; and define the
failure severity and human escalation path.

**Expected evidence.** Per-file manifest; schema and file header; parser/tool
version; entity and relationship counts; required property-set findings;
coordinate/unit report; geometry or placement findings; deterministic report
hash; malformed-model reproduction; MIT attribution and rights record; BIM
coordinator decision.

**Runtime tests (proposed).** Parse each local IFC fixture; compare the
structured summary across two runs; assert that required header/schema fields
are either present or explicitly flagged; detect duplicate GlobalIds, missing
required properties, invalid references, unit/coordinate anomalies and
truncated input; preserve a failing report for each negative fixture. A text
scan or schema pass does not prove clash-free geometry, constructability or
professional conformity.

**Licensing gate.** Retain the local MIT notice and the upstream attribution
recorded by the serializer. Confirm that any parser, schema profile, property
set, sample derivative and downstream publication has compatible terms; the
local MIT file does not clear unrelated sources.

**Professional review.** BIM coordinator or qualified design professional
reviews the check profile, severity thresholds, coordinate interpretation and
any decision that could affect a deliverable or a contract.

**Blocked states.** Parser/schema version not pinned; raw model provenance or
licence incomplete; generated index absent; model is truncated or invalid;
coordinates/units cannot be interpreted; semantic checks are unreviewed; or QA
results are used as design approval.

## 3. Blender automation

**Non-redundancy rationale.** Blender automation is an asset-processing and
reproducibility facet linked to digital asset validation and, where relevant,
visual storytelling. It does not create a second architectural/CAD curriculum
and it cannot turn an interpreted model into verified real-world geometry.

**Observed local evidence and limit.** G19 records a Blender skill in the
`codex/uni-corpus` reference with `head_presence_in_inventory_checkout=false`
and `release_status=blocked` (`UNI_SKILL_COVERAGE_MATRIX_G19.json:129-138`). No
Blender executable, `.blend` fixture or `bpy` automation is established in
the selected checkout by this roadmap's preflight. The local evidence is
therefore a reference/coverage record, not a runtime capability claim.

**Prerequisites.** Select and pin a Blender version; provide an approved
fixture or a clearly labelled synthetic scene; define headless vs interactive
execution; declare camera, units, collections, materials and output contract;
record all external textures/fonts/HDRIs/models; and separate source geometry,
interpretation and concept art.

**Expected evidence.** Blender version and command log; input scene/source
register; `.blend` and script hashes; object/material/camera/collection counts;
scene validation report; output image/render hash; deterministic rerun result;
asset attribution and rights; visual and geometric review record.

**Runtime tests (proposed).** Run a headless scene open; assert expected object
and collection names; run the automation twice and compare a normalized scene
manifest; render a small controlled fixture and compare output metadata/hash
with an allowed tolerance; fail on missing assets, hidden dependency, invalid
paths or non-deterministic random seeds. Do not call a render an as-built,
survey or compliant model.

**Licensing gate.** Blender software terms and every scene asset, texture,
font, HDRI, plug-in and generated derivative require a separate record. No
local Blender asset licence is established here; the facet remains blocked for
publication until rights and attribution are complete.

**Professional review.** Architect/technician or visualisation reviewer
checks the source geometry, interpretation notes, scale, camera and intended
use. If the scene represents a real property, approval of the 2D/source basis
precedes 3D or render use.

**Blocked states.** Blender/runtime unavailable; no approved source geometry;
missing or incompatible asset rights; non-deterministic or incomplete script;
render differs from the approved basis; or a concept render is labelled as
surveyed, authorised, compliant or construction-ready.

## 4. PDF lifecycle

**Non-redundancy rationale.** PDF lifecycle governs source capture, extraction,
versioning, review, publication and archival state. The technical subject of a
PDF remains owned by its canonical document or domain skill; the lifecycle
route does not make a PDF authoritative merely because it is readable.

**Observed local evidence and limit.** `Edilizia_Pack/extract_pdf_text.py` uses
`pypdf`, writes page markers, checkpoints every 25 pages and removes the
progress file on completion (`extract_pdf_text.py:1-34`). The checkout contains
raw PDF/text material under `Edilizia_Pack/raw`, and `Edilizia_Pack/manifest.json`
records source, URL and licence fields. G18 requires artifact state, version,
decision, reviewer and audit trail; a document-shaped file is not an authorised
filing (`UNI_SKILL_DEPENDENCY_GRAPH_G18.json:164-173`). The extractor's
presence is not a completed end-to-end lifecycle test.

**Prerequisites.** Define states such as `ingested`, `extracted`, `review`,
`approved`, `published` and `archived`; capture source hash, page count,
metadata, extraction tool/version, output hash and reviewer; distinguish OCR
from native text; and define retention, redaction and publication policy.

**Expected evidence.** Source PDF and checksum; page-count and metadata
record; extracted text with page anchors; extraction log and restart/recovery
record; visual spot-check; licence/attribution decision; state transitions;
reviewer log; and a final disposition that may remain blocked.

**Runtime tests (proposed).** Run extraction on a small known PDF and compare
page markers and output hash; interrupt at a checkpoint and resume; rerun a
completed source; reject corrupt/encrypted/unreadable input with an explicit
failure; compare text/page counts to a human spot-check; and test path,
encoding and redaction controls. A successful text extraction does not prove
the source is current, complete, legally reusable or professionally correct.

**Licensing gate.** Use the manifest's licence field as an input to review, not
as blanket clearance. Official acts, public-domain material, CC BY-SA material,
commercial sources and derived OCR/text each need a recorded treatment,
attribution and publication/training decision.

**Professional review.** Document controller and, for technical/legal content,
the appropriate engineer, architect, accountant or lawyer review completeness,
version, scope, signatures and intended use before `published` or professional
consumption.

**Blocked states.** Source hash/version missing; extraction incomplete or
unreviewed; OCR/page loss not assessed; rights unknown; redaction/privacy
review open; wrong document state; or a template is mistaken for a signed or
filed professional document.

## 5. SAL reconciliation

**Non-redundancy rationale.** SAL reconciliation is a controlled comparison of
provided progress, quantity, contract and payment records. It is not a new
accounting or price-list corpus, and it cannot replace the responsible
direttore dei lavori, quantity surveyor, accountant or contracting authority.

**Observed local evidence and limit.** `Edilizia_Pack/README.md` describes
glossary coverage including SAL and construction accounting
(`README.md:110-119`) and describes a `parsed/documenti_tecnici.jsonl` corpus
with a SAL template with retentions (`README.md:155-163`). The referenced
`parsed/documenti_tecnici.jsonl` is absent in the selected checkout. No
reconciler, approved measurement ledger, contract, price-list provenance or
live financial integration is established here. The facet is therefore a
proposal, not an implementation claim.

**Prerequisites.** Define a versioned input contract for contract items,
measurement records, units, approved quantities, unit prices, period, prior
SAL, current SAL, retentions, taxes, currency and supporting documents. Keep
source measurements and computed totals separate; use exact decimal arithmetic;
record variation orders and approval status; and define tolerance/rounding
rules with the responsible professional.

**Expected evidence.** Immutable input packet and hashes; source-to-line-item
mapping; unit/quantity/price calculation trace; prior/current/cumulative
totals; retention/tax/currency treatment; discrepancy classification; duplicate
or missing-source report; independent recomputation; and signed or explicitly
pending human decision.

**Runtime tests (proposed).** Reconcile a synthetic fixture with exact decimal
totals; rerun for determinism; test rounding at line and total level; detect
duplicate lines, missing measurements, changed unit prices, cumulative-total
regressions, currency mismatch, unsupported variations and a deliberately
inconsistent SAL. Verify that an unresolved difference produces `blocked` and
no automatic invoice, payment, reminder or filing.

**Licensing gate.** Confirm rights for every price list, contract, invoice,
template and imported document. The local README labels some educational
material as original/public-domain while warning that cited official
standards are excluded or need official verification; that does not clear a
commercial prezzario or a customer document for reuse.

**Professional review.** Direttore dei lavori/contabilità lavori and, where
financial or contractual consequences exist, the responsible accountant or
contract administrator review source measurements, variations, retentions,
taxes, approvals and discrepancy disposition.

**Blocked states.** Missing approved measurement or contract baseline; source
or price-list rights unresolved; arithmetic or currency mismatch; variation not
approved; cumulative totals do not reconcile; professional reviewer absent; or
any request to send, pay, certify or file automatically.

## 6. Current-law lookup

**Non-redundancy rationale.** Current-law lookup is a source-selection,
jurisdiction and effective-date workflow over the canonical Italian PA/legal
owners. It does not copy statutes into a new skill, convert a historical text
into current law, or provide legal advice.

**Observed local evidence and limit.** `Edilizia_Pack/serialize_edilizia.py`
contains a local `NORME` register with titles, source labels, URLs and some
date/currentness wording, including a January 2026 INL edition, DPR 380 and
D.Lgs 36 entries, and it assigns different licence labels during serialization
(`serialize_edilizia.py:58-77, 175-192`). The raw checkout contains some of the
listed files, while generated `parsed/norme_italiane.jsonl` is absent. G17 and
G18 explicitly require jurisdiction, effective date, source and qualified
human review for current-law/professional claims (`UNI_SKILL_TAXONOMY_G17.json:210-223`;
`UNI_SKILL_DEPENDENCY_GRAPH_G18.json:140-149`). The register is not proof of
current validity on 2026-10-18.

**Prerequisites.** Require jurisdiction and question date; prefer a named
authoritative source; record publication/effective/repeal/amendment dates,
retrieval time, checksum and source hierarchy; keep original text separate
from interpretation; define stale/conflicting-source behavior; and add a
qualified reviewer route for legal, procurement, safety, tax or permit claims.

**Expected evidence.** Query scope; source record and version/effective date;
retrieval timestamp and checksum; quoted passage or page/section anchor where
rights permit; interpretation separated from source; conflict/staleness flag;
answer limitation; reviewer role and decision; and a reproducible no-answer
or escalation result.

**Runtime tests (proposed).** Query with a specified jurisdiction/date and
check that the result carries both; supply an older source and require a
staleness flag; supply conflicting versions and require escalation; remove the
date or source and require `blocked`; test citation/anchor retention; and
verify that the route never files, sends, certifies or presents an unreviewed
answer as authoritative.

**Licensing gate.** The local register labels some content as public acts and
the INL item as CC BY-SA 4.0, but each source, edition, transcription,
translation and derivative still needs rights/attribution verification. A URL
or “atto pubblico” label is not a blanket publication or training clearance.

**Professional review.** Qualified legal reviewer for legal interpretation;
qualified technical/procurement/safety reviewer for the corresponding domain;
and a documented scope decision. A lookup can support a professional; it does
not substitute for the professional.

**Blocked states.** Jurisdiction or effective date missing; source only
secondary or stale; amendment/repeal status unresolved; conflict not
resolved; licence/attribution not recorded; reviewer absent; or output would
be used as legal, permit, procurement, safety, tax or professional advice.

## Proposed G20 sequence

1. **G20-00 — lock the register.** Freeze the six IDs, canonical candidates,
   aliases, states and source boundary in the companion JSON decision log.
2. **G20-01 — establish fixtures and rights.** Select the smallest local
   permissive/synthetic fixtures, record checksums and reject unlicensed or
   research-only material from release paths.
3. **G20-02 — implement runtime probes.** Build isolated probes for CAD/IFC,
   Blender and PDF. Store outputs and failures as evidence packets; no
   professional-use claim follows from probe success.
4. **G20-03 — define controlled records.** Specify the PDF lifecycle and SAL
   reconciliation schemas, with decimal arithmetic, version transitions,
   discrepancy states and human approval fields.
5. **G20-04 — build the law route.** Add jurisdiction/effective-date lookup,
   staleness/conflict behavior and source/licence records. Keep it
   reference-only until review.
6. **G20-05 — evaluate and review.** Run deterministic positive/negative tests,
   inspect provenance and rights, assign qualified reviewers and retain all
   blocked cases.
7. **G20-06 — scoped release decision.** Release only the facet whose source,
   non-redundancy, runtime, rights, risk and professional gates all agree.
   Otherwise keep `blocked` and record the missing evidence.

## Source register used for this roadmap

| ID | Local reference | What it establishes here | What it does not establish |
|---|---|---|---|
| S01 | `docs/coordination/UNI_SKILL_TAXONOMY_G17.json:15-21, 23-53, 330-353` | Canonical ownership, facet/alias rules, evidence states and professional boundary. | Factual, legal, licensing, runtime or professional correctness. |
| S02 | `docs/coordination/UNI_SKILL_DEPENDENCY_GRAPH_G18.json:56-63, 164-184, 200-208, 224-232` | Non-overlap, document/runtime/review families and gates. | Implementation or successful runtime execution. |
| S03 | `docs/coordination/UNI_SKILL_COVERAGE_MATRIX_G19.json:6-23, 25-38, 114-153, 204-214` | G19 reference-library status and explicit absence of the four listed `SKILL.md` paths from this inventory HEAD. | Presence of those skills in this checkout or release readiness. |
| S04 | `CAD_Library/training_corpus/README.md:1-60` and `CAD_Library/training_corpus/manifest.jsonl` | Local CAD corpus structure, parser description and licence classes. | CAD API runtime, geometric truth or professional conformity. |
| S05 | `Edilizia_Pack/raw/bim_ifc/ifc_models/`, local `LICENSE`, `Edilizia_Pack/manifest.json`, `Edilizia_Pack/serialize_edilizia.py:194-221` | Raw IFC samples, MIT notice, manifest/serializer design and intended index fields. | Generated index, complete IFC QA or model/design correctness. |
| S06 | `Edilizia_Pack/extract_pdf_text.py:1-34` | Local resumable `pypdf` extraction script with page markers/checkpoints. | End-to-end lifecycle, extraction fidelity, rights or approval. |
| S07 | `Edilizia_Pack/README.md:110-119, 155-163` | README descriptions of SAL/glossary and a described technical-document/SAL corpus, with a verification warning. | Presence of the described parsed corpus, reconciliation implementation or accounting correctness. |
| S08 | `Edilizia_Pack/serialize_edilizia.py:58-77, 175-192` | Local normative source register and differentiated licence labels. | Current validity, authoritative legal interpretation or professional advice. |

The companion `UNI_SKILL_G20_DECISION_LOG.json` records the same boundary in a
machine-readable form. No corpus, source pack, exam, fixture or generated
artifact is modified by this roadmap.
