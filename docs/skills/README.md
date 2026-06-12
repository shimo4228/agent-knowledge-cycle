# Design-pattern skills (moved to standalone repositories)

This directory previously hosted AKC's **design-pattern skills**: long-form
"how" guidance paired 1:1 with the ADRs that motivate them. They are now
published as standalone, installable skill repositories — the same
distribution model as the six [cycle skills](../../README.md#the-cycle).
The paired ADRs (the "why") remain in this repository.

| Skill | Repository | Paired ADR(s) | One-line summary |
|-------|------------|----------------------|------------------|
| when-code-when-llm | [shimo4228/when-code-when-llm](https://github.com/shimo4228/when-code-when-llm) | [ADR-0008](../adr/0008-code-and-llm-collaboration.md) | Per-task decision: is this property structural or semantic? |
| code-and-llm-collaboration | [shimo4228/code-and-llm-collaboration](https://github.com/shimo4228/code-and-llm-collaboration) | [ADR-0008](../adr/0008-code-and-llm-collaboration.md) | Per-pipeline decision: four layering patterns for mixing deterministic code and LLM calls |
| signal-first-research | [shimo4228/signal-first-research](https://github.com/shimo4228/signal-first-research) | [ADR-0010](../adr/0010-human-cognitive-resource-as-central-constraint.md) | Design a research intake filter that admits only information likely to change your next action |

## Installing

Each repository follows the standard Agent Skills layout
(`skills/<name>/SKILL.md`):

```bash
# manual copy
cp -r skills/<skill-name> ~/.claude/skills/<skill-name>

# or via SkillsMP
/skills add shimo4228/<skill-name>
```

## Why they moved

Hosting installable skills two levels deep under `docs/` made them hard
to discover and impossible to install with standard tooling. Moving each
to its own repository matches the cycle-skill distribution model while
the ADR pairing survives as cross-links: each skill's README and
references section points back to its ADR here, and the table above
points forward.
