# UniCostraction G20/G21/G22/G23/G24 — advanced facets, release coverage and governance

Status: roadmap-only, release=blocked, G24 operational governance observed on
2026-10-19 in the requested codex/uni-inventory worktree. G24 is an
operational-assurance layer over G23; it does not implement, certify or
promote any domain facet.

## G24 - operational governance extension

G24 checks whether the G23 assurance system is aligned to explicit objectives,
preserves evidence integrity, can be reproduced across environments, can
recover from operational disruption and learns through controlled feedback.
These five areas are distinct from the G22 controls and G23 assurance
activities: G24 evaluates their system-level operation without redefining
change control, audit records, incident handling, dependency analysis or
release authority.

The matrix uses cumulative states:

- **existing** means a local contract, register, matrix, gate or prior
  coordination artifact was observed;
- **planned** means the operational packet, exercise, review or decision is
  specified but not evidenced as complete;
- **blocked** means an applicable source, licence, currentness, runtime,
  continuity or professional gate remains open;
- **verified (structural)** means only that the named document field,
  reference, matrix row or deterministic structural check exists. It never
  means factual, technical, legal, licence, runtime, financial or professional
  correctness.

### G24 areas

| G24 area | Operational purpose | Non-redundant boundary | Source gate | Licence gate | Currentness gate | Professional boundary | Runtime gate |
|---|---|---|---|---|---|---|---|
| g24.control_objective_alignment | Map a scoped objective to applicable G22 controls, G23 assurance checks, evidence and release decisions. | Tests control-system alignment; it does not create a new control, metric or domain owner. | Objective, scope, canonical owner, evidence references and exclusions are explicit. | Objective route, inputs, fixtures and outputs have intended-use and derivative-right decisions. | Objective period, jurisdiction, version and review horizon are recorded where material. | Alignment is governance review, not technical, legal, financial, safety or professional approval. | Mapping is replayed against the current route and detects missing or contradictory controls. |
| g24.evidence_integrity_chain | Verify identity, custody, transformation history, checksums and linkage across an evidence packet. | Tests integrity of the evidence chain; it does not replace G22 audit records or establish substantive truth. | Every transformation links input, operation, output, checksum or equivalent integrity marker and observer. | Copying, transformation, storage, log and output rights are recorded; restricted evidence remains restricted. | Observation time, source version, validity horizon and invalidation trigger are preserved. | Integrity is not correctness; the qualified reviewer assesses the content and intended use. | The chain is reconstructed from retained artifacts and fails closed on missing or mismatched links. |
| g24.reproducibility_portability | Re-run scoped controls and evidence checks across pinned environments, versions and permitted operating contexts. | Tests repeatability and portability; it does not replace route-specific runtime tests or professional review. | Fixture, source snapshot, command, environment, expected result and variance policy are recorded. | Environments, dependencies, fixtures and generated outputs are cleared for the repeat route. | Re-run date, tool/version, jurisdiction and stale-source behavior are recorded. | Repeatability does not prove design adequacy, legal validity, financial correctness or conformity. | Positive, negative and controlled-variance runs are reproducible; unexplained variance blocks. |
| g24.continuity_recovery | Exercise continuity, checkpoint restoration and controlled recovery when a source, tool, dependency or reviewer path is unavailable. | Tests operational resilience; it does not replace G22 release rollback, revocation or exception authority. | Recovery target, dependency assumptions, checkpoint evidence and recovery decision are traceable. | Backup, checkpoint, tool, plugin, asset and restored output rights are verified for the recovery route. | Recovery uses the correct source/version and records outage time, validity and revalidation needs. | Recovery is not permission to issue a professional deliverable without the required reviewer. | Failure injection, restore, integrity check and safe-stop behavior are recorded; automatic external action is forbidden. |
| g24.feedback_adaptation | Convert measured results, incidents, reviews and residual unknowns into controlled improvement priorities. | Governs learning from evidence; it does not close incidents, approve changes or alter releases automatically. | Feedback item links to metric, incident, review, source and affected decision with rationale. | Feedback data and derived recommendations respect source, disclosure, training and derivative rights. | Trend window, observation date, effective context and revalidation trigger are explicit. | Improvement priority is not a professional conclusion; qualified owners decide consequential changes. | Feedback replay demonstrates that a recommendation is traceable and cannot silently change runtime behavior. |

### G24 coverage matrix

The matrix is conservative and cumulative. Structural verified marks identify
only that a system-level contract is present in local coordination evidence.
Every G24 area remains blocked until its operational exercise, evidence, gates
and professional boundaries are satisfied.

| Area | Existing | Planned | Blocked | Verified (structural only) | Coverage evidence / missing gate |
|---|---:|---:|---:|---:|---|
| Control-objective alignment | Yes | Yes | Yes | Yes | G22 controls and G23 assurance criteria exist; no complete objective-to-control map with exclusions and contradiction review is evidenced. |
| Evidence-integrity chain | Yes | Yes | Yes | Yes | G21/G22 provenance, checksums and audit concepts exist; no reconstructed end-to-end chain with mismatch/absence failures is evidenced. |
| Reproducibility and portability | Yes | Yes | Yes | No | G23 runtime/evaluation gates exist; no cross-environment rerun packet with explained variance is evidenced. |
| Continuity and recovery | Yes | Yes | Yes | No | G22 refresh/rollback boundary exists; no failure-injection, checkpoint-restore and safe-stop exercise is evidenced. |
| Feedback and adaptation | Yes | Yes | Yes | Yes | G23 metrics, incidents and bounded claims exist structurally; no closed feedback loop with controlled recommendation replay is evidenced. |

### G24 source, licence, currentness, professional and runtime gates

Every G24 packet must satisfy all applicable gates, with a documented
not-applicable rationale when a gate genuinely does not apply:

1. **Source gate.** Link the objective, integrity claim, rerun, recovery or
   feedback item to canonical ownership, source locator, source/interpretation/
   example/hypothesis separation, version or effective date, observation time,
   jurisdiction and exact positive or negative evidence.
2. **Licence gate.** Record rights for source, dataset, fixture, environment,
   tool, plug-in, asset, log, backup, derivative and output as applicable.
   Unknown, incompatible or unreviewed rights keep the route blocked.
3. **Currentness gate.** Record validity horizon, retrieval/observation time,
   amendment/repeal or version context, stale-data behavior, invalidation and
   revalidation triggers.
4. **Professional-boundary gate.** Identify the qualified role, exact
   evidence version, reviewed scope, limitations, decision and date.
   Operational resilience or repeatability never becomes professional
   correctness or sign-off.
5. **Runtime gate.** Retain reproducible positive, negative, variance,
   failure-injection, recovery and feedback-replay results where applicable.
   Static presence, a hash or a passing parser is not runtime proof.

### G24 reversible-release criteria

Release remains blocked unless every applicable criterion passes for the
scoped route. A missing, stale, conflicting or unknown item is a blocker:

1. Objective, route, canonical owner, G22 controls and G23 assurance scope
   are frozen and non-contradictory.
2. Evidence identity and transformation chain reconstruct without unexplained
   gaps, mismatches or unowned artifacts.
3. Source, licence and derivative-right decisions cover the full release,
   recovery and replay route.
4. Currentness, jurisdiction, validity horizon and revalidation triggers are
   explicit for material claims and dependencies.
5. Runtime replay covers positive, negative and controlled-variance cases;
   unexplained variance or non-reproducible behavior blocks release.
6. Continuity and recovery exercise the declared checkpoint, restore,
   integrity check, safe-stop and human escalation path.
7. Feedback, incident and measurement signals are traceable, bounded and
   cannot silently modify the released route.
8. Qualified, role-specific professional review covers the exact evidence
   version, limitations, residual unknowns and intended use.
9. Release is scoped, reversible, monitored and revocable under G22/G23
   controls, and authorizes no automatic filing, sending, payment,
   publication, certification, signing, execution or professional approval.

### G24 stop conditions and sequence

G24 remains blocked when objective alignment is incomplete, evidence-chain
integrity cannot be reconstructed, reruns diverge without explanation,
continuity recovery is untested, feedback is untraceable, any source/licence/
currentness/runtime/professional gate is open, or a bounded result would be
mistaken for technical correctness. Structural verification may remain
alongside blocked because it records contract presence, not operation.

1. **G24-00 - freeze operational scope.** Keep the six G20 facets, seven G21
   areas, five G22 areas and five G23 areas; add only the five G24 areas.
2. **G24-01 - map and preserve.** Establish objective-to-control maps and
   reconstruct evidence identity and transformation chains.
3. **G24-02 - replay and recover.** Run cross-environment variance cases and
   failure-injection/checkpoint-recovery exercises where applicable.
4. **G24-03 - review feedback.** Trace metrics, incidents and residual
   unknowns into bounded recommendations with role-specific review.
5. **G24-04 - reversible decision.** Release only when all applicable
   criteria agree and a tested recovery/revocation path remains available.

No G24 area authorizes automatic publication, filing, payment, sending,
certification, signing or execution. No G24 status declares technical
correctness or promotes a reference-only source to verified knowledge.

## G23 - assurance governance extension

G23 checks whether the G22 governance controls are defined, exercised,
measured, incident-aware, dependency-aware and bounded in their attestations.
It is not a sixth governance family and does not create new CAD, IFC, Blender,
PDF, SAL or current-law skills. The five areas below test or constrain G22;
they do not repeat its change-control, evidence-ledger, exception, role or
release/rollback responsibilities.

The matrix uses cumulative states:

- **existing** means a local contract, register, matrix, gate or prior
  coordination artifact was observed;
- **planned** means the assurance packet, metric, exercise, review or decision
  is specified but not evidenced as complete;
- **blocked** means an applicable source, licence, currentness, runtime,
  incident, dependency or professional gate remains open;
- **verified (structural)** means only that the named document field,
  reference, matrix row or deterministic structural check exists. It never
  means factual, technical, legal, licence, runtime, financial or professional
  correctness.

### G23 areas

| G23 area | Assurance purpose | Non-redundant boundary | Source gate | Licence gate | Currentness gate | Professional boundary |
|---|---|---|---|---|---|---|
| g23.control_effectiveness | Test whether each applicable G22 control is designed, exercised and produces retained evidence. | Evaluates control operation; it does not redefine G22 controls or prove the underlying facet correct. | Test claims link to the exact control, source packet, fixture, result and negative case. | Test fixtures, tools, outputs and derivatives have recorded rights for the assurance route. | Test date, tool/version, jurisdiction and refresh trigger are recorded where material. | A passed control test is not engineering, legal, financial, safety or professional acceptance. |
| g23.coverage_measurement | Define denominators, indicators, trend windows and evidence quality signals for scoped coverage. | Measures coverage and evidence health; it does not replace the audit ledger or turn a percentage into correctness. | Metric definition, population, exclusions, source IDs and observation window are explicit. | Inputs and derived reports respect source, dataset, fixture and output rights. | Window, retrieval date, effective period and stale-data behavior are explicit. | Metrics are decision support only; qualified reviewers interpret consequential results. |
| g23.incident_nonconformance | Record deviations, failed gates, recurrence, corrective action and closure evidence. | Handles observed nonconformance and remediation; it does not waive or approve G22 exceptions. | Incident record preserves trigger, evidence, impact, containment, corrective action and verification. | Incident artifacts, logs, fixtures and derivatives retain their use and disclosure decisions. | Incident time, affected version, jurisdiction and active/revoked status are retained. | Material technical, legal, financial, safety or professional incidents escalate to the appropriate role. |
| g23.dependency_impact | Trace how source, tool, licence, version, skill-owner or role changes propagate across scoped routes. | Performs impact analysis over dependencies; it does not replace G22 change control or ownership review. | Dependency edge, affected artifact, evidence snapshot and impact decision are traceable. | Upstream and downstream source, tool, plug-in and derivative rights are rechecked after impact. | Version, effective date, jurisdiction and end-of-support or refresh signals are recorded. | Subject-matter owners review consequential impacts; graph presence is not design or compliance approval. |
| g23.bounded_attestation | Record what a scoped evidence packet supports, what remains unknown and who accepted that bounded statement. | Binds a claim to evidence and limitations; it does not create certification, professional sign-off or global readiness. | Attestation cites the exact evidence snapshot, source status, limitations and residual unknowns. | Attestation route and any publication/training/use disposition have explicit rights decisions. | Attestation carries observation date, validity horizon, jurisdiction and revalidation trigger. | Acceptance is role- and scope-bound; it cannot certify, file, send, pay, sign, publish, execute or replace professional approval. |

### G23 coverage matrix

The matrix is conservative and cumulative. Structural verified marks identify
only that a control or contract is present in local coordination evidence.
Every G23 area remains blocked until the relevant assurance exercise, evidence,
gates and professional boundaries are satisfied.

| Area | Existing | Planned | Blocked | Verified (structural only) | Coverage evidence / missing gate |
|---|---:|---:|---:|---:|---|
| Control effectiveness | Yes | Yes | Yes | No | G22 defines controls and stop conditions; no complete executed-control sample, retained failure or effectiveness conclusion is evidenced. |
| Coverage measurement | Yes | Yes | Yes | Yes | G21/G22 matrices and state definitions exist structurally; no approved denominator, metric run, trend baseline or quality interpretation is evidenced. |
| Incident and nonconformance | Yes | Yes | Yes | No | Blocked states and exception controls exist; no incident register, corrective-action evidence or recurrence check is evidenced. |
| Dependency impact | Yes | Yes | Yes | Yes | G18 dependency/gate concepts and G22 change-control boundaries exist; no completed propagation exercise across a scoped route is evidenced. |
| Bounded attestation | Yes | Yes | Yes | Yes | G22 release criteria and professional boundaries exist; no evidence-linked attestation with residual unknowns and acceptance record is evidenced. |

### G23 source, licence, currentness and professional gates

Each assurance packet must contain all applicable gates, with a justified
not-applicable decision where a gate truly does not apply:

1. **Source gate.** Link the assurance claim to canonical ownership, source
   locator, source/interpretation/example/hypothesis separation, version or
   effective date, observation window, jurisdiction where material and the
   exact positive or negative evidence.
2. **Licence gate.** Record rights for source, dataset, fixture, tool,
   plug-in, font, block, derivative, log and output as applicable. Unknown,
   incompatible or unreviewed rights keep the route blocked.
3. **Currentness gate.** Record retrieval/observation time, validity horizon,
   amendment/repeal or version context, stale-data behavior and revalidation
   trigger for time-sensitive evidence.
4. **Professional-boundary gate.** Identify the qualified role, reviewed
   scope, exact evidence version, limitations, decision and date. Assurance
   metrics and control results do not become technical, legal, financial,
   safety or professional correctness.
5. **Operational evidence gate.** Retain reproducible control tests, metric
   inputs, incident/dependency records, failures and bounded acceptance. A
   static field or passing parser is not operational proof.

### G23 release criteria

Release remains blocked unless every applicable criterion passes for the
scoped route. A missing, stale, conflicting or unknown item is a blocker:

1. The route, canonical owner, G22 controls and G23 assurance scope are fixed.
2. Each applicable G22 control has an exercised positive or negative result
   with reproducible inputs, environment and retained output.
3. Coverage metrics identify population, denominator, exclusions, time window,
   source evidence and interpretation limits.
4. Incidents and nonconformances have containment, owner, corrective action,
   verification, recurrence status and escalation where required.
5. Dependency impact is assessed for changed sources, tools, licences,
   versions, owners, roles and currentness conditions.
6. Source, licence, currentness and professional-boundary gates are explicit
   and independently reviewable.
7. Residual unknowns and risks are visible; no metric or control result
   silently converts blocked evidence into a pass.
8. A bounded attestation identifies evidence snapshot, scope, limitations,
   validity horizon, reviewer and acceptance decision.
9. Release is scoped, reversible and monitored under G22 refresh/rollback
   controls, and authorizes no automatic filing, sending, payment,
   publication, certification, signing, execution or professional approval.

### G23 stop conditions and sequence

G23 remains blocked when assurance tests are absent or non-reproducible, a
metric denominator is undefined, an incident is unresolved, dependency impact
is unknown, source/licence/currentness evidence is stale or incomplete, or a
bounded statement would be mistaken for professional correctness. Structural
verification may remain alongside blocked because it records control presence,
not operational effectiveness.

1. **G23-00 - freeze assurance scope.** Keep the six G20 facets, seven G21
   areas and five G22 areas; add only the five G23 assurance areas.
2. **G23-01 - define measurement.** Fix control tests, metric denominators,
   evidence quality indicators and route-specific observation windows.
3. **G23-02 - exercise and record.** Retain positive/negative tests, one
   incident or nonconformance path and one dependency-impact exercise where
   applicable.
4. **G23-03 - review bounded claims.** Recheck source, rights, currentness,
   professional scope and residual unknowns with role-specific reviewers.
5. **G23-04 - scoped decision.** Release only when all applicable criteria
   agree; otherwise retain blocked and report the missing gate.

No G23 area authorizes automatic publication, filing, payment, sending,
certification, signing or execution. No G23 status declares technical
correctness or promotes a reference-only source to verified knowledge.

## G22 - governance extension

G22 governs how G21 decisions are changed, evidenced, escalated, approved,
refreshed and withdrawn. The five areas below are deliberately cross-cutting:
they do not create new CAD, IFC, Blender, PDF, SAL or current-law skills and
they do not replace their domain or professional owners.

The matrix uses cumulative states:

- **existing** means a local contract, register, gate or prior coordination
  artifact was observed;
- **planned** means the governance packet, control, probe or decision record is
  specified but not evidenced as complete;
- **blocked** means an applicable source, licence, currentness, runtime,
  exception or professional gate remains open;
- **verified (structural)** means only that the named document field,
  reference, matrix row or deterministic structural check exists. It never
  means factual, technical, legal, licence, runtime, financial or professional
  correctness.

### G22 areas

| G22 area | Governance purpose | Non-redundant boundary | Source gate | Licence gate | Currentness gate | Professional boundary |
|---|---|---|---|---|---|---|
| g22.change_control | Version every scope, mapping, gate and release decision; retain impact and rollback references. | Controls change to G21 records; it does not duplicate facet ownership or silently merge/delete content. | Change request links to the affected source, interpretation, evidence and decision IDs. | A changed source, asset, derivative or tool triggers a fresh rights decision; old clearance is not inherited automatically. | Material changes record observation date, effective date, jurisdiction and refresh consequence. | Change approval is not domain/professional sign-off; role and scope remain explicit. |
| g22.evidence_audit_ledger | Make evidence packets, observations, failures, decisions and reviewers traceable and reproducible. | Provides audit traceability; it does not turn a manifest, hash or log into substantive correctness. | Source/interpretation/example/hypothesis separation, locator, version or date, checksum where applicable, and observed-by record. | Asset, fixture, output and derivative rights are recorded per evidence item, including unknown or restricted states. | Time-sensitive evidence carries retrieval/observation time, validity context and stale/refresh status. | Audit completeness does not authorize a professional conclusion; the qualified reviewer must assess the content. |
| g22.risk_exception_escalation | Classify risks and exceptions, assign an owner, compensating control, expiry and escalation path. | Governs unresolved risk; it does not waive a domain, legal, licence or safety requirement. | Exception rationale points to the exact missing or conflicting evidence and preserves the negative case. | No exception can bypass unknown, incompatible or unapproved rights for publication/training/use. | Expired or stale evidence escalates; no silent carry-forward across law, tool or jurisdiction changes. | High-risk exceptions require the appropriate qualified reviewer; a coordinator cannot self-approve. |
| g22.roles_separation | Separate source, rights, currentness, runtime, domain and release decisions and record accountable roles. | Defines responsibility and segregation; it does not perform CAD, BIM, legal, financial or safety review. | Each role is linked to the exact evidence packet and decision version it reviewed. | Rights reviewer authority is distinct from domain/professional review and cannot be inferred from a technical check. | Current-law or time-sensitive interpretations require the competent jurisdiction/domain reviewer. | No self-review for material release; sign-off is scoped, named, dated and version-linked. |
| g22.release_refresh_rollback | Define release, refresh, revocation, rollback and post-release monitoring for a scoped route. | Governs lifecycle disposition; it does not imply global completeness or automatic external execution. | Release record enumerates passed gates, open blockers, evidence snapshot and rollback target. | Release is blocked while an applicable source, asset, derivative or tool rights decision is unresolved. | Refresh/sunset/revocation triggers are explicit; currentness is rechecked before continued use. | Release cannot certify, file, send, pay, sign, publish, execute or replace professional approval. |

### G22 coverage matrix

The matrix is conservative and cumulative. A structural verified mark records
only the presence of a governance control in local coordination documents.
Every G22 area remains blocked until its operational evidence and applicable
professional review exist.

| Area | Existing | Planned | Blocked | Verified (structural only) | Coverage evidence / missing gate |
|---|---:|---:|---:|---:|---|
| Change control | Yes | Yes | Yes | Yes | G17/G18/G21 provide versioned taxonomy, gates and release coverage; a complete change-request ledger, impact record and rollback exercise are not evidenced. |
| Evidence and audit ledger | Yes | Yes | Yes | Yes | Source register, source-separation rule and evidence lifecycle gates exist; reproducible per-artifact audit packets and retained observations are not complete. |
| Risk and exception escalation | Yes | Yes | Yes | No | Blocked states and professional boundaries exist; risk classes, exception approvals, expiries, compensating controls and escalation records are not evidenced. |
| Roles and separation of responsibilities | Yes | Yes | Yes | Yes | G18/G21 role-specific professional boundaries exist; named, qualified, conflict-checked and version-linked approvals are not evidenced. |
| Release, refresh and rollback | Yes | Yes | Yes | No | G21 release remains blocked and source/currentness gates exist; a tested refresh/revocation/rollback packet and post-release monitoring are not evidenced. |

### G22 source, licence, currentness and professional gates

For every proposed release or refresh, the packet must contain all of the
following, with not-applicable decisions justified rather than omitted:

1. **Source gate.** Identify the canonical owner, source locator, source
   category, interpretation/example/hypothesis separation, version or
   effective date, observation/retrieval date, jurisdiction where material and
   the exact evidence or negative case supporting the decision.
2. **Licence gate.** Record rights for source, fixture, tool, plug-in, font,
   block, derivative and output as applicable. Unknown, incompatible or
   unreviewed rights keep the route blocked; a URL, manifest label or local
   notice is not blanket clearance.
3. **Currentness gate.** For law and other time-sensitive material, record
   territory, effective period, retrieval time, amendment/repeal/conflict
   behavior and refresh/sunset trigger. If currentness is not material, record
   why.
4. **Professional-boundary gate.** Name the role qualified to review the
   relevant content, exact version and scope, limitations, decision and date.
   Technical, legal, financial, safety, document and visual reviews remain
   distinct; structural verification never substitutes for sign-off.
5. **Runtime and audit gate.** Where a route is executable, retain pinned
   environment, deterministic input/output, negative cases, failure
   reproduction and an auditable decision record. Static presence is not
   runtime proof.

### G22 release criteria

Release remains blocked unless all applicable criteria pass for the scoped
route; a failed or unknown criterion is an explicit blocker, not an inferred
pass:

1. Scope, canonical ownership and non-redundancy mapping are frozen.
2. The source/evidence packet is complete and traceable to exact local
   records, versions or dates.
3. Licence and derivative-right decisions are explicit for every material
   source, asset, fixture, tool and output.
4. Currentness, jurisdiction and refresh behavior are recorded wherever
   claims can change over time or territory.
5. Runtime/evaluation evidence and negative cases exist wherever the route is
   executable or produces a consequential artifact.
6. Risk and exceptions have an accountable owner, rationale, compensating
   control, expiry and escalation; no exception bypasses rights or
   professional boundaries.
7. Required professional review is independent, qualified, scoped,
   version-linked and dated.
8. The release record names passed gates, remaining limitations, refresh
   triggers and tested rollback/revocation target.
9. The release is scoped and reversible; it authorizes no automatic filing,
   sending, payment, publication, certification, signing, execution or
   professional approval.

### G22 stop conditions and sequence

G22 remains blocked when any source, licence, currentness, evidence, runtime,
exception, role-separation, rollback or qualified-review gate is missing,
unknown, stale, conflicting or expired. A structural verified mark may remain
alongside blocked because it records control presence, not readiness.

1. **G22-00 - freeze governance scope.** Keep the six G20 facets and seven
   G21 areas; add only the five G22 governance areas.
2. **G22-01 - establish traceability.** Assign stable change, evidence, risk,
   role and release record identifiers and link them to the scoped route.
3. **G22-02 - exercise controls.** Reproduce at least one change, one negative
   evidence case, one escalation and one rollback/refresh case per applicable
   route.
4. **G22-03 - independent review.** Recheck source, rights, currentness and
   professional boundaries with role-specific reviewers.
5. **G22-04 - scoped decision.** Release only when every applicable criterion
   agrees; otherwise retain blocked and report the missing gate.

No G22 area authorizes automatic publication, filing, payment, sending,
certification, signing or execution. No G22 status promotes a reference-only
source to verified knowledge.

## G21 - release and coverage extension

G21 is a release-control layer, not a new domain curriculum. It consumes the
six G20 facets and makes their readiness evidence visible. A G21 area may have
more than one mark in the matrix because the states are cumulative:

- **existing** means a local contract, source register, boundary or prior
  coordination artifact exists;
- **planned** means the required packet, probe, review or decision is specified
  but is not established as complete;
- **blocked** means at least one release or professional-use gate is open;
- **verified (structural)** means only that the named local artifact, field,
  path or deterministic document check was observed. It never means factual,
  technical, legal, licence, runtime, financial or professional correctness.

### New G21 areas

| G21 area | Purpose over G20 | Canonical/non-redundant boundary | Source gate | Licence gate | Professional boundary |
|---|---|---|---|---|---|
| g21.nonredundancy_mapping | Resolve each facet to one canonical owner and record aliases/review decisions. | Does not create a seventh domain skill or merge/delete similar content automatically. | G17/G18 IDs, owner, source purpose and human semantic decision. | Record rights when mapping crosses source packs or derivatives. | Human curator reviews intent, provenance and semantic equivalence; similarity is not approval. |
| g21.provenance_context | Attach source, interpretation, example, hypothesis, version/effective date, jurisdiction/period and lifecycle. | Does not replace the technical/legal subject owner. | Complete per-artifact source packet and reproducible observation date. | Source and derivative terms/attribution recorded before training or publication. | Reviewer confirms scope and limitations; source presence is not authority. |
| g21.licence_rights | Decide permitted use, attribution, derivative, publication and training route. | Does not treat a manifest label or URL as blanket clearance. | Source identity, snapshot/checksum and provenance resolve first. | Unknown or incompatible terms keep the route blocked; decision is per source/asset. | Rights reviewer decides publication/training disposition; domain review remains separate. |
| g21.runtime_interoperability | Require target-environment probes, deterministic outputs and retained failures for applicable G20 routes. | Tests workflow behavior; does not duplicate CAD, BIM, document, finance or legal content. | Fixture, tool/version, command, output and failure reproduction recorded. | Fixtures, tools, plugins and outputs have compatible terms. | Runtime success does not prove design adequacy, legal validity or professional conformity. |
| g21.professional_review | Assign the qualified reviewer and record scope, limitations, decision and date. | Defines a stop boundary; it does not perform engineering, legal, accounting or safety practice. | Review packet links to exact version and evidence. | Reviewer may not clear rights outside authority; rights gate remains separate. | CAD/BIM/visual, document, financial/SAL and legal reviewers are role-specific; no sign-off is inferred. |
| g21.currentness_jurisdiction | Make current-law and time-sensitive claims carry territory, effective date, retrieval time, freshness and conflict behavior. | Routes to existing PA/legal skills; does not create a second legal corpus or advice skill. | Prefer authoritative source; preserve amendment/repeal and conflict evidence. | Edition, transcription, translation and derivative permissions are checked separately. | Qualified legal or domain professional reviews interpretation; missing context stops the route. |
| g21.release_evaluation | Aggregate structural, provenance, semantic, runtime, rights and professional decisions for a scoped release. | Releases a scoped route only; it does not imply global completeness. | All upstream evidence IDs and open blockers visible. | No release while an applicable rights decision is unresolved. | Release records qualified review and forbids automatic filing, sending, payment, certification or execution. |

### G21 coverage matrix

The matrix is deliberately conservative. Verified is structural only; an empty
cell means that state is not evidenced for the area. The matrix itself is a
coordination artifact, not a claim that the underlying content is ready.

| Area | Existing | Planned | Blocked | Verified (structural only) | Coverage evidence / missing gate |
|---|---:|---:|---:|---:|---|
| Canonical non-redundancy and mapping | Yes | Yes | Yes | Yes | G17/G18 contracts and G20 owner candidates exist; per-facet semantic decisions and alias review remain open. |
| Provenance and context | Yes | Yes | Yes | Yes | G20 source register and source-separation rules exist; per-artifact version/effective context and reviewer packets are not complete. |
| Licence and rights | Yes | Yes | Yes | No | Local manifests/notices and G20 licence gates exist; no blanket clearance or complete per-source publication/training decisions are evidenced. |
| Runtime and interoperability | Yes | Yes | Yes | No | G18 runtime gate and G20 proposed probes exist; no G21 deterministic evidence packet proves all six workflows. |
| Professional review | Yes | Yes | Yes | No | Professional-boundary text exists; no qualified G21 sign-off is inferred from documentation or static checks. |
| Currentness and jurisdiction | Yes | Yes | Yes | No | G17/G18 vocabulary and local normative register exist; current validity, conflict resolution and legal review remain open. |
| Scoped release evaluation | Yes | Yes | Yes | Yes | G20 decision log and this G21 matrix exist structurally; release is blocked while upstream gates remain open. |

### G21 stop conditions

G21 remains blocked for a facet when any applicable source packet, licence
decision, runtime result, semantic mapping, currentness field or qualified
review is missing. A structural verified mark may be retained alongside
blocked; it records that the control exists, not that the facet passes.

No G21 area authorizes automatic publication, filing, payment, sending,
certification, signing or execution. No G21 status promotes a reference-only
source to verified knowledge.

### G21 sequence

1. **G21-00 - freeze scope.** Keep the six G20 facet IDs and add only the seven
   cross-cutting G21 areas above; do not add duplicate domain IDs.
2. **G21-01 - make coverage explicit.** Maintain the matrix and attach every
   existing, planned, blocked or structural verified mark to a source or
   decision record.
3. **G21-02 - close evidence packets.** Build per-facet provenance, rights,
   runtime and reviewer packets; preserve negative and unresolved cases.
4. **G21-03 - review currentness and risk.** Apply jurisdiction/effective-date
   checks to law and professional claims, and domain-specific review to
   technical, financial, safety and visual outputs.
5. **G21-04 - scoped decision.** Release only a facet whose applicable gates
   agree. Keep all other facets explicitly blocked and report the missing gate.

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
