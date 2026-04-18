# ADR-0010: Human Cognitive Resource as Central Constraint

> **Summary.** AKC is centered on the scarcity of *human* cognitive resources — not agent capability, not context window size, not information volume. The Research phase is redefined as **signal-first**: filter at the intake, before accumulation. Dialogue is front-loaded because intent misalignment at implementation time costs more than the conversation it would have taken to prevent it. This is the implicit design philosophy that has been shaping every AKC phase since inception; ADR-0010 makes it explicit.

## Status
accepted

## Date
2026-04-18

## Context

From v1.0 through v1.7, AKC's six phases shared an implicit center of gravity that was never stated in its own document. Every phase — Research, Extract, Curate, Promote, Measure, Maintain — is designed to protect the cognitive throughput of the person running the cycle. But nowhere in the repository was that stated. Readers could reasonably conclude that AKC optimized for agent capability, knowledge coverage, or information retention. None of those is the actual target.

Three pressures forced the surfacing.

**Pressure 1: the LLM-Wiki wave.** Through early 2026, a cluster of projects — Karpathy's LLM Wiki, claude-obsidian, MemPalace — popularized the pattern of letting LLMs write structured knowledge bases that humans then read. These systems solve the symptom of "too much information" by outsourcing digestion to the LLM. The apparent overlap with AKC's Curate and Promote phases invited confusion: is AKC just a smaller, more opinionated LLM Wiki? The answer is no, but the reason requires a philosophical statement the repository did not yet contain. LLM Wikis optimize for information capture and human searchability. AKC optimizes for what the human does *not* have to read, hold, or re-decide.

**Pressure 2: the origin story of daily research.** The author's `daily research` workflow — one narrowly-scoped report per day, filtered for personal relevance — was conceived after hearing about a high-capacity knowledge worker's practice of processing roughly one hundred deep-research reports per day. The author's reaction was an honest admission: *I cannot digest that volume.* Rather than treating this as a deficit to overcome, the author treated it as a design constraint to accept. The resulting workflow is not a degraded version of the high-capacity practice; it is a different architecture, one that makes cognitive throughput — not information throughput — the primary metric. That architectural choice has sat inside AKC's Research phase as a silent default. This ADR names it.

**Pressure 3: why dialogue is front-loaded.** Running Claude Code at scale reveals a recurring pattern: implementation started without sufficient intent-alignment produces work that does not match the user's intent, which then requires a second and sometimes third cycle of discovery and correction. Each correction consumes human attention on the activity humans are worst at — reconstructing what went wrong after the fact. Pre-implementation dialogue looks expensive because it slows the start; it is actually cheap because it prevents the more expensive downstream cost. AKC's design principle #3 (Non-destructive) and its preference for ADR-style decision capture both reflect this, but neither states the underlying economics. ADR-0010 states it.

The common root: **cognitive resources are scarce on the human side and become relatively scarcer as agent capability grows.** Every competing framework optimizes the agent side (more tools, more memory, more context, more automation). AKC asks the inverse question: given that the human in the loop has a fixed daily budget of attention and judgment, how should the cycle be shaped so that budget is not squandered?

## Decision

AKC elevates human cognitive resource scarcity to an explicit central constraint. Three concrete changes implement this:

### 1. Signal-first Research

The Research phase is redefined. Before v1.8, the rule was "Search for existing libraries, tools, and patterns that solve the same problem." That was always correct but one-sided — it told the agent what to *find*, not what to *refuse to load*.

The new definition adds an intake filter:

> Before searching, define the signal — what information would actually change your next action? During search, broaden generously; during intake, narrow strictly. Information that does not change an action does not deserve to be held.

This is not anti-exploration. Exploration phases are explicitly permitted. The default stance is signal-first; the stance can be relaxed on purpose when the task is learning, not building.

Daily-report workflows that pre-filter feeds for relevance are now a canonical example of the Research phase. They were previously personal practice; ADR-0010 recognizes them as one valid instantiation of the phase.

### 2. Cognitive economy as Design Principle #9

A new design principle is added to the README:

> **Human cognitive resource is the bottleneck.** As agent capability grows, the scarce resource is no longer compute or context but human attention and judgment. AKC's phases are shaped to protect that budget: signal-first intake, pre-implementation dialogue, promotion of recurring decisions to rules so the same judgment is not re-made, and compliance measurement so the human does not re-audit each session manually.

This sits alongside the existing principles (Composable, Observable, Non-destructive, Tool-agnostic, Evaluation scales with model capability, Scaffold dissolution, Security by Absence, Code-LLM Layering).

### 3. Dialogue as investment, not friction

The README's "Why a cycle?" section is extended with one paragraph stating that pre-implementation dialogue is a cognitive-economy investment. This is not a new mechanism; it is an explicit naming of what the cycle already does. ADR-0009's "Non-destructive" principle — propose, then wait — is reframed as a specific case of this more general economics.

### What does not change

- The six phases. Research → Extract → Curate → Promote → Measure → Maintain remain unchanged in number and order.
- ADR-0001 through ADR-0009. All prior decisions remain in effect.
- The reference implementation in `examples/minimal_harness/`. No code changes.
- Tagline. "A knowledge cycle for AI agents — one that grows with the people who shape it" continues to carry the repositioning from ADR-0009. ADR-0010 adds depth, not a new tagline.

## Alternatives Considered

- **Keep the philosophy implicit.** Rejected. The LLM-Wiki wave made the distinction impossible to communicate without stating the center of gravity. Readers were defaulting to the assumption that AKC is about information organization, which is not AKC's target.
- **Update the tagline to name cognitive economy directly.** Rejected. ADR-0009's tagline ("grows with the people who shape it") is only months old and is still being absorbed by readers. Replacing it would dilute bidirectional growth just as that framing starts to stick. Additive depth via ADR-0010 + Design Principle #9 + Research redefinition preserves the ADR-0009 axis while layering cognitive economy on top.
- **Split into two ADRs — signal-first Research and cognitive economy principle.** Rejected. The two are aspects of the same claim. Splitting would invite readers to adopt one without the other; the principle is the reason the phase is redefined, and the phase is the most concrete instance of the principle.
- **Build a filtering tool (daily-report generator) into the repository.** Rejected. AKC defines the cycle, not the implementation. One instantiation (daily report) is mentioned as an example; users with different cognitive profiles will build different filters. The repository stays at the principle layer.
- **Frame this as responding to LLM-Wiki specifically.** Rejected. Naming a specific wave dates the ADR. The underlying observation — that scarcity migrates from machine to human as machines get stronger — is a long-range claim, not a response to one trend.

## Consequences

### Positive

- The LLM-Wiki / MemPalace / obsidian-knowledge-base class of systems is now clearly situated relative to AKC: they solve information-side scarcity (the human can't find or digest what exists), AKC solves attention-side scarcity (the human's fixed judgment budget is the ceiling). Both are valid, they target different resources, and they can coexist.
- Signal-first Research gives agents and users a principled answer to "how much should I read before acting." The default is: enough to change the next action, no more. This shifts Research from a volume metric to a signal metric.
- The origin story of daily research — accepting one's own cognitive limits as a design input — becomes part of the architecture's self-understanding. Future readers can see that AKC is not neutral about cognitive load; it is explicitly designed around it.
- Dialogue-heavy workflows (front-loaded alignment, ADR capture, human approval gates) now have a single economic explanation rather than being justified phase-by-phase.

### Negative

- "Filter strictly" is easy to over-apply. A reader might conclude that all broad reading is waste. It is not — exploration, learning, and wandering are cognitively useful. The rule file mitigates this by stating that signal-first is the default, not a ban on breadth.
- Stating the principle as "human cognitive resource is the bottleneck" is true today but may need revision if cognitive-augmentation tools substantially shift the ceiling. This ADR is a contemporary claim about 2026-era human-agent work, not an eternal law. Future ADRs can amend it.
- Centering the human cognitive budget opens the question of whose cognitive budget — the primary operator, collaborators, or downstream readers of the repository. ADR-0010 is written from the primary operator's perspective; multi-operator generalization is left for future work.

### Neutral

- No code changes. Schemas, reference implementation, and cycle skills are untouched.
- CITATION.cff and llms.txt are updated to reflect the new principle and the new ADR. Version bumps to v1.8.0.

## geo-writer snapshot (Measure phase self-application)

The README is measured with `geo-writer` before and after this change. Both snapshots are retained in version control as an example of the Measure phase being applied to AKC's own documentation.

Measurements run with `~/.claude/skills/geo-writer` on README.md, commit boundary 2026-04-18.

| Check | v1.7.0 (before) | v1.8.0 (after) | Δ |
|-------|-----------------|----------------|---|
| Skyramp (front-30% entity share) | 0.0 (share 28.3%) FAIL | 0.0 (share 29.7%) FAIL | front share +1.4pt |
| Chunk self-contained | 0.467 (7/15) FAIL | 0.467 (7/15) FAIL | no change |
| Question heading ratio (H2 only) | 0.143 (2/14) FAIL | 0.143 (2/14) FAIL | no change |
| Entity density | 0.166 OK | 0.157 OK | -0.009 (remains above 0.15 target) |
| Definition density | 0.0 FAIL | 0.0 FAIL | no change |
| Word count | 1584 | 1786 | +202 (new cognitive-economy content) |

**Interpretation.** The v1.8.0 additions are cognitive-economy content concentrated in "Why a cycle?" (new H3 subsection) and Design Principles (new principle #9). No regressions: entity density remains OK; all FAILs were pre-existing structural issues in the README (skyramp, chunk length, question-heading ratio, definition density). A dedicated GEO-focused README refactor is a separate concern and out of scope for this ADR.

The new H3 "Whose cognitive budget is the cycle protecting?" *is* a question heading, but the geo-writer script only counts H2 headings for that metric. This is consistent with GEO research on top-level heading prominence and not a bug to fix here.

This snapshot is the first application of the Measure phase to AKC's own documentation. Future releases can reuse the same script and compare diffs in successive ADRs to track the README's GEO trajectory over time.

## Relationship to other ADRs

- **ADR-0009 AKC is a Cycle, Not a Harness** — ADR-0010 builds on ADR-0009. "Grows with the people who shape it" described the *direction* of the cycle (bidirectional); ADR-0010 describes the *economics* that make the direction possible (the human budget is the scarce input).
- **ADR-0005 Human Approval Gate** — the gate exists because human approval is cognitively expensive and must not be wasted on low-value decisions. ADR-0010 gives that design the underlying economics.
- **ADR-0008 Code and LLM Collaboration** — code owns determinism so the human does not hold it; LLMs own meaning so the human does not re-derive it. Both are cognitive-economy moves.

---

**Notes.** This ADR grew out of a conversation triggered by a `daily research` report on the 2026-04 LLM-Wiki pattern (Karpathy, claude-obsidian, MemPalace). The report asked whether those systems were an upgrade path for AKC's Curate and Promote phases. The answer was no — but finding the reason required articulating the central constraint that AKC had been honoring without naming. ADR-0010 is the naming.
