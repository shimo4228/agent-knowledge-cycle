Language: English | [日本語](README.ja.md)

# Agent Knowledge Cycle (AKC)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19200726.svg)](https://doi.org/10.5281/zenodo.19200726)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/shimo4228/agent-knowledge-cycle)
[![GitMCP](https://img.shields.io/endpoint?url=https://gitmcp.io/badge/shimo4228/agent-knowledge-cycle)](https://gitmcp.io/shimo4228/agent-knowledge-cycle)

**A knowledge cycle for AI agents — one that grows with the people who shape it.**

Agent Knowledge Cycle (AKC) is a six-phase growth cycle for persistent AI
agents. It turns repeated agent experience into reusable knowledge — skills,
rules, and documentation — under human approval, keeping the agent aligned with
the operator's evolving intent while spending the scarce resource — human
attention and judgment — only where it matters. The cycle changes the human
too: operating it sharpens the judgment that steers it. Built for people who
operate coding agents or persistent AI harnesses day to day, it runs inside
Claude Code or any comparable harness.

Companion paper: *Harness Alignment and Harness Drift: Why Intent, Unlike
Correctness, Resists Automation* — doi:[10.5281/zenodo.20578272](https://doi.org/10.5281/zenodo.20578272)

## Why AKC

**The bottleneck has moved.** Most agent frameworks optimize the agent side:
more tools, memory, context, or automation. AKC starts from the inverse
constraint: as agent capability grows, the scarce resource is the human
attention and judgment required to steer the loop
([ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md)).
Skills go stale, rules accumulate residency cost, and documentation drifts —
every phase of the cycle exists to keep that maintenance from consuming the
operator's fixed budget.

**Intent alignment, not just correctness.** Tests and linters can check whether
one output passes a specification; they cannot check whether a changing harness
still matches what the operator now means, because intent itself moves as the
operator's judgment sharpens through use. AKC calls the configuration-layer
version of this activity **harness alignment** and its failure mode **harness
drift** — the derivation is in
[ADR-0017](docs/adr/0017-harness-alignment-and-drift.md) and the companion paper.

**The cycle changes the human too.** Curate and Promote force the operator to
decide what knowledge is worth retaining; Measure then tests whether those
decisions changed behavior. Over time the agent becomes more coherent and the
human becomes better at judging coherence — the cycle grows *with* the people
who shape it, not merely *for* them.

## The cycle

AKC turns experience into durable behavior through six phases: Research filters
intake, Extract captures reusable patterns, Curate audits what accumulated,
Promote moves selected patterns into behavior-shaping rules, Measure checks
whether behavior changed, and Maintain keeps documents and artifacts coherent.

```mermaid
flowchart TD
  E[Experience] --> R[Research<br/>signal-first intake]
  R --> X[Extract<br/>reusable pattern]
  X --> C[Curate<br/>structural + semantic audit]
  C --> P[Promote<br/>human-gated rule or skill change]
  P --> M[Measure<br/>observable behavior]
  M --> T[Maintain<br/>docs and artifact hygiene]
  T --> E
```

| Phase | Current external skill | Purpose |
|---|---|---|
| Research | [search-first](https://github.com/shimo4228/search-first) | Search broadly, intake only signal that can change the next action |
| Extract | [learn-eval](https://github.com/shimo4228/learn-eval) | Extract reusable session patterns with quality gates |
| Curate | [skill-health](https://github.com/shimo4228/skill-health) + [skill-stocktake](https://github.com/shimo4228/skill-stocktake) + [rules-stocktake](https://github.com/shimo4228/rules-stocktake) | Run structural debt checks before semantic review of skills and always-loaded rules |
| Promote | [rules-distill](https://github.com/shimo4228/rules-distill) | Turn recurring patterns into durable rules |
| Measure | [skill-comply](https://github.com/shimo4228/skill-comply) | Test whether agents actually follow skills and rules |
| Maintain | [context-sync](https://github.com/shimo4228/context-sync) | Keep documentation roles clean and facts fresh |

Three design-pattern skills — [when-code-when-llm](https://github.com/shimo4228/when-code-when-llm),
[code-and-llm-collaboration](https://github.com/shimo4228/code-and-llm-collaboration),
[signal-first-research](https://github.com/shimo4228/signal-first-research) —
carry the cycle's reusable design judgments. The phase set and phase-to-skill
bindings are a mutable snapshot, not AKC's fixed essence
([ADR-0019](docs/adr/0019-cycle-structure-is-provisional.md)).

## Install

The lightest install is the standalone
[**shimo4228/akc-cycle**](https://github.com/shimo4228/akc-cycle) rules file —
it gives an AI agent the six-phase behavior without installing any phase skills:

```bash
# From a clone of github.com/shimo4228/akc-cycle, copy the rule
# into your agent's rules directory.
cp rules/common/akc-cycle.md ~/.claude/rules/common/akc-cycle.md
```

Adopt in stages: the rules file alone lets the cycle emerge in ordinary
conversation; add the phase skills above when you want guided, step-by-step
execution; fork any of it — AKC defines the cycle, not the implementation.
Skills are scaffolding meant to dissolve once the cycle is internalized
([docs/scaffold-dissolution.md](docs/scaffold-dissolution.md)).

## What's in this repo

| Area | Contents |
|---|---|
| Decision record | ADR catalog in [`docs/adr/`](docs/adr/), with permanent gaps at 0001, 0006, and 0007 from the v2.0.0 extraction |
| AI navigation | [`graph.jsonld`](graph.jsonld) for the concept map, [`llms.txt`](llms.txt) for routing, [`llms-full.txt`](llms-full.txt) for a self-contained factual reference (includes the nine design principles) |
| Specifications | [`schemas/episode-log.schema.json`](schemas/episode-log.schema.json), [`schemas/knowledge.schema.json`](schemas/knowledge.schema.json) |
| Reference implementation | [`examples/minimal_harness/`](examples/minimal_harness/), a dependency-free Python demo of the three memory layers and two-stage distill pipeline |
| Routing map | [`docs/CODEMAPS/architecture.md`](docs/CODEMAPS/architecture.md), the canonical file-level navigation index |

## Limitations

The bidirectional loop can fail on the human side —
[ADR-0014](docs/adr/0014-failure-modes-of-the-bidirectional-loop.md) names gate
complacency, deskilling, and delegation-feedback divergence — and on the
artifact side as harness drift. The two can compound, which is why AKC treats
maintenance as a cycle rather than a one-time configuration. AKC makes these
risks explicit and keeps the human approval gate as the structural defense; it
does not claim to eliminate them.

## Positioning

Harness engineering improves the scaffold so outputs are correct on the first
try; AKC keeps the scaffold aligned with what the operator means as that intent
evolves ([ADR-0009](docs/adr/0009-akc-is-a-cycle-not-a-harness.md),
[ADR-0017](docs/adr/0017-harness-alignment-and-drift.md)). AKC's individual
operations overlap prior agent-memory work such as Voyager, Agent Workflow
Memory, ReMe, and MemGPT; its delta is loop ownership — a structural human
approval gate ([ADR-0005](docs/adr/0005-human-approval-gate.md)), bidirectional
judgment growth, and attention-side scarcity. The full citation trail is in
[ADR-0013](docs/adr/0013-positioning-within-agent-memory-literature.md),
ADR-0017, and [`llms-full.txt`](llms-full.txt).

## Origin & Acknowledgments

This architecture was first proposed and implemented by Tatsuya Shimomoto
([@shimo4228](https://github.com/shimo4228), ORCID
[0009-0002-6168-4162](https://orcid.org/0009-0002-6168-4162)) in
February 2026, building on
[Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code)
by [@affaan-m](https://github.com/affaan-m), the baseline harness used in daily
practice. AKC emerged when the author's own added skills and rules grew large
enough that stale skills, contradictory rules, and drifting documentation became
their own maintenance problem. The first five cycle skills were contributed to
ECC between February and March 2026; `context-sync` was developed independently.

## How to Cite

AKC carries two DOIs: the concept DOI
[10.5281/zenodo.19200726](https://doi.org/10.5281/zenodo.19200726) (used by the
badge) always resolves to the latest version, while each archived release has
its own DOI — cite the release DOI below.

If you use or reference AKC, cite the archived release metadata in
[`CITATION.cff`](CITATION.cff), also available as
[`codemeta.json`](codemeta.json):

```bibtex
@software{shimomoto2026akc,
  author       = {Shimomoto, Tatsuya},
  title        = {Agent Knowledge Cycle (AKC)},
  year         = {2026},
  version      = {2.4.0},
  doi          = {10.5281/zenodo.21067957},
  url          = {https://doi.org/10.5281/zenodo.21067957},
  note         = {A knowledge cycle for AI agents -- one that grows with the people who shape it}
}
```

In text: Shimomoto, T. (2026). *Agent Knowledge Cycle (AKC)*.
doi:[10.5281/zenodo.21067957](https://doi.org/10.5281/zenodo.21067957).

## Related Work

The research-ecosystem hub is
[`shimo4228/shimo4228`](https://github.com/shimo4228/shimo4228); it carries the
canonical relationship map for the broader set of research lines.

| Repository | Relationship to AKC |
|---|---|
| [Contemplative Agent](https://github.com/shimo4228/contemplative-agent) | Upstream engineering substrate for AKC's early ADRs and downstream operational re-implementation of the six-phase cycle |
| [Agent Attribution Practice](https://github.com/shimo4228/agent-attribution-practice) | Sibling genre library; AKC = cycle mechanism, AAP = attribution practice content |
| [Authorship Strategy](https://github.com/shimo4228/authorship-strategy) | Downstream research line on how outputs diffuse outside the operator-agent pair |
| [Attention, Not Self](https://github.com/shimo4228/attention-not-self) | Sibling research line federated at the ecosystem level |
| [doctrine-corpus](https://github.com/shimo4228/doctrine-corpus) | Bilingual judgment-eliciting Q&A corpus that includes AKC as one source line |
| [existence-proof](https://github.com/shimo4228/existence-proof) | Pre-line working repository complementing Authorship Strategy |

Japanese development notes are on [Zenn](https://zenn.dev/shimo4228); English
translations are on [Dev.to](https://dev.to/shimo4228).

## License

MIT
