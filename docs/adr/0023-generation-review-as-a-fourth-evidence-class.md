# ADR-0023: Generation Review as a Fourth Retirement Evidence Class

> **Summary.** ADR-0022 named three retirement evidence classes — silence (telemetry shows the artifact unused), ablation (necessary), transfer (the completion certificate). All three answer a question of the form *is this rule still doing work?*, and all three treat usage as the thing to be explained away: silence retires what never fires, ablation and transfer retire what fires but is no longer needed. None of them can see the failure mode where **a rule fires on every session and the firing itself is the cost** — an over-constraint written for a weaker model generation, whose premise has expired while its instruction still has to be read and reconciled against the model's own judgment. On such a rule the silence check reports full usage right up to the point where full usage is the problem, and ablation-on-the-home-distribution reports a difference (the rule *is* changing behavior — for the worse). ADR-0023 records the falsifiable claim — *the three existing evidence classes are structurally blind to negative information differential* — and names a fourth class, **generation review**: an audit scheduled by the model release cadence rather than by the usage log, admitting the vendor's own prompt-engineering guidance as evidence. It is the sibling of ADR-0022 in the same way ADR-0022 is the sibling of ADR-0016: ADR-0016 specifies which surface a Measure instrument observes, ADR-0022 which distribution it tests against, ADR-0023 what schedules it and what it is blind to.

## Status

**accepted** — the structural argument is deductive given how the telemetry layer works (an always-loaded rule cannot produce a silence signal), and there is one own-cycle observation (2026-07-25, recorded in `docs/scaffold-dissolution.md`). The honest limitation is stated in the Decision: the *harm* — reasoning spent reconciling conflicting instructions — was reported by the vendor for its own evaluations, not measured in this cycle. This ADR therefore asserts blindness, which is structural, and does not assert a locally-measured effect size.

## Date

2026-07-25

## Context

The dissolution norm has grown its instruments in order. The 2026-07-09 retirement was the first decided by an instrument rather than by narrative impression: a deterministic usage-telemetry layer fed Curate's silence check, one month of logs showed zero organic activations for a design-pattern skill, and the skill was retired the same day. ADR-0022 then sharpened the completion criterion from one test to two — same-context ablation indistinguishability is *necessary*, held-out transfer is the *completion* evidence — and named the three evidence classes retirement decisions must declare: silence, ablation, transfer.

The three classes share a premise that had not been examined: that a rule's problem shows up as an *absence*. Silence detects absence of use. Ablation detects absence of effect. Transfer detects absence of portability. All three were built against the mechanisms the norm document knew about at the time — user-side internalization, AI-side accumulation, platform-side absorption — and in all three of those mechanisms the scaffold ends up *redundant*: it adds nothing, so its retirement is free and its signature is an absence.

The 2026-07-25 observation broke that premise. Anthropic reported that Claude Code's own system prompt had been cut by more than 80% for the Claude 5 generation with no measurable loss on its coding evaluations, and named the mechanism: guardrails written to prevent a weaker model's worst cases now arrive as *conflicting instructions* the stronger model must spend reasoning to resolve. Applying the same audit to the operator's harness found the same shape — an absolute prohibition that is simply wrong in a large class of cases, a nine-step decision matrix front-loaded into sessions that write no code, two sections of one file each declaring itself canonical, and six language-specific rule files resident in sessions containing none of that language. The rules layer fell from 43,971 to 19,240 characters with nothing discarded that had a home.

Every one of those rules was firing. The prohibition fired on every code edit; the decision matrix loaded in every session; the language rules were injected unconditionally — verified in a session containing no Python at all. On the silence check, this is a maximally healthy rules layer. The instrument was working correctly and reporting the opposite of the truth, because the question it asks — *is this used?* — is the wrong question for this failure mode.

This is what the negative pole of the information-differential law names (added to `docs/scaffold-dissolution.md` in the same change): a zero-differential artifact merely wastes context and can wait for the next stocktake; a negative-differential one degrades the behavior it was written to protect, and the longer it stays the more it looks like a working rule — because it keeps firing.

## Decision

1. **Name a fourth retirement evidence class: generation review.** A retirement may declare its evidence as *generation review* — the substrate's model generation changed, and the rule was written against the previous generation's failure modes. Its declaration carries the generation boundary crossed and the specific over-constraint pattern found (blanket prohibition, exhaustive procedure, repeated emphasis, enumerated examples, front-loaded decision table). Retirement decisions continue to name their evidence class, now from four: silence, ablation, transfer, generation review.

2. **Record the falsifiable claim.** *Silence, ablation, and transfer are structurally blind to negative information differential.* Silence cannot fire for an always-loaded rule, by construction. Same-context ablation reports a difference and therefore reads the rule as load-bearing, which is the correct reading of the measurement and the wrong conclusion — the rule is bearing load in the wrong direction. Transfer inherits the same defect: an expired constraint reproduces its effect in a held-out context perfectly well. The claim is falsified by exhibiting a negative-differential rule that any of the three classes flags for retirement on its own.

3. **Generation review is scheduled by the model release cadence, not by the usage log.** The other three classes are triggered by accumulated observation and may run at any convenient interval. This one has an external clock, and the audit cannot be deferred to the next scheduled stocktake: between the generation boundary and the audit, the rules layer is actively degrading the judgment it was written to protect. Model-side capability turnover is also the fastest of the four mechanisms, because the model release cadence runs ahead of the platform feature cadence.

4. **The vendor's own prompt-engineering guidance is admissible evidence.** Where the platform publisher states which prompting practices its current generation has made unnecessary or counterproductive, that statement is evidence about the substrate and may be cited directly in a retirement decision. It is cheaper and broader than local ablation, and it certifies something different: it speaks to the model's capability, not to this operator's internalization. A generation-review retirement therefore retires the constraint for every user-agent pair at once (as platform absorption does, Implication 5) while claiming nothing about anyone's learning. It must not be recorded as evidence of internalization.

### What this decision does not add

No instrument. The other three classes each have or imply a procedure — a telemetry query, a paired compliance run, a held-out construction. Generation review as specified here is a scheduled human-and-agent reading of the rules layer against a published capability claim, and the cost it is looking for — reasoning spent reconciling contradictions — is not measured locally at all; it is asserted by the vendor for the vendor's own evaluations, and inferred here from the structure of the rules found. Constructing a local instrument for conflict cost is left open. It is the same open question ADR-0022 left for held-out transfer, in a different place: 0022 lacks a reference construction, 0023 lacks a metric.

Nor does this decision add a fifth vector to the dissolution taxonomy. The `rules/common/akc-cycle.md` framing of **two vectors** — inward and downward — is retained: model-capability turnover is a trigger for the *downward* audit, with the substrate's judgment in place of its features. The four mechanisms in `docs/scaffold-dissolution.md` remain the finer-grained account of the same two vectors.

## Alternatives Considered

### (a) Treat this as a special case of platform-side absorption

Both are exogenous, both retire the scaffold for everyone at once, and both live under the downward vector. Folding model turnover into platform absorption would keep the taxonomy at three mechanisms and three evidence classes. Rejected because the two differ in the one property that determines urgency: platform absorption leaves a *redundant* scaffold, model turnover leaves a *harmful* one. A single class whose members differ on "can this wait for the next stocktake?" cannot carry a scheduling rule, and the scheduling rule is the operationally load-bearing part of this decision.

### (b) Extend the silence check instead of adding a class

Make the telemetry layer flag always-loaded rules whose content overlaps current substrate guidance, so the existing instrument covers the case. Rejected as a category error of the kind the harness's own code-vs-LLM seam warns about: detecting that a rule *exists* is structural and cheap, but deciding whether its premise has expired against the current generation's judgment is semantic and cannot be delegated to the telemetry layer. Enumeration could be automated; the verdict is the human-and-agent reading this class names. This remains a candidate for the *enumerate* half once a conflict-cost metric exists.

### (c) Withhold the ADR until conflict cost is measured locally

Wait for an own-cycle measurement of reasoning spent on contradictory instructions before recording anything, as ADR-0022 waited for external controlled evidence before revising the completion criterion. Rejected because the load-bearing claim here is the *blindness*, which is structural and already established — the instruments cannot see this class of failure regardless of how large its cost turns out to be. Withholding would leave the norm document asserting a completion criterion whose three evidence classes are known to be incomplete. The unmeasured part is scoped explicitly in Status and in "What this decision does not add" instead.

## Consequences

### Positive

- The completion criterion stops over-claiming. A rules layer that passes silence, ablation, and transfer can no longer be described as audited; it has been audited against absence, not against expired premises.
- Retirement decisions gain a class for the cheapest available evidence. Vendor prompt-engineering guidance was already being read; it now has a declared standing in the norm rather than entering decisions informally.
- The urgency asymmetry becomes explicit and actionable: zero-differential artifacts wait for the next stocktake, negative-differential ones do not.
- Implication 1 gains a boundary. "Zero usage is the success signal" remains true for the three absence-detecting classes and is now stated as not covering the inverse case, where full usage is the failure signal — which removes a reading under which a maximally-firing rules layer looks maximally healthy.

### Negative

- A class with no instrument sits alongside three that have or imply one, which weakens the norm's claim that dissolution is observable rather than narratable. The 2026-07-25 retirement was decided by reading, not by measurement — closer in kind to the 2026-06-10 observation than to 2026-07-09.
- Admitting vendor statements as evidence introduces a dependency on the publisher's disclosure practice and on the accuracy of evaluations this cycle cannot inspect. A vendor claim of "no measurable loss" is a claim about the vendor's eval suite, not about the operator's work.
- The audit has an external clock the operator does not control, and model generations can arrive faster than a rules layer can be re-read.

### Neutral

- Nothing in the six-phase structure changes. Generation review is a Curate-phase evidence class, and the existing Curate scaffolds (skill-stocktake, rules-stocktake) are where it would be executed; rules-stocktake's Dissolve verdict already carries the downward vector this class triggers.
- The count of retirement evidence classes is now four, and `docs/scaffold-dissolution.md` states it in one place. Per the repo's numeric-claim discipline, other documents point rather than restate.

## Relationship to other ADRs

- **ADR-0022** (transfer as the completion test) — direct sibling. 0022 asked whether the instrument tests the right *distribution*; 0023 asks whether the instrument can see this *class of failure* at all, and what schedules the audit. 0022's three evidence classes become four.
- **ADR-0016** (which surface a Measure instrument observes) — the third member of the same series: surface (0016) → distribution (0022) → schedule and blind spot (0023).
- **ADR-0019** (the cycle's structure is provisional) — this ADR is that principle applied to the norm's own instruments: the three evidence classes were a snapshot, not a closed set.
