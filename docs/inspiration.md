# Inspiration and Prior Art

AKC did not emerge in a vacuum. Several of its core design decisions are
adapted from an earlier, more opinionated research repository:

## Upstream: a daily signal filter

[github.com/shimo4228/claude-skill-daily-research](https://github.com/shimo4228/claude-skill-daily-research)

Before Contemplative Agent existed, the author was running a daily research
pipeline — a `claude -p`-driven cron job that selected two trending topics
per day, conducted multi-stage web research, and wrote signal-filtered
reports to an Obsidian vault. Two things about this upstream matter for AKC:

1. **It is how Contemplative Agent got started.** One of the daily reports
   surfaced Laukkonen et al. (2025)'s *Contemplative Inference* paper. That
   report is what motivated the author to begin the Contemplative Agent
   project, whose engineering substrate in turn became the prior art for
   several of the ADRs listed below.
2. **It is how ADR-0010 got written.** The LLM-Wiki-pattern report that
   triggered ADR-0010's conversation was itself a daily-research output.
   The pipeline that surfaced the question also implemented the answer —
   a fact noted in ADR-0010's "Origin loop" Notes.

The pipeline is therefore both the earliest implementation of AKC's
Research phase (it predates the ADR by about a year) and the signal filter
that made every downstream AKC decision possible. It was skillified in
April 2026 under the `claude-skill-daily-research` name so it installs as
a standard Claude Code skill. The pattern the pipeline embodies is
documented, in abstract form and without personal references, in
[`docs/skills/signal-first-research.md`](skills/signal-first-research.md).

## Contemplative Agent

[github.com/shimo4228/contemplative-agent](https://github.com/shimo4228/contemplative-agent)

Contemplative Agent is an independent research project exploring
Contemplative Constitutional AI (Laukkonen et al., 2025) on a local 9B
language model. It is an *opinionated* agent: it ships with a specific
constitution, a specific identity template, and a specific research goal.

Underneath that opinionated surface is a set of engineering decisions that
are useful regardless of the philosophy on top. AKC lifts those decisions
into a harness-neutral form:

| AKC component | Prior art in contemplative-agent |
|---------------|----------------------------------|
| [ADR-0001 Security by Absence](adr/0001-security-by-absence.md) | `docs/adr/0007-security-boundary-model.md` |
| [ADR-0002 Immutable Episode Log](adr/0002-immutable-episode-log.md) | `src/contemplative_agent/core/episode_log.py`, ADR-0004 |
| [ADR-0003 Three-Layer Distillation](adr/0003-three-layer-distillation.md) | `docs/adr/0004-three-layer-memory-architecture.md` |
| [ADR-0004 Two-Stage Distill Pipeline](adr/0004-two-stage-distill-pipeline.md) | `docs/adr/0008-two-stage-distill-pipeline.md` |
| [ADR-0005 Human Approval Gate](adr/0005-human-approval-gate.md) | `docs/adr/0012-human-approval-gate-for-behavior-modifying-commands.md` |
| [ADR-0006 Single External Adapter](adr/0006-single-external-adapter.md) | `docs/adr/0015-one-external-adapter-per-agent.md` |
| [ADR-0007 Untrusted Content Boundary](adr/0007-untrusted-content-boundary.md) | `docs/adr/0007-security-boundary-model.md` |
| [`examples/minimal_harness/`](../examples/minimal_harness/) | `src/contemplative_agent/core/{episode_log,knowledge_store,distill}.py` |

## What AKC does not carry over

AKC is explicitly **not** a contemplative framework. The following
contemplative-agent elements are left upstream and are not part of AKC:

- The four axioms (emptiness, non-duality, mindfulness, boundless care)
- The identity templates in `config/templates/contemplative/`
- The meditation adapter (`adapters/meditation/`) and Active Inference
  experiments
- `docs/adr/0002-paper-faithful-ccai-implementation.md`
- Any prompt text that references CCAI, axioms, or contemplative practice

AKC takes the engineering substrate; contemplative-agent keeps the
philosophy. Both are valid, and they are intentionally kept as separate
repositories so that each can evolve independently.

## Relationship model

Contemplative Agent is **prior art and inspiration**, not a downstream
implementation. AKC does not depend on it; contemplative-agent does not
depend on AKC. Changes in one repository do not require changes in the
other. When AKC files are adapted from contemplative-agent source, the
adapted files carry an in-file credit at the top.

## Citing contemplative-agent

If your work builds on the engineering substrate (memory layers, distill
pipeline, security model) and you found it through AKC, please also credit
the original repository:

> Shimomoto, T. (2026). Contemplative Agent.
> https://github.com/shimo4228/contemplative-agent
