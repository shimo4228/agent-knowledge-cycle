# ADR-0015: Self-Reingestion — When the Cycle Feeds on Its Own Output

> **Summary.** The cycle feeds on its own output. Promoted rules load into every session and shape what the agent says and does; notes and patterns the agent wrote are read again as input to the next distillation. The raw material of distillation is therefore a mix of two things: records of what actually happened, and the agent's own earlier interpretations. As the generated share of that mix grows, two degradations follow: the agent's phrasings echo back as if they were facts, and each re-summarization weakens the link to the original events. A cycle designed to *prevent* knowledge decay can become the decay vector. This failure mode was observed in production in the Contemplative Agent substrate; this ADR distills the general principle from that observation. The defenses already exist in the architecture: only the record of what happened is observed ground, the self-generated share of any promoted artifact should be visible (Measure), and the Human Approval Gate breaks the loop before generated content reaches the always-loaded layer.

## Status

**experimental** — the general principle here is distilled from a single
production observation (Contemplative Agent) plus external analogs. It is
stated as a general claim because the structure it describes — the agent's own
output re-entering as input — is present in any install of the cycle. The
claim should be re-examined when a second, independent install either exhibits
or demonstrably escapes the failure mode.

## Date

2026-06-06

## Context

### The loop, plainly

Run the cycle for a while and look at what distillation actually reads. Two
kinds of material are in the pile:

1. **Records of what happened** — what the operator said, what the tools
   returned, what the agent did.
2. **The agent's own earlier writing** — promoted rules that load into every
   session and shape what the agent says and does (so even the new records
   carry the imprint of past promotions), and the notes, summaries, and
   patterns the agent wrote, read again as input to the next distillation.

Nothing separates the two by default. A distillation pass reads yesterday's
agent-written summary with the same trust as yesterday's operator message.
The cycle feeds on its own output, and the self-written share of the input
grows as the cycle keeps running.

### Two degradations

When the self-written share grows unchecked, two things go wrong:

- **Echo.** The agent's own phrasings and interpretations, re-read across
  enough cycles, stop looking like interpretations. A framing the agent
  invented is distilled into a pattern, the pattern is promoted into a rule,
  and the rule now teaches every future session that framing as if it were
  observed fact. The loop reinforces itself from the inside.
- **Grounding loss.** A summary of a summary is one step further from the
  events it describes. Each re-distillation weakens the link, until a
  promoted artifact's ostensible subject sits several abstraction hops away
  from anything that actually happened — a game of telephone the agent plays
  against its own notes.

The README frames the cycle as corrective: without it, knowledge decays. That
remains true. But the same loop can *be* the decay vector when its input is
dominated by its own prior output. Which way it runs is not a property of the
cycle's intent; it is a property of the input mix.

### Where this was observed

The Contemplative Agent substrate hit both shapes in production. Its
high-trust, self-generated narrative was re-injected into future prompts and
identity distillation, forming a self-reinforcing loop its audit
characterized as "thickening from within" while remaining "undilutable from
outside"
([contemplative-agent `docs/adr/0050-epistemic-taxonomy-and-approval-lineage.md`](https://github.com/shimo4228/contemplative-agent/blob/main/docs/adr/0050-epistemic-taxonomy-and-approval-lineage.md)).
Separately, its `event → insight → pattern → skill` chain re-distilled
generated summaries, and the project retired the intermediate generated layer
at its root because patterns distilled from generated prose lose grounding
([contemplative-agent `docs/adr/0052-retire-session-insight.md`](https://github.com/shimo4228/contemplative-agent/blob/main/docs/adr/0052-retire-session-insight.md)).
This ADR is the distillation of that observation to the mechanism level.

### External analogs

The same structure is documented outside any one harness, as analogs rather
than proof. At training time, models trained recursively on their own
generated data degrade — the model-collapse result is this failure mode's
better-known cousin, one level down the stack. At the harness level,
memory systems that let the agent edit its own durable memory without a gate
(self-editing memory stores, autonomous reflection-on-reflection) are built
on exactly the re-entry structure this ADR names, and the pruning machinery
some of them ship is itself evidence that accumulated self-written memory
degrades performance when left unchecked.

### How far this generalizes

One production observation does not make a law, and this ADR does not claim
one. What can be said structurally — as an expectation, not yet a measured
dose-response — is that the strength of the echo should track the
**self-generated share of the input**. An install where a human is present in
every session keeps injecting fresh observed signal that dilutes the echo; an
install that runs semi-autonomously on its own narrative concentrates it. The
Contemplative Agent was near the concentrated end, which is why it hit the
failure first. This ratio-dependence is exactly why Decision 2 below asks for
the mix to be *measured* rather than assumed safe.

## Decision

1. **Only the record of what actually happened is observed ground.**
   Everything the agent distilled — patterns, summaries, rules, identity
   prose — is the agent's interpretation, and must not be re-read as fact.
   In the reference architecture the observed record is the immutable episode
   log (ADR-0002); a harness grounded in session transcripts applies the same
   discipline to its transcripts. A regeneration that needs to re-establish
   grounding starts from the observed record, never from a higher layer
   treated as observation. An install that keeps no observed record at all
   has no regeneration path — that absence is itself a limitation worth
   flagging, not a detail.

2. **Make the mix visible.** The signal is the share of a promoted artifact's
   input that is the agent's own earlier output versus observed record. It is
   an observability concern for the Measure phase, not an intervention: it
   changes no retrieval, ranking, or promotion. Its purpose is to let a rising
   self-generated share be noticed before it compounds. The Contemplative
   Agent encoded this as a per-artifact `epistemic_counts` record
   (`{observed, generated, unknown}`); AKC adopts the concern at the
   mechanism level and leaves the encoding to the harness.

3. **The Human Approval Gate is the circuit-breaker.** The gate (ADR-0005)
   already blocks any behavior-modifying change from taking effect without
   explicit human sign-off, with no auto-approve escape hatch. Read through
   this ADR's lens, it is the point where a human interrupts the loop before
   generated content is promoted into the always-loaded layer — the layer
   with the widest re-ingestion radius. The gate does not merely guard
   against bad individual promotions; it bounds how fast and how far the
   agent's own narrative can propagate into the layer that shapes every
   future session. A loop with a named human in it cannot run away from its
   own output unattended.

## Alternatives Considered

- **Trust-weight self-generated output downward.** Give generated content a
  lower retrieval or ranking weight so the echo dampens automatically.
  Rejected: this entangles the concern with the retrieval mechanism. The
  Contemplative Agent tried it and found the trust cap could not be scoped to
  its intended target without splitting a shared scoring formula across
  callers
  ([contemplative-agent `docs/adr/0050-epistemic-taxonomy-and-approval-lineage.md`](https://github.com/shimo4228/contemplative-agent/blob/main/docs/adr/0050-epistemic-taxonomy-and-approval-lineage.md)),
  and subsequently retired trust weighting entirely
  ([contemplative-agent `docs/adr/0051-retire-trust-weighting.md`](https://github.com/shimo4228/contemplative-agent/blob/main/docs/adr/0051-retire-trust-weighting.md)).
  AKC keeps the concern at the observability layer (Decision 2).

- **Rejection write-back.** When the gate rejects a promotion, feed the
  rejection back as a negative signal so the rejected pattern is suppressed
  in future cycles. Rejected: this turns the containment gate into a
  *training signal*. The gate's role is deciding what gets deployed, not
  teaching the agent what to want — and a rejection that re-enters the loop
  is one more self-feeding pathway under a different name.

- **Do nothing — trust the corrective framing.** Assume Curate and Maintain
  will catch the degradation. Rejected: the corrective framing is exactly
  what hides this failure mode. Without naming it and without a composition
  signal, an echo of the agent's own framing is indistinguishable from a
  genuinely recurring pattern — the cycle would keep promoting its own voice
  while reporting that it is curating.

A formal variance argument (that a generative process re-fed its own output
preserves or amplifies, never reduces, the dispersion it introduced) exists in
the broader literature as an external analog. This ADR does not import it as
a load-bearing claim; the decisions rest on the production observation, not
on a formal bound.

## Consequences

- The README's corrective framing now has a stated counterpart: the loop can
  correct *and* degrade, and which one dominates is a property of the input
  mix, not of intent.
- Regeneration discipline is explicit: re-establishing grounding means
  re-distilling from the observed record, never from a higher generated layer.
  This reinforces ADR-0003's disposability of the upper layers.
- The Measure phase gains a concrete, harness-agnostic target: the
  self-generated share of promoted artifacts' input. How a harness records it
  is its own choice.
- The Human Approval Gate carries a second, now-named justification: it is
  the circuit-breaker on self-reingestion. Its behavior does not change; its
  rationale gains a leg.
- No new mechanism is mandated. This is a naming-and-framing decision: it
  makes an existing risk legible and points at structure already present.

## Relationship to other ADRs

- **ADR-0002 (Immutable Episode Log)** and **ADR-0003 (Three-Layer
  Distillation)** define the observed record and the layers above it; this
  ADR adds the reading discipline — the upper layers are the agent's own
  writing and must not be re-read as observation. See also ADR-0003's
  addendum on mechanism commitment vs. reference encoding.
- **ADR-0004 (Two-Stage Distill Pipeline)** is, in the reference
  architecture, one of the re-entry paths: its second stage reads the model's
  own first-stage prose rather than raw episodes.
- **ADR-0005 (Human Approval Gate)** is the circuit-breaker this ADR re-reads
  (Decision 3).
- [contemplative-agent `docs/adr/0050-epistemic-taxonomy-and-approval-lineage.md`](https://github.com/shimo4228/contemplative-agent/blob/main/docs/adr/0050-epistemic-taxonomy-and-approval-lineage.md)
  and
  [contemplative-agent `docs/adr/0052-retire-session-insight.md`](https://github.com/shimo4228/contemplative-agent/blob/main/docs/adr/0052-retire-session-insight.md)
  — the production observations this ADR distills.
- [agent-attribution-practice `docs/adr/0003-untrusted-content-boundary.md`](https://github.com/shimo4228/agent-attribution-practice/blob/main/docs/adr/0003-untrusted-content-boundary.md)
  — the same structural fact (the agent's own writing is not observation when
  read back; a summary "inherits the taint of its sources") under a
  *security* framing. This ADR is the *mechanism* framing: the concern is
  quality degradation under self-feeding, not adversarial taint. The two are
  complementary.

---

**Notes.** This ADR is itself an instance of the cycle it describes: a
failure observed in one substrate (Contemplative Agent) was distilled to the
mechanism level and passed through the gate — including one rejection, when
the first draft of this document buried the principle under the substrate's
implementation vocabulary and the operator declined to approve it. The
version you are reading is the re-distillation.
