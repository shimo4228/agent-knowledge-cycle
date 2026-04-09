# ADR-0001: Security by Absence as a First-Class Principle

> **Summary.** Dangerous agent capabilities — shell execution, arbitrary network access, filesystem traversal, dynamic code evaluation — are not restricted. They are never implemented. Prompt injection cannot grant abilities the harness was never built to have.

## Status
accepted

## Date
2026-04-09

## Context

AI agents accumulate capabilities over time: shell execution, arbitrary
HTTP, filesystem traversal, credential access. Each capability becomes a new
attack surface. Prompt injection — increasingly well-documented — can turn any
capability the agent possesses into an exploit vector, regardless of how the
agent was instructed to use it.

The conventional response is to **restrict** dangerous capabilities: allowlists,
sandboxes, permission prompts, guardrail LLMs. These approaches defend against
known misuse patterns but fail open when the restriction layer itself is
bypassed or misconfigured. Every added restriction is also a piece of code that
must be maintained, tested, and kept in sync with the capabilities it governs.

A harness that aspires to be auditable and long-lived needs a stronger, simpler
guarantee than "restricted."

## Decision

AKC adopts **Security by Absence** as a first-class design principle:

> Dangerous capabilities are not restricted. They are **never implemented**.

The harness does not ship code that executes shell commands, opens arbitrary
network connections, or traverses the filesystem outside a narrowly defined
data directory. Prompt injection cannot grant abilities the harness was never
built to have.

### What is not implemented

| Capability | Status |
|------------|--------|
| Shell / subprocess execution from the agent core | Absent |
| Arbitrary outbound HTTP | Absent (single pinned adapter only; see ADR-0006) |
| Filesystem writes outside the agent's data directory | Absent |
| Arbitrary file reads outside the agent's data directory | Absent |
| Dynamic code loading / `eval` / `exec` of LLM output | Absent |
| Network-reachable control plane / remote command channel | Absent |

### What this defends against

- **Prompt injection escalation** — malicious content in logs, knowledge, or
  external input cannot invoke capabilities that do not exist in the codebase.
- **Supply chain drift** — a compromised dependency cannot gain new attack
  surface unless the harness itself is patched to add it.
- **Misconfiguration failure modes** — there is no restriction layer to
  misconfigure, because there is nothing to restrict.
- **Audit ambiguity** — "does capability X exist?" is answerable by `grep`.

### What this does NOT defend against

- **LLM-generated false outputs** — the harness does not protect against the
  LLM producing incorrect or misleading text within its allowed output channel.
- **Data exfiltration through the pinned adapter** — if a single external
  adapter exists (ADR-0006), content written through it can still leak.
- **Local privilege issues** — file permissions, process isolation, and OS-level
  hardening are the operator's responsibility.
- **Prompt injection influencing content** — injected text can still change
  what the agent *says* through its permitted output channel; it just cannot
  gain new capabilities.

### Applying the principle

Before adding any new module, dependency, or capability, ask:

1. Does this introduce a new side effect the harness previously could not
   perform? (shell, network, file write outside data dir, dynamic code)
2. If yes, is there a threat model in which an attacker-controlled input could
   reach it? If yes, **do not add it**. Find a design that does not require it.
3. If the capability is genuinely unavoidable, it must go through ADR-0006
   (Single External Adapter) and ADR-0005 (Human Approval Gate).

## Alternatives Considered

- **Restrict at runtime (sandboxes, allowlists)** — Effective against known
  patterns but fails open on misconfiguration and adds maintained code.
- **Guardrail LLM / policy model** — Probabilistic, not deterministic.
  Inadequate for capability gating.
- **Capability tokens / permission prompts** — Shifts the burden to the user
  and is vulnerable to prompt injection convincing the user to approve.

## Consequences

- AKC ships as specifications, schemas, and a minimal reference example —
  not as a feature-rich agent framework.
- Some convenient affordances (one-shot shell, open HTTP) are deliberately
  unavailable. Users who need them build their own adapter and own the risk.
- Code review gains a simple rule: "does this PR add a new side-effect type?"
  If yes, the PR either triggers a new ADR or is rejected.

## Audit test

Security by Absence is auditable with `grep`. If your codebase is clean,
a single command returns zero hits (or only hits inside a reviewed
adapter that was explicitly allowed by an ADR):

```bash
git grep -nE "subprocess|os\.system|\beval\(|\bexec\(|urlopen|requests\.(get|post|put|delete|patch)" \
  -- ':!docs' ':!examples' ':!tests'
```

Tune the exclusions to your project. The rule is: **if the answer to
"does capability X exist?" is not answerable by `grep`, you do not have
Security by Absence — you have hope.** Add the grep to CI to make the
check deterministic.

See [`docs/skills/llm-agent-security-principles.md`](../skills/llm-agent-security-principles.md)
for the full "how" reference, including the audit-test rationale,
HTTP and credential hardening patterns, and a design-review checklist.

---

**Inspired by:** [contemplative-agent `docs/adr/0007-security-boundary-model.md`](https://github.com/shimo4228/contemplative-agent).
The threat model in that ADR was the seed for this one; moltbook-specific
details have been removed to make the principle harness-neutral.
