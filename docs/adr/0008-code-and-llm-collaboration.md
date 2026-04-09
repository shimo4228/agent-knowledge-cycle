# ADR-0008: Code and LLM Collaboration

> **Summary.** Code owns determinism, auditability, and control flow. LLMs own meaning. The two are layered explicitly through four named patterns (LLM→Code guard, Code filter→LLM, LLM judge + Code enforce, Code orchestrator + LLM worker). The LLM never owns durable state or termination.

## Status
accepted

## Date
2026-04-09

## Context

Harness design repeatedly runs into the same question: "should this step
be a deterministic function or an LLM call?" Framed that way, the
question produces bad answers in both directions.

- Teams that prefer determinism write regex-based classifiers for what
  are fundamentally semantic tasks ("is this a bug report or a feature
  request?"), then accumulate exceptions until accuracy plateaus.
- Teams that prefer LLMs call them for tasks a three-line `str.endswith`
  or `json.loads` would answer in a nanosecond, paying latency and
  nondeterminism for nothing.

A self-improving harness makes this worse because the pipelines it
builds — episode logging, distillation, rule promotion, compliance
measurement — all mix structural and semantic work in the same flow.
If the boundary between "code territory" and "LLM territory" is not
explicit, the pipeline develops seams where responsibility is unclear
and failures concentrate.

The ADRs already in place pin down pieces of the answer implicitly:
ADR-0004 (two-stage distill) is really a code-orchestrator-plus-LLM-worker
pattern; ADR-0005 (human approval gate) is really a judge-plus-enforce
pattern; ADR-0007 (untrusted content boundary) is really a guard on LLM
output before it reaches persistent state. But nothing in the repo
states the underlying principle, so each new pipeline re-derives it.

## Decision

AKC adopts **Code-LLM Layering** as a first-class design decision:

> Code owns determinism, auditability, and control flow. LLMs own
> meaning. Layer them explicitly, make the contract between layers
> strict, and never let the LLM own durable state or termination.

### The split

| Concern | Owner |
|---------|-------|
| Loop termination, retry budget, step sequencing | Code |
| Schema validation, format checks, byte-level equality | Code |
| Persistent writes, mutation of rules / identity / config | Code |
| Classification, extraction, summarization, judgment | LLM |
| "Does this mean the same as that?" / semantic similarity | LLM |
| "Is this an improvement?" / quality assessment | LLM (as input to a code-owned decision) |

When a responsibility does not have a clear owner, the pipeline will
fail at that seam.

### The four layering patterns

Real pipelines are built out of four patterns, described in full in the
[`code-and-llm-collaboration`](../skills/code-and-llm-collaboration.md) skill:

1. **LLM → Code guard.** LLM produces structured output; code validates
   against schema + forbidden-pattern + size checks before the output
   touches persistent state.
2. **Code filter → LLM.** Code narrows a large, noisy input first (by
   date, type, size, structural relevance); the LLM does semantic work
   on the curated subset.
3. **LLM judge + Code enforce.** LLM decides (accept / reject / score);
   code takes the deterministic action, with a human gate for
   high-stakes changes (ADR-0005).
4. **Code orchestrator + LLM worker.** A deterministic loop owns
   termination, retries, state, and error handling; the LLM does one
   focused semantic task per step. Never invert this.

Real pipelines compose these: an orchestrator wraps everything, each
step filters then calls the LLM, each LLM output passes a guard, and
any state mutation goes through a judge-enforce pair.

### The single-task decision

For a single task (not a pipeline), the question is "is this property
**structural** or **semantic**?" The [`when-code-when-llm`](../skills/when-code-when-llm.md)
skill spells out the test: *can two inputs with the same bytes mean
different things in different contexts?* If yes, use an LLM. If no,
use code — and expect 100% accuracy.

### Relationship to existing ADRs

- **ADR-0004 Two-Stage Distill Pipeline** — an instance of Pattern 4
  (orchestrator) combined with Pattern 1 (guard on the Stage 2 output).
- **ADR-0005 Human Approval Gate** — an instance of Pattern 3, with the
  human as the final enforcer of high-stakes changes.
- **ADR-0007 Untrusted Content Boundary** — the guard in Pattern 1 is
  where the boundary is enforced at the "LLM output meets persistent
  state" seam.

ADR-0008 names the principle these three ADRs already rely on.

## Alternatives Considered

- **Leave it implicit.** Each pipeline re-derives the patterns from
  first principles. This is how we got here and is what drove the
  decision to write this ADR.
- **"Prefer code" as a blanket rule.** Matches the regex-first
  temperament but collapses onto semantic tasks, where it produces
  brittle classifiers. Rejected.
- **"Prefer LLM" as a blanket rule.** Matches the let-the-model-decide
  temperament but breaks on simple structural checks and surrenders
  control flow. Rejected.
- **Prescribe one canonical pattern (e.g. always orchestrator+worker).**
  Too restrictive. Real pipelines need all four patterns, composed.

## Consequences

- Every new pipeline in AKC (and in any harness using AKC) can be
  described in terms of the four patterns. Code review gains the
  question: *"which pattern is this, and where are its guard /
  enforce / orchestrator responsibilities?"*
- The two design-pattern skills (`when-code-when-llm`,
  `code-and-llm-collaboration`) are the canonical "how" reference and
  live in [`docs/skills/`](../skills/).
- Existing ADRs-0004/0005/0007 gain a shared vocabulary. Future
  refactoring can point at "Pattern 1" or "Pattern 4" instead of
  re-explaining the shape each time.
- The rule "LLM never owns durable state" becomes auditable: grep for
  calls where LLM output is written to disk without passing through a
  validator.

---

**Inspired by:** internal contemplative-agent skills
`code-and-llm-collaboration` and `when-code-when-llm`, distilled from
repeated pipeline design friction during self-improving-agent work.
