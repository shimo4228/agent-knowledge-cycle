# ADR-0012: Front-load the Three Core Themes in Front-door Documentation

> **Summary.** AKC is held together by three claims — (1) human cognitive resources are the scarce constraint, (2) the cycle keeps agent behavior aligned with the operator's evolving intent rather than with a static specification, and (3) the cycle changes the human as much as it changes the agent. Through v2.0.x, all three were present in the repository but distributed across ADR-0010, Design Principle #8, the "Why a cycle?" section, and the harness-engineering relationship section. None were front-loaded in the documents readers and AI search engines actually open first: README.md, llms.txt, and llms-full.txt. ADR-0012 reorders those three documents so the three themes appear in priority order — cognitive resource → intent alignment → the cycle changes the human too — before the six-phase mechanism. The tagline is preserved per ADR-0010's existing decision.

## Status
accepted

## Date
2026-05-08

## Context

ADR-0010 (2026-04-18) named human cognitive resource scarcity as AKC's central constraint and added Design Principle #8 to the README. ADR-0011 (2026-04-19) declared the cycle genre-neutral. Both decisions are correct and remain in effect. What ADR-0012 addresses is a downstream observation that surfaced after both ADRs had been in place for several weeks: readers were still describing AKC as "a six-phase cycle for keeping agent skills updated" — a mechanism description — and not as the cognitive-economy + intent-alignment system that the ADRs intended.

Three signals made the gap concrete.

**Signal 1: README lead is mechanism-first.** The opening sentence of "What is AKC?" was *"AKC treats agent knowledge as a living asset: episodes are logged immutably, distilled into patterns, promoted to rules, and continuously audited."* The grammatical subject is *agent knowledge*; the verb chain is mechanism. The cognitive-economy framing — strongest in ADR-0010's first sentence — appeared at line 144 of the README, behind a 50-line repository tree. A reader scrolling top-down hit mechanism, then file structure, then rationale — the inverse of what ADR-0010 implies should be visible first.

**Signal 2: Intent alignment is reactive in the README.** The phrase "intent alignment" appears once in the README, inside the *Relationship to Harness Engineering* section, framed as a contrast to harness engineering's correctness focus. As an independent claim — that AKC's purpose is to keep behavior aligned with the operator's evolving intent — it has no dedicated position. A reader who never reaches the harness-engineering section never encounters the framing.

**Signal 3: The bidirectional loop is described in jargon.** The most prominent statement of the loop reads *"it is a bidirectional growth loop where human and agent co-develop through sustained interaction."* For a reader who has not absorbed AKC vocabulary, "bidirectional growth loop" parses as filler. The descriptive claim — *the cycle changes the human too* — is shorter, clearer, and already present elsewhere in the same section, but never leads.

llms.txt and llms-full.txt sit closer to ADR-0010's center of gravity (the cognitive-resource paragraph appears in the second blockquote paragraph of llms.txt; the central-constraint Q&A is question 9 of llms-full.txt). But neither *leads* with the three themes. AI search engines that excerpt the first paragraph or first three Q&As surface the mechanism description, not the constraints that motivate it.

The common diagnosis: the three themes were correct, additive, and ADR-backed — and they were nonetheless invisible to anyone who entered through the front door without already knowing what to look for. Front-door documents had drifted out of alignment with the ADRs that govern them.

## Decision

AKC's front-door documents are restructured so the three core themes appear in priority order — **cognitive resource → intent alignment → the cycle changes the human too** — before the six-phase mechanism. Concrete changes:

### 1. README.md "What is AKC?" rewrite

The opening section is rewritten in four paragraphs:

1. **Cognitive resource (theme #1).** First sentence states ADR-0010's central claim: as agent capability grows, the scarce resource is human attention and judgment. ADR-0010 is linked inline.
2. **Intent alignment (theme #2).** Second paragraph distinguishes alignment from correctness. Correctness can be checked by tests; alignment cannot, because intent itself moves as the operator's judgment sharpens.
3. **The cycle changes the human too (theme #3).** Third paragraph leads with the descriptive claim — *the cycle changes the human too* — and uses the tagline ("grows *with* the people who shape it, not *for* them") as the textual hook. The technical name *bidirectional growth loop* is preserved at the end of the paragraph as an "underneath" reference, not as the headline.
4. **Six phases as the means.** Fourth paragraph names the phases as the mechanism that operationalizes the first three.

### 2. README.md "Why AKC" H2 placed before the repo tree

The existing "Why a cycle?" and "Whose cognitive budget is the cycle protecting?" sections are merged into a single H2 — "Why AKC" — placed immediately after "What is AKC?" and **before** the repository tree. Three H3 subsections appear in theme order: *The bottleneck has moved*, *Aligned with intent, not just correct*, *The cycle changes the human too*.

The repository tree, the cycle table, the rules-install instructions, and design principles all remain — they are pushed below "Why AKC" rather than rewritten. The intent-alignment paragraph in *Relationship to Harness Engineering* is shortened to a positioning contrast and points back to "Why AKC".

### 3. llms.txt blockquote reordered

The five-paragraph blockquote is reordered: cognitive resource → intent alignment (newly written, drawn from ADR-0010 + the harness-engineering contrast) → the cycle changes the human too → six-phase mechanism + signal-first → not-a-harness positioning → ships-as. Existing wording is preserved wherever possible; only the intent-alignment paragraph is new prose.

### 4. llms-full.txt opening rewrite + Q&A reorder

The opening definition (line 8) is rewritten so the grammatical subject is *cognitive resource scarcity*, with the six-phase loop appearing in the same sentence as the means rather than the headline. The Q&A list is reordered: *What is AKC's central constraint?* is promoted from Q9 to Q2; a new Q3 — *How does AKC frame intent alignment?* — is inserted. The remaining questions retain their original answers but renumber.

### 5. Translations sync

The Japanese mirror `README.ja.md` is updated after the English source is approved. `docs/glossary.md` is extended with five new keyword rows (intent alignment, bottleneck, cognitive economy, scarce resource, co-develop) before translation begins, so the translator reaches the target vocabulary.

(Historical note: at the time of the original decision, this step covered five language versions — ja, es, pt-BR, zh-CN, zh-TW. The es / pt-BR / zh-CN / zh-TW mirrors were retired on 2026-05-15 after traffic data showed statistically zero unique human viewers and LLM crawlers reliably translate from the English source on demand. Step 5 now applies only to the Japanese mirror.)

### 6. GitHub repo About is updated

The repository description is rewritten from 181 to ~290 chars to surface theme #1 (scarcity of human attention and judgment) and theme #2 (aligned with operator intent) inside the existing tagline lead. Topics are pruned of v1.x and v2.0.0-extraction residue (`self-improvement`, `self-improving-agent`, `prompt-injection`, `security-by-absence`) and extended with five theme-aligned topics (`agent-alignment`, `human-in-the-loop`, `cognitive-economy`, `human-ai-collaboration`, `signal-first`).

### What does not change

- **Tagline.** *"A knowledge cycle for AI agents — one that grows with the people who shape it"* remains. ADR-0010 already considered and rejected replacing it; that decision stands. The tagline carries theme #3 in compressed form, and ADR-0012 builds on that compression rather than overwriting it.
- **Six phases.** Research → Extract → Curate → Promote → Measure → Maintain remain unchanged in number, name, and order.
- **ADRs in effect.** ADR-0002 through ADR-0011 remain in effect. ADR-0012 reorders how readers encounter them; it does not amend their content.
- **Reference implementation.** No code changes to `examples/minimal_harness/` or to the JSON schemas.
- **Design principles.** The eight design principles remain. DP #8 (Cognitive economy) and DP #3 (Non-destructive) are referenced inline from the new "Why AKC" section but are not rewritten.

## Alternatives Considered

- **Update the tagline to name cognitive economy directly.** Rejected, restating ADR-0010's reasoning. The tagline carries theme #3 in compressed form. Replacing it to name theme #1 explicitly would either dilute theme #3 or balloon the tagline beyond its current length. The body-rewrite path achieves the same surfacing without disturbing the tagline that ADR-0009 introduced and ADR-0010 protected.

- **Add a new top-level H2 *before* "What is AKC?" — e.g., "The constraint behind AKC".** Rejected. A reader's first scan is the H1 plus the first H2. Inserting a new H2 ahead of "What is AKC?" would push the canonical project description down by one section and would invite future readers to ask which is the actual self-description. Rewriting "What is AKC?" so the three themes lead inside it preserves the document's existing top-level shape.

- **Leave the README untouched and rely on ADR-0010 + Design Principle #8.** Rejected. ADR-0010 was published 2026-04-18 and Design Principle #8 was added the same day. By 2026-05-08, the README front-door had had three weeks of operation under ADR-0010, and the gap between ADR statement and reader interpretation had not closed. The mechanism-first lead in the README is doing more work than DP #8 can reverse.

- **Write a new ADR but make no document changes — leave restructure for later.** Rejected. The repository is approaching a DOI-versioned release. An ADR that describes a future change, with no corresponding edit, would invite drift between the ADR catalogue and the actual front door — exactly the failure mode ADR-0011 warned against in its second falsifiable commitment ("`docs/skills/` will host only cycle-mechanic skills" — a structural test, not a hopeful one).

- **Translate llms.txt and llms-full.txt as part of the same restructure.** Deferred. Both documents currently exist only in English. Whether to translate them is a separate decision (cost vs. AI-search-engine multilingual coverage) and is out of scope for ADR-0012.

## Consequences

### Positive

- The three themes become identifiable at a glance. A reader who scans only the first thirty lines of README.md, the blockquote of llms.txt, or the first three questions of llms-full.txt now encounters all three.
- AI search engines that excerpt the first paragraph or first three Q&As of llms-full.txt will surface the cognitive-economy + intent-alignment framing rather than the mechanism description. The GEO/SEO surface area for theme-shaped queries ("how do AI agents stay aligned with operator intent?", "what limits human-in-the-loop AI workflows?") expands measurably.
- The harness-engineering relationship section becomes a positioning contrast rather than the only place the alignment claim is stated. Readers entering via Mitchell Hashimoto's vocabulary still find the contrast, but readers entering with no context now have an independent statement to engage with.
- The repository tree drops below the rationale rather than above it. The tree's role as a navigation aid (rather than as the description of the project) is made explicit by position.

### Negative

- LLMs that have already trained on the v2.0.x README and llms-full.txt will continue to surface mechanism-first answers until their next training cut. This is a transient cost, not a structural problem; the repository can do nothing to accelerate it.
- A reader returning to the repository after several weeks will encounter a different lead than they remember. The tagline is preserved precisely to mitigate this — the most-quoted phrasing is the part that does not change.
- "Why AKC" before the repository tree adds one more H2 that a reader scrolls past before reaching `git clone` instructions. This is the cost of moving rationale ahead of mechanism; ADR-0012 considers it the right trade-off, given that mechanism-first was the failure mode being corrected.

### Neutral

- No code changes. No schema changes. The eight design principles, six phases, and reference implementation are unchanged. ADR-0012 is a documentation-architecture decision, not an architectural one.

## Relationship to other ADRs

- **ADR-0009 (AKC is a Cycle, Not a Harness).** ADR-0009 set the cycle as the sole defining characteristic and introduced the "grows with the people who shape it" tagline. ADR-0012 protects that tagline while bringing the body of the front-door documents into alignment with the three themes ADR-0010 and the surrounding ADRs already governed.
- **ADR-0010 (Human Cognitive Resource as Central Constraint).** ADR-0010 identified the scarce resource and added Design Principle #8. ADR-0012 finishes the work: it surfaces the principle in the documents readers encounter first. The two ADRs together make cognitive economy both a stated principle (ADR-0010) and a document-level commitment (ADR-0012).
- **ADR-0011 (Cycle Applies to Any Knowledge Body).** ADR-0011's three falsifiable commitments protect the cycle from genre creep. ADR-0012 borrows the same review test: the front-door restructure must not introduce genre-specific content into the lead, and concrete instances (constitutional values, contemplative-agent's amend workflow) remain in `examples/` and Related Work — not in "Why AKC" or in the llms.txt blockquote.

## Verification

ADR-0012's commitments are observable:

1. The first thirty lines of `README.md` contain at least one phrase from each of the three theme clusters: {*cognitive resource*, *scarcity*, *human attention/judgment*}, {*intent alignment*, *aligned with intent*}, {*changes the human too*, *grows with*, *co-develop*}.
2. `README.md`'s table of contents has *Why AKC* between *What is AKC?* and *What's in this repo*.
3. `llms.txt`'s blockquote leads with the cognitive-resource paragraph; the second paragraph addresses intent alignment; the third paragraph addresses the cycle changing the human.
4. `llms-full.txt`'s Q2 is *What is AKC's central constraint?* and Q3 is *How does AKC frame intent alignment?*.
5. The five language versions of `README.md` retain the same H2/H3 structure as the English source.

A reviewer can check all five conditions in under five minutes. If any of them regresses in a future change, ADR-0012 is the artifact that records the original commitment.

---

**Notes.** ADR-0012 differs from ADR-0010 and ADR-0011 in shape: it is not introducing a new principle (ADR-0010) nor a new positioning claim (ADR-0011). It is enforcing the visibility of decisions already made. Treat it as a structural test of the front-door documents against the cumulative theme set ADR-0009, ADR-0010, and ADR-0011 jointly imply.
