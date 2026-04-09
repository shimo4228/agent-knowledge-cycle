# ADR-0004: Two-Stage Distill Pipeline (Free-form → Format)

> **Summary.** Distillation is split into a free-form reasoning stage followed by a strict formatting stage, so the LLM never has to discover content and satisfy a schema in the same call. This decoupling substantially improves quality on smaller local models.

## Status
accepted

## Date
2026-04-09

## Context

A straightforward distillation prompt asks the LLM to read N episodes and
emit a structured JSON array of patterns in one shot. In practice — especially
on smaller local models — single-stage constrained decoding produces shallow,
generic patterns: "the agent responded to a user", "the conversation involved
code". The constraint (JSON schema, required fields) competes with the
reasoning budget, and the model spends its tokens satisfying the format
instead of finding signal.

The prior art in contemplative-agent (ADR-0008) documents a concrete quality
improvement from 2/10 to roughly 12/16 (human rubric) by splitting distillation
into two stages.

## Decision

Distillation is a two-stage pipeline:

### Stage 1 — Free-form reasoning

The LLM is given the raw episodes and a minimal prompt asking it to think out
loud: what patterns recur, what surprised it, what the agent should remember.
Output is unstructured prose. No JSON schema, no required fields, no length
limit beyond the model's context window.

The goal of Stage 1 is *insight*. Format compliance is not evaluated here.

### Stage 2 — Formatting

The Stage 1 prose is fed back to the LLM with a formatting prompt: "Rewrite
the following reflection as a JSON array of patterns matching this schema."
Stage 2 receives a fully-specified schema and is free to spend its entire
reasoning budget on structure because the content has already been decided.

### Why this works

- Stage 1 is free to be exploratory because no structural failure can happen.
- Stage 2 is free to be strict because no semantic discovery has to happen.
- Failures are localized: empty Stage 2 output points to a format bug,
  empty Stage 1 output points to a content bug.

### Template hook

The reference implementation exposes Stage 1's prompt as a template parameter.
Swap the template to change what the distillation *looks for* (errors,
decisions, user preferences) without rewriting the pipeline.

## Alternatives Considered

- **Single-stage constrained decoding** — What we replaced. Cheap but
  produces shallow patterns on smaller models.
- **Three or more stages** — Diminishing returns in the prior art. Stage 1
  (reason) + Stage 2 (format) captures the essential decoupling.
- **Skip the LLM and use heuristics** — Fast but misses cross-episode
  patterns that require language understanding.

## Consequences

- Distillation cost roughly doubles (two LLM calls per batch) but the quality
  gain on local 9B-class models is large enough to justify it.
- The pipeline has two places to inject guidance (what to look for, how to
  format it). Most experimentation should target the Stage 1 template.
- An implementation that loses Stage 1 and re-runs only Stage 2 from cached
  prose is a valid optimization for re-formatting without re-reasoning.

---

**Inspired by:** [contemplative-agent `docs/adr/0008-two-stage-distill-pipeline.md`](https://github.com/shimo4228/contemplative-agent),
which documents the original quality measurements.
