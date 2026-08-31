# ADR-0024: The Judge/Build/Human Three-Role Loop as the Operational Form of Attention Scarcity

> **Summary.** ADR-0005 gates every behavior-shaping change on named human sign-off; ADR-0010 names human attention and judgment, not model compute, as the cycle's central constraint. In the operator's harness practice, task ledgers grew because filing is the cheapest operation available, and by 2026-08-17 the observed ledgers held no dispatchable work — the bottleneck was judgment, not implementation. A gate alone does not scale that constraint: when the human is also the judge of every open task, the scarce resource is spent on triage rather than on direction. Since 2026-08-17 the operator's harness has run a three-role loop instead — a judge tier that verifies each task's premise, decides whether it is worth doing, dispatches accepted work, and independently inspects results; a build tier that implements and halts on a refuted premise; and a human who holds only direction-setting and the final merge switch. ADR-0024 names this loop a mechanism-level concept of the cycle: the operational form the human approval gate takes under attention scarcity. The gate itself is unchanged — binary, human, positioned at merge — what moves upstream to the judge tier is attention, not authority.

## Status

accepted

## Date

2026-09-01

## Context

ADR-0005 requires named human sign-off on every change that shapes future agent behavior — the gate is extrinsic by design and stays so. ADR-0010 names the resource that gate is built to protect: not agent capability, not context window, but human cognitive resource — attention and judgment — as the scarcity the whole cycle is shaped around.

That naming was made at the level of the cycle's phases. What it did not yet describe was what happens when the artifact under the gate is not a single proposed change but an open-ended task ledger — a running list of candidate work that anyone, including the agent itself, can add to at near-zero cost. In the operator's harness practice, task ledgers grew for exactly that reason: filing a task is the cheapest operation in the system, cheaper than doing the work and cheaper than deciding whether the work is worth doing. By 2026-08-17 the observed ledgers had accumulated entries but no dispatchable work — every open item still needed a human read before it could be handed to an implementer. The bottleneck was judgment, not implementation. In one sibling repository, review-origin filings accounted for 22 of the 30 new entries in the period observed (the source record does not bound the observation window); a manual dispatch of 7 tasks on 2026-08-16 found that 2 of the 7 task premises were refuted at pre-implementation verification, before any implementation work began. These figures come from the operator's harness records, dated as noted, and are not reproduced or independently verifiable from this repository.

A gate alone does not scale under this condition. ADR-0005's gate is correctly binary and correctly human at the point where behavior changes — but a ledger of candidate tasks is upstream of that point, and if the human is also the one who reads, verifies, and triages every entry on the ledger, the scarce resource named in ADR-0010 is spent on sorting rather than on the direction-setting judgment the gate exists to protect.

Since 2026-08-17 the operator's harness has run a three-role loop in response. A **judge tier** — one stronger-model session per repository — verifies each task's premise against the code before any implementation is attempted, decides whether the task is worth doing at all, packages and dispatches the work that is accepted, and independently inspects the results once a build session reports completion. A **build tier** — a fresh session per task — implements the accepted work, records its evidence in commit bodies, and halts if it discovers the task's premise has been refuted rather than pushing through on a false premise. The **human** in this loop holds direction-setting and answers a digest of one decision per message rather than reading the ledger directly, and retains the one irreducible switch: the merge into main.

A prior operator record bears on how this loop should be read against the cycle's existing structure. A 2026-07-09 operator triage decision declined to bind task-ledger maintenance to the Maintain phase, on the grounds that it was too trivial — coordination-state hygiene, not knowledge-artifact hygiene (a translated paraphrase; the original is a row in the operator's private task ledger, not reproducible from this repository, like the numbers above). That decision was correct for what it covered, and the three-role loop does not reopen it: ledger hygiene is still not what this ADR records.

## Decision

1. **Name the three-role loop — judge / build / human — a mechanism-level concept of the cycle**: the operational form the human approval gate takes under attention scarcity. The judge tier spends model judgment to conserve human judgment (premise verification, worth-doing verdicts, dispatch, independent acceptance); the build tier implements; the human holds only direction and the final switch. The gate stays binary and human at the point of merge — what moves upstream to the judge tier is the attention the triage step consumes, not the authority the gate holds.

2. **Scope boundary.** AKC records the role topology only — that a judge tier verifies and dispatches, a build tier implements, and a human sets direction and merges. Ledger formats, claim/lease mechanics, scheduling, and digest plumbing are harness content; they are recorded solely as relation facts on the operator harness's ecosystem node in `graph.jsonld`, per the mechanism-only inclusion rule, not as mechanism in AKC's core.

3. **The 2026-07-09 rejection stands for what it covered.** Ledger hygiene remains outside the cycle; that disposition is not reversed. This clause is itself the dated weakening record: the original rejection lives in an operator-private ledger that cannot carry a published annotation, so its surviving scope (ledger hygiene stays out) and its expired premise — that there was nothing beyond hygiene to promote, which lapsed when the three-role topology emerged in practice on 2026-08-17 — are recorded here, dated, with the original left unedited. Rejection records are dated hypotheses, not permanent exclusions (ADR-0026, recorded in the same release as this ADR).

## Review-when

If the substrate comes to natively hold a judge → build → human-gate loop over a task ledger — resident workflow orchestration in the platform itself rather than an operator-assembled practice — the operational description recorded here collapses into a native capability, and the mechanism should be re-audited at the next generation review (the external clock named in [ADR-0023](./0023-generation-review-as-a-fourth-evidence-class.md)). If the human re-enters per-task judgment — a dispatch cycle in which the human reads the ledger directly instead of answering the judge tier's digest — the judge tier is failing to conserve the attention it is meant to conserve; record each such cycle as a dated instance in place, and treat two consecutive cycles of it as this condition firing.

## Alternatives Considered

### Leave it out entirely, letting the 2026-07-09 rejection stand as written

Rejected. That rejection covered ledger hygiene specifically. The three-role topology is about where finite human judgment sits in the cycle at large — exactly ADR-0010's subject matter — and declining to record it would leave Theme 1 (human cognitive resource scarcity) without its operational answer at scale.

### Promote the full ledger machinery — state vocabulary, claims, leases — as mechanism

Rejected. Those are enforcement conveniences that vary per harness, and the operator's own records include a prior instance of ledger machinery ballooning when it was treated as a first-class system in its own right. The mechanism-only inclusion rule places this material in the relation-facts layer, not in AKC's core.

### Record it as an example under `examples/` only

Rejected. The loop is not an instance of one phase; it is the shape the human approval gate takes at scale, spanning the gate and the judgment that feeds it. An example placement would document an instance without recording the mechanism claim it is evidence for.

### Record it as a dated addendum to ADR-0005 instead of a new ADR

Rejected. Nothing in ADR-0005 is weakened or amended — the gate's holder, binary character, and position are unchanged — so an addendum would misuse the weakening-annotation form on a record whose content stands. And the loop is a concept spanning the gate and the judgment upstream of it, not a clarification of the gate; burying it inside a gate record would leave the topology undiscoverable as a mechanism in its own right.

## Consequences

### Positive

- Theme 1 (human cognitive resource scarcity) gains its operational answer: when human judgment is the bottleneck, spend model judgment to conserve it, and keep the human at the direction-setting and merge points.
- The gate of ADR-0005 is described at scale — how it holds when the upstream artifact is an open-ended ledger rather than a single proposed change — without weakening its binary, named-human character.
- Downstream implementers of the cycle get a named topology (judge / build / human) to adapt rather than an implied division of labor they would otherwise have to reconstruct.

### Negative

- The evidence is one operator's roughly two weeks of practice (2026-08-17 through this ADR's date, 2026-09-01) — a single-operator observation, not a controlled or cross-operator result.
- The supporting numbers (2 of 7 task premises refuted at pre-implementation verification; 22 of 30 new entries from review-origin filings) come from the operator's harness records, not from this repository, and are not independently reproducible from what AKC ships.

### Neutral

- No change to the six-phase structure. No new instrument is added to Measure or elsewhere.
- The loop is a topology over the existing gate (ADR-0005) and existing phases, not a new phase or a new gate.

## Relationship to other ADRs

- **[ADR-0010](./0010-human-cognitive-resource-as-central-constraint.md) (Human Cognitive Resource as Central Constraint).** This ADR is that constraint's operational form — the scarcity ADR-0010 names is here made into a concrete role assignment: which resource (model or human judgment) is spent at which step.
- **[ADR-0005](./0005-human-approval-gate.md) (Human Approval Gate).** The gate is unchanged in kind and in who holds it. This ADR restructures what reaches the gate — the judge tier absorbs triage so the human's judgment is spent on direction and the final switch, not on sorting every candidate task.
- **[ADR-0019](./0019-cycle-structure-is-provisional.md) (The Cycle's Structure Is Provisional).** The three-role topology, like the phase-to-skill bindings ADR-0019 describes, is held provisionally — the current best articulation of where judgment sits, not a fixed essence, subject to the Review-when conditions above.
- **[ADR-0018](./0018-record-downstream-applications-as-first-class-context.md) (Record Downstream Applications as First-Class Context).** The harness practice this ADR adapts from is exactly the kind of downstream application ADR-0018 established the discipline for: recorded as first-class context, with relation facts and no imported content.
- **[ADR-0026](./0026-expiry-conditioned-knowledge.md)** (recorded in the same release as this ADR). Supplies the dated-hypothesis reading applied here to the 2026-07-09 rejection: rejection records expire with their premises rather than binding permanently.
