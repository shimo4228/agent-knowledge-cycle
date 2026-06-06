# ADR-0014: Failure Modes of the Bidirectional Loop

> **Summary.** Theme 3 — *the cycle changes the human too* — has so far been stated only in its positive direction: as the human curates and promotes knowledge, their judgment about good agent behavior sharpens. But a loop that can grow judgment can also erode it. This ADR names three mechanism-level failure modes of the bidirectional loop — gate complacency, deskilling, and delegation-feedback divergence — and articulates the structural features of AKC that resist them. The claim is not that AKC immunizes the human against these failures; it is that the cycle's existing structure already encodes specific defenses, and naming the failure twin keeps Theme 3 honest.

## Status
**experimental**

## Date
2026-06-06

## Context

Theme 3 (ADR-0012) holds that AKC is not a one-directional optimization
loop in which the agent improves in isolation: agent behavior and human
judgment co-develop. Every statement of this theme in the repository —
the README's "The cycle changes the human too" section, the graph's
`bidirectional-growth-loop` node, ADR-0009's third problem, ADR-0012's
third paragraph — frames the loop in its positive direction. The human
curates, and their sense of what is worth keeping sharpens. The human
promotes, and their judgment about what makes a good rule sharpens. The
human measures, and they learn what separates a rule from a vague
aspiration. The word in all of these is *grows*.

A loop that can grow judgment can also erode it. The same coupling that
lets sustained interaction sharpen the operator can, under different
conditions, let it dull. A bidirectional loop has a failure twin for
every growth claim, and a theme that only ever appears in its positive
direction is a theme that has not yet been stress-tested. Readers can
reasonably ask: what happens when the loop runs the other way? Without
an answer, Theme 3 reads as an optimistic assertion rather than a
mechanism with known boundaries.

This ADR names three mechanism-level failure modes. It stays at the
mechanism layer deliberately: these are properties of the loop's
structure, not claims about any particular operator, domain, or harness.
The empirical literature on each failure mode (automation complacency,
skill atrophy, feedback degradation) is paper-stage material; this ADR
does not carry that citation apparatus. It records the failure modes as
structural facts about a coupled human-agent loop and articulates which
features of AKC's existing design already resist them.

### The three failure modes

**(i) Gate complacency / automation bias.** ADR-0005 routes every
behavior-modifying change through a human approval gate. The gate's value
depends on the human actually reading what they approve. As the agent
becomes more reliable, the prior shifts: a stream of well-formed,
usually-correct proposals trains the operator to approve by default. The
gate is still there, the click still happens, but the judgment behind the
click has thinned to a reflex. This is the loop running backward through
the Promote phase — the very phase ADR-0005 was built to protect — and
it is worst exactly where Theme 1 (ADR-0010) bites hardest. Under a
constrained attention budget, the cheapest action is to trust the
proposal, and a trustworthy agent makes that cheap action feel safe. The
attention scarcity that motivates the cycle is also the amplifier of its
gate's failure.

**(ii) Deskilling.** The growth direction of Theme 3 says supervision
sharpens judgment. The failure direction says over-delegation starves it.
The tacit expertise required to supervise an agent — to notice that a
proposed rule is subtly wrong, that a promoted pattern will misfire in
cases the agent did not consider — is maintained by exercise. If the
human stops doing the underlying work and only reviews the agent's
output, the faculty that review depends on atrophies. The endpoint is a
human who can no longer tell a good proposal from a plausible one, which
collapses the human side of the loop. Deskilling does not announce
itself; it is the gradual loss of the capacity that made the human's role
load-bearing in the first place.

**(iii) Delegation-feedback divergence.** This is the failure twin of the
growth loop itself. The growth loop assumes the human's judgment and the
agent's behavior stay coupled: the human shapes the agent, the shaped
agent surfaces situations that re-shape the human, and the two track each
other. Divergence is what happens when that coupling breaks while
delegation continues. The agent keeps acting on the operator's behalf,
but the feedback that would correct it no longer reaches a human who is
still in a position to use it — because attention has moved on (mode i),
or because the judgment needed to interpret the feedback has atrophied
(mode ii), or simply because the volume of delegated work has outrun the
human's capacity to stay coupled to it. The two ends of the loop drift
apart while the machinery keeps running. This is the most dangerous mode
because, unlike a stalled loop, a diverged loop still produces output —
it just produces output that no human is meaningfully steering.

## Decision

AKC names these three failure modes as known boundaries of Theme 3, and
articulates the structural defenses already present in the cycle. The
defenses are properties of mechanism, not exhortations to the operator.
"Be careful" is not a defense; a structure that makes carelessness harder
is.

### (a) The gate is a circuit-breaker, not a delay

ADR-0005's approval gate has no "auto-approve after N days" path and no
"approved by the LLM itself" path. This is the structural defense against
runaway coevolution: a loop that could promote its own changes without a
human would have no point at which divergence (mode iii) could be
arrested. AKC's gate is a circuit-breaker on the loop, not a speed bump
in front of an inevitable write. The absence of an auto-approve escape
hatch is what makes the gate a defense against divergence rather than a
formality the loop eventually routes around. Gate complacency (mode i)
degrades the gate's *quality*; the no-escape-hatch design ensures the
gate's *existence* cannot be eroded by the loop itself, only by the human
choosing to attend less — which keeps the failure on the human side of
the boundary, where it can be noticed, rather than dissolving the
checkpoint structurally.

### (b) Curate and Promote are active judgment acts, not passive consumption

This is the anti-deskilling argument (mode ii), and it is structural
rather than aspirational. AKC's Curate and Promote phases do not ask the
human to read what the agent produced and assent. They ask the human to
*decide*: which accumulated patterns are worth keeping (Curate), and
which recurring decisions are stable enough to become rules (Promote).
These are acts of judgment that exercise exactly the faculty deskilling
erodes. A cycle built around passive consumption — read the agent's
knowledge base, approve its summaries — would actively cultivate the
atrophy this ADR warns about. AKC's phases are built around active
judgment instead, so the normal operation of the cycle keeps the human's
supervisory faculty in use. The defense against deskilling is that the
cycle's central acts are themselves the exercise that prevents it.

### (c) The gate forces articulation, not a yes/no click

The deepest defense against gate complacency (mode i) is that ADR-0005's
gate produces a *diff or proposal file* that the operator reviews, edits,
and commits — and that the commit becomes part of an audit trail. The
operation is not a one-bit accept/reject. It asks the human to engage
with the specific content of the change at the level of a diff, and to
own the result by committing it under their name. Articulation is more
resistant to reflexive approval than a binary click: it is harder to
rubber-stamp a change you have to read line by line and sign for than one
you dismiss with a single keystroke. This does not eliminate complacency
— a sufficiently inattentive operator can commit a diff unread — but it
raises the floor. The gate's default action is not "approve"; it is
"read, possibly edit, then commit," which is a structurally heavier act
than assent.

### What this decision does not claim

- It does not claim AKC prevents these failures. A human determined to
  stop attending will diverge from the loop regardless of structure. The
  claim is bounded: AKC's existing structure resists these modes more
  than an autonomous or passive-consumption alternative would, and naming
  the modes makes the residual risk legible.
- It does not add a new phase, skill, or mechanism. The three defenses
  are re-readings of structure ADR-0005 and the six phases already carry.
  Naming the failure twin does not require new machinery; it requires
  stating that the machinery was already load-bearing against failure,
  not only in service of growth.
- It does not encode domain-specific mitigations. Per the mechanism-only
  rule (ADR-0011), concrete instances of how a given operator or domain
  guards against deskilling belong to downstream projects, not to the
  cycle.

## Alternatives Considered

- **Leave Theme 3 one-directional.** Rejected. A growth claim with no
  stated failure twin is an advertisement, not a mechanism. The
  bidirectional loop's downside is the obvious first question a critical
  reader asks; leaving it unanswered weakens the theme it is meant to
  protect.

- **Add a mitigation phase or an anti-complacency skill.** Rejected. A
  new phase would claim AKC has a workflow for resisting deskilling, which
  re-imports the genre-specificity ADR-0011 extracted. The defenses are
  properties of existing structure; surfacing them as a new skill would
  turn a structural fact into a magnet for domain examples.

- **Carry the empirical literature (automation complacency, skill
  atrophy, feedback-loop degradation) into this ADR.** Rejected as
  out of layer. The citation apparatus is paper-stage material. An ADR
  records a judgment about AKC's structure; loading it with external
  evidence would blur the boundary between the decision record and the
  paper that argues the decision to an academic audience.

- **Frame the failure modes as risks to warn the operator about.**
  Rejected. "Warn the operator" puts the defense on the human's vigilance,
  which is precisely the resource Theme 1 says is scarce and modes (i)
  and (ii) say is eroding. The defenses worth recording are the
  structural ones — features of the loop that hold even as vigilance
  thins — not exhortations that fail exactly when they are most needed.

## Consequences

### Positive

- Theme 3 gains a failure twin, which makes it falsifiable rather than
  aspirational. A reader can now ask "does AKC's gate actually resist
  complacency?" and find a structural answer instead of an optimistic
  assertion.
- The no-escape-hatch design of ADR-0005's gate is reframed: it is not
  only an autonomy boundary but a circuit-breaker against the
  bidirectional loop's worst failure mode. The same structure answers two
  questions.
- The active-judgment character of Curate and Promote acquires a second
  justification. ADR-0010 framed them as cognitive-economy moves; this
  ADR adds that they are also the exercise that keeps the human's
  supervisory faculty from atrophying.

### Negative

- Naming failure modes invites the inference that AKC has solved them.
  The "What this decision does not claim" section guards against this, but
  the risk remains that a casual reader takes the named defenses as
  guarantees rather than as bounded structural resistance.
- The boundary between this mechanism-level ADR and the paper-stage
  treatment of the same failure modes must be maintained deliberately.
  Future contributors may be tempted to import the empirical citations
  here; the Alternatives section records why that import is out of layer.

### Neutral

- No code changes. No schema changes. No change to the six phases or the
  reference implementation. This is a positioning ADR; its effect is on
  how Theme 3 is read and on the test future Theme-3 prose must pass
  (does it acknowledge the failure twin?).

## Relationship to other ADRs

- **ADR-0005 Human Approval Gate** — the source of all three structural
  defenses. The gate's no-escape-hatch design is the circuit-breaker
  (defense a); its diff-and-commit operation is the articulation
  requirement (defense c). ADR-0014 re-reads ADR-0005 as a defense
  against the bidirectional loop's failure twin, not only as an autonomy
  boundary.
- **ADR-0010 Human Cognitive Resource as Central Constraint** — Theme 1
  is the amplifier of gate complacency (mode i): under a constrained
  attention budget, default-approval is the cheapest action, and a
  reliable agent makes that cheapness feel safe. The constraint that
  motivates the cycle is also what makes its gate vulnerable, which is why
  the defense has to be structural rather than a demand for more
  attention.
- **ADR-0012 Front-load the Three Core Themes** — the source of Theme 3
  in its positive direction. ADR-0014 supplies the negative direction the
  front-door framing omits, keeping Theme 3 honest without changing how it
  leads.
- **ADR-0011 Cycle Applies to Any Knowledge Body** — the mechanism-only
  rule that keeps this ADR at the structural layer: domain-specific
  mitigations and empirical citations belong downstream, not in the
  cycle.

---

**Notes.** This ADR was prompted by the observation that every statement
of Theme 3 in the repository runs in one direction. A bidirectional loop
named only by its growth direction is half-described. The work here is not
to add a mechanism but to read the mechanism already present as a defense
against the failure twin — and, in doing so, to make Theme 3 a claim that
can be argued with rather than only agreed to.
