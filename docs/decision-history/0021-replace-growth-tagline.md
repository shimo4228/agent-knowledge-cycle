# ADR-0021: Replace the Growth Tagline

> **Summary.** ADR-0009 introduced the tagline "A knowledge cycle for AI agents — one that grows with the people who shape it," and ADR-0010 and ADR-0012 each explicitly reaffirmed keeping it. That tagline now collides with Nous Research's Hermes Agent tagline, "The agent that grows with you" (released February 2026, 46k+ GitHub stars) — Hermes's phrasing predates AKC's by two months, so AKC's tagline reads as derivative to the large and growing audience that encounters Hermes first. The collision is also semantically inverting: Hermes's "grows" describes agent-side autonomous self-improvement with no human gate, the exact framework class AKC positions against, so the shared vocabulary obscures AKC's actual differentiator instead of stating it. ADR-0021 replaces the tagline with "A knowledge cycle for AI agents — agent behavior compounds, human judgment sharpens," a parallel two-clause construction that drops the shared "grows with … you/them" structure entirely, encodes bidirectionality in its own syntax, and reuses vocabulary already anchored in the repository's abstracts and README body.

## Status

accepted

## Date

2026-07-08

## Context

ADR-0009 (2026-04-11) introduced the tagline "A knowledge cycle for AI agents — one that grows with the people who shape it" as the single-sentence carrier of AKC's bidirectional-growth repositioning. ADR-0010 considered and rejected replacing it ("Update the tagline to name cognitive economy directly" — rejected because the tagline was "only months old and still being absorbed by readers"). ADR-0012 reaffirmed the same decision explicitly: "Tagline … remains. ADR-0010 already considered and rejected replacing it; that decision stands."

That reaffirmed position now collides with an external release. Nous Research's Hermes Agent shipped in February 2026 under the tagline "The agent that grows with you" and has since drawn 46k+ GitHub stars (https://github.com/nousresearch/hermes-agent). Hermes's tagline predates AKC's own tagline (introduced April 2026) by two months. Temporal priority runs against AKC: to anyone who encounters Hermes first — an audience that is large and still growing — AKC's "one that grows with the people who shape it" reads as a derivative echo of "The agent that grows with you," not as an independent phrase.

The collision is not merely surface-level; it is semantically inverting. Hermes's "grows" describes agent-side autonomous self-improvement with no human approval gate — precisely the framework class AKC defines itself against (ADR-0005's Human Approval Gate, and the contrast with ReAct-style autonomous agents the author has separately flagged as unfit for this reason). Sharing that vocabulary conflates AKC with agent-centric growth marketing at exactly the point — the tagline, first contact — where AKC most needs to signal the opposite: a human-gated, bidirectional loop, not an ungated agent optimizing itself.

The project author raised the collision on 2026-07-08 and chose replacement over any of the alternatives that would have preserved some form of the "grows with" phrasing.

## Decision

Replace the tagline with **"A knowledge cycle for AI agents — agent behavior compounds, human judgment sharpens."** The Japanese README mirrors this as 「AI エージェントのための知識サイクル — エージェントの振る舞いは積み上がり、人間の判断は研がれる。」

The new form deliberately abandons the structure shared with Hermes (relative clause + "grows with" + a person object) in favor of a parallel two-clause construction with no second person and no "with." Bidirectionality is carried by the syntax itself — one clause per end of the loop — rather than by a single verb applied to a human object, so the tagline now states theme #1 (human judgment) and theme #3 (the bidirectional loop) at the same time, in the same breath, where the old tagline carried only theme #3.

The vocabulary is not new coinage: "judgment sharpens" already appears in the CITATION.cff / .zenodo.json abstracts and in the README body ("operating it sharpens the judgment that steers it"), so the replacement anchors densely to existing repository language rather than introducing a fresh phrase (coin-sparingly / anchor-densely discipline).

Scope of supersession is narrow. This ADR supersedes only the tagline-preservation clauses of ADR-0010 (its rejected alternative, "Update the tagline to name cognitive economy directly") and ADR-0012 (its "Tagline … remains" clause). Everything else in ADR-0009, ADR-0010, and ADR-0012 stands unchanged. The Measure checklists in ADR-0012 and ADR-0020 survive unchanged too: their theme-3 cluster check ({*changes the human too*, *grows with*, *co-develop*} within the README's first 30 lines) still passes via the body sentence "The cycle changes the human too" (README, near line 15), so no historical ADR text needs editing to keep those checklists green.

The tagline is updated in the same diff across: README.md (tagline, theme-3 body echo, BibTeX note), README.ja.md (same three spots), llms.txt (blockquote lead), llms-full.txt (harness-relation answer), CITATION.cff (abstract lead), .zenodo.json (description lead), codemeta.json (description lead — the CITATION.cff mirror), and docs/CODEMAPS/architecture.md (invariant #1, which now names the new tagline and cites this ADR). CHANGELOG gains an Unreleased entry; the Zenodo/citation surfaces pick up the change at the next release.

## Alternatives Considered

### Keep the tagline unchanged

Rejected. Temporal priority runs against AKC (Hermes: 2026-02; AKC's tagline: 2026-04), and the conflation cost grows as Hermes's popularity grows. ADR-0010's original reason for keeping the tagline — "still being absorbed by readers" — is now outweighed: what readers are increasingly absorbing is the wrong association, not the intended one.

### Verb-only swap: "one that sharpens the people who shape it"

Rejected by the author. It retains the same relative-clause-acting-on-people structure as Hermes's tagline and still reads as a derivative of "The agent that grows with you" — only the verb changed, not the shape that causes the collision.

### Two-sentence form: "A knowledge cycle for AI agents. It changes the human, too."

Considered. This form is maximally consistent with the existing theme-3 wording already used in the README body. It was not chosen because the parallel two-clause construction encodes bidirectionality directly in its own syntax and carries two themes (human judgment and the bidirectional loop) in a single sentence, rather than deferring theme #3 to a second sentence.

## Consequences

### Positive

- The tagline no longer borrows the vocabulary of the agent-centric self-improvement frameworks AKC defines itself against; first-contact readers now get theme #1 and theme #3 in one line instead of a phrase they may attribute to Hermes.
- Bidirectionality is stated more explicitly than before (two clauses, one per end of the loop) rather than compressed into a single "grows with" verb.
- The replacement vocabulary ("judgment sharpens") is already anchored in CITATION.cff / .zenodo.json / README body, so the change adds no new terms to track.

### Negative

- Three months of "grows with the people who shape it" circulation — readers, LLM training snapshots, citations of v2.x metadata — now point at a retired phrase.
- Historical ADRs (0009, 0010, 0012, 0018) still quote the old tagline verbatim; this is intended (they are records of past decisions, not live surfaces), but a reader skimming only those ADRs will see a phrase no longer present in the front door.
- The rewrite touches eight files in one diff (README.md, README.ja.md, llms.txt, llms-full.txt, CITATION.cff, .zenodo.json, codemeta.json, architecture.md), which is more surface area than a typical wording change.

### Neutral / Follow-ups

- Lesson recorded: taglines built from generic growth vocabulary are collision-prone in a fast-moving ecosystem; phrasing anchored in the project's own canonical vocabulary (rather than shared with the surrounding market) is more durable against this kind of drift.
- ADR-0012's and ADR-0020's Measure checklists are unaffected and require no edits; both still pass via the unchanged README body sentence.

## Relationship to other ADRs

- **ADR-0009 (AKC is a Cycle, Not a Harness)** — builds on it. The cycle-not-harness repositioning stands untouched; only the tagline artifact ADR-0009 introduced is replaced. The bidirectional claim it signaled is preserved and stated more explicitly in the new form.
- **ADR-0010 (Human Cognitive Resource as Central Constraint)** — amends its rejected alternative ("Update the tagline to name cognitive economy directly"). The rejection rationale — the tagline was still being absorbed — no longer holds under the Hermes collision. The new tagline additionally surfaces ADR-0010's own axis (human judgment) at first contact, which the old tagline did not.
- **ADR-0012 (Front-load Three Core Themes)** — amends its "Tagline … remains" clause. The three-theme front-loading discipline and its Measure checklist are unchanged and still pass.
- **ADR-0020 (README Minimal Floor)** — no change. Its checklist's theme-3 cluster is still satisfied by the unchanged README body sentence.
