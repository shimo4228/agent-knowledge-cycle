# Design-pattern skills

This directory holds **design-pattern skills**: long-form guidance that
complements AKC's architecture decision records with concrete "how"
material. They are distinct from the six [**cycle skills**](../../README.md#the-cycle)
(`search-first`, `learn-eval`, `skill-stocktake`, `rules-distill`,
`skill-comply`, `context-sync`), which live in external repositories
and implement the phases of the self-improvement loop.

| Layer | Purpose | Where it lives |
|-------|---------|----------------|
| Cycle skills | Run one phase of the cycle | External GitHub repositories, installed into your agent |
| Design-pattern skills | Teach a cross-cutting design pattern that shows up in multiple phases | Here, alongside the ADRs that motivate them |

Design-pattern skills pair 1:1 with ADRs so the "why" and the "how"
stay in sync. When an ADR changes, the matching skill gets reviewed.

## Current skills

| Skill | Corresponding ADR(s) | One-line summary |
|-------|----------------------|------------------|
| [when-code-when-llm](when-code-when-llm.md) | [ADR-0008](../adr/0008-code-and-llm-collaboration.md) | Per-task decision: is this property structural or semantic? |
| [code-and-llm-collaboration](code-and-llm-collaboration.md) | [ADR-0008](../adr/0008-code-and-llm-collaboration.md) | Per-pipeline decision: four layering patterns for mixing deterministic code and LLM calls |
| [llm-agent-security-principles](llm-agent-security-principles.md) | [ADR-0001](../adr/0001-security-by-absence.md), [ADR-0006](../adr/0006-single-external-adapter.md), [ADR-0007](../adr/0007-untrusted-content-boundary.md) | Concrete defense patterns (HTTP, credentials, LLM hosts) for the three structural security ADRs |
| [signal-first-research](signal-first-research.md) | [ADR-0010](../adr/0010-human-cognitive-resource-as-central-constraint.md) | Design a research intake filter that admits only information likely to change your next action |

## Installing as Claude Code skills

Each file is a valid Claude Code skill with frontmatter. To install:

```bash
mkdir -p ~/.claude/skills/<skill-name>
cp docs/skills/<skill-name>.md ~/.claude/skills/<skill-name>/SKILL.md
```

They can also be read as plain documentation — the frontmatter is
harmless Markdown.
