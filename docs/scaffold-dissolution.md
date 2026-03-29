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

In a session on 2026-03-29, all six AKC phases were executed through conversation. No AKC skill was explicitly invoked:

| AKC Skill | Phase | What happened in conversation |
|-----------|-------|-------------------------------|
| search-first | Research | Investigated ECC v1.9.0 diff, evaluated Python-related changes |
| skill-stocktake | Curate | Reviewed 33 skills one by one through dialogue → reduced to 16 |
| skill-comply | Measure | Discovered eval-harness duplicates testing.md rule |
| rules-distill | Promote | Saved feedback_python_review to memory during cleanup |
| learn-eval | Extract | Externalized insights as two article drafts |
| context-sync | Maintain | Ran /context-sync at the end to verify documentation consistency |

## Why This Happens

### User-side learning

Through repeated AKC cycles, users develop an implicit understanding of when to audit, when to distill, and what to measure. They no longer need the skill's step-by-step instructions — they ask the right questions naturally.

### AI-side accumulation

Each cycle leaves traces in the persistent layers:
- **Rules** (`rules/`) absorb cycle principles through distillation
- **Memory** (`memory/`) accumulates feedback and decision history
- **ADRs** (`docs/adr/`) record design decisions

These are loaded as context every session. The AI can follow cycle principles without reading skill files, because the principles are already embedded in the rules and memory it consumes.

### The training wheels analogy

Skills are training wheels on a bicycle:
- At first, you fall without them (the cycle doesn't run without skills)
- Once you can ride, they get in the way (skills consume context for no benefit)
- Removing them doesn't make you forget how to ride (cycle principles persist in rules and memory)

## Implications

1. **Success is not measured by skill usage** — Skills becoming unused is the success condition, not a failure.
2. **Skills are temporary teaching materials, not permanent tools** — Once they have transmitted their concepts, they can be retired.
3. **Cycle persistence depends on rules and memory, not skills** — Deleting skills does not break the cycle as long as principles are embedded in persistent layers.
4. **New user-agent pairs need the scaffolding again** — Scaffolding is person-dependent. A different context requires reconstruction.

## Relationship to Design Principles

This concept aligns with AKC's existing design principles:

- **Composable** — Because each skill is independent, each can become unnecessary independently.
- **Non-destructive** — Deleting skills preserves all accumulated rules, memory, and ADRs.
- **Observable** — skill-comply can verify whether the cycle runs even without skills installed.
