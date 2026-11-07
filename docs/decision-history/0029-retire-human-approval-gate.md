# ADR-0029: Retire the Human Approval Gate as a Structural Requirement

> **Summary.** On 2026-11-07 the author removed the Human Approval Gate ([ADR-0005](./0005-human-approval-gate.md)) from AKC's definition. AKC no longer states that it is not autonomous or that every change to behavior-shaping artifacts structurally requires a named human sign-off. What the human holds is the boundary of what is handed to a human — an enumeration the operator keeps in the harness, such as the author's always-loaded boundary rule — and that enumeration is a harness asset, not a structural requirement of AKC. The human-held switch in the three-role loop ([ADR-0024](./0024-judge-build-human-three-role-loop.md), [ADR-0028](./0028-authority-by-artifact-class-in-the-three-role-loop.md)) stays as the author's operating choice.

## Date

2026-11-07

## Context

On 2026-04-09 (v1.5.0) ADR-0005 made every change that modifies future agent behavior — rules, skills, identity, and the ADRs and READMEs that document behavior — wait for an explicit, named human approval, with no "auto-approve after N days" escape hatch and no path on which the LLM approves its own change. Its 2026-06-06 addendum presented the gate as AKC's contribution rather than a guardrail, and argued that the human is the one verifier whose failures are not correlated with the generator's. `CLAUDE.md` carried the caveat "AKC は autonomous でない" and the `human approval gate` concept node in `graph.jsonld` said "AKC is not autonomous". What the gate closed at that time was the path on which an agent writes its own rules, skills, or identity without anyone reading the change: an unchecked change in the always-loaded layer shapes every later session and what later distillation reads, so it reinforces itself ([ADR-0015](./0015-loop-failure-modes-self-reingestion.md) named the gate as the circuit-breaker there).

The running instance narrowed twice before this entry. On 2026-08-02 the human-gate rule and its evidence-file hook retired from the author's harness because the substrate's own defaults absorbed the stop, and AKC unlinked it ([ADR-0027](./0027-mental-model-and-instance.md)). On 2026-09-15 the harness consolidated what goes to the human into one always-loaded boundary rule (`rules/common/boundary.md` in [claude-harness](https://github.com/shimo4228/claude-harness); harness record 0069, cited in ADR-0028), and ADR-0028 recorded merge authority by artifact class.

On 2026-11-07 the author judged that the gate had gone stale ([claude-harness record 0102](https://github.com/shimo4228/claude-harness/blob/main/docs/decision-history/0102-remove-change-blocking-mechanisms.md), written in Japanese). In the author's words it takes a judgment that belongs to a larger organization and pushes it down to the individual — 「マイクロマネジメントだ」 ("it is micromanagement"). The author also judged it redundant at least within the personal implementation, because the current Claude Code permission classifier carries this boundary surface, and that in personal practice the named sign-off on each behavior-shaping change had become a ritual. These are the author's judgments of that day, not measurements. The same record removed other mechanisms in the author's environment that resisted change, and on the same day the decision records of every repository became past-tense history (in this repository, commit 46f967d).

## Decision

1. **Removed the gate from AKC's definition.** The claims that AKC is not autonomous and that every change to behavior-shaping artifacts structurally requires a named human sign-off were taken out of the current documents. ADR-0005 stays as written, as the record of what was decided on 2026-04-09.

2. **Placed the human's part in the boundary enumeration.** What the human holds is the boundary of what is handed to a human — a list such as the author's harness boundary rule (publication, billing, outbound messages, unattended changes to rules, skills, hooks, permissions, and the like). The list is a harness asset owned by the operator; AKC does not prescribe its contents and does not require any artifact class to be on it.

3. **Detached the three-role loop's human switch from the gate.** The human-held switch in the judge/build/human loop — direction-setting, admission, and merge of the protected class (ADR-0024, narrowed by ADR-0028) — stays as the author's operating choice. It is no longer derived from a structural requirement of AKC.

4. **Rewrote the current documents to match.** The front door (`README.md`, `README.ja.md`, `CLAUDE.md`), `llms.txt`, `llms-full.txt`, `graph.jsonld`, `docs/glossary.md`, `examples/constitution_amend/README.md`, `examples/minimal_harness/README.md`, and the Unreleased section of `CHANGELOG.md` now describe the gate in the past tense with this entry as its retirement. Where they used the gate as a defense or as positioning, they now name what remains: Curate and Promote as the operator's own decisions about what is kept and promoted, and the operator's boundary enumeration. The positioning delta against the agent-memory prior art ([ADR-0013](./0013-positioning-within-agent-memory-literature.md)) is restated as loop ownership — the operator decides what is kept, what is promoted, and where the boundary lies — rather than as a structural gate. The failure-twin defenses named in [ADR-0014](./0014-failure-modes-of-the-bidirectional-loop.md) and ADR-0015 are described the same way; those entries stay as written. The *human-gated* property of harness alignment ([ADR-0017](./0017-harness-alignment-and-drift.md), the [position paper](https://doi.org/10.5281/zenodo.20578272)) was left as written: it says that intent has no verifier outside the operator, which this entry does not change; whether the word is reread as "operator-decided" is open.

## Review-when

- An agent rewrites rules, skills, or identity without the change passing through anything the operator's boundary hands to a human, and the author reverts it (counted from `Revert` commits on main and the author's revert instructions, in any repository running the cycle). The author's stated first step is to re-examine the boundary enumeration; the outcome is open.
- The substrate stops confirming consequential or irreversible actions first, or its permission classifier stops covering writes to rules, skills, and identity. The premise in Context that the substrate carries this boundary surface then no longer holds; re-examine whether AKC needs a structural requirement again.
- A reader operating agents at organizational scale reports that AKC without the gate gives them no answer about sign-off. Decide whether AKC records an organization-scale boundary separately.

## Alternatives Considered

### Keep the gate as it is

The gate was the core of the concept: ADR-0005's addendum called it the contribution, and the positioning against the prior art rested on it. Rejected on the author's judgment that the named sign-off had become a ritual in the personal practice and that the substrate's classifier carries the same boundary surface.

### Keep the model and mark the instance as deviating

[ADR-0027](./0027-mental-model-and-instance.md) allows the mental model to stand while an instance is marked as deviating from it; ADR-0028 considered and rejected the same option for the merge switch. Rejected on the author's judgment that the model itself was stale — the gate brought an organization-scale judgment down to an individual — not only the instance.

### Keep the gate for the always-loaded rules layer only

ADR-0005 names the rules layer as the extreme case. Rejected: the author's harness boundary rule already hands unattended rule changes to the human, so the line exists where the operator listed it; writing it into AKC's definition would keep the structural requirement in a narrower form.

### Weaken the gate to a recommendation

Keep ADR-0005's table as advice ("operators should approve behavior-shaping changes"). Rejected: under the author's positive-form writing rule for documents an LLM follows, a named "do not let the agent write this" is recalled by the reader as an option to act on, and a recommendation with no structure behind it describes nothing the running instance does.

## Consequences

### Easier

- In personal operation the approval ritual is gone; the operator spends attention on the boundary list and on Curate and Promote, not on a sign-off per change.
- The concept matches the running instance: what the documents say the human holds is what the author's harness actually hands to the human.

### Harder

- AKC no longer has a structural answer of its own to self-reinforcement into the always-loaded layer. The answer exists only where an operator's boundary lists those writes. The substrate's classifier that the author relies on is model-side, and ADR-0028's Consequences already noted that model-side checks correlate with the generator; ADR-0005's uncorrelated-verifier argument is not answered here, only set aside for the personal implementation.
- The "ritual" observation is the gate complacency that ADR-0014 predicted and treated as a failure to defend against. This entry reads it instead as a reason to retire the gate; the two readings stand side by side.
- ADR-0028's protected class was defined as what ADR-0005 gates, and its rejection of judge merges for that class rested on ADR-0005. That class now has no grounding in AKC itself; it stands as the author's operating choice.
- Public material that explained the gate as AKC's core — the published DOI versions up to v2.9.0, the [position paper](https://doi.org/10.5281/zenodo.20578272), and the author's articles — now differs from the repository. The differences are carried by the next release's README and release note.
- The positioning against the agent-memory prior art loses its sharpest structural line; "the operator owns the loop" is a weaker distinction than "no change lands without a named sign-off".
- Readers who operate agents at organizational scale need a different answer. For them a named sign-off can still be the right boundary, and AKC no longer states one; the boundary enumeration is theirs to write.
- Reversing this means rewriting the same ten documents again, and the published DOI versions would then differ in the other direction.

### Neutral

- ADR-0005, ADR-0013, ADR-0014, ADR-0015, ADR-0017, ADR-0024, and ADR-0028 keep their text. The line between records and behavior-shaping artifacts (the line of approval) remains available as a criterion an operator can use when writing the enumeration.
