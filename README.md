Language: English | [日本語](README.ja.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [Português (Brasil)](README.pt-BR.md) | [Español](README.es.md)

# Agent Knowledge Cycle (AKC)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19200726.svg)](https://doi.org/10.5281/zenodo.19200726)

A knowledge cycle for AI agents — one that grows with the people who shape it.

## What is AKC?

AKC starts from a single observation: as agent capability grows, the
scarce resource is no longer compute or context — it is the human
attention and judgment running the loop. AKC is centered on that
scarcity. See [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md).

Protecting that budget reframes what the cycle is for. The goal is
not "the agent produced individually correct output" — it is "the
agent's behavior stays aligned with the operator's intent across
sessions". Correctness can be checked by tests; alignment cannot,
because intent itself moves as the operator's judgment sharpens.

Alignment is therefore sustained over time, not configured once. The
cycle changes the human too: through Curate, Promote, and Measure
decisions, the operator's judgment about what makes good agent
behavior sharpens session by session — which is why the tagline says
the cycle grows *with* the people who shape it, not *for* them.
Underneath, this is a bidirectional growth loop where agent behavior
and human judgment co-develop.

Six composable phases — Research → Extract → Curate → Promote →
Measure → Maintain — operationalize this. Signal-first intake so
attention is not spent on what cannot change action; recurring
decisions promoted to rules so the same judgment is not re-made;
observable compliance so the human does not re-audit each session
manually. Without this loop, agent knowledge degrades — skills go
stale, rules contradict each other, documentation drifts from code.

AKC ships as specifications, schemas, ADRs, and a minimal reference
example. Bring your own LLM and your own adapter.

## Why AKC

### The bottleneck has moved

As agent capability grows, the scarce resource is no longer compute
or context but human attention and judgment. Every competing framework
optimizes the agent side — more tools, more memory, more context,
more automation. AKC asks the inverse question: given that the human
in the loop has a fixed daily budget of attention and judgment, how
should the cycle be shaped so that budget is not squandered?

AKC's phases are shaped around that scarcity. Research is signal-first
so intake does not exceed digestion. Promote converts recurring
decisions into rules so the same judgment is not re-made every
session. Measure replaces manual re-auditing with observable
compliance checks. Pre-implementation dialogue is front-loaded because
intent misalignment discovered at review time is more expensive than
the conversation that would have prevented it. Running the cycle is
not free — but it is how the cycle protects the one resource that
does not scale with the model. See [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md).

| Maintenance problem | AKC response |
|---------|-------------|
| Skills go stale | skill-stocktake audits quality periodically |
| Rules don't match practice | skill-comply measures actual behavioral compliance |
| Knowledge is scattered | rules-distill promotes recurring patterns to principles |
| Documentation drifts | context-sync detects role overlaps and stale content |
| Wheels get reinvented | search-first checks for existing solutions first |
| Learnings are lost | learn-eval extracts patterns with quality gates |

Each row replaces a maintenance task the human would otherwise carry
manually. The cycle is not free, but it is cheaper than re-doing the
same audit every time the question recurs.

### Aligned with intent, not just correct

Correctness can be automated: tests, types, linters, and review tools
all check whether an output passes specific criteria. Alignment cannot
be automated to the same degree, because intent itself moves as the
operator's judgment sharpens through use. An agent can satisfy every
correctness check and still drift from intent.

AKC's design choices reflect this. Design Principle #3 (Non-destructive)
— propose, then wait for confirmation — keeps every change at a
checkpoint where intent can be re-stated. Pre-implementation dialogue
is treated as a cognitive-economy investment, not as friction. The
distinction also explains how AKC differs from harness engineering:
harnesses optimize correctness on the first try, while AKC keeps the
harnesses themselves aligned with intent as that intent evolves. See
[Relationship to Harness Engineering](#relationship-to-harness-engineering)
for the layered comparison.

### The cycle changes the human too

Through repeated Curate and Promote decisions, users sharpen their
judgment about what knowledge is worth keeping. Through Research,
they develop better intuition for when to adopt existing solutions
versus building new ones. Through Measure, they learn what makes a
good rule versus a vague aspiration. AKC is not a one-directional
optimization loop where the agent improves in isolation — agent
behavior and human judgment co-develop through sustained interaction.
The tagline — *one that grows with the people who shape it* — names
exactly this property.

## What's in this repo

Nine ADRs, eight design principles, three design-pattern skills, two
JSON schemas, one ~500-line runnable reference implementation, and the
rules file that installs the whole cycle in a single `cp`. AKC defines
three memory layers and four code-LLM layering patterns. The six cycle
skills listed below remain the opinionated, full-fat implementation of
each phase.

AKC ships **two kinds of skills**:

- **Cycle skills** (external repositories) — one per phase of the
  self-improvement loop: `search-first`, `learn-eval`, `skill-stocktake`,
  `rules-distill`, `skill-comply`, `context-sync`.
- **Design-pattern skills** ([`docs/skills/`](docs/skills/)) — long-form
  "how" guides paired 1:1 with ADRs. These are cross-cutting and apply
  in multiple phases.

For the full repository tree and document-role routing, see [`docs/CODEMAPS/architecture.md`](docs/CODEMAPS/architecture.md).

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

## Design Principles

1. **Composable** — Each skill works independently. Use one or all six.
2. **Observable** — skill-comply produces quantitative compliance rates, not subjective assessments.
3. **Non-destructive** — Every skill proposes changes and waits for confirmation. Nothing is auto-applied.
4. **Tool-agnostic in concept** — Designed for Claude Code but the architecture applies to any agent with persistent configuration.
5. **Evaluation scales with model capability** — Small models benefit from rubric-based scoring; reasoning models (Opus-class) evaluate with full context and qualitative judgment. AKC does not prescribe one approach — it matches evaluation depth to the model's reasoning capacity.
6. **Scaffold dissolution** — Skills are scaffolding. As the user and agent internalize the cycle, skills become unnecessary and rules alone sustain the loop. See [docs/scaffold-dissolution.md](docs/scaffold-dissolution.md).
7. **Code-LLM Layering** — Code owns determinism, auditability, and control flow. LLMs own meaning. Layer them explicitly; never let the LLM own durable state or termination. See [ADR-0008](docs/adr/0008-code-and-llm-collaboration.md).
8. **Human cognitive resource is the bottleneck** — As agent capability grows, the scarce resource is no longer compute or context but human attention and judgment. Every phase is shaped to protect that budget: signal-first intake in Research, rule promotion so the same decision is not re-made, compliance measurement so the human does not re-audit manually, and front-loaded dialogue because misaligned implementation costs more than the conversation that would have prevented it. See [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md).
9. **Genre neutrality** — The cycle is a mechanism, not content. The same six phases operate on any coherent body of agent knowledge — behavioral patterns, domain expertise, or constitutional values — and AKC takes no position on which a downstream project cares about. What changes per genre is the evaluation criteria, prompt templates, and audit queries; the phases stay identical. See [ADR-0011](docs/adr/0011-cycle-applies-to-any-knowledge-body.md).

## Relationship to Harness Engineering

AKC shares common ground with [harness engineering](https://mitchellh.com/writing/my-ai-adoption-journey) (Mitchell Hashimoto, 2025) — the practice of engineering solutions so that an agent never repeats the same mistake, through a combination of improved prompts (e.g., AGENTS.md updates) and programmatic tools (scripts, verification commands). Both aim to make agents more reliable. They differ in what they focus on.

| Layer | Question | Addressed by |
|-------|----------|-------------|
| Harness | "Is this output correct?" | Individual linters, tests, scripts |
| AKC | "Are the harnesses themselves still valid?" | skill-comply, skill-stocktake, context-sync |

**Correctness vs intent alignment.** Harness engineering focuses on getting the right result the first time — preventing known errors through better instructions and automated checks. AKC is more concerned with a different question: is the agent's behavior aligned with the operator's evolving intent? See [Why AKC → Aligned with intent](#aligned-with-intent-not-just-correct) for the standalone treatment.

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
  version      = {2.1.0},
  doi          = {10.5281/zenodo.20076396},
  url          = {https://doi.org/10.5281/zenodo.20076396},
  note         = {A knowledge cycle for AI agents — one that grows with the people who shape it}
}
```

Or in text:

> Shimomoto, T. (2026). Agent Knowledge Cycle (AKC). doi:10.5281/zenodo.20076396

## Related Work

- [Contemplative Agent](https://github.com/shimo4228/contemplative-agent) — An
  independent research repository exploring Contemplative Constitutional AI
  on a local 9B model. Its engineering substrate (three-layer memory,
  two-stage distillation) was the prior art that seeded AKC's ADRs.
  See [`docs/inspiration.md`](docs/inspiration.md) for details.
- [Agent Attribution Practice (AAP)](https://github.com/shimo4228/agent-attribution-practice) —
  Sibling genre library (DOI [10.5281/zenodo.19652014](https://doi.org/10.5281/zenodo.19652014)).
  AKC v2.0.0's extracted security triplet (ADR-0001, ADR-0006, ADR-0007) was
  re-expressed there, alongside five additional ADRs, as eight harness-neutral
  ADRs on accountability distribution in autonomous AI agents. AKC is the
  cycle (mechanism); AAP is the practice (content).
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
