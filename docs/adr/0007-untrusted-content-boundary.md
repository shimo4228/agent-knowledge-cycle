# ADR-0007: Untrusted Content Boundary

## Status
accepted

## Date
2026-04-09

## Context

A self-improving agent's memory is populated, directly and indirectly, by
text it did not author: user messages, tool output, the LLM's own
hallucinations, content fetched from the adapter. Every line of that memory
then flows back into future prompts.

The usual threat model frames "user input" as untrusted and "agent-generated
text" as trusted. That framing is wrong for a self-improving agent. The
agent's own distillation output is a summary of untrusted input, processed
by a probabilistic model that has no reliable way to refuse malicious
content. **The summary inherits the taint of its sources.**

## Decision

All accumulated agent state — episode logs, knowledge store, identity —
is treated as **untrusted content** whenever it is read back into a prompt.

### Write-time rules

- External input (adapter responses, user messages, tool output) is recorded
  verbatim in the episode log. No sanitization at write time beyond what is
  structurally necessary (valid JSON).
- Recording is atomic: one line per event, no partial writes.

### Read-time rules

- When loading a knowledge file, validate against a forbidden-substring list
  before accepting the content. If a forbidden pattern is present, fail
  closed (treat the file as empty and log a warning) rather than fail open.
- When injecting accumulated content into a prompt, wrap it in an explicit
  boundary marker (e.g. `<untrusted_content>...</untrusted_content>`) so the
  model has a clear signal about which parts of its context it did not
  itself author.
- When producing identity or rules from distillation, validate the output
  against forbidden patterns before accepting the change.

### Forbidden substring list

The list itself is a project-specific concern. AKC does not ship a canonical
list; the reference implementation in [`examples/minimal_harness/`](../../examples/minimal_harness/)
shows the shape (a plain Python tuple checked case-insensitively) so
operators can define their own.

### Why validation, not filtering

Filtering ("remove the bad parts") hides evidence of tampering and lets
downstream code consume a partially-sanitized document as if it were clean.
Validation ("reject if any bad part is present") preserves the forensic
trail and forces a human to look at the file.

## Alternatives Considered

- **Trust agent-authored memory** — Ignores the fact that agent-authored
  text is a function of untrusted input. Unsafe.
- **Filter on read** — Hides tampering and produces silently-partial state.
- **Encrypt memory and trust the decrypted form** — Encryption guarantees
  confidentiality, not integrity against the entity doing the writing. The
  agent *is* the writer, so this doesn't help.

## Consequences

- Forbidden-pattern validation is cheap (one pass, case-insensitive) and
  can be run on every load.
- A tainted knowledge file becomes visible immediately: the warning log
  signals a specific file, and the operator can inspect it before deciding
  whether to reset the store from the episode log.
- Prompt injection gains no privileged pathway through memory, even though
  the memory itself may still contain injected text.

---

**Inspired by:** [contemplative-agent `docs/adr/0007-security-boundary-model.md`](https://github.com/shimo4228/contemplative-agent),
sections on input sanitization and configuration file validation.
