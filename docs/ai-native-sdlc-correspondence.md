# AKC and the AI-Native SDLC Playbook

**As of 2026-08-25.** Anthropic published *The AI-Native SDLC Playbook* on
2026-08-21; this document is written against the version archived on
2026-08-24 ([archived copy](https://web.archive.org/web/20260824134825/https://claude.com/blog/the-ai-native-sdlc-playbook),
verified 2026-08-25 to carry the same article body as the live page). The
playbook is a living vendor document that can be revised at its live URL
without notice, so every claim below about "the playbook" is a claim about
that dated text, not about whatever is published there when you read this.

## Two loops, not one mapping

The playbook runs six stages — Plan, Design, Build, Test, Deploy, Maintain.
AKC runs six phases — Research, Extract, Curate, Promote, Measure, Maintain.
The matching count is a coincidence, and reading it as a stage-to-phase table
produces nonsense. The two are different loops moving different objects.

The playbook's loop — call it the **product loop**; the term is this
document's, the loop is the playbook's — moves a software change from intent
to production and back. Each stage ends by committing an artifact the next
stage reads — intent, spec, plan, the diff and its tests, the PR and its
findings, the incident record — and a breached control band in production
writes the next intent, which restarts the loop. Its object is a change to the
product.

AKC's loop — call it the **harness loop** here; AKC's own vocabulary says
knowledge cycle — turns experience into durable knowledge, the skills, rules,
and documentation that shape future behavior, under human approval. Its object
is the configuration that steers the agent, not the product the agent ships.
Running it is what sustains harness alignment; left unrun, the same
configuration drifts (ADR-0017).

The two are coupled rather than parallel, and the coupling has a direction.
One turn of the product loop is what produces the experience the harness
loop's Research and Extract phases consume: the mistake the agent made twice,
the incident nobody had an eval for, the review finding that keeps recurring.
Running the product loop generates harness-loop input whether or not there is
anywhere to put it.

The playbook contains the second loop. It appears in Stage 3 as corrections
written into CLAUDE.md and institutional knowledge versioned as skills; in
Stage 4 as an eval suite that runs whenever agent configuration changes and
that must be maintained as a live suite, because cases stop discriminating as
models improve; in Stage 5 as a monthly tuning pass over the review policy and
as non-negotiable hooks moved into managed settings; and in Stage 6 as
dismissed findings tuning the detection bands. The playbook states the
principle plainly for one layer: agent configuration steers the agent and
"deserves the regression testing that code gets."

What it does not do is name that second loop as a loop. It has no phases of
its own, no owner distinct from the stage that surfaced it, no stage of its
own, and no cadence owned by the loop as a whole — the schedules that do
exist (a monthly tuning pass, a nightly eval run) belong to individual plays.
It is a set of good habits distributed across four stages, each attached to
whichever product-loop moment happened to reveal it. AKC is that second loop
made explicit: six named phases, each with an owned asset and a place to run.

## Where the playbook gestures at each phase

Conceding first, in the manner of
[ADR-0013](adr/0013-positioning-within-agent-memory-literature.md): most of
what AKC's phases do is already gestured at somewhere in the playbook. The
table locates each gesture and rates how strongly it corresponds.

| AKC phase | Where the playbook gestures at it | Strength |
|---|---|---|
| **Research** — signal-first intake ([search-first](https://github.com/shimo4228/search-first)) | Nothing. The only research-shaped artifact named is a subagent that explores the codebase and reports back without flooding the main context (Stage 3) — internal, per-task, and scoped to context economy, not an intake discipline for knowledge arriving from outside. | gap |
| **Extract** — reusable pattern ([learn-eval](https://github.com/shimo4228/learn-eval)) | A working rule that a mistake made twice becomes a correction in CLAUDE.md (Stage 3), repeated on the review side when a finding is flagged a second time (Stage 5); each production incident becoming an eval that stays in the suite as a regression test (Stage 4); dismissed findings tuning the detection bands, which live in version-controlled config (Stage 6). | strong — but three mechanisms spread over four stages, none named as one activity |
| **Curate** — audit what accumulated ([skill-health](https://github.com/shimo4228/skill-health) + [skill-stocktake](https://github.com/shimo4228/skill-stocktake) + [rules-stocktake](https://github.com/shimo4228/rules-stocktake) + [agent-stocktake](https://github.com/shimo4228/agent-stocktake)) | A monthly pass in which the tech lead tunes the review setup by rating findings and capping nit volume in REVIEW.md (Stage 5); keeping CLAUDE.md under a page because anything stale costs context for no benefit (Stage 3); the note that eval cases must be added as old ones stop discriminating (Stage 4). | embryonic — habit and cadence, no systematic audit of the accumulated set |
| **Promote** — human-gated behavior change ([rules-distill](https://github.com/shimo4228/rules-distill)) | The gate is present at every layer and well specified: code owners approve CLAUDE.md changes in PR review, the policy owner signs off skill changes (Stage 3), non-negotiable hooks move into managed settings individual engineers cannot switch off (Stage 5). A placement rule of thumb says what belongs in a skill rather than in CLAUDE.md or a prompt (Stage 3). | mixed — the human gate exists; the distillation judgment — which experience deserves to become durable at all — reduces to a "twice" threshold plus that placement rule |
| **Measure** — observable behavior ([skill-comply](https://github.com/shimo4228/skill-comply)) | An eval suite that runs on any change to CLAUDE.md, skills, or hooks and on a schedule; configuration changes gated on the result, so a skill change that drops the pass rate is reviewed before it merges; pass rate tracked over time (Stage 4). Testing that a skill actually triggers, by asking for the task in different ways (Stage 3). | strongest correspondence |
| **Maintain** — docs and artifact hygiene ([context-sync](https://github.com/shimo4228/context-sync) + [repo-asset-stocktake](https://github.com/shimo4228/repo-asset-stocktake)) | Not the playbook's Stage 6. The nearest gestures are review flagging that a change has made CLAUDE.md outdated (Stage 5), read-only pipeline steps that draft the changelog, and gated write steps that update generated docs (Stage 5). | false friend |

The last row is the one worth flagging explicitly, because the shared name
invites the error. AKC's Maintain is documentation and artifact hygiene: keep
the roles of context files clean, find assets whose consumers have vanished.
The playbook's Stage 6 Maintain is production monitoring: agents watch live
deployments, a deterministic script detects a breached control band, and the
diagnosis is written back into the loop as a new intent. The names match and
the referents do not. In two-loop terms the mismatch is exact — the playbook's
Maintain is the product loop's re-entry point, the stage that *generates* new
work, while AKC's Maintain is the harness loop's hygiene phase, the one that
keeps the loop's own records readable. Mapping the two by name maps a source
of work onto a cleanup of records.

## What the gaps mean

The two weak rows are Research and Curate, which are the two phases AKC exists
for.

Look at what triggers each of the playbook's harness-loop habits: most are
events in the product loop — a mistake repeated, an incident, a review finding
raised twice, a dismissed band breach — and the rest are per-play schedules, a
monthly pass that rates review findings, a nightly run that tests the current
configuration. What no trigger does is sweep the accumulated set: nothing asks
which of the skills, corrections, and eval cases that piled up should still be
there, and nothing brings in knowledge from outside the organization's own
trajectories. Those are exactly the failures AKC was built from — skills go
stale, rules accumulate residency cost, documentation drifts — and none of
them announces itself with an event, or shows up in a run that only tests
what the set currently does.

This is a scale difference, not a defect of the playbook. Read what each play
assumes is staffed and the roles are explicit: a platform engineer stands up
the eval suite, a tech lead tunes REVIEW.md monthly and sets the human
threshold, each policy has a named owner who signs off skill changes, a
service owner triages the band-breach queue. Where those roles exist,
event-and-schedule maintenance is sufficient, because someone is paid to
notice what their play surfaces. AKC
is written for the operator running the same loop alone, where all of those
roles are one person and maintenance has no one to be assigned to
([ADR-0010](adr/0010-human-cognitive-resource-as-central-constraint.md)). At
that scale intake and audit have to be named phases or they do not happen at
all.

The two documents also stand in slightly different places on where the human
is. The playbook opens on the observation that the bottleneck has moved to
the human-speed steps around the build phase, is explicit that human
attention moves rather than disappears — it concentrates at the gates,
shifting to the artifacts that must be reviewed — and it closes on the image
of the loop running with human judgment above it. Its response is to automate
the bottleneck steps away. AKC agrees on the constraint and adds two claims
the playbook does not make: that the scarcity grows relatively worse as agent
capability grows, so the budget must be conserved rather than only routed
around (ADR-0010), and that the human is among the loop's outputs — Curate
and Promote force the operator to decide what is worth keeping, and deciding
that repeatedly sharpens the judgment that steers the loop. In AKC's framing,
above the loop is also inside it.

## Artifact correspondence: intent and the RFC

The playbook's Plan stage produces `intent.md`: a proto-spec written in the
originator's own words, committed to a shared, version-controlled home the
product owner watches, covering the problem, the proposed outcome, the
affected users and systems, the constraints, and the open questions. Its
load-bearing properties are that it is version-controlled, readable by both a
person and an agent, and accepted or rejected as a merge.

At operator scale that artifact already has a name: a proposal record in RFC
form. A public `rfcs/` directory in the repository where the work happens is a
faithful intent home — the playbook's own guidance is that the simplest home
for a single product is an `intent/` folder in the product repo, with a
dedicated intent repository only worth the overhead when intent spans many
repositories; `rfcs/` is the same shape under an older name.

The field mapping is close enough that the RFC template, in the Rust RFC
lineage, is a superset of the intent template rather than an alternative to
it:

| intent field | RFC section |
|---|---|
| Problem | Motivation |
| Proposed outcome | Summary |
| Affected users and systems | Guide-level explanation (users), Reference-level explanation (systems) |
| Constraints | Reference-level explanation |
| Open questions | Unresolved questions |

The RFC sections with no counterpart — drawbacks, rationale and alternatives,
prior art, future possibilities — are surplus in the useful direction: an
intent home should accept a document lighter than a full RFC without
rejecting one heavier. Adopting RFC form for intent costs nothing new and
inherits a review convention older than the agent question.

## A scale condition on continuous evals

The Measure row is the strongest correspondence in the table, and it carries
the clearest scale condition.

The playbook's continuous-evals play presumes two things a team has. A corpus:
it suggests collecting 20 to 50 real tasks from recent work, each written up
with the checks that define an acceptable outcome. And a staffed triage: the
team that owned an incident writes its eval, a platform engineer stands up the
suite, the team owning a configuration change approves it against the results.
Both are reasonable at team scale, and neither is free at operator scale.

One decomposition — this document's, not the playbook's — is useful before
reading the evidence. As written, the play's acceptance checks are
deterministic: scripts that assert tests pass, lint is clean, behavior is
unchanged. A model passing verdicts appears elsewhere in the playbook — an
adversarial reviewing agent, layered agentic review at the merge gate. Call
these the deterministic tier and the judge tier of configuration measurement.

Operator-scale evidence from the author's own practice (2026-08 — one
operator, roughly 50 skills) suggests the judge tier degrades first. An
LLM-judge skill-audit pilot returned zero true defects across 48 skills: every
finding was a false positive. A separate instrument built to measure how often
skills actually fired read a constant zero and was retired as a dead gauge
rather than believed. The transfer assumption here is explicit: a skill-audit
judge is not an eval-suite judge, but both are LLM verdicts passed over an
operator-scale corpus, and it is the corpus size the failure tracked. Neither
result contradicts the playbook. Both suggest that below some corpus size the
judge tier produces noise the operator must then triage — spending precisely
the budget the instrument was meant to protect.

The deterministic tier carries the same intent and does fire at that scale:
regression tests over hooks and configuration lint, run on every
configuration change — the playbook's own principle that configuration
steering the agent deserves the regression testing code gets — and every
incident converted into a permanent regression test. The playbook itself
insists on the same separation where the stakes are highest, keeping band
detection entirely deterministic with no model involved and invoking the
model only after a breach. Read as a scale condition rather than a critique:
keep the deterministic tier at every scale, and add the judge tier once the
corpus is large enough that its verdicts are worth triaging.

## What does not change

- **The six phases.** Research → Extract → Curate → Promote → Measure →
  Maintain are unchanged in number, name, and order. This document maps them
  against an external framework; it does not redefine them, and the playbook's
  Stage 6 does not rename AKC's Maintain.
- **The three core themes.** Cognitive-resource scarcity, intent alignment,
  and the cycle changing the human are unchanged (ADR-0012). No fourth theme
  enters here.
- **ADRs in effect.** No ADR is amended or superseded. This is Related-Work
  positioning in the lineage of ADR-0013 — concede, then locate — applied to a
  vendor practice document rather than to the research literature.
- **Mechanism-only scope.** No concrete instance, operator-specific asset, or
  domain content enters the core from this document (ADR-0011).

## Dated addenda

The playbook lives at a URL that can change; this correspondence is pinned to
the version archived on 2026-08-24. Future revisions get dated entries in this
section — what changed in the playbook, and what it does or does not move in
the mapping above — rather than a silent rewrite of the text above them.
ADR-0013 keeps its addenda the same way and for the same reason: a positioning
that quietly re-writes itself as its subject moves is not a record of
anything.

*No addenda yet.*
