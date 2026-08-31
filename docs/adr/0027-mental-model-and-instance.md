# ADR-0027: Mental Model and Instance — Core Owns Judgment, Instances Ground It

> **Summary.** The mechanism-only inclusion rule kept domain content out of AKC's core by confining concrete instances to `examples/`, in service of genre neutrality (ADR-0011) and the cycle-not-harness boundary (ADR-0009). ADR-0018 then made downstream applications first-class as relationship facts and DOIs. Practice outgrew the wording: the README's phase table already links ten running skill instances, two concept-scaffold repositories were linked from the front door (one, human-gate, is unlinked in this same release as a retired instance), and the v2.7.0 release presents the running four-layer operational form ahead of the six-phase mechanism. On 2026-09-01 the same rule was cited, in session, to justify withholding the instance links behind the Worldviews and Enforcement layers — and the author's verdict was that the rule now obstructs understanding: a mechanism without a visible instance cannot be understood, and excluding two rows while ten skill links already stand is incoherent. ADR-0027 replaces the mechanism/content cut with the accurate one — **mental model versus instance**. Core owns the judgment (ADRs, concepts, cycle structure); instances are linked as first-class grounding, not inlined; and links follow the running state, retired dated rather than left to rot.

## Status

accepted

## Date

2026-09-01

## Context

The mechanism-only inclusion rule is the front-door convention that concrete instances live in `examples/` only, and that core, ADRs, the cycle figure, and `graph.jsonld` carry none. It was written to keep domain content from diluting the genre-neutral cycle ([ADR-0011](./0011-cycle-applies-to-any-knowledge-body.md)) and to keep AKC from becoming a harness ([ADR-0009](./0009-akc-is-a-cycle-not-a-harness.md)). [ADR-0018](./0018-record-downstream-applications-as-first-class-context.md) then made downstream applications first-class as relationship facts plus DOIs — a partial loosening, recording that a relationship exists without importing the content behind it.

Practice has outgrown the wording since. The README's phase table links ten running skill instances. Two concept-scaffold repositories were linked from the front door. The v2.7.0 release presents the running four-layer operational form before the six-phase mechanism it grounds — the instance-first ordering the rule's original wording did not anticipate.

This is also not the first time the rule's wording invited a misreading. [ADR-0019](./0019-cycle-structure-is-provisional.md) (2026-06-30) had already corrected the same conflation once — its Context records that "reference a skill" had been conflated with "import content", and that the mechanism-only rule forbids the latter, not the former. On 2026-09-01, in session, the conflation re-ran anyway: the rule was cited to justify *not* linking the instances behind the Worldviews and Enforcement layers, on the reading that instance links are content and content stays out. The author's verdict on reading that justification was that the rule now obstructs understanding rather than protecting genre neutrality: a mechanism without a visible instance cannot be understood, and with ten skill instances already linked from the same front door, excluding further rows on the same rule is incoherent — the rule was mostly not being followed, the exceptions were doing more work than the rule, and a correct reading that has to be re-derived per session is not holding (the same declaration-without-structure failure ADR-0026 records for the dated-hypothesis reading).

The author's diagnosis was that "content" had conflated two different things. One is domain genre — which behavioral pattern, which value set, which threat model flows through the cycle — and that stays out per ADR-0011; AKC still takes no position on it. The other is a running instance — a skill, a rule, a hook, a gate, a loop — that demonstrates the mechanism operating; excluding those from the front door does not protect genre neutrality, it just makes the mechanism illegible. The proposed correction is the accurate reorganization: mental model versus instance.

## Decision

1. **The load-bearing distinction is mental model / instance, not mechanism / content.** AKC core owns the mental model — judgments (ADRs), concepts (`graph.jsonld`), the cycle structure. Instances — running skills, rules, hooks, gates, loops — are owned downstream and linked as first-class grounding. What remains prohibited is inlining instance content into core (duplication): a link may carry a one-to-two-line relation fact saying what the instance is and how it relates; anything longer reproduces the instance and crosses the line. The domain-content position is unchanged: [ADR-0011](./0011-cycle-applies-to-any-knowledge-body.md) is untouched, and which genre of knowledge flows through the cycle is still not AKC's concern.

2. **Grounding expectation.** Every mechanism concept carries an edge to at least one public instance where one exists — in the graph, an `implements`-direction edge; in the front door, a link. A concept with no public instance says so rather than hiding it. The expectation applies from this release forward: concepts recorded before it mostly carry ADR-direction (`groundedIn`) edges only, and backfilling their `implements` edges is a named open obligation, not a silent assumption (see Consequences).

3. **Links follow the running state.** When an instance retires from the running practice, the front-door link is removed or annotated, dated; a retired instance's graph node remains as a dated relation fact and still grounds its concept until a running instance replaces it. First instance of this discipline: the human-gate rule was retired from the operator's harness on 2026-08-02, with a retirement note published in the [human-gate repository](https://github.com/shimo4228/human-gate) itself; its README link is removed in this release on the author's direction of 2026-09-01. The repository remains published as history.

4. **`examples/` keeps its existing role** for in-repo minimal instances.

## Review-when

If instance links begin pulling instance content inline — a front-door section reproducing the body of a rule or skill, rather than a dated link with a one-to-two-line relation fact — tighten back toward exclusion. If `implements`-direction instance edges come to outnumber Concept nodes in `graph.jsonld`, the concept layer is being crowded by its grounding; revisit the "every concept" expectation in Decision 2.

## Alternatives Considered

### Keep the mechanism-only wording and treat the existing links as tolerated exceptions

Rejected. The exception list already exceeds the rule — ten skill links plus the concept-scaffold repositories — and a rule mostly honored in the breach misleads future sessions about what the repository actually practices.

### Drop the boundary entirely and host instances inside AKC

Rejected. That turns AKC into a harness ([ADR-0009](./0009-akc-is-a-cycle-not-a-harness.md)) and re-couples the portable cycle to one operator's stack.

### Keep the mechanism/content vocabulary and add an "links are allowed" clause

Rejected, per the author's 2026-09-01 judgment: mental model / instance is the accurate cut. "Content" had conflated two different things — domain genre, which stays out per ADR-0011, and running instances, which ground the model — and patching the old vocabulary with an exception clause would leave that conflation in place for the next session to trip over.

### Change nothing and just add the links, on ADR-0019's reading

The strongest do-nothing variant: ADR-0019 had already ruled that the rule forbids importing content, not referencing instances, so the links could have been added under the existing vocabulary with no migration. Rejected because that correct reading had now failed to hold twice — ADR-0019 stated it in June, and the 2026-09-01 session re-derived the wrong reading anyway. A reading that must be re-explained per session is a declaration without structure, the failure mode ADR-0026 records; replacing the vocabulary that keeps inviting the misreading is the structural fix.

## Consequences

### Positive

- The front door can ground every layer of the operational form in a visible instance; a mechanism no longer has to be taken on faith.
- The incoherence between the rule as written and the rule as practiced is resolved in the direction practice had already taken.
- Retirements become dated, visible events instead of silent link rot: the human-gate case is now a recorded instance of the discipline rather than an implicit gap.

### Negative

- Link maintenance becomes a standing obligation. The running state changes faster than releases, so links can lag between releases.
- The Worldviews, Enforcement, and Attention topology rows' harness-side instances live inside the bundled harness distribution rather than as standalone repositories, so their front-door links (added in this release, on the author's 2026-09-01 direction) point at file paths inside that distribution — more brittle than repository-root links, and a sharper form of the link-maintenance obligation above when the harness restructures.
- The grounding expectation ships unmet for most of the existing concept layer: the pre-existing Concept nodes carry ADR-direction (`groundedIn`) edges, not `implements`-direction instance edges, even where public instances exist (the design-pattern skill repositories among them). Backfilling those edges is an open obligation this ADR names but does not perform.

### Neutral

- Genre-neutrality ([ADR-0011](./0011-cycle-applies-to-any-knowledge-body.md)) and cycle-not-harness ([ADR-0009](./0009-akc-is-a-cycle-not-a-harness.md)) are unchanged; this ADR moves the vocabulary that sits on top of them, not the positions themselves.
- [ADR-0018](./0018-record-downstream-applications-as-first-class-context.md)'s relationship-facts discipline is extended, not replaced.
- [ADR-0024](./0024-judge-build-human-three-role-loop.md)'s scope clause — ledger mechanics recorded as relation facts, per the mechanism-only inclusion rule — is unchanged in substance and now reads under the new vocabulary.

## Relationship to other ADRs

- **[ADR-0018](./0018-record-downstream-applications-as-first-class-context.md) (Record Downstream Applications as First-Class Context).** Extended: from "record downstream applications as first-class context" to "ground every mechanism concept in an instance." The relationship-facts discipline ADR-0018 established is the mechanism this ADR generalizes into a standing expectation.
- **[ADR-0009](./0009-akc-is-a-cycle-not-a-harness.md) (AKC is a Cycle, Not a Harness).** Bounds this decision: instances stay downstream — linking is not hosting. The cycle/harness layer separation is unchanged.
- **[ADR-0011](./0011-cycle-applies-to-any-knowledge-body.md) (Cycle Applies to Any Knowledge Body).** Unchanged: the domain-genre position survives the vocabulary change. What AKC does not take a position on is still which genre of knowledge flows through the cycle, not whether an instance may be linked.
- **[ADR-0019](./0019-cycle-structure-is-provisional.md) (The Cycle's Structure Is Provisional).** The closest prior decision on this subject: its Context already corrected the reference-vs-import conflation once, and its parsimony clause kept "the mechanism-only rule" as a live gate. That correct reading failed to hold (Context above); this ADR makes it structural, and ADR-0019's mechanism-only wording now carries a dated note pointing here. The parsimony function survives: the evidence bar and the inlining prohibition still gate what enters core.
- **[ADR-0026](./0026-expiry-conditioned-knowledge.md) (Expiry-Conditioned Knowledge).** Applied twice: the mechanism-only rule is read as a dated hypothesis whose premise expired, and the weakened load-bearing wording in ADR-0018, ADR-0019, and ADR-0024 received the dated in-place notes ADR-0026's Decision 3 prescribes — the first uses of the `> **Note**` form on published ADRs.
- **[ADR-0024](./0024-judge-build-human-three-role-loop.md) (The Judge/Build/Human Three-Role Loop).** Its Decision 2 scope clause, recording ledger mechanics as relation facts per the mechanism-only inclusion rule, reads unchanged in substance under this ADR's mental-model/instance vocabulary.
