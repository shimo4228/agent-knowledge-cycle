# ADR-0026: Expiry-Conditioned Knowledge

> **Summary.** External knowledge in the LLM and agent field goes stale on a roughly one-week scale — methods, tools, specifications, and market intuitions are routinely superseded within weeks; this is the operator's resident worldview as of 2026-08. The cycle stores the opposite kind of thing: judgments — decision records, curated knowledge, rejection records — and a stored judgment read as permanent keeps constraining new ideas after its premise has died. The operator reported exactly this in the harness on 2026-08-19 — sessions felt bound by past decision records five days after a declaration that "decision records are scaffolds" had been added; a subjective report with zero recorded case-level instances at baseline, stated as such in Context. The structural remedy adopted that day was an explicit expiry-conditions section captured at write time, dated in-place weakening instead of deletion, and a reading protocol that checks Date and the expiry section before treating a record as binding; a 2026-08-24 instruction extended the same reading to rejection records. AKC already reads its own ADRs as dated hypotheses informally, but its format has no expiry field, and an expiry condition can only be captured at write time or never. ADR-0026 imports a `## Review-when` section into the AKC ADR format, placed after `## Decision`, required from ADR-0024 onward (with an explicit null rendering) and not backfilled into 0002–0023, and extends the same reading to this repo's rejection records — with ADR-0024's Decision 3, which records the 2026-07-09 triage rejection's surviving scope and expired premise, as the first instance of the reading.

## Status

**accepted** — the load-bearing decision is procedural (a format field and a reading protocol) and cheap to reverse via its own Review-when. The honest limitation: the harm it remedies rests on a single-operator subjective report with zero recorded case-level instances at baseline (2026-08-19), stated in Context and carried as a Negative consequence; this ADR asserts the write-time-or-never structure of expiry capture, which is deductive, and does not assert a measured suppression effect.

## Date

2026-09-01

## Context

External knowledge in the LLM and agent field goes stale on a roughly one-week scale. Methods, tools, specifications, and market intuitions are routinely superseded within weeks of being current. This is the operator's resident worldview as of 2026-08, and it already governs how the cycle treats *incoming* information: recommendations carry an as-of date, and claims are weighted by how recently they were checked against a primary source.

The cycle's own storage runs on the opposite assumption. Decision records, curated knowledge, and rejection records are written once and then read back across sessions, months later, without re-verification. A stored judgment read as permanent keeps constraining new ideas after the premise that produced it has died — the storage layer does not share the staleness worldview the intake layer already has.

The operator reported this in the harness on 2026-08-19: sessions felt bound by past decision records, suppressing free ideation — five days after a declaration that "decision records are scaffolds" had been added to the harness's own rules. The upstream record is explicit about the strength of this evidence: it is a subjective operator report, with zero recorded case-level instances at baseline (no session or commit is on file in which a decision record demonstrably stopped an idea, as of 2026-08-19). What the report supports is that the declaration alone had not changed the felt behavior: stating that a record is provisional, without a mechanism a reader checks before treating the record as binding, left the records functioning as before — in the operator's judgment, which is all the evidence there is.

The structural remedy adopted in harness practice on 2026-08-19 had three parts: an explicit expiry-conditions section, captured at the time a judgment is written, stating what observation or premise failure would void or weaken it; dated weakening annotations appended in place when a premise does fail, rather than deleting the original record; and a reading protocol — read the record's date and its expiry-conditions section first, a fired expiry condition removes binding force, and a conflict between a new idea and an old record is presented as a supersede candidate, not a veto.

A 2026-08-24 operator instruction extended the same reading to rejection records specifically: a rejection that carries no expiry condition is a weak presumption rather than a permanent bar, and — critically — divergence-stage ideation must not use rejection records as refutation at all; verification against them happens only at the adoption stage, after new ideas have already been generated.

AKC already reads its own ADRs informally as dated hypotheses — a stored judgment weighed against its Context premises and Date rather than treated as an unconditional rule. But the AKC ADR format has no field for expiry conditions, and an expiry condition can only be captured at the moment a judgment is written; it cannot be reconstructed afterward without inventing what the author would have said. The informal reading and the harness's structural remedy point at the same gap in the format.

## Decision

1. **Stored judgments carry expiry conditions.** A recommendation or decision states what observation or premise failure would void or weaken it; intake states its as-of date. A recommendation that cannot name an expiry condition is treated as freshness-unknown and weighted weakly. Scope: the principle is stated for the cycle's stored judgment generally, but the instrument this ADR ships (clauses 2 and 3) binds the ADR layer only; whether and how the same discipline reaches Layer 2 / Layer 3 curated knowledge (ADR-0003) is left open, with no instrument shipped here.

2. **Import a `## Review-when` section into the AKC ADR format, placed after `## Decision`.** It is required for ADR-0024 onward — the three ADRs shipping together in this release all carry it — with an explicit null rendering, not omission, when there is nothing to expire: "none — a record, not a standing decision". ADRs 0002–0023 are not backfilled; they remain read by their Context premises and Date, per the existing dated-hypothesis reading.

3. **Weakening is annotated in place, dated, and never deleted** — `> **Note (YYYY-MM-DD, ADR-NNNN)**` appended under the affected section of a published ADR. Rejection records receive the same reading: they are dated hypotheses, not permanent vetoes. Where the weakened record cannot carry a published annotation — the 2026-07-09 triage rejection lives in an operator-private ledger — the weakening is recorded in the new ADR instead: ADR-0024's Decision 3 records that rejection's surviving scope and expired premise in place of an annotation on the original, and is this repo's first instance of the dated-weakening reading (the `> **Note**` form itself has no instance yet).

   > **Note (2026-09-01, ADR-0027)**: the parenthetical above expired the same day — ADR-0027's vocabulary supersede placed the first three `> **Note**` annotations on published ADRs (0018, 0019, 0024).

## Review-when

If three consecutive new ADRs render Review-when as "none — a record, not a standing decision", demote the section to optional prose inside Consequences. If the substrate natively tracks decision freshness — dates and expiry conditions checked at read time — this format mechanism becomes a downward-dissolution candidate.

## Alternatives Considered

### (a) Reading protocol only, with no format change

Keep the informal dated-hypothesis reading and add no new section. Rejected: an expiry condition can only be captured at write time, so new ADRs would keep accruing without one, and the format would never close the gap it was written into. The harness observation is direct evidence against this option: a reading declaration alone, with no structural change, did not change the binding behavior it was meant to loosen.

### (b) A `weakened` status value in the Status enum

Add a new value to the ADR Status field to mark records whose premise has partially failed. Rejected: a dated in-place annotation at the point of weakening carries the same information together with its location and reasoning, without adding an enum value or a status-transition bookkeeping discipline the repo would then have to maintain.

### (c) Backfill Review-when into ADRs 0002–0023

Add the new section retroactively to every existing ADR. Rejected: an expiry condition written after the fact would be invented post hoc — precisely the false precision this ADR exists to prevent, since expiry conditions can only be captured at write time. The older records keep the existing premise-plus-date reading instead.

## Consequences

### Positive

- The cycle's storage now obeys the same staleness worldview it already applies to external knowledge — stored judgment gets the treatment external knowledge already gets.
- Rejection records stop functioning as permanent vetoes while remaining fully on the record, matching the 2026-08-24 reading.
- Readers of any ADR from 0024 on get a uniform first-read protocol: check Date, then check Review-when, before treating the record as binding.

### Negative

- The section is one more required input per new ADR.
- The section can degenerate into boilerplate; its own Review-when clause above is written to watch for exactly that failure mode.
- ADRs 0002–0023 remain without the section, so two reading modes — premise-plus-date and explicit Review-when — coexist indefinitely.
- The evidence for the harm this ADR remedies is the weakest in this release: a single-operator subjective report with zero recorded case-level instances at baseline (2026-08-19). The format decision is cheap and procedural, but the claim that unexpired-looking records were suppressing ideation rests on the operator's judgment alone.

### Neutral

- No change to the six-phase structure.
- The format import comes from operator harness practice observed on 2026-08-19, continuing this repo's existing pattern of adapting record-keeping practice from a running system rather than designing it from scratch.

## Relationship to other ADRs

- **[ADR-0019](./0019-cycle-structure-is-provisional.md) (The Cycle's Structure Is Provisional).** ADR-0019 holds the cycle's own structure lightly on the Emptiness axiom, as a disposition. ADR-0026 gives that disposition a per-decision instrument — an explicit, checkable expiry-conditions field — rather than leaving provisionality as a global disclaimer applied at read time by the reader's own judgment.
- **[ADR-0017](./0017-harness-alignment-and-drift.md) (Harness Alignment and Harness Drift).** The record format co-evolves with the harness practice it aligns to: the Review-when mechanism is imported directly from a change made in the operator's harness, the same relationship ADR-0017 names between AKC and the harness it keeps aligned.
- **[ADR-0023](./0023-generation-review-as-a-fourth-evidence-class.md) (Generation Review as a Fourth Retirement Evidence Class).** Generation review's external clock — a rule's premise expiring on the model release cadence rather than on a usage log — is one class of expiry condition. Review-when generalizes the instrument: "the substrate generation changed" is a premise failure with a schedule, expressible in the same field this ADR adds.
- **[ADR-0024](./0024-judge-build-human-three-role-loop.md).** Carries this repo's first instance of the dated-weakening reading, written under the protocol this ADR establishes: its Decision 3 records the 2026-07-09 triage rejection's surviving scope and expired premise, in place of an annotation the operator-private original cannot carry, with the original left unedited.
