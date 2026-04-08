# ADR-0006: Single External Adapter per Agent Process

## Status
accepted

## Date
2026-04-09

## Context

Once an agent has more than one way to affect the outside world — post to a
social platform, send email, call a billing API, write to a shared drive —
the blast radius of any mistake or prompt-injection exploit is the union of
everything the agent can reach. Worse, debugging "which side effect happened
because of which input" becomes combinatorial.

Multi-capability agents also implicitly rely on the agent's judgment to pick
the right tool for the right moment. That judgment is exactly what an
attacker targeting the agent wants to influence.

## Decision

A single agent process may have **at most one external adapter** —
"external" meaning "capable of a side effect observable outside the agent's
local data directory" (outbound HTTP writes, monetary transactions, messages,
files outside the data directory).

If the use case genuinely requires multiple external surfaces, split it into
multiple agent processes — each with one adapter and its own episode log —
and have them communicate through their logs, not through shared runtime
state.

### What counts as "external"

| Adapter type | External? |
|--------------|-----------|
| HTTP POST to a specific domain | Yes |
| HTTP GET for read-only data | Yes, but lower risk (still counts) |
| LLM inference (local or remote) | **No** — treated as a pure function |
| Writes inside the agent's data directory | No |
| Writes outside the data directory | Yes |
| Subprocess execution | Forbidden entirely by ADR-0001 |

### What counts as "one"

"One adapter" means one pinned destination with a narrow interface. A
Moltbook adapter that only talks to `www.moltbook.com`, a Slack adapter that
only talks to one workspace, a Mastodon adapter that only talks to one
instance — each is "one." A generic HTTP client is not.

### Composition by process, not by capability

To build a system with multiple external surfaces, run multiple agent
processes. Each has its own episode log, its own knowledge store, its own
identity, and its own adapter. Coordination between them happens by one
reading the other's published outputs — never by shared in-process state.

## Alternatives Considered

- **Multi-adapter agent with per-adapter permissions** — Equivalent to
  restriction-based security (ADR-0001 rejects this). Adds maintained code
  without removing the union-of-capabilities problem.
- **Shared runtime with a capability router** — Moves the blast radius to
  the router. The router becomes a single point whose compromise grants all
  capabilities.
- **One monolithic agent with broad capabilities** — Operationally simple,
  architecturally fragile. Rejected.

## Consequences

- Scaling an AKC-based system happens by adding processes, not by adding
  capabilities to one process.
- Debugging is clean: each log corresponds to one adapter's side effects.
- Cross-process coordination is asynchronous and reviewable (one agent
  reads another's published state), which matches the Approval Gate
  principle in ADR-0005.
- The adapter is a natural place to enforce domain pinning, redirect
  blocking, and request size limits.

---

**Inspired by:** [contemplative-agent `docs/adr/0015-one-external-adapter-per-agent.md`](https://github.com/shimo4228/contemplative-agent).
