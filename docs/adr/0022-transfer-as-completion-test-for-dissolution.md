# ADR-0022: Transfer as the Completion Test for Dissolution

> **Summary.** The dissolution Completion Criterion (`docs/scaffold-dissolution.md`) has defined internalization as ablation indistinguishability: run compliance measurement with and without the rule loaded — when the two are indistinguishable, internalization is complete and the rule may be deleted. That test is run on the same task distribution the rule has been operating in, and on that distribution it cannot separate two different explanations of the same result: *the judgment has been internalized* and *the surrounding context is carrying the behavior*. External controlled evidence (EvoAgentBench, arXiv:2607.05202) shows that transfer is where skill value is actually decided: under an ability-supported yet instance-disjoint split, curated skill content transfers positively in all 24 evaluation cells while no automatic extraction method sustains positive gain in all settings, with negative transfer reaching −36.3 points in software engineering. ADR-0022 records the falsifiable claim — *same-context ablation indistinguishability does not certify internalization* — and revises the Completion Criterion into two stages: ablation indistinguishability is **necessary** evidence, and held-out transfer — the same judgment reproducing in a context that shares the principle but not the instances — is the **completion** evidence. ADR-0022 is the sibling of ADR-0016: ADR-0016 specifies which surface a Measure instrument must observe (agent text, not only tool calls); ADR-0022 specifies which distribution it must test against (held-out, not only same-context).

## Status

**experimental** — the trigger is external controlled evidence plus a structural argument, not an observed failure in this cycle's own operation (n=0: no own-cycle case yet where same-context ablation passed and held-out transfer failed — the ablation criterion itself has never been executed; the one instrument-verified retirement to date, 2026-07-09, was decided by telemetry silence, not ablation). Promotion to accepted should be re-examined when the first own-cycle transfer observation exists, in either direction.

## Date

2026-07-23

## Context

The Completion Criterion in `docs/scaffold-dissolution.md` ("Completion Criterion and Dissolution Order") supplies the termination test for dissolution: *"run compliance measurement (skill-comply) with and without the rule loaded — when the two are indistinguishable, internalization is complete and the rule may be deleted."* The criterion made dissolution observable rather than narratable, and that was its point.

Two facts about the criterion, as it stands, matter here.

**First, it has never been executed.** The repository's three dissolution observations rest on other evidence classes: the 2026-03-29 observation is narrative (the cycle ran without skills being invoked), the 2026-06-10 observation is platform absorption (the host shipped native equivalents), and the 2026-07-09 observation — the first instrument-verified retirement — was decided by the telemetry silence check (zero organic activations over a month), not by an ablation run. Silence is valid evidence for retiring an unused artifact; it is not a claim about internalization. The ablation criterion remains a defined, untested instrument specification.

**Second, its test distribution is silently the training distribution.** The with/without comparison runs in the same repository, task genre, and session lineage the rule has been operating in. On that distribution, indistinguishability has two competing explanations the test cannot separate: (a) the judgment has been absorbed into the operator-agent pair's durable layers (internalization — the thing dissolution claims); or (b) the surrounding context — CLAUDE.md phrasing, sibling rules, memory entries, the operator's own prompts, the repository's conventions — carries enough signal that the behavior appears with or without the rule *in this context*, and would disappear with it elsewhere (context-carry). A third confound compounds the ambiguity: a zero gap can also mean the rule was never load-bearing on those tasks at all — indistinguishable because both conditions fail, or both succeed for unrelated reasons. A criterion that reads any of these as "internalization complete" will delete rules that were only locally supported.

The external trigger is EvoAgentBench (Gao et al. 2026, arXiv:2607.05202), a benchmark for agent self-evolution via ability transfer. Its design contribution is precisely the discipline the Completion Criterion lacks: the benchmark is *"ability-supported yet instance-disjoint"* — every test task is backed by verified training-side ability support, but no test task repeats a training instance (528/267 train/test split). Under that control, across 4 domains × 2 scaffolds × 3 backbones = 24 cells, curated ability content (the curator-side "Anchor Skill" reference — ability-grounded skills with deterministic retrieval, explicitly not a deployable method) yields positive per-domain gain in all 24 cells, while no automatic extraction method evaluated (Memento, ReasoningBank, GEPA) sustains positive gain in all settings — Memento reaches −36.3 points of negative transfer on one software-engineering cell. The result the benchmark exists to surface is invisible to same-distribution evaluation: a skill store can look beneficial where it was built and be net harmful one controlled step away. Primary verified against arXiv (title, abstract, Table 3 values) on 2026-07-23; the corroboration-side reading of the same evidence — the first controlled comparison on the axis of the human-gate delta — is recorded in ADR-0013's 2026-07-23 addendum, not here.

The structural lesson transfers directly. Dissolution's completion question — "has the judgment moved into the durable layers, so the explicit artifact can go?" — is a transfer question, not a same-distribution question. The existing criterion asks it on the wrong distribution.

## Decision

AKC revises the dissolution Completion Criterion into a two-stage test:

> **Stage 1 — ablation (necessary).** Run compliance measurement with and without the rule loaded, in the context the rule has been operating in. Indistinguishability is necessary evidence: if the two conditions differ, the rule is still load-bearing and dissolution has not completed. But indistinguishability alone certifies nothing — it cannot separate internalization from context-carry, or from the rule never having been load-bearing.
>
> **Stage 2 — held-out transfer (completion evidence).** The same judgment must reproduce in a held-out context: one that shares the principle's applicability but not the surface instances — a different repository, task genre, or session lineage. Only transfer certifies that the judgment lives in the durable layers rather than in the local context. Held-out means instance-disjoint, not merely re-run.

The decision is framed as a **falsifiable claim**:

> A rule whose ablation is indistinguishable in the context it was learned in can still fail to reproduce in a held-out context. A Completion Criterion that tests only same-context ablation will therefore retire rules that were context-carried, not internalized.

The claim is falsifiable in the strong direction: if, over accumulated observations, rules that pass same-context ablation reliably also pass held-out transfer, the second stage is redundant and should be dropped — the criterion would revert to its one-stage form and this ADR would be superseded.

Two consequences follow for any Measure instrument used in dissolution decisions:

1. **The test distribution is part of the instrument's specification.** A compliance report must state what distribution it measured on — same-context or held-out — because the same number certifies different things on each. This parallels ADR-0016's requirement that the observation surface be specified; together the two ADRs specify a Measure instrument along both axes: what it observes, and against what it tests.

2. **Retirement decisions name their evidence class.** The repository now has three distinct classes: *silence* (telemetry shows the artifact unused — retires an artifact, claims nothing about internalization), *ablation* (behavior indistinguishable in-context — necessary for dissolution, not sufficient), and *transfer* (judgment reproduces held-out — the completion certificate). The 2026-07-09 retirement remains valid under this classification: it was a silence-based retirement of an absorbed skill, and never claimed to be an internalization certificate.

### What this decision does not add

- **No new phase.** The six phases are unchanged. ADR-0022 sharpens what the existing Measure phase must test against when it serves dissolution decisions, exactly as ADR-0016 sharpened what it must observe.
- **No reference instrument in AKC.** How to construct a held-out context at solo-operator scale — where there is no 528/267 task pool, and the operator's repositories share conventions by design — is an open instrument-design question, and AKC does not ship an answer. AKC states the requirement the instrument must satisfy; it does not build the instrument (the same boundary ADR-0016 drew for text observability).
- **No change to the dissolution order prediction.** The predicted order (generally-stated principles first, taste-encoding thresholds last) is unchanged; this ADR changes when "dissolved" may be declared, not what dissolves first.

## Alternatives Considered

- **Amend `scaffold-dissolution.md` only, with no ADR.** Rejected. The revision is a judgment — *same-context indistinguishability is not sufficient* — and judgments belong in ADRs so they survive document rewrites (the same reasoning by which ADR-0013 rejected a README-only positioning). The norm document carries the criterion; the ADR carries why the criterion changed.

- **Build a scaled-down EvoAgentBench-style transfer instrument into AKC.** Rejected. The no-reference-instrument boundary (ADR-0016) applies: AKC states requirements on Measure instruments and does not ship them. Additionally, whether a controlled ability-supported split is constructible at all at solo-operator scale is an open question — deciding it inside this ADR would be design by assertion.

- **Make held-out transfer a necessary condition for any retirement.** Rejected while experimental. Held-out contexts are not always constructible (a rule about one repository's release pipeline may have no second context to transfer to), and silence-based retirement of unused artifacts must remain available — it retires the artifact without claiming internalization. Transfer is the completion evidence for *dissolution claims*, not a gate on all deletion.

- **Record EvoAgentBench as corroboration in ADR-0013 and change nothing here.** Rejected. The finding is not only corroboration of the human-gate delta; it contradicts the sufficiency of the existing Completion Criterion — a tension with a standing repository norm, not a confirmation of one. Recording the corroboration while leaving the criterion would preserve a test known to conflate context-carry with internalization.

## Consequences

### Positive

- The Completion Criterion becomes honest about what it can certify. "Indistinguishable here" and "internalized" are no longer conflated, and the criterion inherits the control discipline the external evidence showed to be decisive.
- Retirement decisions gain a named evidence-class vocabulary (silence / ablation / transfer), so future dissolution records state what kind of evidence backed them — the 2026-07-09 record is retroactively classifiable without being retroactively weakened.
- Together with ADR-0016, the Measure phase now has a two-axis instrument specification (observation surface × test distribution) that any future compliance tool can be reviewed against.

### Negative

- Held-out contexts cost more than same-context ablation — a second repository or task genre must exist and be exercised. For some rules no such context exists, and their dissolution claims will remain unverifiable rather than cheaply (and falsely) certifiable. This is accepted: an unverifiable claim marked unverifiable is better than a wrong certificate.
- Rules awaiting transfer evidence stay loaded longer, spending context budget that the one-stage criterion would have reclaimed. The cost is bounded by the operator's judgment about when a transfer opportunity is worth constructing.
- The ADR rests on external evidence and structural argument with zero own-cycle observations — the reason its status is experimental. It may be revised or withdrawn when own-cycle evidence arrives.

### Neutral

- No code changes, no schema changes, no change to the six phases or the reference implementation. `docs/scaffold-dissolution.md` (and its Japanese mirror) are revised in the same change that introduces this ADR, per the current documentation-sync discipline — unlike ADR-0016, whose front-door alignment was deferred to a separate change.

## Relationship to other ADRs

- **ADR-0016 (Measuring Thinking-Centric Phases).** The sibling decision. ADR-0016 specifies the Measure instrument's observation surface (agent text promoted to observable events); ADR-0022 specifies its test distribution (held-out, when the question is internalization). Both correct the same failure shape — an instrument whose silent default (tool-calls-only; same-context-only) systematically misreads exactly the question it was built to answer.
- **ADR-0019 (The Cycle's Structure Is Provisional).** The Completion Criterion is part of the cycle's self-description, and this revision is the disposition ADR-0019 records — held lightly, revised through the cycle's own operation — applied to the criterion itself.
- **ADR-0013 (Positioning Within the Agent-Memory Literature).** The 2026-07-23 addendum records the same evidence from the corroboration side: EvoAgentBench's curated-versus-automatic contrast is the first controlled comparison on the axis of the human-gate delta (ADR-0005). The two readings share one primary source; the tension side (this ADR) and the corroboration side (the addendum) are deliberately kept in their respective homes.
- **ADR-0010 (Human Cognitive Resource as Central Constraint).** A false internalization certificate spends the scarcest resource twice: the operator deletes a rule on bad evidence, then pays attention again when the behavior degrades in the next context. The two-stage criterion is cognitive economy applied to deletion decisions.

---

**Notes.** This ADR was prompted by an external benchmark rather than by an observed failure in this cycle — the inverse of ADR-0016, whose trigger was a measurement artifact in the reference instrument. That difference is why ADR-0016 is accepted and ADR-0022 is experimental: the evidence bar for accepted status is observed pain or repeated practice, and what exists today is a controlled external result plus a structural argument that the current criterion cannot distinguish internalization from context-carry. The first own-cycle transfer observation — a rule passing same-context ablation and then either reproducing or failing to reproduce held-out — decides the promotion question in either direction.
