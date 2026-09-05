# Scaffold Dissolution — The Self-Obsolescence of AKC Skills

## Concept

AKC skills are **scaffolding**. As users and AI agents repeatedly run the cycle, both internalize its principles. The cycle begins to run naturally through conversation, without explicitly invoking any skill. Eventually, the skills become unnecessary.

```
Phase 1: Skills teach the behavior
  /skill-stocktake → Learn how to audit skills
  /skill-comply    → Learn how to measure compliance

Phase 2: The cycle becomes internalized
  Skills are not invoked, yet auditing and compliance checking
  happen naturally in conversation.
  Cycle principles accumulate in rules and memory.

Phase 3: Skills become unnecessary
  User: Cycle thinking patterns are second nature
  AI:   Rules and memory are sufficient to reconstruct cycle behavior
  Skills as explicit artifacts become redundant.
```

## Evidence

### 2026-03-29 — the cycle runs without skills

In a session on 2026-03-29, all six AKC phases were executed through conversation. No AKC skill was explicitly invoked:

| AKC Skill | Phase | What happened in conversation |
|-----------|-------|-------------------------------|
| search-first | Research | Investigated ECC v1.9.0 diff, evaluated Python-related changes |
| skill-stocktake | Curate | Reviewed 33 skills one by one through dialogue → reduced to 16 |
| skill-comply | Measure | Discovered eval-harness duplicates testing.md rule |
| rules-distill | Promote | Saved feedback_python_review to memory during cleanup |
| learn-eval | Extract | Externalized insights as two article drafts |
| context-sync | Maintain | Ran /context-sync at the end to verify documentation consistency |

### 2026-06-10 — dissolution by platform absorption

Three months later, a second dissolution pathway appeared — one the original concept did not anticipate. A stocktake of the personal harness (Claude Code, built on the ECC ecosystem) found that the host platform had shipped native equivalents of the hand-built verification loop: built-in `verify`, `code-review`, and `security-review` skills, and a native plan mode. The local counterparts — assembled with considerable effort only ~3 months earlier — had become name-colliding duplicates.

The outcome: six skills and one rule file deleted (further stale sections trimmed), net −1,429 / +124 lines, recorded as a harness ADR with explicit retirement criteria (built-in duplication / obviation by model knowledge / version-dependent description). The stocktake itself was triggered by a plain conversational request — the Curate phase ran end-to-end without `/skill-stocktake` being invoked, replicating the 2026-03-29 observation.

What survived the stocktake follows a clean law (see "What Survives" below): a 453-line OWASP checklist (zero differential against model knowledge) was retired; a 45-line personal session-spawning skill (full differential) was kept.

### 2026-07-09 — first telemetry-verified retirement (rules-layer absorption)

A third observation closed the loop between dissolution and measurement. The operator's harness carries a deterministic usage-telemetry layer (Measure) whose output feeds Curate's silence check. One month of logs showed that signal-first-research — one of the three design-pattern skills — had zero organic activations: no explicit invocations, and every file read traced back to an audit or cross-reference session, not to working use. The principle itself was firing daily — but through the always-loaded rules layer (the Research phase rule) and the search-first phase skill. The skill's operational content had been fully absorbed: the internalization pathway, completed and now instrumentally visible.

The local install was retired the same day, with references repointed to the rules-layer canonical. The published repository persists unchanged as the citable design-pattern artifact — dissolution removes the installed scaffold, not the recorded judgment. Two things distinguish this observation from the earlier two: the retirement was decided by an instrument (the silence check) rather than by narrative impression, meeting the "observable, not just narratable" criterion below in practice; and it confirms Implication 1 directly — zero usage was read as the success signal it is.

### 2026-07-25 — dissolution by model-capability turnover (the scaffold turns harmful)

A fourth observation changed the sign of the phenomenon. The three earlier pathways all end with a scaffold that has become *redundant* — it adds nothing, so removing it is free. This one ends with a scaffold that has become *costly to keep*.

The trigger was exogenous and published: Anthropic reported that Claude Code's own system prompt had been cut by more than 80% for the Claude 5 generation with no measurable loss on its coding evaluations, and named the mechanism — guardrails written to prevent a weaker model's worst cases now arrive as *conflicting instructions* the stronger model must spend reasoning to resolve ("leave documentation as appropriate" against "DO NOT add comments"). The constraint's premise had expired, and its cost had not.

Applying the same audit to the operator's harness found the same shape. The always-loaded rules layer measured 43,971 characters across 20 files, and carried: an over-constraint stated as an absolute ("ALWAYS create new objects, NEVER mutate" — simply wrong for in-place numeric work, builders, and accumulators); a nine-step task-type × pipeline decision matrix front-loaded into every session, including sessions that write no code; two sections of the same file each declaring itself the canonical one; and six language-specific rule files resident in every session regardless of language — verified injected in a session containing no Python at all. The rules layer fell to 19,240 characters (−56%, 20 → 14 files) with nothing discarded that had a home: the decision matrix moved to a skill loaded at implementation time, the language rules folded into an existing skill that already held the same domain, and the absolute was relaxed to match the vendor's own replacement wording — *write code that reads like the surrounding code*.

Two features distinguish this observation. The evidence class was **vendor disclosure** — cheaper and broader than local ablation, but it certifies something different: it speaks about the model's capability, not about this operator's internalization, so it retires the constraint for everyone at once (as platform absorption does, Implication 5) while claiming nothing about anyone's learning. And the retirement was **self-prescribed**: the rules layer already carried the Scaffold Dissolution clause, whose downward vector states that a hand-written rule over a domain the substrate now handles becomes a stale copy that can override and degrade the newer default. The clause had been written for platform absorption; model-capability turnover is the same argument with the substrate's *judgment* in place of its *features*, and the clause was amended to name it.

A third feature is measurable only in aggregate: after the cut, the largest resident cost in that harness was no longer the rules layer but the skill listing — 60 skill descriptions totalling 23,473 characters against a listing budget of roughly 1% of the context window. Dissolution relocates the constraint rather than removing it.

### 2026-09-05 — platform absorption of a documentation scaffold (hand-maintained codemaps → language server)

A fifth observation extends platform absorption from *skills* to *documents*. The operator's repos each carried `docs/CODEMAPS/`: hand-maintained Markdown describing file-level code structure (module inventories, import graph, per-pipeline data-flow prose) for the LLM of the next session to read. In the largest repo the set had grown to six files and ~205 KB — the architecture file alone ~30k tokens — and since June it had taken 159 commits to keep aligned with 197 source commits. Nobody read it: the author never did, and no session was observed reaching for it — sessions reach for the language server, `grep`, and the ADR a docstring cites.

The absorbing feature was the coding platform's native LSP tool: symbol search, references, and call hierarchy answered live from the checkout (`incomingCalls` on one function → 17 callers, line-accurate, no install beyond the pyright already present). With that in place the codemap's structural content had an information differential of zero — a stored snapshot of what the tool derives on demand — and its remaining prose had a *negative* differential: the dated brackets threaded through the data-flow sections were a changelog inlined into the body, duplicating `git log` at the cost of one sync commit per source commit. A bounded audit before deletion found 25 of 27 rationale items already present in the owning ADR or in the docstring beside the guard; two were moved, nothing else.

The retirement removed the documents, the freshness hook and readings that policed them, and — at the harness level — the skill and agent that produced them, so the mechanism cannot regrow. An independent build-or-not review had recommended keeping a per-repo opt-out instead of removing the producer; the author overrode it, and the difference is recorded in the harness ADR as a transfer condition. That is the caveat this observation carries for the Completion Criterion below: the evidence here is a **reader-side instrument run plus a measured maintenance cost**, not a held-out transfer. It is necessary evidence — the scaffold's premise (a reader with no symbol index) has expired, the way the 2026-07-25 premise expired — but the transfer half arrives only as the nine sibling repos that still hold codemaps, this one included, delete theirs and answer structure questions without them.

## Why This Happens

### User-side learning

Through repeated AKC cycles, users develop an implicit understanding of when to audit, when to distill, and what to measure. They no longer need the skill's step-by-step instructions — they ask the right questions naturally.

### AI-side accumulation

Each cycle leaves traces in the persistent layers:
- **Rules** (`rules/`) absorb cycle principles through distillation
- **Memory** (`memory/`) accumulates feedback and decision history
- **ADRs** (`docs/adr/`) record design decisions

These are loaded as context every session. The AI can follow cycle principles without reading skill files, because the principles are already embedded in the rules and memory it consumes.

### Platform-side absorption

The host platform itself absorbs the scaffold: the tool or model ships the capability natively, making the local artifact redundant regardless of whether anyone internalized it. Unlike the first two mechanisms, this one is exogenous — driven by the platform's release cadence, not by practice. The 2026-06-10 observation measured the lag at roughly three months from hand-built loop to built-in feature.

### Model-side capability turnover

The scaffold's *premise* expires rather than its function being duplicated. A constraint written to keep a weaker model out of its worst cases — a blanket prohibition, an exhaustive procedure, a repeated emphasis, an enumerated set of examples — has no duplicate in the newer platform; what changed is that the behavior it was preventing no longer occurs, while the instruction it adds still has to be read and reconciled. This is the only pathway of the four that is exogenous *and* makes the scaffold actively harmful rather than merely idle: the other three leave a scaffold that costs context, this one leaves a scaffold that costs judgment. Its clock is the model release cadence, which is faster than the platform's feature cadence, and it is the pathway least visible to local telemetry — a rule that fires on every session shows full usage right up to the point where its firing became the problem.

### The training wheels analogy

Skills are training wheels on a bicycle:
- At first, you fall without them (the cycle doesn't run without skills)
- Once you can ride, they get in the way (skills consume context for no benefit)
- Removing them doesn't make you forget how to ride (cycle principles persist in rules and memory)

The analogy holds for the first three mechanisms and breaks for the fourth. Training wheels left on a bicycle are dead weight; they do not steer. An expired constraint does steer — it argues against the rider's own balance. The 2026-07-25 observation is better read as a stabiliser bolted at an angle that was correct for a heavier frame.

## What Survives: The Information-Differential Law

Dissolution sorts artifacts by a single criterion — not sophistication, but the **information differential** between the artifact and what the model/platform already knows:

- **Differential negative — must be removed, not merely allowed to lapse.** Constraints whose premise has expired: guardrails against a weaker model's worst cases, now read as instructions to reconcile against a capability the model already has. These do not sit idle waiting to be pruned; they contradict the live default and consume reasoning to resolve. The 2026-07-25 observation is this class.
- **Differential zero — dissolves.** Universal procedures (code review checklists, TDD steps, build-fix loops) are training data; the platform absorbs them first.
- **Differential full — persists.** Personal context (one's own repos, voice conventions, publication pipelines), live external-service operations (DOI registries, dataset mirrors, knowledge-graph endpoints), and the harness's own self-management have no training-data substitute.

The negative pole is the reason dissolution cannot be left to attrition. A zero-differential artifact merely wastes context and can wait for the next stocktake; a negative-differential one degrades the behavior it was written to protect, and the longer it stays the more it looks like a working rule — because it keeps firing.

A general-purpose harness therefore purifies over time into an operating system for its owner's specific practice. Looking "niche and strange" is not decay; it is what remains when the rising tide of general capability submerges everything generic.

## Completion Criterion and Dissolution Order

Dissolution is observable, not just narratable. The Measure phase supplies a termination test, in two stages (ADR-0022):

1. **Ablation (necessary).** Run compliance measurement (skill-comply) with and without the rule loaded, in the context the rule has been operating in. If the two conditions differ, the rule is still load-bearing. But indistinguishability alone is not the certificate — on the rule's home distribution it cannot separate *internalized* from *carried by the surrounding context* (or from the rule never having been load-bearing there at all).
2. **Held-out transfer (completion evidence).** The same judgment must reproduce in a held-out context — a different repository, task genre, or session lineage that shares the principle but not the surface instances. Only transfer certifies that the judgment lives in the durable layers rather than in the local context. Then the rule may be deleted.

The external evidence for requiring the second stage is EvoAgentBench (arXiv:2607.05202), whose ability-supported yet instance-disjoint split showed that skill value is decided at transfer, not on the home distribution: curated skill content transferred positively in all 24 evaluation cells, while no automatic extraction method sustained positive gain in all settings — reaching −36.3 points of negative transfer in software engineering. A store of extracted behavior can look beneficial where it was built and be net harmful one controlled step away; a completion test that never leaves the home context cannot see the difference.

Retirement decisions accordingly name their evidence class, from four: **silence** (telemetry shows the artifact unused — retires an artifact, claims nothing about internalization; the 2026-07-09 retirement above is this class), **ablation** (necessary), **transfer** (the completion certificate), or **generation review** (the substrate's model generation changed and the rule was written against the previous generation's failure modes; the 2026-07-25 retirement above is this class, ADR-0023). The norm document carries its own death-determination criterion; ADR-0022 sharpened it from one test to two, and ADR-0023 added the fourth class.

The first three classes all detect an **absence** — of use, of effect, of portability — because the three mechanisms they were built against all leave the scaffold *redundant*. Model-capability turnover leaves it *harmful*, and is therefore invisible to all three: silence cannot fire for an always-loaded rule by construction, and same-context ablation correctly reports a difference, which reads as load-bearing when the load is being borne in the wrong direction. Generation review has an external clock — the model release cadence — and unlike the other three its audit cannot wait for the next convenient stocktake.

The predicted order of dissolution follows the differential law applied to AKC itself:

1. **First**: generally-stated behavioral principles (Research, Curate) — closest to what platforms absorb.
2. **Last**: the judgment thresholds inside Extract and Promote — *what is worth keeping* encodes the operator's taste, for which there is no universal answer.

The last line to remain will be a preference, not a rule.

## Implications

1. **Success is not measured by skill usage** — Skills becoming unused is the success condition, not a failure.
2. **Skills are temporary teaching materials, not permanent tools** — Once they have transmitted their concepts, they can be retired.
3. **Cycle persistence depends on rules and memory, not skills** — Deleting skills does not break the cycle as long as principles are embedded in persistent layers.
4. **New user-agent pairs need the scaffolding again** — Scaffolding is person-dependent. A different context requires reconstruction.
5. **Platform absorption retires scaffolding for everyone** — Unlike person-dependent internalization, capability shipped natively by the host platform makes the scaffold unnecessary for all future user-agent pairs at once.
6. **A model generation change is a retirement trigger, and the audit cannot be deferred** — When the substrate's judgment improves, constraints written for the previous generation flip from idle to harmful. Full telemetry is not a defence: an always-loaded rule reports full usage precisely while its firing is the cost. So the model release cadence, not the usage log, is what schedules this audit — and the vendor's own prompt-engineering guidance is admissible evidence for it.

## Relationship to Design Principles

This concept aligns with AKC's existing design principles:

- **Composable** — Because each skill is independent, each can become unnecessary independently.
- **Non-destructive** — Deleting skills preserves all accumulated rules, memory, and ADRs.
- **Observable** — skill-comply can verify whether the cycle runs even without skills installed.
