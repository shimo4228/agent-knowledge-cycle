# AKC Rules

Behavioral principles for AI agents implementing the Agent Knowledge Cycle. These rules distill the AKC phases into actionable guidance that works without installing individual AKC skills.

Copy this file to your agent's rules directory (e.g., `~/.claude/rules/`) and the cycle will run through natural conversation.

## Research — Search before building

Before creating a new module, utility, or abstraction:

1. Search for existing libraries, tools, and patterns that solve the same problem
2. Evaluate candidates for fitness (security, maintenance, relevance)
3. Adopt or extend an existing solution when one fits; build only when none do

**Trigger**: Any task that introduces a new dependency or creates a utility that might already exist.

## Extract — Capture reusable patterns from sessions

When a session produces a non-obvious solution, workaround, or decision:

1. Identify whether the pattern is reusable beyond this specific context
2. Evaluate quality before saving — not every solution deserves to persist
3. Save to the appropriate layer: memory for observations, skills for workflows, rules for principles

**Trigger**: End of a productive session, after a hard-won debugging victory, or when the user explicitly asks to learn from the session.

## Curate — Audit accumulated knowledge

Skills, rules, and learned patterns accumulate over time. Periodically:

1. Check for redundancy — two components covering the same concern
2. Check for staleness — references to deleted components, outdated advice
3. Check for silence — components that exist but never get triggered
4. Remove or consolidate what fails these checks

**Trigger**: When the number of skills/rules grows noticeably, when a component references something that no longer exists, or when the user asks for cleanup.

## Promote — Elevate recurring patterns to rules

When the same guidance appears in three or more places (skills, memory, conversation):

1. Extract the cross-cutting principle
2. Write it as a rule (concise, actionable, with a trigger condition)
3. Remove the redundant occurrences from lower layers

Rules are loaded every session and shape behavior reliably. Skills are triggered probabilistically. Promotion moves knowledge from the probabilistic layer to the deterministic layer.

**Trigger**: Noticing the same advice being given repeatedly, or finding the same pattern in multiple skills.

## Measure — Verify behavioral change quantitatively

Subjective assessment ("I think it's following the rule") is insufficient:

1. Define what compliance looks like in observable terms
2. Check whether the behavior actually occurs (tool call sequences, outputs, test results)
3. If compliance is low, investigate whether the rule is unclear, the trigger is wrong, or the rule conflicts with another

**Trigger**: After adding or modifying a rule, or when the user questions whether a rule is being followed.

## Maintain — Keep documentation roles clean

Every documentation file serves one of four roles: Context (how to work here), Architecture (what the code looks like), Decisions (why it's this way), External (what this project is). Periodically:

1. Verify each file serves exactly one role
2. Check for content that belongs in a different role (e.g., design rationale in a context file → should be an ADR)
3. Check numeric claims against reality (file counts, test counts, version numbers)
4. Remove or update stale content rather than letting it accumulate

**Trigger**: After major refactoring, when context files exceed ~200 lines, or when documentation claims feel wrong.

## Security by Absence — Don't implement what can be exploited

Dangerous capabilities are safer absent than restricted. Before adding a new
module, dependency, or capability:

1. Ask whether it introduces a new side effect the harness previously could
   not perform (shell execution, arbitrary network, filesystem writes outside
   the data directory, dynamic code loading, remote control channels)
2. If yes, assume an attacker-controlled input could reach it via prompt
   injection or a compromised dependency
3. Prefer a design that does not require the capability. If it is genuinely
   unavoidable, route it through a single pinned adapter (see ADR-0006) and
   a human approval gate (see ADR-0005)

Restrictions (allowlists, sandboxes, permission prompts) are code that must
be maintained and can fail open on misconfiguration. Capabilities that do
not exist in the codebase cannot be granted by any prompt.

**Trigger**: Any PR that adds a new dependency, a new external surface, or
a new side-effect type. Also: whenever a feature request reaches for
"just shell out to …" or "just fetch …".

See [`docs/adr/0001-security-by-absence.md`](adr/0001-security-by-absence.md)
for the threat model and the full list of what the harness does not
implement.

## Scaffold Dissolution

These rules are scaffolding. As the user and agent internalize the cycle through practice:

- The rules become implicit in how work is approached
- Individual rules may be simplified or removed as their principles are absorbed into conversation patterns
- Success is measured not by rule count, but by whether the cycle runs naturally without explicit invocation

See [scaffold-dissolution.md](scaffold-dissolution.md) for the full concept.
