Language: English | [日本語](README.ja.md)

# Agent Knowledge Cycle (AKC)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19200727.svg)](https://doi.org/10.5281/zenodo.19200727)

A knowledge cycle for AI agents — one that grows with the people who shape it.

## What is AKC?

AKC treats agent knowledge as a living asset: episodes are logged immutably,
distilled into patterns, promoted to rules, and continuously audited.
Six composable phases (Research → Extract → Curate → Promote → Measure →
Maintain) keep skills, rules, and docs aligned with reality. Without a
maintenance loop, agent knowledge degrades: skills go stale, rules
contradict each other, documentation drifts from the code.

This is not a one-directional optimization loop — the cycle changes
the human too. See [Why a cycle?](#why-a-cycle) below.

AKC ships as specifications, schemas, ADRs, and a minimal reference
example. Bring your own LLM and your own adapter.

## What's in this repo

```
agent-knowledge-cycle/
├── docs/
│   ├── akc-cycle.md              # Behavioral rules — the cycle as a single rules file
│   ├── scaffold-dissolution.md   # Skills are scaffolding; here is how they dissolve
│   ├── inspiration.md            # Prior art
│   ├── adr/
│   │   ├── 0002-immutable-episode-log.md         # JSONL, append-only, umask 0600
│   │   ├── 0003-three-layer-distillation.md      # Raw → Knowledge → Identity/Rules
│   │   ├── 0004-two-stage-distill-pipeline.md    # Free-form → structured format
│   │   ├── 0005-human-approval-gate.md           # No auto-promotion to rules
│   │   ├── 0008-code-and-llm-collaboration.md    # Code owns control flow, LLMs own meaning
│   │   ├── 0009-akc-is-a-cycle-not-a-harness.md  # Cycle as sole defining characteristic
│   │   ├── 0010-human-cognitive-resource-as-central-constraint.md  # Signal-first Research; cognitive economy
│   │   └── 0011-cycle-applies-to-any-knowledge-body.md  # Cycle is genre-neutral about what flows through it
│   └── skills/                   # Design-pattern skills paired 1:1 with ADRs
│       ├── when-code-when-llm.md                 # Per-task: structural vs semantic
│       ├── code-and-llm-collaboration.md         # Per-pipeline: four layering patterns
│       └── signal-first-research.md              # Intake-filter design for ADR-0010
├── schemas/
│   ├── episode-log.schema.json   # Layer 1 record shape
│   └── knowledge.schema.json     # Layer 2 pattern shape
└── examples/
    ├── minimal_harness/          # Mechanism demo — cycle on behavioral patterns
    │   ├── episode_log.py        # Layer 1
    │   ├── knowledge_store.py    # Layer 2 + time decay + forbidden-substring validation
    │   ├── distill.py            # Two-stage pipeline, LLM-agnostic
    │   └── demo.py               # python3 -m examples.minimal_harness.demo
    └── constitution_amend/       # Reference to downstream — cycle on constitutional values
        └── README.md             # Maps the AKC phases onto contemplative-agent's amend workflow
```

Eight ADRs, eight design principles, three design-pattern skills, two
JSON schemas, one ~300-line runnable reference implementation, and the
rules file that installs the whole cycle in a single `cp`. AKC defines
three memory layers and four code-LLM layering patterns.
The six cycle skills listed below remain the opinionated, full-fat
implementation of each phase.

AKC ships **two kinds of skills**:

- **Cycle skills** (external repositories) — one per phase of the
  self-improvement loop: `search-first`, `learn-eval`, `skill-stocktake`,
  `rules-distill`, `skill-comply`, `context-sync`.
- **Design-pattern skills** ([`docs/skills/`](docs/skills/)) — long-form
  "how" guides paired 1:1 with ADRs. These are cross-cutting and apply
  in multiple phases.

## The cycle

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
| [search-first](https://github.com/shimo4228/claude-skill-search-first) | Research | Search broadly, filter by signal — intake only what would change the next action |
| [learn-eval](https://github.com/shimo4228/claude-skill-learn-eval) | Extract | Extract reusable patterns from sessions with quality gates |
| [skill-stocktake](https://github.com/shimo4228/claude-skill-stocktake) | Curate | Audit installed skills for staleness, conflicts, and redundancy |
| [rules-distill](https://github.com/shimo4228/claude-skill-rules-distill) | Promote | Distill cross-cutting principles from skills into rules |
| [skill-comply](https://github.com/shimo4228/claude-skill-comply) | Measure | Test whether agents actually follow their skills and rules |
| [context-sync](https://github.com/shimo4228/claude-skill-context-sync) | Maintain | Audit documentation for role overlaps, stale content, and missing decision records |

## Rules — Install the cycle without the skills

You don't need all six skills to run the cycle. The [`docs/akc-cycle.md`](docs/akc-cycle.md) file distills the six phases into behavioral principles that any AI agent can follow through natural conversation.

### Quick install

```bash
# Copy to your agent's rules directory
cp docs/akc-cycle.md ~/.claude/rules/common/akc-cycle.md
```

That's it. The cycle will run through conversation — no skills, no plugins, no CLI tools.

### What the rules cover

| Phase | Rule summary |
|-------|-------------|
| Research | Search broadly, filter by signal — intake only what would change the next action |
| Extract | Capture reusable patterns from sessions with quality evaluation |
| Curate | Periodically audit for redundancy, staleness, and silence |
| Promote | Elevate patterns that recur 3+ times to the rule layer |
| Measure | Verify behavioral change quantitatively, not subjectively |
| Maintain | Keep documentation roles clean and content fresh |

### Skills vs Rules

- **Skills** provide deep, step-by-step workflows for each phase. Install them when you want guided execution.
- **Rules** provide principles and trigger conditions. Install them when you want the cycle to emerge naturally from conversation.
- Both can coexist. Rules ensure the cycle runs even when skills aren't triggered.

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

The cycle also changes the human. Through repeated Curate and Promote decisions, users sharpen their judgment about what knowledge is worth keeping. Through Research, they develop better intuition for when to adopt existing solutions versus building new ones. Through Measure, they learn what makes a good rule versus a vague aspiration. AKC is not a one-directional optimization loop where the agent improves in isolation — it is a bidirectional growth loop where human and agent co-develop through sustained interaction.

### Whose cognitive budget is the cycle protecting?

The human's. As agent capability grows, the scarce resource is no longer compute or context but human attention and judgment. AKC's phases are shaped around that scarcity: Research is signal-first so intake does not exceed digestion; Promote converts recurring decisions into rules so the same judgment is not re-made every session; Measure replaces manual re-auditing with observable compliance checks; and pre-implementation dialogue is front-loaded because intent misalignment discovered at review time is more expensive than the conversation that would have prevented it. Running the cycle is not free — but it is how the cycle protects the one resource that does not scale with the model. See [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md).

## Design Principles

1. **Composable** — Each skill works independently. Use one or all six.
2. **Observable** — skill-comply produces quantitative compliance rates, not subjective assessments.
3. **Non-destructive** — Every skill proposes changes and waits for confirmation. Nothing is auto-applied.
4. **Tool-agnostic in concept** — Designed for Claude Code but the architecture applies to any agent with persistent configuration.
5. **Evaluation scales with model capability** — Small models benefit from rubric-based scoring; reasoning models (Opus-class) evaluate with full context and qualitative judgment. AKC does not prescribe one approach — it matches evaluation depth to the model's reasoning capacity.
6. **Scaffold dissolution** — Skills are scaffolding. As the user and agent internalize the cycle, skills become unnecessary and rules alone sustain the loop. See [docs/scaffold-dissolution.md](docs/scaffold-dissolution.md).
7. **Code-LLM Layering** — Code owns determinism, auditability, and control flow. LLMs own meaning. Layer them explicitly; never let the LLM own durable state or termination. See [ADR-0008](docs/adr/0008-code-and-llm-collaboration.md).
8. **Human cognitive resource is the bottleneck** — As agent capability grows, the scarce resource is no longer compute or context but human attention and judgment. Every phase is shaped to protect that budget: signal-first intake in Research, rule promotion so the same decision is not re-made, compliance measurement so the human does not re-audit manually, and front-loaded dialogue because misaligned implementation costs more than the conversation that would have prevented it. See [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md).

## Relationship to Harness Engineering

AKC shares common ground with [harness engineering](https://mitchellh.com/writing/my-ai-adoption-journey) (Mitchell Hashimoto, 2025) — the practice of engineering solutions so that an agent never repeats the same mistake, through a combination of improved prompts (e.g., AGENTS.md updates) and programmatic tools (scripts, verification commands). Both aim to make agents more reliable. They differ in what they focus on.

| Layer | Question | Addressed by |
|-------|----------|-------------|
| Harness | "Is this output correct?" | Individual linters, tests, scripts |
| AKC | "Are the harnesses themselves still valid?" | skill-comply, skill-stocktake, context-sync |

**Correctness vs intent alignment.** Harness engineering focuses on getting the right result the first time — preventing known errors through better instructions and automated checks. AKC is more concerned with a different question: "is this aligned with the owner's intent?" An agent can avoid all known mistakes yet still diverge from design intent. Design Principle #3 (Non-destructive) reflects this — propose, then wait for confirmation, because intent alignment is difficult to fully automate.

**Reactive vs proactive.** Harness engineering is reactive by nature — each mistake triggers a new harness. AKC's skill-comply and skill-stocktake take a proactive approach, periodically auditing whether skills and rules are actually followed and whether they remain relevant. Design Principle #5 scales this evaluation to model capability — rubrics for small models, holistic judgment for frontier models.

## Customization

The reference implementations linked above are starting points. Fork them, rewrite them, adapt them to your agent and workflow. AKC defines the cycle — not the implementation. What matters is that the phases (extract → curate → promote → measure → maintain) form a closed loop, not how each phase is built.

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
  doi          = {10.5281/zenodo.19200727},
  url          = {https://doi.org/10.5281/zenodo.19200727},
  note         = {A knowledge cycle for AI agents — one that grows with the people who shape it}
}
```

Or in text:

> Shimomoto, T. (2026). Agent Knowledge Cycle (AKC). doi:10.5281/zenodo.19200727

## Related Work

- [Contemplative Agent](https://github.com/shimo4228/contemplative-agent) — An
  independent research repository exploring Contemplative Constitutional AI
  on a local 9B model. Its engineering substrate (three-layer memory,
  two-stage distillation) was the prior art that seeded AKC's ADRs.
  See [`docs/inspiration.md`](docs/inspiration.md) for details.
- [Articles on Zenn](https://zenn.dev/shimo4228) — Development journal (Japanese)
- [Articles on Dev.to](https://dev.to/shimo4228) — English translations

## Acknowledgments

AKC stands on the foundation of [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code)
by [@affaan-m](https://github.com/affaan-m). ECC was the baseline
harness I used every day, and its skills and rules gave me a rich
starting point to build on. Over months of daily use I added my own
skills and rules on top of ECC, and they proliferated faster than I
could track — skills went stale, rules started contradicting each
other, documentation drifted from the code. I kept having to audit
the mess and decide what to keep, what to merge, and what to promote
into a durable rule. The six-phase cycle is what that recurring
maintenance work looked like once I noticed the shape of it.

Without ECC as the ground to stand on, AKC would not exist. Deep
thanks to affaan-m and every contributor to ECC.

## References

AKC was built from practice, not theory. The following works were not
consulted during the process described above, but the resulting cycle
seems to share something with the ideas in them. They are listed here
for readers who might find the resonance interesting.

- [Mind in Life](https://www.hup.harvard.edu/books/9780674057517) (Evan Thompson, 2007) —
  The bidirectional loop between human and agent has something in common
  with the enactivist idea of structural coupling.
- [A Beautiful Loop: An Active Inference Theory of Consciousness](https://www.sciencedirect.com/science/article/pii/S0149763425002970)
  (Laukkonen, Friston, & Chandaria, 2025) — The way the human updates
  rules and skills by observing what the agent actually does feels
  vaguely like a recursive self-modeling loop.

## License

MIT
