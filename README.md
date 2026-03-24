# Agent Knowledge Cycle (AKC)

A cyclic self-improvement architecture for AI coding agents.

## What is AKC?

AI coding agents accumulate skills, rules, and learned patterns over time. Without a maintenance loop, this knowledge degrades — skills go stale, rules contradict each other, documentation drifts from reality.

AKC is a set of six composable skills that form a closed self-improvement loop:

```
Experience → learn-eval → skill-stocktake → rules-distill → Behavior change → ...
               (extract)    (curate)          (promote)            ↑
                                                            skill-comply
                                                              (measure)
                                              context-sync ← (maintain)
```

Each skill addresses one phase of the knowledge lifecycle:

| Skill | Phase | What it does |
|-------|-------|-------------|
| [search-first](https://github.com/shimo4228/claude-skill-search-first) | Research | Search for existing solutions before building new ones |
| [learn-eval](https://github.com/shimo4228/claude-skill-learn-eval) | Extract | Extract reusable patterns from sessions with quality gates |
| [skill-stocktake](https://github.com/shimo4228/claude-skill-stocktake) | Curate | Audit installed skills for staleness, conflicts, and redundancy |
| [rules-distill](https://github.com/shimo4228/claude-skill-rules-distill) | Promote | Distill cross-cutting principles from skills into rules |
| [skill-comply](https://github.com/shimo4228/claude-skill-comply) | Measure | Test whether agents actually follow their skills and rules |
| [context-sync](https://github.com/shimo4228/claude-skill-context-sync) | Maintain | Audit documentation for role overlaps, stale content, and missing decision records |

## Why a cycle?

Static configuration drifts. Skills get added but never reviewed. Rules accumulate but compliance is never measured. Documentation grows stale.

AKC treats agent knowledge as a living system that requires continuous maintenance — not a one-time setup.

| Problem | AKC response |
|---------|-------------|
| Skills go stale | skill-stocktake audits quality periodically |
| Rules don't match practice | skill-comply measures actual behavioral compliance |
| Knowledge is scattered | rules-distill promotes recurring patterns to principles |
| Documentation drifts | context-sync detects role overlaps and stale content |
| Wheels get reinvented | search-first checks for existing solutions first |
| Learnings are lost | learn-eval extracts patterns with quality gates |

## Design Principles

1. **Composable** — Each skill works independently. Use one or all six.
2. **Observable** — skill-comply produces quantitative compliance rates, not subjective assessments.
3. **Non-destructive** — Every skill proposes changes and waits for confirmation. Nothing is auto-applied.
4. **Tool-agnostic in concept** — Designed for Claude Code but the architecture applies to any coding agent with persistent configuration.

## Origin

This architecture was first proposed and implemented by Tatsuya Shimomoto ([@shimo4228](https://github.com/shimo4228)) in February 2026.

The first five skills were contributed to [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code) between February and March 2026. context-sync was developed independently.

## How to Cite

If you use or reference the Agent Knowledge Cycle architecture, please cite:

```bibtex
@software{shimomoto2026akc,
  author       = {Shimomoto, Tatsuya},
  title        = {Agent Knowledge Cycle (AKC)},
  year         = {2026},
  url          = {https://github.com/shimo4228/agent-knowledge-cycle},
  note         = {A cyclic self-improvement architecture for AI coding agents}
}
```

Or in text:

> Shimomoto, T. (2026). Agent Knowledge Cycle (AKC). https://github.com/shimo4228/agent-knowledge-cycle

## Related Work

- [Contemplative AI framework](https://github.com/shimo4228/contemplative-agent) — Autonomous agent design inspired by Laukkonen et al. (2025)
- [Articles on Zenn](https://zenn.dev/shimo4228) — Development journal (Japanese)
- [Articles on Dev.to](https://dev.to/shimo4228) — English translations

## License

MIT
