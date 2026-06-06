Language: English | [日本語](README.ja.md)

# Agent Knowledge Cycle (AKC)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19200726.svg)](https://doi.org/10.5281/zenodo.19200726)

<details>
<summary>AI-facing reading order</summary>

1. [`graph.jsonld`](graph.jsonld) — canonical machine-readable relationship map (six phases, phase-skill bindings, three memory layers, code-LLM patterns)
2. [`llms.txt`](llms.txt) — compact navigation index
3. [`llms-full.txt`](llms-full.txt) — consolidated factual reference
4. README and project-specific docs — narrative and detail

For the canonical relationship map of shimo4228's research ecosystem, see https://github.com/shimo4228/shimo4228/blob/main/graph.jsonld

</details>

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
Measure → Maintain — operationalize this. Without this loop, agent
knowledge degrades — skills go stale, rules contradict each other,
documentation drifts from code. How each phase protects the attention
budget is unpacked in [Why AKC](#why-akc) below.

AKC ships as specifications, schemas, ADRs, and a minimal reference
example. Bring your own LLM and your own adapter.

## Why AKC

### The bottleneck has moved

Every competing framework optimizes the agent side — more tools, more
memory, more context, more automation. AKC asks the inverse question:
given that the human in the loop has a fixed daily budget of attention
and judgment, how should the cycle be shaped so that budget is not
squandered?

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
correctness check and still drift from intent. The behavior-level
distinction is [intent alignment](https://ai-alignment.com/clarifying-ai-alignment-cec47cd69dd6)
(Christiano, 2018) — an agent trying to do what its operator wants it
to do — which AKC extends across time and down into the artifacts
that shape behavior.

AKC's design choices reflect this. Design Principle #3 (Non-destructive)
— propose, then wait for confirmation — keeps every change at a
checkpoint where intent can be re-stated. Pre-implementation dialogue
is treated as a cognitive-economy investment, not as friction. The
distinction also explains how AKC differs from harness engineering:
harnesses optimize correctness on the first try, while AKC keeps the
harnesses themselves aligned with intent as that intent evolves — the
activity AKC names **harness alignment**
([ADR-0017](docs/adr/0017-harness-alignment-and-drift.md)). See
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

## The cycle

AKC is a set of six composable skills, one per phase of the cycle:

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
| Promote | Elevate recurring patterns to the rule layer |
| Measure | Verify behavioral change quantitatively, not subjectively |
| Maintain | Keep documentation roles clean and content fresh |

### Skills vs Rules

- **Skills** provide deep, step-by-step workflows for each phase. Install them when you want guided execution.
- **Rules** provide principles and trigger conditions. Install them when you want the cycle to emerge naturally from conversation.
- Both can coexist. Rules ensure the cycle runs even when skills aren't triggered.

## What's in this repo

Fifteen ADRs, nine design principles, three design-pattern skills, two
JSON schemas, one ~500-line runnable reference implementation, and the
rules file that installs the whole cycle in a single `cp`. AKC defines
three memory layers and four code-LLM layering patterns. The six cycle
skills listed above remain the opinionated, full-fat implementation of
each phase.

AKC ships **two kinds of skills**:

- **Cycle skills** (external repositories) — one per phase of the
  cycle: `search-first`, `learn-eval`, `skill-stocktake`,
  `rules-distill`, `skill-comply`, `context-sync`.
- **Design-pattern skills** ([`docs/skills/`](docs/skills/)) — long-form
  "how" guides paired 1:1 with ADRs. These are cross-cutting and apply
  in multiple phases.

For the full repository tree and document-role routing, see [`docs/CODEMAPS/architecture.md`](docs/CODEMAPS/architecture.md).

## Design Principles

1. **Composable** — Each skill works independently. Use one or all six.
2. **Observable** — skill-comply produces quantitative compliance rates, not subjective assessments. A compliance instrument must observe the agent's *reasoning* — verdicts and plans stated in text — not only its tool calls, or the thinking-centric phases (Research, Curate) are systematically under-reported. See [ADR-0016](docs/adr/0016-measuring-thinking-centric-phases.md).
3. **Non-destructive** — Every skill proposes changes and waits for confirmation. Nothing is auto-applied.
4. **Tool-agnostic in concept** — Designed for Claude Code but the architecture applies to any agent with persistent configuration.
5. **Evaluation scales with model capability** — Small models benefit from rubric-based scoring; reasoning models (Opus-class) evaluate with full context and qualitative judgment. AKC does not prescribe one approach — it matches evaluation depth to the model's reasoning capacity.
6. **Scaffold dissolution** — Skills are scaffolding. As the user and agent internalize the cycle, skills become unnecessary and rules alone sustain the loop. See [docs/scaffold-dissolution.md](docs/scaffold-dissolution.md).
7. **Code-LLM Layering** — Code owns determinism, auditability, and control flow. LLMs own meaning. Layer them explicitly; never let the LLM own durable state or termination. See [ADR-0008](docs/adr/0008-code-and-llm-collaboration.md).
8. **Human cognitive resource is the bottleneck** — As agent capability grows, the scarce resource is no longer compute or context but human attention and judgment. Every phase is shaped to protect that budget — see [Why AKC → The bottleneck has moved](#the-bottleneck-has-moved) and [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md).
9. **Genre neutrality** — The cycle is a mechanism, not content. The same six phases operate on any coherent body of agent knowledge — behavioral patterns, domain expertise, or constitutional values — and AKC takes no position on which a downstream project cares about. What changes per genre is the evaluation criteria, prompt templates, and audit queries; the phases stay identical. See [ADR-0011](docs/adr/0011-cycle-applies-to-any-knowledge-body.md).

## Limitations

The third theme — *the cycle changes the human too* — has an honest
twin: a loop that can sharpen judgment can also erode it. Three
mechanism-level failure modes run the bidirectional loop backward:
**gate complacency** (a stream of usually-correct proposals trains the
operator to approve by reflex), **deskilling** (a human who only
reviews the agent's output lets the faculty supervision requires
atrophy), and **delegation-feedback divergence** (the agent keeps
acting while the feedback that would correct it no longer reaches a
human positioned to use it). AKC's defense is structural, not
exhortation: the human approval gate
([ADR-0005](docs/adr/0005-human-approval-gate.md)) is a
circuit-breaker with no auto-approve path, and Curate and Promote are
active judgment acts — the cycle's normal operation is itself the
exercise that resists deskilling. The full analysis is in
[ADR-0014](docs/adr/0014-failure-modes-of-the-bidirectional-loop.md).

## Relationship to Harness Engineering

AKC shares common ground with [harness engineering](https://mitchellh.com/writing/my-ai-adoption-journey) (Mitchell Hashimoto, 2025) — the practice of engineering solutions so that an agent never repeats the same mistake, through a combination of improved prompts and programmatic tools. Both aim to make agents more reliable. They differ in what they focus on.

| Layer | Question | Addressed by |
|-------|----------|-------------|
| Harness | "Is this output correct?" | Individual linters, tests, scripts |
| AKC | "Are the harnesses themselves still valid?" | skill-comply, skill-stocktake, context-sync |

Harness engineering optimizes correctness on the first try, and is
reactive by nature — each mistake triggers a new harness; AKC audits
proactively and asks the intent question instead (see
[Why AKC → Aligned with intent](#aligned-with-intent-not-just-correct)).
The harness layer now also has its own automated improvement loop:
[Meta-Harness](https://arxiv.org/abs/2603.28052) searches over harness
code to maximize benchmark scores — autonomous, score-driven **harness
optimization** on the correctness axis. AKC's activity is the
human-gated counterpart on the intent axis: **harness alignment**,
keeping the harness aligned with the operator's evolving intent. Its
failure mode is **harness drift** — skills go stale, rules stop
matching practice, documentation diverges from code. The two
activities are complementary, not competing: a harness can score
better on a fixed benchmark while sliding away from what its operator
now wants. See [ADR-0017](docs/adr/0017-harness-alignment-and-drift.md)
for the full derivation and the drift-vocabulary lineage.

Where the dominant pattern in self-evolving-agent work and
platform-side memory features lets the agent itself decide what to
persist, AKC inverts the default: cross-layer promotion (from the
probabilistic skills/memory layer to the deterministic rules layer)
requires a *named human sign-off*. The gate is not a missing
automation feature — it is the load-bearing contribution, the edge
where the operator's evolving intent enters the loop. See the
[ADR-0005 addendum](docs/adr/0005-human-approval-gate.md).

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
  version      = {2.2.0},
  doi          = {10.5281/zenodo.20565806},
  url          = {https://doi.org/10.5281/zenodo.20565806},
  note         = {A knowledge cycle for AI agents — one that grows with the people who shape it}
}
```

Or in text:

> Shimomoto, T. (2026). Agent Knowledge Cycle (AKC). doi:10.5281/zenodo.20565806

## Related Work

- [Contemplative Agent](https://github.com/shimo4228/contemplative-agent) — An
  independent research repository exploring Contemplative Constitutional AI
  on a local 9B model. The relationship runs in both directions. Upstream,
  its engineering substrate (three-layer memory, two-stage distillation) was
  the prior art that seeded AKC's ADRs — see
  [`docs/inspiration.md`](docs/inspiration.md). Downstream, it is the
  operational re-implementation of AKC in the autonomous-agent context: its
  pipeline maps the six phases onto code, the agent runs the cycle over its
  own episode logs with no fine-tuning, and every promotion passes through
  a human approval gate. The demonstration is ongoing.
- [Agent Attribution Practice (AAP)](https://github.com/shimo4228/agent-attribution-practice) —
  Sibling genre library (DOI [10.5281/zenodo.19652013](https://doi.org/10.5281/zenodo.19652013)).
  AKC v2.0.0's extracted security triplet (ADR-0001, ADR-0006, ADR-0007) was
  re-expressed there, alongside seven additional ADRs, as ten harness-neutral
  ADRs on accountability distribution in autonomous AI agents. AKC is the
  cycle (mechanism); AAP is the practice (content).
- [Articles on Zenn](https://zenn.dev/shimo4228) — Development journal (Japanese)
- [Articles on Dev.to](https://dev.to/shimo4228) — English translations

Four more DOI-registered repositories crystallized out of the same daily
operation the cycle runs in — recorded here as relationship facts and
DOIs only ([ADR-0018](docs/adr/0018-record-downstream-applications-as-first-class-context.md)):

- [Authorship Strategy](https://github.com/shimo4228/authorship-strategy) (DOI [10.5281/zenodo.20263316](https://doi.org/10.5281/zenodo.20263316)) — AKC defines how knowledge cycles inside the operator-agent pair; Authorship Strategy addresses how the cycle's outputs diffuse outside it.
- [Attention, Not Self](https://github.com/shimo4228/attention-not-self) (DOI [10.5281/zenodo.20262112](https://doi.org/10.5281/zenodo.20262112)) — sibling research line, federated at the research-program level.
- [doctrine-corpus](https://github.com/shimo4228/doctrine-corpus) (DOI [10.5281/zenodo.20337008](https://doi.org/10.5281/zenodo.20337008)) — bilingual judgment-eliciting Q&A corpus; AKC is one of its four source lines.
- [existence-proof](https://github.com/shimo4228/existence-proof) (DOI [10.5281/zenodo.20558800](https://doi.org/10.5281/zenodo.20558800)) — pre-line working repository complementing Authorship Strategy.

The canonical relationship map of the whole research program lives in the
[hub repository's graph.jsonld](https://github.com/shimo4228/shimo4228/blob/main/graph.jsonld).

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

AKC was built from practice, not theory — the six-phase shape was
noticed in the daily maintenance of a real harness, not derived from a
literature. That stance does not exempt the project from naming the
work it overlaps. The full positioning is recorded in
[ADR-0013](docs/adr/0013-positioning-within-agent-memory-literature.md).

### Agent-memory literature — conceded overlap, located delta

Run as an isolated operation — "induce a skill from this session,"
"prune stale memories," "reflect these episodes into a pattern" — an
AKC phase is *not* a new mechanism. The precedents are named: skill
induction in Voyager (Wang et al., 2023) and Agent Workflow Memory
(Wang et al., 2024); memory curation in ReMe (Cao et al., 2025) and
LangMem (LangChain, 2025); reflection and memory hierarchies in
Generative Agents (Park et al., 2023) and MemGPT (Packer et al., 2023);
framework vocabulary in CoALA (Sumers et al., 2023) and
*Externalization in LLM Agents* (Zhou et al., 2026). AKC's delta lives
on the shared axis those systems define — *how an agent turns its own
experience into durable, reusable knowledge* — and it is the three core
themes restated as a literature delta:

1. **A structural human approval gate**, where the prior art closes the
   loop autonomously ([ADR-0005](docs/adr/0005-human-approval-gate.md)).
2. **Bidirectional human-judgment growth as the target**, where the
   prior art optimizes the agent or its context ([ADR-0009](docs/adr/0009-akc-is-a-cycle-not-a-harness.md)).
3. **Human attention as the scarce resource**, where the prior art
   treats context, memory consistency, or task capability as binding
   ([ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md)).

These systems were identified as prior art *for positioning*, not
consulted during AKC's construction; the distinction is preserved from
the practice-first stance above.

### Software-evolution and alignment literature — vocabulary lineage

AKC's vocabulary for its own activity — **harness alignment** and its
failure mode **harness drift** — is derived from established terms
rather than coined fresh: intent alignment from
[Christiano (2018)](https://ai-alignment.com/clarifying-ai-alignment-cec47cd69dd6),
software evolution as feedback from [Lehman (1980)](https://users.ece.utexas.edu/~perry/education/SE-Intro/lehman.pdf),
architectural drift from [Perry & Wolf (1992)](https://users.ece.utexas.edu/~perry/work/papers/swa-sen.pdf),
practical drift from Snook (2000, *Friendly Fire*; as characterized in
secondary literature), harness and harness optimization from
[Meta-Harness](https://arxiv.org/abs/2603.28052) (Lee et al.), and
behavioral drift in LLM agents from [Agent Drift](https://arxiv.org/abs/2601.04170)
(Rath). AKC's delta is only what no single source covers: an alignment
target that is operator intent and itself evolves, a human-gated loop,
and a loop that changes the human too. Unlike the agent-memory
positioning above, these sources were consulted *for the vocabulary
derivation itself* (2026-06-06). The full derivation is recorded in
[ADR-0017](docs/adr/0017-harness-alignment-and-drift.md).

### Philosophical resonances — not consulted during construction

The following works were genuinely *not* consulted during the process
described above, but the resulting cycle seems to share something with
the ideas in them. They are listed for readers who might find the
resonance interesting.

- [Mind in Life](https://www.hup.harvard.edu/books/9780674057517) (Evan Thompson, 2007) —
  The bidirectional loop between human and agent has something in common
  with the enactivist idea of structural coupling.
- [A Beautiful Loop: An Active Inference Theory of Consciousness](https://www.sciencedirect.com/science/article/pii/S0149763425002970)
  (Laukkonen, Friston, & Chandaria, 2025) — The way the human updates
  rules and skills by observing what the agent actually does feels
  vaguely like a recursive self-modeling loop.

## License

MIT
