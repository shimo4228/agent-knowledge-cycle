# ADR-0005: Human Approval Gate for Behavior-Modifying Changes

> **Summary.** Changes that modify future agent behavior — rules, skills, identity — are proposed and wait for explicit human approval before taking effect. The harness never auto-applies them, and no "auto-approve after N days" escape hatch exists.

## Status
accepted

## Date
2026-04-09

## Context

A self-improving agent that edits its own rules, skills, or identity without
human review can drift silently. Even with high-quality distillation, a
single bad pattern promoted to the rules layer changes every future session.
The cost of review is small; the cost of an unnoticed regression to core
behavior is large and can be hard to trace back to its cause.

AKC's "Promote" phase explicitly moves knowledge from the probabilistic layer
(skills, memory) to the deterministic layer (rules). That promotion is
exactly the step that most deserves a human in the loop.

## Decision

Any change that modifies future agent behavior must be **proposed, reviewed,
and explicitly approved** before it takes effect. The harness does not
auto-apply such changes.

### What requires approval

| Change type | Requires approval? |
|-------------|---------------------|
| Appending to the episode log (Layer 1) | No (write-through, immutable) |
| Updating the knowledge store (Layer 2) | No (pure function of Layer 1) |
| Adding or editing a rule (Layer 3) | **Yes** |
| Adding or editing a skill | **Yes** |
| Updating identity | **Yes** |
| Editing an ADR or README that documents behavior | **Yes** |

### How approval happens

The harness produces a **diff or proposal file** and stops. The operator
reviews it, edits if needed, and commits. There is no "auto-apply after N
days" escape hatch and no "approved by the LLM itself" path.

For interactive sessions, the operator says "yes" in conversation and the
agent writes the file. For batch / scheduled runs, the output is a patch file
or a pull request — never a direct write.

### Why the distinction matters

Layers 1 and 2 are disposable and reproducible (ADR-0003). Regenerating them
from scratch is a supported recovery path. Layer 3 is the layer that shapes
future distillation, so an unchecked change there is self-reinforcing.

## Alternatives Considered

- **Auto-apply everything** — Fast feedback, but a bad promotion cascades
  through every future session and is hard to detect post hoc.
- **Approval only for "large" changes** — Requires defining "large," which
  is exactly the judgment call a human should be making.
- **Voting / consensus across multiple LLM critics** — Expensive and still
  probabilistic. Does not give the operator ownership of behavior.

## Consequences

- The cycle cannot run fully unattended past the Promote phase. This is
  intentional; AKC's value proposition is "human-aligned self-improvement,"
  not "autonomous self-improvement."
- Approval creates an audit trail: git history of the rules directory is a
  record of every intentional behavioral change.
- `skill-comply` (the Measure phase) benchmarks *approved* rules, so it can
  legitimately ask "is the agent following what the human agreed to?"

---

### Addendum — 2026-06-06: Why the gate is the contribution, not a guardrail

This ADR has been read as a safety guardrail bolted onto an otherwise
autonomous loop — a reasonable reading, but the wrong one. The gate is not a
restriction *on* the cycle; it is a load-bearing part of what the cycle *is*.
Three threads make the case that the human sign-off is the contribution, and
that its non-autonomy is a deliberate architectural stance rather than a
missing feature.

**1. AKC inverts the autonomous-promotion default.** The dominant pattern in
self-evolving-agent work is that the agent itself decides what to persist.
Voyager grows its own skill library from successful trajectories; Reflexion
(Shinn et al., [arXiv:2303.11366](https://arxiv.org/abs/2303.11366)) and ExpeL
(Zhao et al., [arXiv:2308.10144](https://arxiv.org/abs/2308.10144)) write their
own reflections and lessons back into memory; Generative
Agents synthesize and store reflections autonomously; A-MEM (Xu et al.,
[arXiv:2502.12110](https://arxiv.org/abs/2502.12110)), Mem0 (Chhikara et al.,
[arXiv:2504.19413](https://arxiv.org/abs/2504.19413)), and LangMem
manage memory write-back as an agent-internal operation; Agent Workflow Memory
(AWM) and ReMe induce reusable workflows from past runs without a human in the
write path. In each, a human-in-the-loop is *optional* — a guardrail one may
add. The Darwin Gödel Machine lineage pushes this further: Hyperagents (Zhang
et al., [arXiv:2603.19461](https://arxiv.org/abs/2603.19461)) lets the agent
edit its own improvement mechanism, folding task-solving and self-modification
into one editable program. AKC inverts this. Cross-layer promotion — moving a
pattern from the probabilistic skills/memory layer to the deterministic rules
layer — requires a *named human sign-off*. The gate is not optional and not a
convenience; it sits on the one edge of the cycle that rewrites future
behavior, and it is structural.

**2. The gate is load-bearing, not decorative.** Scalable-oversight work gives
a concrete reason the promotion edge is the right place to spend human
judgment. When the entity proposing a change and the entity checking it are
the same system, the check inherits the proposer's blind spots — the
generator–verifier gap that scalable-oversight research tries to widen rather
than assume away. An LLM that distills a pattern and then approves its own
promotion is a generator verifying itself, with the verifier's variance
correlated to the generator's. Worse, because Layer 3 shapes future
distillation (see "Why the distinction matters" above), an unchecked bad
promotion is not a one-off error but a seed: the next cycle distills against
corrupted rules, amplifying the error recursively. The human at the promotion
edge is the one verifier whose failures are *not* correlated with the
generator's. This is not offered as a formal proof; it is the reason the gate
earns its cost.

**3. AKC's Promote is extrinsic metacognition — and stays that way by
design.** Liu and van der Schaar
([arXiv:2506.05109](https://arxiv.org/abs/2506.05109)) distinguish *intrinsic*
metacognition (an agent's own ability to evaluate and adapt its learning
process) from *extrinsic* metacognition (fixed, human-designed loops), and
argue that truly self-improving agents must internalize the former. By that
taxonomy AKC's Promote phase is squarely extrinsic: a human-designed loop with
a human evaluator at the decision point. AKC does not treat this as a
limitation to be engineered away. Recent platform-side memory features —
file-based memory tools the agent uses to persist, revise, and reorganize
what it learns across sessions
([Anthropic memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool))
— automate parts of the Extract and Curate phases. But their output lands in a
file-based memory layer; it does not reach rules, identity, or weights. They
make the *intake* phases more autonomous while leaving Promote untouched.
AKC's stance is that this is correct, not incidental: the promotion edge is
where the human's evolving intent enters the loop, and an extrinsic gate is
how that intent stays in the loop rather than being optimized out of it. A
fully intrinsic AKC would be a different, less human-aligned thing — the cycle
is what it is *because* the gate stays extrinsic.

---

**Inspired by:** [contemplative-agent `docs/adr/0012-human-approval-gate-for-behavior-modifying-commands.md`](https://github.com/shimo4228/contemplative-agent).
