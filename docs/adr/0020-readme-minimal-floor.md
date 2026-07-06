# ADR-0020: Minimal-floor README with Single-location Theme Presentation

> **Summary.** ADR-0012 correctly front-loaded the three core themes into README.md, but its prescription — a four-paragraph "What is AKC?" rewrite *and* a three-subsection "Why AKC" H2, both covering the same three themes in the same order — produced a double presentation. Combined with a skill list spread across three separate tables, the README grew dense enough (302 lines, 8 tables) to draw an operator complaint. ADR-0020 moves README.md to a minimal floor: the three themes get exactly one full presentation, the skill list collapses to one table, and everything else becomes a pointer into the repository's existing machine-readable floor (llms.txt, llms-full.txt, graph.jsonld) rather than a second copy of it. ADR-0012's front-load principle and its llms.txt / llms-full.txt commitments are unchanged; only the README-internal repetition and the assumption that README should itself be the full information floor are corrected.

## Status

accepted

## Date

2026-07-07

## Context

ADR-0012 (2026-05-08) front-loaded the three core themes in front-door documentation. Its README-side prescription created a double presentation: §1 rewrote "What is AKC?" as four paragraphs covering the three themes, and §2 added a "Why AKC" H2 with three H3 subsections covering the same three themes in the same order. Verification conditions 1, 2, and 5 froze this structure in place.

The resulting shape produced observed pain. On 2026-07-07 the operator reported that the README — 302 lines, 8 tables — is too dense; the same information recurs. Intent alignment appears in three places, the bidirectional loop in two, harness drift in four, the six-phase enumeration in three, and the skill list is spread across three different tables: the "Why AKC" maintenance-pressure table, the phase→skill scaffolding table, and the three-level adoption table. The README was trying to carry the project's entire explanation on its own.

The repository already maintains a machine-readable floor for that explanation: llms.txt (navigation), llms-full.txt (consolidated Q&A + factual reference, covering the nine design principles, the harness-engineering contrast, and the references trail), and graph.jsonld (concept map). Holding a second full copy of that floor inside README.md duplicates maintenance and is the structural root of the density complaint — every fact kept in two places is a fact that can drift between the two.

This is the same failure family ADR-0012 itself corrected — front-door drift — now surfacing in the opposite direction. ADR-0012 fixed the themes' *invisibility*; the fix overshot into *repetition*. ADR-0020 treats this as a second, corrective pass in the same lineage rather than a reversal of ADR-0012.

## Decision

1. **README.md moves to a minimal-floor structure.** It keeps only: (a) a short lead with definition, tagline, and companion-paper DOI; (b) a single "Why AKC" section — the *only* full presentation of the three themes, in the fixed order cognitive resource → intent alignment → the cycle changes the human too; (c) the cycle diagram with the single phase→skill table; (d) install instructions; (e) the fact table; (f) a compact repo-contents table; (g) short Limitations and Positioning paragraphs that point to the governing ADRs; (h) merged Origin & Acknowledgments; (i) How to Cite; (j) compact Related Work; (k) License.

2. **Everything else becomes a pointer, not a copy.** The nine design principles point to llms-full.txt + their individual ADRs; the References subsections point to ADR-0013 / ADR-0017 + llms-full.txt; the Harness Engineering comparison table collapses to a pointer to ADR-0009 / ADR-0017; the Customization section becomes one sentence in Install; the maintenance-pressure table becomes one or two prose sentences inside "Why AKC"; the three-level adoption table becomes two or three sentences in Install. No new documents are created. If a pointer-target gap is found during the rewrite, llms-full.txt is supplemented rather than the gap being patched back into README.

3. **ADR-0012's front-load principle is retained.** The first thirty lines of README.md must still contain at least one phrase from each of the three theme clusters, and the themes must still appear before the six-phase mechanism. What is amended is narrower than ADR-0012 itself: only the README-internal double presentation (ADR-0012 §1's four-paragraph "What is AKC?" theme treatment plus §2's H3×3) and the implicit license that gave README responsibility for the full information floor.

4. **Scope limit.** ADR-0012's commitments for llms.txt (blockquote ordering: cognitive resource → intent alignment → the cycle changes the human) and llms-full.txt (Q2 = central constraint, Q3 = intent alignment) remain in force unchanged. No pain was observed on the machine-readable side; those files gain explicit responsibility as the canonical floor rather than being rewritten.

5. **README.ja.md mirrors the English source in the same change**, per the existing en/ja convention (the four other language mirrors were already retired per ADR-0012 §5's historical note).

## Alternatives Considered

### Comply within ADR-0012's verification letter without amending it

Keep the "Why AKC" H2 position and the first-thirty-lines phrases; only compress "What is AKC?" into a shorter lead. Rejected: ADR-0012 §1/§2 explicitly prescribe the double presentation as written. Deduplicating the README while leaving the ADR's text untouched would leave the ADR and the front door contradicting each other — the exact ADR-catalogue-vs-front-door drift ADR-0012's own Alternatives section warned against.

### Keep the double presentation and merely shorten each occurrence

Rejected. Shortening both occurrences would reduce line count but leave the repetition structure intact — and that structure, not raw length, is the root of the observed pain.

### Re-legislate the whole front door, including the llms.txt / llms-full.txt commitments

Rejected. No pain was observed on the machine-readable side, and the repository's ADR evidence bar admits only observed pain or repeated practice, not a symmetry argument ("we changed README, so we should also change llms.txt").

## Consequences

### Positive

- README becomes scannable at first contact.
- Each concept has exactly one README home.
- The maintenance surface shrinks: one skill table instead of three.
- llms-full.txt's role as the canonical information floor becomes explicit rather than assumed.
- The density complaint's structural root — duplicated presentation — is removed rather than patched.

### Negative

- Readers who relied on the README as a self-contained reference must now follow pointers to llms-full.txt or the individual ADRs.
- LLMs trained on the v2.x README will continue to surface the old double-presentation structure until their next training cut. This is transient, as ADR-0012 already noted for the equivalent risk on its own change.
- ADR-0012's verification checklist must now be read together with this ADR; a reviewer checking ADR-0012 conditions 1, 2, and 5 in isolation will find them superseded here.

### Neutral / Follow-ups

- No code, schema, or mechanism changes. Six phases, tagline, and the DOI line are unchanged. Like ADR-0012, this is a documentation-architecture decision, not an architectural one.
- Future README line-count regression past roughly 200 lines (see Verification condition 4) is the trigger to re-audit against this ADR rather than to add a new ADR outright.

## Relationship to other ADRs

- **ADR-0012 (Front-load the Three Core Themes)**: amended, not revoked. The front-load principle and the llms.txt / llms-full.txt commitments survive unchanged; only the README-internal double presentation and the README-as-full-floor assumption are superseded. ADR-0020 is the second correction in the same front-door alignment family — ADR-0012 corrected invisibility, ADR-0020 corrects the overshoot into repetition that ADR-0012's own fix produced.
- **ADR-0010 (Human Cognitive Resource as Central Constraint)**: unaffected. Theme #1 remains the central constraint and remains front-loaded in the single "Why AKC" presentation.
- **ADR-0009 (AKC is a Cycle, Not a Harness)**: the tagline it introduced remains unchanged.
- **ADR-0011 (Cycle Applies to Any Knowledge Body)**: the genre-neutrality review test continues to apply to the rewritten lead — no genre-specific content enters the shortened "Why AKC" section.
- **ADR-0019 (Cycle Structure Is Provisional)**: same spirit applied to a different layer — there, the phase/skill binding is a provisional snapshot revisable on observed pain; here, the README's shape is the provisional structure being revised for the same reason.

## Verification

ADR-0020's conditions replace ADR-0012's conditions 1, 2, and 5 for README.md; ADR-0012's conditions 3–4 (covering llms.txt and llms-full.txt) stay in force unchanged.

1. The first thirty lines of `README.md` contain at least one phrase from each theme cluster: {*cognitive resource*, *scarcity*, *human attention/judgment*}, {*intent alignment*, *aligned with intent*}, {*changes the human too*, *grows with*, *co-develop*}.
2. The three themes receive exactly one full (multi-sentence) presentation in `README.md`, located before the six-phase mechanism section.
3. `README.md` contains exactly one skill-listing table (the phase→skill table).
4. `README.md` line count stays in the low hundreds (target ≈120–140 lines); a regression past ~200 lines is a signal to re-audit against this ADR.
5. `README.ja.md` retains the same H2 structure as the English source.

---

**Notes.** ADR-0020 is a corrective pass on ADR-0012's own fix, not a reversal of it — the same relationship ADR-0019 has to the reification it caught. The repository's front-door documents are themselves subject to the cycle they describe: a structure judged correct in May can be judged overshot in July, and the correction is recorded rather than silently patched.
