# minimal_harness — AKC reference implementation

A dependency-free Python reference that demonstrates AKC's three-layer
memory architecture and two-stage distill pipeline. Standard library
only. No network. No API keys. Around 300 lines of code total.

## What it shows

| File | Layer / concept | ADR |
|------|-----------------|-----|
| `episode_log.py` | Layer 1 — append-only JSONL, `umask(0o177)`, daily partitioning | [ADR-0002](../../docs/adr/0002-immutable-episode-log.md) |
| `knowledge_store.py` | Layer 2 — distilled patterns, time decay, forbidden-substring validation | [ADR-0003](../../docs/adr/0003-three-layer-distillation.md), [ADR-0007](../../docs/adr/0007-untrusted-content-boundary.md) |
| `distill.py` | Two-stage distill pipeline (free-form → format), LLM-agnostic | [ADR-0004](../../docs/adr/0004-two-stage-distill-pipeline.md) |
| `demo.py` | End-to-end run with a deterministic fake LLM | — |

What this reference intentionally does **not** implement:

- Layer 3 (identity / rules). That requires human review. See [ADR-0005](../../docs/adr/0005-human-approval-gate.md).
- Any external adapter. See [ADR-0006](../../docs/adr/0006-single-external-adapter.md).
- Shell execution, arbitrary HTTP, filesystem writes outside the log
  directory. See [ADR-0001](../../docs/adr/0001-security-by-absence.md).

## Run the demo

From the repository root:

```bash
python -m examples.minimal_harness.demo
```

Expected output (abbreviated):

```
[Layer 1] wrote 3 episodes to /tmp/.../logs
[Layer 2] stage1_reflection='Across the session I noticed...'
[Layer 2] added 2 patterns to /tmp/.../knowledge.json
[Layer 2] top patterns by effective importance:
  - (0.800) [important] The agent should summarize long user turns before responding.
  - (0.200) [noise] Empty sessions contain no signal.
[demo] done — no Layer 3 in this reference; see ADR-0005.
```

The demo uses a deterministic fake LLM so the whole pipeline runs offline.
To plug in a real model, replace `fake_llm` in `demo.py` with any callable
of type `(prompt: str) -> str`.

## Provenance

The three core modules are adapted from the
[contemplative-agent](https://github.com/shimo4228/contemplative-agent)
research repository (commit `2dbde9d`). Project-specific content has been
removed; each file carries an in-file credit at the top. See
[`docs/inspiration.md`](../../docs/inspiration.md) for the full attribution.
