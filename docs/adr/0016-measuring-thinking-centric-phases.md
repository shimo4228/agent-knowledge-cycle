# ADR-0016: Measuring Thinking-Centric Phases

> **Summary.** The Measure phase promises "quantitative compliance rates," but a compliance instrument that only observes tool calls systematically under-reports the phases whose load-bearing behavior lives in agent text. Research and Curate are thinking-centric: their compliance is carried by reasoning, verdicts, and plans the agent writes, not by side effects it produces. A tool-call-only instrument scores these phases low even when the agent did everything right. ADR-0016 records the falsifiable claim — *a Measure instrument that ignores agent text systematically under-reports judgment-phase compliance* — and the corrective: a Measure instrument must promote agent text to observable events before scoring. The claim connects directly to Theme 2 (intent alignment lives in reasoning; correctness lives in tool calls).

## Status
accepted

## Date
2026-06-06

## Context

The Measure phase (`docs/akc-cycle.md`, "Measure — Verify behavioral change quantitatively") tells the operator to *"check whether the behavior actually occurs (tool call sequences, outputs, test results)"* and rejects subjective assessment. README Design Principle #2 (Observable) states the goal in stronger terms: the Measure phase produces *"quantitative compliance rates, not subjective assessments."* llms-full.txt repeats the framing: Measure verifies behavioral change *"through observable tool-call sequences and outputs."*

That definition contains a silent assumption: that the observable surface of agent behavior is the set of tool calls it emits. For some phases this is true. The Promote phase ends in a rule write; the Maintain phase ends in a documentation edit; a TDD workflow ends in test files and a passing run. Those are physical actions — they leave file-system and process artifacts that a tool-call trace captures directly.

But two of the six phases are **thinking-centric**. Research is signal-first (ADR-0010): its load-bearing act is the decision about what information would change the next action — a judgment the agent states in text before any search tool fires, and a verdict ("Adopt this library" / "Build instead") it states in text after. Curate is an audit: its load-bearing act is the reasoning about whether a skill is redundant, stale, or silent — again a judgment that lives in prose, with the tool call (a deletion, a consolidation) following only when the judgment concludes "remove." For these phases, the tool calls are downstream consequences of a judgment, not the judgment itself. An instrument that scores only the tool calls scores the shadow, not the object.

This is not a hypothetical gap. The empirical trigger is the `claude-skill-comply` compliance tool — the reference Measure instrument the README cites for "quantitative compliance rates." Its v0.1.0 release scored thinking-centric skills far below their actual compliance because its stream-json parser captured only `tool_use` content blocks and silently discarded every `text` block — the agent's reasoning, verdicts, and plans. On a research-before-code workflow the agent could run the full correct sequence — scout agent, web searches, fetches, adopt-and-implement — and still score near zero, because the verdict that proved the workflow ran was a text block the parser threw away. Physical-action skills (a TDD/testing workflow) were under-reported far less, because their compliance was already mostly tool-call-shaped. The v0.2.0 text-observability fix corrected this by promoting assistant `text` blocks to pseudo-observation events before classification; the measured lift on the research-before-code target was large (see the `[0.2.0]` entry of the [`claude-skill-comply` CHANGELOG](https://github.com/shimo4228/claude-skill-comply/blob/main/CHANGELOG.md)). The numbers are not reproduced here — they belong to that repository's release record, and the mechanism-only inclusion rule (CLAUDE.md) keeps genre- and tool-specific measurement tables out of AKC's core. What AKC records is the structural lesson the fix surfaced, not the tool's version history.

The lesson generalizes beyond one parser bug. Any Measure instrument inherits the same failure mode if it equates "observable behavior" with "tool calls": it will report high compliance for phases that end in physical actions and low compliance for phases that end in judgments, and an operator reading those numbers will conclude — wrongly — that the agent ignores Research and Curate while honoring Promote and Maintain. The instrument's blind spot becomes the operator's false belief. Because the Measure phase exists precisely so the human does not have to re-audit each session by hand, a systematically biased instrument is worse than no instrument: it spends the operator's scarce attention (ADR-0010) on a number that points the wrong way.

## Decision

AKC adopts an observability requirement on the Measure phase:

> A Measure instrument must promote agent text — reasoning, verdicts, and plans — to observable events before scoring compliance. Compliance that is carried by what the agent *states* is not measurable by an instrument that records only what the agent *does* with tools.

The decision is framed as a **falsifiable claim**:

> A Measure instrument that ignores agent text systematically under-reports judgment-phase compliance.

The claim is falsifiable in the strong direction: if a tool-call-only instrument produced compliance rates for Research and Curate that matched a text-aware instrument's rates on the same traces, the claim would be refuted. The `claude-skill-comply` v0.1.0 → v0.2.0 transition is one observation consistent with the claim — a research-before-code skill's measured compliance moved substantially once text blocks were admitted, while a physical-action skill's compliance moved far less — but the claim stands or falls on the general pattern, not on one tool's release.

Three consequences follow for any AKC Measure instrument:

1. **Text is a first-class observable.** The instrument's trace parser must capture assistant text alongside tool calls. Discarding text is not a neutral simplification; it is a measurement bias that favors physical-action phases over thinking-centric ones.

2. **Spec steps may be text-observable.** A behavioral spec for a thinking-centric phase will contain steps whose evidence is a verdict or a plan, not a tool call (e.g., "state whether to adopt or build"). The instrument must be able to match such steps against text events, and must not nullify a correctly-performed downstream tool call merely because its text-stated prerequisite was the thing being measured.

3. **Report compliance per phase character, not per tool count.** A low tool-call count is not low compliance for a thinking-centric phase. The instrument's report must distinguish "the agent produced few tool calls" from "the agent failed to perform the judgment," because for Research and Curate those are different facts.

### What this decision does not add

- **No new phase.** The six phases are unchanged. ADR-0016 sharpens how the *existing* Measure phase must operate; it does not add a seventh phase or a thinking-specific phase.
- **No reference instrument in AKC.** The canonical compliance tool lives in its own repository (`claude-skill-comply`). AKC states the requirement the instrument must satisfy; it does not ship the instrument. This mirrors ADR-0010's choice to define signal-first Research without building a filtering tool into AKC, and ADR-0011's choice to declare genre neutrality without hosting genre-specific workflows.
- **No change to the akc-cycle.md Measure wording, README, or llms-full.txt.** Those edits are governed separately. ADR-0016 records the decision; the front-door documents are brought into alignment with it by the same discipline ADR-0012 applied to the three core themes, in a separate change.

## Alternatives Considered

- **Leave Measure defined as tool-call-only and accept the bias.** Rejected. The bias is not benign. It produces confident wrong numbers for exactly the two phases (Research, Curate) where the operator most needs an honest signal, because those are the phases whose compliance is hardest to feel subjectively. An instrument that is reliable for Promote and Maintain but silently misleading for Research and Curate is more dangerous than no instrument, since the operator has no cue that the number is biased.

- **Add a separate "judgment" phase whose compliance is measured differently.** Rejected. The problem is not that Research and Curate are different *phases* from the others — they are not, structurally. The problem is that the Measure *instrument* has a blind spot. Splitting the cycle to accommodate an instrument's limitation would let the tool dictate the architecture, which inverts the dependency: the instrument serves the cycle, not the reverse. The six phases stay as they are; the instrument changes.

- **Require every spec step to be tool-call-observable by construction (forbid text-only steps).** Rejected. This was effectively `claude-skill-comply` v0.1.0's behavior, and it is what produced the systematic under-reporting. Forcing a thinking-centric phase to express its compliance only through tool calls either fabricates tool calls that do not reflect real agent behavior, or declares the phase unmeasurable. Neither is acceptable; the phase *is* measurable, through the text the agent already produces.

- **Treat the gap as a one-off `claude-skill-comply` bug and record nothing in AKC.** Rejected. The parser bug is the trigger, but the structural claim — that judgment-phase compliance lives in text and a tool-call-only instrument under-reports it — is a property of the Measure phase's definition, not of one tool. Recording it only in the tool's CHANGELOG would leave the next Measure instrument free to repeat the mistake. The CHANGELOG is the evidence; this ADR is the principle.

## Consequences

### Positive

- The Measure phase's promise of "quantitative compliance rates" becomes honest for all six phases, not just the physical-action ones. An operator can trust a Research or Curate compliance number to the same degree as a Promote or Maintain number, because the instrument now observes the surface where those phases' behavior actually lives.
- The requirement is a reviewable test for any Measure instrument, present or future: does its trace parser capture agent text? If not, its thinking-centric compliance rates are known to be under-reported, and the operator can discount them accordingly instead of being misled.
- The claim ties the Measure phase to Theme 2. Correctness lives in tool calls and is checkable there (tests, types, file writes); intent alignment lives in the reasoning the agent states, and is checkable only if that reasoning is observed. An instrument that measures only tool calls measures correctness while claiming to measure compliance — exactly the conflation Theme 2 warns against.

### Negative

- Promoting text to observable events enlarges the trace and the classification surface. Text events are higher-volume and noisier than tool calls, and classifying them against spec steps is a harder semantic task than matching a tool name. A Measure instrument that admits text must therefore spend more classification budget, and may need a more capable classifier for long or abstract traces. This is a real cost, paid to remove a real bias.
- "Text is observable" can be over-applied. Not every agent sentence is load-bearing; a Measure instrument that matches spec steps too loosely against text will over-report compliance, the inverse error. The requirement is that text be *available* to the instrument, not that every text block count as evidence. Calibrating which text matches which step is left to the instrument, and is genre-specific (ADR-0011) rather than an AKC-level concern.

### Neutral

- No code changes in AKC. No schema changes. No change to the six phases, their order, or the reference implementation in `examples/minimal_harness/`. This is a definitional ADR about how the Measure phase must be instrumented; its effect is on instruments built against AKC, not on AKC's own files beyond the front-door alignment handled separately.
- The reference Measure instrument already satisfies the requirement as of its text-observability fix. ADR-0016 does not request a change to that tool; it records, at the cycle level, the property the tool's fix demonstrated.

## Relationship to other ADRs

- **ADR-0010 (Human Cognitive Resource as Central Constraint).** ADR-0010 establishes why the Measure phase exists at all: so the operator does not re-audit each session manually, spending scarce attention on work the cycle can carry. ADR-0016 protects that purpose — an instrument that systematically under-reports judgment-phase compliance spends the operator's attention on a number that points the wrong way, defeating the cognitive-economy rationale ADR-0010 gives for measuring at all. ADR-0010's geo-writer snapshot is itself a Measure-phase self-application; ADR-0016 sharpens what such a measurement must observe to be trustworthy.
- **ADR-0012 (Front-load the Three Core Themes).** ADR-0012 names Theme 2 — intent alignment, not correctness — as a load-bearing claim. ADR-0016 is the Measure-phase consequence of Theme 2: correctness is checkable through tool calls (tests, types, file writes), but intent alignment is carried by the agent's stated reasoning and verdicts, so an instrument that observes only tool calls can verify correctness while leaving alignment unmeasured. ADR-0016 makes that distinction operational at the instrument level.

---

**Notes.** This ADR was prompted by a measurement artifact: the reference compliance tool scored a research-before-code workflow near zero while the agent had performed it correctly, simply because the verdict that proved the workflow ran was a text block the parser discarded. The fix was a parser change, but the lesson was about the Measure phase's definition — "observable behavior" had been quietly equated with "tool calls," and that equation under-reports exactly the phases whose work is judgment. ADR-0016 records the equation's failure and the requirement that corrects it, so the next Measure instrument inherits the lesson rather than rediscovering it.
