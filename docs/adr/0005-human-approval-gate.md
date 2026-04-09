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

**Inspired by:** [contemplative-agent `docs/adr/0012-human-approval-gate-for-behavior-modifying-commands.md`](https://github.com/shimo4228/contemplative-agent).
