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

The host platform itself absorbs the scaffold: the tool or model ships the capability natively, making the local artifact redundant regardless of whether anyone internalized it. Unlike the first two mechanisms, this one is exogenous — driven by the platform's release cadence, not by practice — and it is currently the fastest of the three. The 2026-06-10 observation measured the lag at roughly three months from hand-built loop to built-in feature.

### The training wheels analogy

Skills are training wheels on a bicycle:
- At first, you fall without them (the cycle doesn't run without skills)
- Once you can ride, they get in the way (skills consume context for no benefit)
- Removing them doesn't make you forget how to ride (cycle principles persist in rules and memory)

## What Survives: The Information-Differential Law

Dissolution sorts artifacts by a single criterion — not sophistication, but the **information differential** between the artifact and what the model/platform already knows:

- **Differential zero — dissolves.** Universal procedures (code review checklists, TDD steps, build-fix loops) are training data; the platform absorbs them first.
- **Differential full — persists.** Personal context (one's own repos, voice conventions, publication pipelines), live external-service operations (DOI registries, dataset mirrors, knowledge-graph endpoints), and the harness's own self-management have no training-data substitute.

A general-purpose harness therefore purifies over time into an operating system for its owner's specific practice. Looking "niche and strange" is not decay; it is what remains when the rising tide of general capability submerges everything generic.

## Completion Criterion and Dissolution Order

Dissolution is observable, not just narratable. The Measure phase supplies a termination test: run compliance measurement (skill-comply) with and without the rule loaded — when the two are indistinguishable, internalization is complete and the rule may be deleted. The norm document carries its own death-determination criterion.

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

## Relationship to Design Principles

This concept aligns with AKC's existing design principles:

- **Composable** — Because each skill is independent, each can become unnecessary independently.
- **Non-destructive** — Deleting skills preserves all accumulated rules, memory, and ADRs.
- **Observable** — skill-comply can verify whether the cycle runs even without skills installed.
