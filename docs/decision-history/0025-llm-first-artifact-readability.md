# ADR-0025: LLM-First Artifact Readability

> **Summary.** The cycle's artifacts — skills, rules, distilled knowledge, tests, decision records — are read, edited, and reviewed by the next session's LLM, not by a human, and the operator's harness has been shaping itself around that fact without ever stating it: machine gates are selected on LLM-first axes (bug class caught, canonical formatting for diff stability, edit-reliability budgets, explicit type enforcement at boundaries, deliberately not human-aesthetic style linters), a frozen golden-output layer guards machine-parsed output against silent drift, and README investment is justified precisely because the README is the one surface a human reads. ADR-0025 names the reader explicitly: the default reader, editor, and reviewer of cycle artifacts is the next session's LLM. Optimizing for that reader is the quality bar itself — a change of audience, not a lowering of it — and what is preserved for that reader is verifiability (types, tests, frozen goldens, stated invariants), not readability, which is derivable on demand. The human-readability budget is spent only on the README and the surface text of outputs; everywhere else, density and self-containment for the LLM reader outrank fine prose, and the enforcer of the standard is the machine gate, not the human eye.

## Status

accepted

## Date

2026-09-01

## Context

The cycle produces and maintains artifacts across its layers — skills, rules, distilled knowledge (ADR-0003's Layer 2 and Layer 3), tests, and decision records. These artifacts are not written once and left alone: they are read back, edited, and reviewed in every later session that touches the harness. That is the reader the cycle actually has, and on 2026-08-31 the operator confirmed it directly: humans read only the README and the surface text of outputs. Everything else in the artifact set is consumed by the next session's LLM.

This was already true in practice before it was stated. The practices running in the operator's harness assume an LLM reader without saying so (these are descriptions of that harness's practice, not artifacts this repository ships or reproduces). Machine gates for the artifact set are selected on axes that make sense for a machine-and-LLM pipeline, not for a human proofreader: which bug class the gate catches, whether its output is canonical (diff-stable) rather than merely acceptable, whether it protects edit reliability against a fixed budget, and whether it enforces explicit types at module boundaries. Human-aesthetic style linters are deliberately absent from that selection — they optimize for a reader the pipeline does not have. Separately, a frozen golden-output layer exists specifically to guard machine-parsed output against silent drift; the concern that layer answers is not "would a human find this ugly" but "would a downstream parser silently misread this." And README investment is treated as justified in a way no other artifact's prose investment is, precisely because the README is the one artifact whose readership is actually human.

ADR-0008 already drew a boundary that this context sits next to: code owns determinism, auditability, and control flow, and LLMs own meaning, with structural checking assigned to code and semantic judgment assigned to the LLM. That split answers *who checks what*. It does not answer *who reads what* — ADR-0008 is silent on whether the artifacts code and LLM operate on are themselves written for a human or an LLM consumer. The gap is exactly where the harness's already-running practices (gate selection, golden freezing, README-only prose investment) had been operating on an unstated assumption.

Left unstated, the assumption produces two costs. First, artifacts that are polished for a reader who is not reading them: prose smoothing, discursive explanation, and stylistic variation spent on files whose actual reader would rather have a self-contained, densely typed unit that fits in its context window. Second, a standard with no explicit enforcer: without naming the reader, there is no principled way to decide whether an artifact that "reads well" to a human but fails a machine gate is acceptable, or whether an artifact that reads poorly to a human but passes every gate is a problem. ADR-0025 closes that gap by naming the reader the harness has already been building for.

## Decision

AKC adopts LLM-first artifact readability as an explicit standard for the cycle's artifacts.

1. **Name the reader.** The default reader, editor, and reviewer of cycle artifacts — skills, rules, distilled knowledge, tests, decision records — is the next session's LLM. Optimizing for this reader is the quality bar itself, not a lowering of it: the change is a change of audience, and the LLM reader is often less forgiving than a human one. Ambiguous, clever, or bloated artifacts come back as bounced edits in the next session, not as a shrug. What LLM readability consists of: locality (self-contained units that fit in context) over deep abstraction; explicitness over cleverness; types and invariant comments as beacons. The measuring stick is context economy, not human cognitive load.

2. **Preserve verifiability, not readability.** Explanations are derivable — an LLM reader can regenerate an explanation of an artifact on demand, so prose readability is not the layer worth protecting. What cannot be regenerated on demand is the preservation layer: types, tests, frozen goldens, and stated invariants. That layer is what gets saved; readable prose around it is not.

3. **The machine gate enforces the standard, not the human eye.** An artifact that fails its gate is unacceptable even if no human ever reads it. The gate, not a reviewer's aesthetic judgment, is the arbiter of whether an artifact meets the LLM-first bar. Scope: AKC records the standard — who the reader is and what that implies — as mechanism; the gates themselves are per-harness instruments, and AKC ships none for its own artifacts. As with the cycle's other instrument gaps (ADR-0022's held-out construction, ADR-0023's conflict-cost metric), naming the enforcer is not shipping it.

4. **The human-readability budget has one line item.** Human-facing prose investment is spent on the README and the surface text of outputs, and nowhere else. Decision records, tests, and commit messages are written for the LLM reader: density and self-containment outrank fine prose in all of them.

## Review-when

If explanation-regeneration proves unreliable — two dated instances within one substrate generation of a derived explanation contradicting the artifact's own preserved layer (a type, a test, a frozen golden, or a stated invariant) — the boundary of the preservation layer must be redrawn. If human co-editing of cycle artifacts returns as a primary mode (for instance, team-scale operation), the reader assumption breaks and the budget allocation with it.

## Alternatives Considered

### (a) Keep optimizing all artifacts for human readability

Rejected. This spends the scarce resource ADR-0010 names — human attention and judgment — polishing surfaces for a reader who, per the 2026-08-31 confirmation, does not read them. Prose investment on artifacts nobody reads is spent, not saved.

### (b) Treat readability as reader-neutral ("good writing is good for both")

Rejected. The two readers rank the same properties in opposite directions — locality versus deep abstraction, explicit repetition versus DRY indirection — and treating them as coincident hides exactly the trade-off this ADR exists to record. A standard that claims to serve both readers at once will, in practice, default to whichever reader the writer has in mind, silently.

### (c) Drop human-facing investment entirely

Rejected. The README and the surface text of outputs are where the human decides whether to trust and adopt anything the cycle produced. ADR-0020 establishes the README as the single human-facing front door and caps what it may hold; ADR-0025 confines the human budget to that capped surface — it neither removes the surface nor licenses expanding it.

## Consequences

### Positive

- Artifact quality becomes checkable by gates rather than arguable by taste — a concrete extension of the enforcement stance ADR-0008 already assigns to code.
- Context economy becomes an explicit, discussable metric for artifacts, instead of an unnamed byproduct of "keeping things short."
- The readability budget stops being spent twice on the same artifact: prose polish and machine-gate compliance are no longer competing, unstated claims on the same file.

### Negative

- The reader claim rests on a single-operator confirmation dated 2026-08-31; it has not been tested against a second operator or a team-scale harness.
- Artifacts optimized for LLM locality can be genuinely hostile to human onboarding beyond the README — a new human reader who opens a rule or a decision record directly, rather than starting from the README, meets prose that was not written for them.
- The preservation layer decays silently if the golden and test layers that carry it are not maintained; naming the layer does not by itself keep it maintained.
- The standard is expensive to reverse: once a corpus of decision records, tests, and rules has been written LLM-first, restoring human-readable prose across it — should the Review-when conditions fire — is a rewrite, not a toggle.

### Neutral

- ADR-0008's executor split is unchanged: ADR-0008 assigns who checks (code vs. LLM), and this ADR names who reads (the next session's LLM). The two are adjacent, not overlapping.
- The six-phase cycle structure is untouched. This is a standard for how artifacts within the existing phases are written, not a new phase or a change to phase order.

## Relationship to other ADRs

- **ADR-0008 (Code and LLM Collaboration)** — adjacent, not overlapping. ADR-0008 splits structural checking from semantic judgment; ADR-0025 names the audience of the artifacts both operate on. ADR-0008 answers who checks; ADR-0025 answers who reads.
- **ADR-0010 (Human Cognitive Resource as Central Constraint)** — the readability budget this ADR restricts to the README and output surface text is a direct allocation of the scarce resource ADR-0010 centers the whole cycle on. Spending that budget on artifacts an LLM reads is the waste ADR-0010 already warns against.
- **ADR-0020 (Minimal-floor README)** — the README is the single line item of the human-facing budget this ADR names. ADR-0020's minimal-floor discipline for that one surface is unchanged and unextended by this ADR.
- **ADR-0003 (Three-Layer Distillation)** — the distillation layers' artifacts are written for this reader: the next session is the consumer of Layer 2 and Layer 3's distilled knowledge.
