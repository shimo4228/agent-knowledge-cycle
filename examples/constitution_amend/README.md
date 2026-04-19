# constitution_amend — cycle-on-values example

An example of the AKC cycle applied to **constitutional values** rather than behavioral patterns. This directory contains no implementation; it points at the canonical instance that already exists in [contemplative-agent](https://github.com/shimo4228/contemplative-agent) and maps it to the AKC phases so a reader can see how the same cycle handles a different knowledge body.

This example exists because of ADR-0011 (genre neutrality): the cycle is a mechanism, and constitutional values are one valid thing the mechanism can operate on. `minimal_harness/` demonstrates the mechanism on behavioral patterns; `constitution_amend/` demonstrates it on values.

## What Constitution-amend does

Constitution-amend is a workflow that feeds accumulated constitutional experience back into an agent's ethical axioms. Instead of the operator rewriting axioms by hand when lived evidence suggests a gap, the cycle collects evidence, evaluates whether enough has accumulated, and proposes an amended constitution for human review.

The canonical implementation in contemplative-agent consists of two artifacts:

- A Python function (`amend_constitution`) that orchestrates the pipeline: retrieves constitutional patterns from the knowledge store, filters via a view registry to the constitutional slice, runs a minimum-evidence check (≥3 patterns), and calls an LLM with the amend prompt.
- A prompt template (`constitution_amend.md`) that instructs the LLM to amend the constitution while preserving structure, augmenting only (never deleting original clauses), and consolidating within a per-section cap.

Files are not written by the function — the human approval gate (matching AKC's ADR-0005) is the caller's responsibility.

## Mapping to the AKC cycle

| AKC phase | Behavioral instance (`minimal_harness/`) | Constitutional instance (contemplative-agent) |
|-----------|------------------------------------------|-----------------------------------------------|
| **Research** | Signal-first intake of session evidence | Same — signals that bear on ethical behavior are admitted; noise is not |
| **Extract** | Free-form reflection → structured pattern via two-stage distill | Same distill pipeline; constitutional patterns are tagged for the "constitutional" view |
| **Curate** | Audit knowledge store for staleness and redundancy | View registry routes patterns by semantic relevance to the constitutional view |
| **Promote** | Recurring pattern becomes a rule after human approval | `amend_constitution` proposes an updated axiom file when ≥3 constitutional patterns accumulate; human approval required before write |
| **Measure** | Compliance check: does the agent follow the promoted rule? | Same shape: does behavior align with amended axioms? |
| **Maintain** | Context sync: docs, skills, rules stay aligned with code | Same shape: axiom files, identity templates, and distill prompts stay aligned |

The mechanism is identical. What changes is the knowledge body — behavioral observations vs. constitutional patterns — and therefore the evaluation criteria, the prompt templates, and the audit queries.

## Why this lives in `examples/`, not `docs/skills/`

ADR-0011 commits that `docs/skills/` hosts only cycle-mechanic skills — not content-tied workflows. Constitution-amend is content-tied: it carries opinions about what belongs in a constitution, what counts as a constitutional pattern, and what kinds of amendments are legitimate. Those opinions belong with the genre that holds them (the contemplative-agent lineage), not with AKC.

`examples/` is the right home because it is **descriptive** rather than **prescriptive**. `minimal_harness/` shows how the three-layer memory works; `constitution_amend/` shows how a downstream project runs the cycle on values. Neither example claims to be normative AKC guidance. AKC ships no constitution, no axioms, and no opinion on which values a downstream project should hold.

## Where to find the implementation

The Python function, prompt template, and supporting view-registry code live in the [contemplative-agent](https://github.com/shimo4228/contemplative-agent) repository. Look for:

- `core/constitution.py` — the `amend_constitution` function
- `config/prompts/constitution_amend.md` — the LLM prompt template
- The view registry that filters patterns by semantic relevance to the constitutional slice

Replicating the pattern for a different values system (a different constitution, a different axiom file, a different set of ethical commitments) is a matter of supplying the corresponding prompts, axiom files, and view filters — the cycle wiring stays the same.

## Related

- [ADR-0011 Cycle Applies to Any Knowledge Body](../../docs/adr/0011-cycle-applies-to-any-knowledge-body.md) — the positioning statement that makes this example legitimate.
- [`minimal_harness/`](../minimal_harness/) — the behavioral-pattern counterpart. Same mechanism, different knowledge body.
- [`docs/inspiration.md`](../../docs/inspiration.md) — contemplative-agent as prior art and upstream home for genre-specific content.
