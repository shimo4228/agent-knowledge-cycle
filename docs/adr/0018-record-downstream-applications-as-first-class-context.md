# ADR-0018: Record Downstream Applications as First-Class Context

> **Summary.** While drafting the AKC position paper (2026-06-06), the author found that the repository could not serve as its own primary source: it lacked the downstream context the paper required. AKC is the start-of-program repository — formalized and DOI-registered first — yet its self-description of Contemplative Agent was past-direction only ("upstream engineering substrate"), with no record that the same repository now re-implements the six-phase cycle as running code. Four DOI-registered downstream repositories (authorship-strategy, attention-not-self, doctrine-corpus, existence-proof) were entirely unmentioned. This is an instance of the Maintain phase's own concern — documentation drifting from reality — occurring in the repository that defines the phase. ADR-0018 records the corrective: AKC documents its downstream applications as first-class context, recording relationship facts and DOIs only, importing no downstream content, and preserving the mechanism-only inclusion rule.

## Status

accepted

## Date

2026-06-06

## Context

AKC is the start-of-program repository: its core thesis, six phases, and three memory layers were formalized and DOI-registered before any downstream work existed. Later repositories grew from the same daily operation the cycle runs in, and they reference AKC explicitly. Contemplative Agent calls itself "the operational implementation" of AKC, maps its pipeline onto the six phases in its README ("This pipeline is the AKC six phases mapped onto code"), and tags 11 of its own ADRs with `[AKC: phase]` markers. Three of the four DOI-registered downstream repositories — authorship-strategy (10.5281/zenodo.20263316), attention-not-self (10.5281/zenodo.20262112), and doctrine-corpus (10.5281/zenodo.20337008) — reference AKC's concept DOI in their deposit metadata; the fourth, existence-proof (10.5281/zenodo.20558800), is a pre-line working repository that references authorship-strategy.

AKC itself, completed early, did not know its own downstream. Its description of Contemplative Agent ran in one direction only: "upstream engineering substrate that seeded ADR-0002–0005." This framing was accurate at the time it was written. It is now incomplete. Contemplative Agent re-implements the six-phase cycle as code and runs it over its own episode logs, with every promotion human-gated — a demonstration of the cycle operating under the conditions AKC specifies. That role change is not recorded anywhere in the AKC repository. The four downstream DOI repositories are not recorded at all.

The consequence surfaced concretely during drafting of the AKC position paper. The paper's evidence claim — the cycle runs as Markdown skills on the author's Claude Code harness and as a code re-implementation in Contemplative Agent — requires both instances to be attested in the primary source. The primary source is this repository. The repository contained neither the Contemplative Agent re-implementation fact nor the downstream research line. The paper could not cite AKC for its own two-instance evidence.

This is a Maintain-phase failure: documentation drifting from reality. The Maintain phase description in docs/akc-cycle.md names exactly this pattern — "Check numeric claims against reality" and "Remove or update stale content rather than letting it accumulate." The failure is occurring in the repository that defines the phase, which is the Maintain phase's own self-application condition.

A secondary observation: the repository's bidirectional-growth tagline ("the cycle grows with the people who shape it") had no observable evidence in the repository while the evidence existed one repository away.

## Decision

AKC records its downstream applications as first-class context. The decision has four clauses.

1. **Record Contemplative Agent's role as two-way.** The upstream substrate fact (ADR-0002–0005 adapted from Contemplative Agent) is preserved. The downstream re-implementation fact is added alongside it: Contemplative Agent re-implements the six-phase cycle in the autonomous-agent context, runs the cycle over its own episode logs, and gates every promotion through a human approval gate — demonstration ongoing. Wording stays verbatim-consistent with Contemplative Agent's own public record to prevent paraphrase drift.

2. **Record research lines and working repositories with relationship facts and DOIs.** Four DOI-registered repositories crystallized from the same daily operation the cycle runs in — authorship-strategy (10.5281/zenodo.20263316), attention-not-self (10.5281/zenodo.20262112), doctrine-corpus (10.5281/zenodo.20337008), and existence-proof (10.5281/zenodo.20558800) — and are recorded in README, llms.txt, and graph.jsonld. Distribution-layer repositories (claude-harness, akc-mcp, daily-research, research-program hub) are recorded in graph.jsonld and llms-full.txt only.

3. **Record relationship facts and DOIs only — import no downstream content.** No strategy payloads, corpus content, or threat models from downstream repositories enter AKC's core. The mechanism-only inclusion rule (CLAUDE.md) is preserved: AKC records relationships between artifacts, not the content of those artifacts.

4. **Encode the downstream relationships in graph.jsonld.** Contemplative Agent gains an `implements` edge to the six-phase-loop concept, using the same predicate the minimal_harness reference implementation uses. The AKC research line gains `workExample` edges to Contemplative Agent and minimal_harness. The four DOI-registered downstream repositories gain `derivesFrom` / `siblingOf` edges as their relationship warrants.

## Alternatives Considered

### Leave the silence as design

Treat the absence of downstream documentation as a deliberate choice ("AKC does not document reverse dependencies"). Rejected: the silence was not a choice, it was staleness. The paper-drafting attempt surfaced it as observed pain — the repository could not serve as its own primary source. A deliberate choice would have been recorded at the time; there is no such record. The bidirectional-growth tagline had no observable evidence in the repository while the evidence existed one repository away.

### Record only in CHANGELOG as maintenance work, no ADR

Treat the downstream additions as routine maintenance and record them only in the CHANGELOG. Rejected: the role change of Contemplative Agent — from past-direction substrate to substrate plus running re-implementation — is a positioning judgment. Future sessions returning to the self-description of Contemplative Agent must not silently revert that judgment by re-applying the old framing. Positioning judgments of this kind are what the decision record exists for; CHANGELOG entries carry no such forward constraint.

### Import downstream content wholesale

Describe what authorship-strategy or doctrine-corpus contain — their strategies, corpus structure, or threat models — rather than recording only relationship facts and DOIs. Rejected: this violates the mechanism-only inclusion rule (CLAUDE.md) and the falsifiable commitments of [ADR-0011](./0011-cycle-applies-to-any-knowledge-body.md). AKC records relationships, not content. The downstream repositories own their own content; importing it would bind AKC's core to content that evolves and belongs elsewhere.

## Consequences

### Positive

- The repository becomes self-sufficient as the primary source for the position paper's two-instance evidence claim: the cycle runs as Markdown skills on the author's Claude Code harness and as a code re-implementation in Contemplative Agent, with both instances now attested here.
- The bidirectional-growth tagline gains observable evidence: the downstream research line (authorship-strategy, attention-not-self, doctrine-corpus, existence-proof) is what the daily operation crystallized.
- LLM-facing surfaces (graph.jsonld, llms.txt, llms-full.txt) expose the downstream ecosystem for citation and discovery; queries that arrive via the downstream repositories can now navigate back to AKC's primary source.
- The Contemplative Agent description is made accurate in both directions, removing a source of future confusion for agents reading the repository as a navigator (CLAUDE.md use case).

### Negative

- Downstream descriptions can go stale again as downstream repositories evolve and re-release. This mapping adds a recurring Maintain-phase obligation: re-check cross-references when downstream repositories issue new versions or change their self-descriptions.
- The existence-proof entry is the weakest edge: that repository carries no direct AKC reference and self-describes as pre-line. Its entry preserves that status discipline verbatim; recording it at all is a judgment call that adds a relationship the downstream side does not assert.

### Neutral

- No change to the six phases, three core themes, design principles, JSON schemas, or reference implementation. ADR-0018 is a documentation and graph-encoding decision; it introduces no new mechanism.
- The Maintain phase's definition is unchanged. This ADR is itself the record of a Maintain-phase execution on the repository's own self-description — an instance of the phase running, not a revision of what the phase is.

## Relationship to other ADRs

- **[ADR-0009](./0009-akc-is-a-cycle-not-a-harness.md) (AKC is a Cycle, Not a Harness).** Unaffected. The downstream mapping records relations between artifacts, not a runtime dependency of AKC on its downstream repositories. The cycle/harness layer separation ADR-0009 drew is preserved.
- **[ADR-0011](./0011-cycle-applies-to-any-knowledge-body.md) (Cycle Applies to Any Knowledge Body).** The downstream mapping observes ADR-0011's three falsifiable commitments: no domain content enters AKC's core, only relationship facts and DOIs. The four downstream repositories are evidence that the cycle ran on different knowledge bodies; AKC records the relationships, not the bodies.
- **[ADR-0013](./0013-positioning-within-agent-memory-literature.md) (Positioning Within the Agent-Memory Literature).** Complemented. ADR-0013 positions AKC against external prior art; ADR-0018 positions AKC within the author's own program. The two positioning axes are orthogonal.
- **The Maintain phase definition** (docs/akc-cycle.md). This ADR is itself the record of a Maintain-phase execution on the repository's own self-description: the phase's concern — documentation drifting from reality — occurred here, and this ADR is the corrective. No change to the Maintain phase definition is made; the event is recorded as an instance, not a revision.

---

**Notes.** The trigger was a paper-drafting session in which the repository could not serve as its own primary source. The structural cause was not a missing ADR but missing documentation of the downstream ecosystem. ADR-0018 records the corrective decision — record downstream applications as first-class context, import no downstream content — so future sessions do not silently revert the Contemplative Agent description to the past-direction-only framing. The existence-proof entry is marked explicitly as the weakest edge; its inclusion preserves the status discipline that downstream establishes for itself. All four DOI strings are taken verbatim from the deposit metadata of the downstream repositories.
