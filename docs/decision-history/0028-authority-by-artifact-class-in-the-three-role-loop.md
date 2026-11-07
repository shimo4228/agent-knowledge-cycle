# ADR-0028: Authority by Artifact Class in the Three-Role Loop

> **Summary.** ADR-0024 named the judge/build/human loop and placed one irreducible switch with the human: the merge into main, for every task the loop produces — "what moves upstream to the judge tier is attention, not authority." On 2026-09-15 the operator's harness moved that switch for one class of output. A task branch the human had admitted is now merged by the judge tier once a deterministic gate passes on the exact change and the judge's own inspection passes — provided the diff stays outside a protected class: rules, skills, identity, ADRs and other documents that describe behavior, the control plane (hooks, permissions, scheduled tasks, settings), and the verification machinery (the verify gate, CI configuration, test assertions the task did not name). Changes inside that class still wait for the human. ADR-0028 records that placement as the mental model: **authority is placed by artifact class**. ADR-0005's gate is unchanged. For admitted task output, the human's authority is exercised at admission — which tasks exist and on what acceptance conditions — and through a revert-count withdrawal condition, not at the merge.

## Status

accepted — partially supersedes [ADR-0024](./0024-judge-build-human-three-role-loop.md) Decision 1 (the human-held merge switch, for admitted task output outside the protected class only); a dated note is placed there

## Date

2026-09-25

## Context

[ADR-0024](./0024-judge-build-human-three-role-loop.md) (2026-09-01) recorded the three-role loop with the human holding "direction-setting and the final merge switch" and stated that the gate "stays binary and human at the point of merge." That was an accurate description of the operator's harness on that date.

On 2026-09-15 the operator changed it. The harness decision record ([claude-harness ADR-0069](https://github.com/shimo4228/claude-harness/blob/main/docs/adr/0069-boundary-rule-and-judge-merges.md), written in Japanese) consolidated six scattered statements of what goes to the human and what may be done without asking into one always-loaded boundary rule, and moved the final switch for admitted work to the judge tier:

- The judge tier fast-forwards a task branch into main, and pushes it where a remote exists, after its own acceptance check — diff scope, re-running the verify gate, the evidence in the commit body, conformance to the task's chain. The digest to the human becomes an after-the-fact report (merged / left, with the reason). The build tier still stops at its task branch, so implementer and inspector stay separate sessions.
- Unattended diffs that touch rules, hooks, permissions, scheduled tasks, or the verify gate still go to the human, and the gate's approval ledger stays human-operated. The boundary rule's list of what is handed to the human also includes ADRs and skills. The judge's acceptance step bounces any change to the verify gate, CI configuration, settings, or a test assertion the task did not name.
- The human keeps admission: filing and dropping tasks is the human's decision, and the judge only proposes.
- The withdrawal condition is written into the same record: if a judge merge breaks main and the human reverts it more than twice in three months, the switch returns to the human.
- The recorded motive is a classification of acceptable accidents — stating which risks are taken rather than only which are forbidden — not an observed waiting cost. The same record gives the claim-to-release interval (an upper bound on build time plus merge wait) at that date as a median of 1.0 h and a maximum of 7.1 h over 37 harness tasks, and a median of 0.8 h and a maximum of 52.9 h over 61 Contemplative Agent tasks.

Two later harness records refine the same boundary. On 2026-09-24 build sessions moved to cloud sessions by default ([claude-harness ADR-0075](https://github.com/shimo4228/claude-harness/blob/main/docs/adr/0075-cloud-session-as-default-build-executor.md)); for those branches the verify re-run is replaced by the repository CI's result on the exact branch tip. On 2026-09-25 build sessions were allowed to propose follow-up tasks with a reproduction recipe ([claude-harness ADR-0076](https://github.com/shimo4228/claude-harness/blob/main/docs/adr/0076-build-proposals-with-reproducer-and-opus-5-5-packet-rules.md)), with the filing decision left to the human — admission stays human even when the proposal originates in the build tier.

What has been observed since the switch moved (2026-09-15 to 2026-09-25, measured 2026-09-25): zero reverts on main in the two repositories running the loop in that window (`git log main --since=2026-09-15 --grep='^Revert'` in each), against five tasks released as done in the operators' claim ledgers (one harness, four Contemplative Agent). Release-as-done is a proxy for judge merges, not a count of them: a task can close without a merge (a measurement, a refuted premise), and the ledgers do not record which closures were merged by the judge. The Contemplative Agent history is public; the harness history and the claim ledgers are operator records, not reproducible from this repository.

[ADR-0005](./0005-human-approval-gate.md) never covered this output. Its approval table gates rules, skills, identity, and documents that describe behavior, and forbids any path on which the LLM approves those changes itself. The merge of all task output into main was ADR-0024's addition, not ADR-0005's requirement.

## Decision

1. **Place authority by artifact class.** A protected class stays binary and human at the point of merge: the artifacts ADR-0005 gates (rules, skills, identity, ADRs and other documents that describe behavior), the control plane (hooks, permission grants, scheduled task definitions, settings), and the verification machinery whose change would move what counts as verified (the verify gate, CI configuration, test assertions the admitted task did not name). The class is read in whichever repository the loop works on: when that repository is itself an agent, its code is task output, and its own rules, identity, and decision records are in the class. For admitted task output outside the class, the merge closes on two checks made outside the build session: a deterministic gate that passes on the exact change, and an inspection by the judge tier.

2. **Name where the human's authority over task output now sits.** Chiefly at admission: the human decides which tasks exist and on what acceptance conditions (filing and dropping stay human; the judge and build tiers only propose). The running instance adds per-task human OKs at a few further points — dispatching to or bouncing a cloud session on a public repository, and acceptance defaults the judge fills in. The switch's placement is itself a dated hypothesis with a withdrawal condition counted from reverts (Review-when).

3. **Retire ADR-0024's claim that the human holds the merge switch for every task.** The retired scope is exactly that clause; a dated note in ADR-0024 Decision 1 states what of the loop is unchanged.

## Review-when

- **Reverts.** More than two judge-merged commits on main are reverted by the human within any rolling three-month window, counted together across all repositories running the loop. A revert counts once whether it appears as a `Revert` commit (`git log main --grep='^Revert'`), as a revert instruction the human writes into the judge's digest, or as both; reverts of commits the human merged do not count. Changes to the acceptance check itself (such as CI replacing the verify re-run on 2026-09-24) do not restart the count. The judge tier reports the count as one line per triage cycle, as the harness record fixes. When it fires, the switch returns to the human and this ADR is superseded in that direction.
- **The class line fails.** A judge-merged diff is found to have touched an artifact in the protected class — once is enough. Re-audit the class boundary before the loop merges again.
- **Admission is bypassed.** A task reaches judge acceptance without a human admission decision — filed and admitted by the judge or build tier alone. The current claim ledgers record a task's origin but not who admitted it, so this condition is not yet observable mechanically; until it is, it is checked by the author's reading of the digest.
- **The substrate moves.** The substrate stops honoring a standing, recorded authorization for merges and pushes (it treats every merge as confirm-first regardless of the operator's boundary rule), or it natively gains class-based merge authority (protected paths enforced by the platform), which would make the operator's list redundant. Either way, re-audit at the next generation review ([ADR-0023](./0023-generation-review-as-a-fourth-evidence-class.md)).

## Alternatives Considered

### Annotate ADR-0024 only, leaving the mental model unchanged

Coherent under [ADR-0027](./0027-mental-model-and-instance.md): the model could stand and its grounding be marked as deviating. Rejected by the author (2026-09-25), whose judgment is that placing authority by artifact class is the better model, not a local deviation to be tolerated — the class line is already implicit in ADR-0005's table, and the running practice made it explicit.

### Annotate now, and change the model only after a full withdrawal window passes without firing

The strongest form of waiting, given how thin the evidence is. Rejected by the author (2026-09-25): the model is recorded now as a dated hypothesis, and the withdrawal condition makes it reversible on the same evidence that waiting would collect.

### Keep the human merge switch for all task output

Rejected in the harness record by the operator (2026-09-15), on the classification of acceptable accidents: an admitted, gate-passing, independently inspected merge of task output was put on the "taken" side. Waiting time was not the reason (medians under an hour at the time). The withdrawal condition keeps this reversible on evidence.

### Move protected-class merges to the judge tier as well

Rejected. For rules, skills, and identity that is the LLM-approved path ADR-0005 forbids, and a change to the control plane or the verification machinery moves the gate itself. The class line in Decision 1 is where the gate's own reason — an unchecked change there is self-reinforcing — applies.

### Record it as an amendment to ADR-0005

Rejected. ADR-0005's scope and holder do not change; what changes is ADR-0024's topology claim about the merge of all task output. Amending the gate record would suggest the gate was weakened when it was not.

## Consequences

### Positive

- The front door, the graph, and the running harness agree on where authority sits (updated in the same change as this ADR).
- The line between the protected class and task output — implicit in ADR-0005's table — becomes an explicit part of the loop's topology, so a downstream implementer can see which merges must wait for a human and which may not need to.
- The human's authority over task output has a named location (admission, acceptance conditions, the withdrawal condition) instead of an assumed one at the merge.

### Negative

- The evidence is thin: ten days, five tasks released as done (a proxy that over-counts judge merges), zero reverts, one operator. It is a record of a running decision, not a measured result.
- The two checks are outside the build session but not independent in the sense ADR-0005's addendum gives the human: the judge and the build tier are sessions of the same model family, so their errors correlate. The placement rests on task output not being self-reinforcing, not on the judge being an uncorrelated verifier.
- The withdrawal signal is lagging and has low sensitivity. It counts only damage the human notices once the change is in use, and the operator does not routinely read merged code or review reports.
- The class line is narrower in the running instance than in the human-approval-gate concept's wording. The concept names lint configuration and dependency manifests among evidence-producing artifacts; the instance does not hold those back from judge acceptance. The gap is recorded here rather than closed.
- The placement depends on the admission discipline holding, and admission is not yet observable in the ledgers (Review-when).
- The class boundary must be enforced per harness. The operator's harness does it with an always-loaded list and by bouncing gate-touching diffs at acceptance; a harness without such a list has no line to apply.

### Neutral

- [ADR-0005](./0005-human-approval-gate.md) is unchanged in scope, holder, and binary character.
- The six-phase structure and the three-role topology — judge verifies, decides, dispatches, and inspects; build implements and halts on a refuted premise; human sets direction — are unchanged.

## Relationship to other ADRs

- **[ADR-0024](./0024-judge-build-human-three-role-loop.md) (The Judge/Build/Human Three-Role Loop).** Partially superseded: its Decision 1 clause that the human holds the merge switch for all task output is retired for admitted task output outside the protected class. A dated note in its Decision 1 records what of the loop stands.
- **[ADR-0005](./0005-human-approval-gate.md) (Human Approval Gate).** Unchanged, and deliberately left without a note: its table never covered task output, so its text is not weakened. (The operator's harness did annotate its own gate record for the same change, harness ADR-0019, because that record composed every approval of a deterministic gate plus a human intent judgment; there the clause itself moved.)
- **[ADR-0010](./0010-human-cognitive-resource-as-central-constraint.md) (Human Cognitive Resource as Central Constraint).** Applied one step further: the human's attention is no longer spent on merges of admitted, gate-passing task output, and is kept for admission and for the protected class.
- **[ADR-0026](./0026-expiry-conditioned-knowledge.md) (Expiry-Conditioned Knowledge).** The placement is held as a dated hypothesis with an observable withdrawal condition, and ADR-0024's weakened clause receives the dated in-place note its Decision 3 prescribes.
- **[ADR-0027](./0027-mental-model-and-instance.md) (Mental Model and Instance).** The instance moved first (2026-09-15); this ADR records the author's judgment that the model should move with it, and the gate's running instance — the harness's always-loaded boundary rule — is linked from the front door as grounding.
