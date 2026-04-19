# ADR-0011: Cycle Applies to Any Knowledge Body

> **Summary.** AKC's cycle is a mechanism, not a content filter. The six phases operate on any coherent body of agent knowledge — behavioral patterns, domain expertise, or constitutional values — and AKC takes no position on which of those a downstream project cares about. This ADR pairs with the ADR-0009 addendum extracting the security triplet: the extraction is the concrete act, and this ADR is the principle that explains why such extractions are correct whenever a knowledge body belongs to a specific genre rather than to the cycle itself.

## Status
accepted

## Date
2026-04-19

## Context

Through v1.x, AKC carried ADR-0001 Security by Absence, ADR-0006 Single External Adapter, and ADR-0007 Untrusted Content Boundary as core ADRs. ADR-0009 (2026-04-11) demoted Security by Absence from a co-equal pillar to Design Principle #7, but the demotion was rhetorical. The underlying files — two ADRs and the `llm-agent-security-principles.md` skill — remained in the repository, carrying a specific threat model inherited from contemplative-agent: a local autonomous agent making side effects in the world through a narrow adapter surface.

v2.0.0 completes the work ADR-0009 started by extracting those files entirely. See the ADR-0009 addendum (2026-04-19) for the concrete decision. What that extraction surfaces, and what this ADR records, is the principle: the security triplet was not wrong, it was *genre-specific*. The cycle does not require it, does not forbid it, does not have an opinion on it. An AKC user building a pure documentation-distillation agent does not need Security by Absence as an AKC-level principle. A contemplative-agent clone does. The cycle works identically for both.

This raises a positioning question the repository had been ducking: can the cycle run on *values* — an agent's constitution, its four axioms, its identity statements — the same way it runs on engineering patterns? The structural answer is yes. Extract → Curate → Promote is the same mechanism whether it operates on "the agent kept re-deriving the two-stage distill pattern" (behavioral) or on "the agent kept encountering situations where compassion was the load-bearing criterion" (constitutional). AKC had no ADR taking a position on this, and without one, the repository would drift either toward importing values-specific content (re-doing the security-triplet mistake in a new domain) or toward denying that values can run through the cycle at all.

The right answer is the minimal one: declare the cycle genre-neutral and let each downstream project own its content.

## Decision

AKC adopts **Genre Neutrality** as a first-class positioning statement:

> The cycle is a mechanism. The content that flows through the cycle is the downstream project's concern, not AKC's. AKC takes no position on whether a knowledge body is behavioral, domain-specific, or constitutional. The same six phases apply identically to all of them.

Three falsifiable commitments follow:

1. **No future ADR in AKC will encode domain-specific content beyond what the six phases require.** If a future decision pressures the repository to adopt a specific threat model, a specific value set, a specific adapter philosophy, or any other opinion tied to one class of agent, that decision belongs in a downstream project — not here.
2. **`docs/skills/` will host only cycle-mechanic skills.** The three remaining design-pattern skills (`when-code-when-llm`, `code-and-llm-collaboration`, `signal-first-research`) describe how the cycle works, not what it works on. A PR adding, for example, a "constitutional-values-distillation.md" skill would violate this commitment and require revisiting ADR-0011.
3. **External projects may cite AKC as their cycle substrate.** Contemplative-agent-rules can cite AKC for Extract/Curate/Promote mechanics while owning its own axioms. A compliance-automation harness can do the same while owning its own regulation catalogue. AKC makes no claim about either set of content; it claims only that the cycle is how knowledge about either set stays coherent over time.

### What this decision does not add

- No new skill. Genre neutrality is a positioning claim, not a workflow. A `constitution-amend` skill would immediately violate commitment 2 and would replay the security-triplet's fate. The right place for such workflows is whatever downstream project runs the cycle on values.
- No new phase. The existing six phases already accommodate any knowledge body; adding a "values-specific" phase would claim AKC has an opinion on values, which contradicts the decision itself.
- No change to ADR-0003 three-layer distillation. Layer 3 (Identity and Rules) already accommodates any kind of promoted knowledge — behavioral or constitutional. Naming values specifically inside ADR-0003 would over-constrain a deliberately general architecture.

## Alternatives Considered

- **Add a `constitution-amend` skill.** Rejected. A skill tied specifically to values would re-import the genre-specificity that ADR-0009's addendum just extracted. Future readers would infer that AKC cares about constitutional content; the extraction's whole point is that it does not. Downstream projects already have `contemplative-agent-rules/rules/contemplative/` for this — AKC does not need a parallel location.

- **Expand ADR-0003 to name "values" at Layer 3.** Rejected. ADR-0003 describes memory shape: Layer 1 raw, Layer 2 distilled, Layer 3 promoted. The shape is genre-neutral by construction — rules that come out of ADR-0003's Layer 3 can be engineering rules or axioms, and ADR-0003 does not ask which. Adding values-specific language would turn a structural ADR into a content ADR.

- **Write ADR-0011 plus a skill.** Rejected as strictly worse than ADR-only. The skill adds discoverability the ADR does not, but discoverability is exactly the mechanism by which genre-specific content re-enters the repository. Every skill is a magnet for examples, and examples become opinions. The ADR-only path starves that magnet.

- **Do nothing; let each user infer genre neutrality.** Rejected. ADR-0009 demonstrated that implicit positioning drifts: the security triplet sat in AKC for months after it had conceptually outgrown it. Without an ADR declaring genre neutrality explicitly, the next genre-specific contribution (from the author or from a downstream contributor) would accumulate the same way the security triplet did.

## Consequences

### Positive

- The mechanism/content boundary becomes citeable. Projects building on AKC can state that they are using AKC for the cycle while retaining their own values, axioms, threat models, or domain content — no confusion about whether AKC sanctions those specifics.
- Future PRs have a clear test. Anything that encodes genre-specific content has to make its case against the three commitments above. Genre neutrality is no longer a feeling; it is a reviewable criterion.
- The security-triplet extraction (ADR-0009 addendum) is no longer a one-off event but an instance of a principle. If another genre-specific artifact surfaces later, the extraction path is already laid out.

### Negative

- AKC becomes less useful as a standalone recipe for "how to build an agent like contemplative-agent." It never was that, but users who inferred it was will have a clearer disappointment. The README, Related Work section, and inspiration.md all point at contemplative-agent for that purpose; after ADR-0011 the pointing becomes mandatory rather than optional.
- The discoverability cost mentioned above is real. Users who need a values-amendment workflow have to find or build it themselves. AKC will not host it.

### Neutral

- No code changes. No schema changes. No change to the six phases or the reference implementation. This is a positioning ADR; its effect is on future PRs, not on current files beyond what the R1 quarantine already did.

## Relationship to other ADRs

- **ADR-0009 AKC is a Cycle, Not a Harness** — ADR-0009 declared the cycle as the sole defining characteristic. ADR-0011 generalizes that declaration: the cycle is defining precisely because it is genre-neutral about what flows through it. Read ADR-0009's 2026-04-19 addendum together with this ADR.
- **ADR-0003 Three-Layer Distillation** — ADR-0003 is the structural counterpart. Memory shape is genre-neutral; ADR-0011 says content is, too.
- **ADR-0010 Human Cognitive Resource as Central Constraint** — ADR-0010 identifies the scarce resource that motivates the cycle. The human running the cycle may be working on engineering patterns, scientific findings, or ethical axioms. ADR-0010's constraint applies equally to all; ADR-0011 names why.

## Concrete instance in the wild

The [contemplative-agent](https://github.com/shimo4228/contemplative-agent) project has a Constitution-amend workflow (`core/constitution.py` + `config/prompts/constitution_amend.md`) that runs the AKC cycle on constitutional values: constitutional patterns accumulate in the knowledge store, the amend function retrieves them via a view registry, proposes an updated axiom file when ≥3 patterns accumulate, and defers the file write to a human approval gate. The mechanism is the same one `examples/minimal_harness/` demonstrates; only the knowledge body differs.

A description of the mapping, along with a phase-by-phase comparison to `minimal_harness/`, lives in [`examples/constitution_amend/`](../../examples/constitution_amend/). That directory intentionally ships no implementation — the canonical code is in the contemplative-agent repository — so AKC retains genre neutrality while making the structural claim of this ADR observable.

---

**Notes.** This ADR was prompted by a conversation about where a "Constitution-amend" workflow belongs. The structural observation — that Extract → Curate → Promote is isomorphic whether operating on engineering patterns or on constitutional values — invited a choice: absorb the workflow into AKC, or declare that AKC does not own it. Absorbing would have re-imported the mistake that the security triplet made visible. Declaring genre neutrality is the version that stays small, stays honest, and lets downstream projects own what they should own.
