# ADR-0019: The Cycle's Structure Is Provisional — Skills, Bindings, and Phases Held Lightly

> **Summary.** The phase-to-skill binding is a snapshot of mutable scaffolding, not a fixed bijection. Curate is layered: skill-health (structural, code-owned, ADR-0008) clears dangling-reference debt before skill-stocktake (semantic, LLM-owned) judges quality. The skill set both grows (skill-health joins) and dissolves (skill-comply may be absorbed by the host harness), and the six-phase decomposition itself is the current best articulation, not a fixed essence. Per the Emptiness axiom, AKC holds its own structure provisionally — including this ADR.

## Status

accepted — for the provisionality principle and the Curate code-layer decision. skill-comply's substrate-dissolution is recorded as an **experimental** observation (n=1), not a retirement.

## Date

2026-06-30

## Context

graph.jsonld encodes a "bijective phase-to-skill binding" and names it load-bearing: each of the six phases is "bound bijectively" to exactly one skill (Curate ↔ skill-stocktake). A positioning question — where does the harness skill `skill-health` sit in the cycle? — was run through a four-lens council. skill-health is a deterministic structural lint: it scans a skill library for *missing artifacts* (a SKILL.md that references a script, agent, or sibling skill that no longer exists on disk). Reading the binding as an inviolable invariant, the council concluded skill-health was effectively *forbidden* from the cycle: a second skill in Curate would break the bijection, and a specific `~/.claude` skill is an "instance," which the mechanism-only rule keeps out of core.

That conclusion was a reification error, and the operator caught it. Three of its load-bearing steps do not survive inspection:

1. **The bijective binding was treated as a fixed essence rather than a snapshot.** AKC's own ADR-0008 (Code-LLM Layering) says pipelines layer code and LLM and that the patterns compose; its guard section draws the line precisely — *the structure of a structural check is mechanism; only the populated rubric is content*. skill-health is exactly that: the structural, code-owned half (does a reference resolve? a filesystem `exists()` at 100% accuracy), distinct from the SkillOps four-dimension health rubric (content, which correctly stays in the skill). ADR-0008 does not merely permit a code layer in Curate — it predicts one.

2. **"Reference a skill" was conflated with "import content."** AKC already references nine specific skill instances (six cycle skills + three design-pattern skills) as external repositories. Naming skill-health as Curate's code layer is the same kind of reference, not an import of genre-specific content. The mechanism-only rule forbids the latter, not the former.

3. **The absence of skill-health from the repo was read as deliberate exclusion, and "no observed pain" as decisive.** In fact, running skill-health as the structural pre-pass to Curate is long-standing operator practice — the repeated-practice evidence the bar accepts. The absence was an *unrecorded* practice, not an exclusion.

The first correction, taken alone, invites a second reification: declare "the six phases" the new invariant beneath the mutable skills. The operator rejected this too, on the Emptiness axiom (contemplative-axioms, Laukkonen et al. 2025, Appendix C): *"all beliefs, goals, and conceptual frameworks are provisional and lack any fixed, ultimate essence … refrain from rigidly reifying any single objective as final."* Reifying the phase set repeats the same mistake one level up. AKC's own Theme 2 already implies this: intent is a *moving* criterion, and a cycle whose target moves cannot freeze its own frame.

## Decision

AKC holds its own structure provisionally. No layer of the cycle's self-description — skills, bindings, or the phase set — is a fixed essence; each is the current best articulation, load-bearing for now and revised through the cycle's own operation (the Maintain and Curate phases already operate on AKC's self-description, ADR-0018).

Concretely:

- **The phase-to-skill binding is a snapshot, not a bijection.** Each phase currently has zero-or-more bound skills. Where a phase's work is layered (ADR-0008), it carries both a structural/code skill and a semantic/LLM skill. graph.jsonld, the README phase table, and llms.txt are reworded from "bound bijectively to X" to "currently scaffolded by X (a snapshot, mutable per this ADR)."

- **Curate is layered.** Its code/structural layer is **skill-health** (dangling-reference / missing-artifact scan; deterministic; an ADR-0008 guard); its semantic/judgment layer is **skill-stocktake** (Keep/Improve/Retire/Merge). The order is enumerate-then-decide: skill-health clears structural debt, then skill-stocktake judges what survives. skill-health is published as a standalone repository (`github.com/shimo4228/skill-health`) and referenced like the other cycle skills. The SkillOps health rubric stays in the skill (content), not in AKC core.

- **The skill set both grows and dissolves.** skill-health *joining* Curate and skill-comply *possibly leaving* Measure are one phenomenon in two directions. On current operator observation, skill-comply (Measure) is becoming unnecessary as the host harness (Claude Code) absorbs skill-compliance natively — the downward / substrate-absorption vector of scaffold dissolution. This is recorded as **experimental** (n=1, an emerging judgment), not a retirement; if it holds, skill-comply dissolves the way the 2026-06-10 platform-absorption observation already retired six skills and one rule.

- **The phase set is provisional too.** Six phases is the current decomposition, not a fixed count. "Six phases" stays in the front-door docs as the present articulation — framed as provisional rather than removed; a future deepening may merge, split, or rename phases without that being an "invariant violation."

- **This ADR is provisional.** It records a disposition — hold the structure lightly, revise through the cycle — not a new fixed frame. What persists across revisions is the disposition and the judgment lineage, not any particular structure.

## Alternatives Considered

- **Keep the bijective binding as an invariant and exclude skill-health.** Rejected: it fabricated a prohibition that contradicts long-standing practice, mistaking mutable scaffolding for fixed essence, and would force inverting skill-health's own correct self-positioning.
- **De-reify the skills but declare the six phases invariant.** Rejected: it relocates the same reification one level up and contradicts the Emptiness axiom and Theme 2's moving criterion.
- **Add skill-health as a seventh phase, or renumber the cycle.** Rejected: skill-health is a *layer within* Curate, not a new phase; the phase count is not changed by this ADR, only de-reified.
- **Treat the structure as arbitrary flux.** Rejected: provisional is not arbitrary. The structures remain the load-bearing current articulation, used and useful; they are held lightly, not discarded.
- **Import the SkillOps four-dimension rubric into AKC core as mechanism.** Rejected: a populated rubric is content (the ADR-0008 guard line, ADR-0011); only the structural discipline is mechanism. The rubric stays in skill-health.

## Consequences

- The "bijective phase-to-skill binding" language is retired across graph.jsonld, README en/ja, and llms.txt in favor of a mutable-snapshot framing; Curate gains skill-health as its code layer alongside skill-stocktake.
- A future skill addition or dissolution (skill-comply, others) is normal cycle operation, not an invariant violation — removing the friction that made the council fabricate a prohibition.
- skill-health is published and referenced like the other cycle skills; its rubric stays content-side.
- The repo's parsimony is preserved differently: not by a fixed skill/phase count, but by the mechanism-only rule and the evidence bar continuing to gate what enters core. Provisionality is not a license to add freely — observed pain or repeated practice is still required.
- A risk: "everything is provisional" can be misread as "nothing is load-bearing," weakening the cycle's usefulness as a stable reference. Mitigation: the docs state the structure is the current best articulation and load-bearing now; *provisional* governs revisability, not present authority.
- skill-comply's status is now openly uncertain. Measure is not removed; its compliance-checking function is flagged as a candidate for substrate absorption — tracked, not decided.

## Relationship to other ADRs

- **Extends ADR-0009 (cycle, not harness).** ADR-0009 made the cycle AKC's sole defining characteristic; ADR-0019 adds that even the cycle's structure is held provisionally — the defining characteristic is the disposition to revise it, not its current shape.
- **Applies ADR-0008 (Code-LLM Layering).** Curate's two layers (skill-health structural / skill-stocktake semantic) are the concrete per-phase instance ADR-0008's patterns previously lacked; the guard / threat-model line is what keeps the rubric content-side.
- **Bounded by ADR-0011 (genre neutrality / mechanism-only).** Referencing skill-health is permitted; importing its populated rubric is not.
- **Continues ADR-0018 (cycle on its own self-description).** ADR-0018 ran a Maintain pass on the repo's self-description; ADR-0019 extends the target of that self-revision to the binding and phase structure themselves.
- **Grounded in contemplative-axioms (Emptiness).** The provisionality of all frameworks, held lightly, is the axiom this ADR operationalizes for AKC's own structure.
