# Changelog

All notable changes to AKC are recorded here. AKC follows semantic
versioning; breaking changes to positioning or public interfaces bump the
major version.

## Unreleased

### Removed

- **Multi-language README mirrors (es, pt-BR, zh-CN, zh-TW)** retired on 2026-05-15. Repository now ships English (`README.md`) + Japanese (`README.ja.md`) only. Decision driven by traffic data: 30-day GitHub traffic showed 11 unique human viewers across all README versions combined, while 106 unique cloners (and downstream LLM crawler fetches) drove the actual interaction. LLM crawlers (ChatGPT, Qwen, Gemini observed 2026-05) reliably translate the English source on demand, making the mirrors performative rather than functional. Glossary, CODEMAPS, and ADR-0012 updated to reflect the two-language convention. Prior content remains in git history for restoration if audience evidence changes.

## v2.1.0 — 2026-05-08

Front-door restructure. README, llms.txt, and llms-full.txt are reorganized
so the three core themes — (1) human cognitive-resource scarcity as the
central constraint, (2) intent alignment over individual correctness, and
(3) the cycle changing the human as much as the agent — appear in priority
order before the six-phase mechanism. Tagline preserved per ADR-0010. See
[ADR-0012](docs/adr/0012-front-load-three-core-themes.md) for the
positioning rationale.

### Why v2.1.0 and not v2.0.1

The reading order of the front-door documents changes meaningfully — what
appears first determines what AI search engines and human readers learn
about AKC. v2.0.x readers encountered mechanism-first prose; v2.1.0 readers
encounter the constraint and the alignment goal first. This is additive
(no ADRs amended, no design principles changed, no schemas or reference
implementation touched), so no major bump is warranted, but the front
door's signature changes enough that it deserves a minor bump.

### Changed

- **README.md "What is AKC?"** is rewritten in four paragraphs that lead
  with cognitive-resource scarcity, then intent alignment, then the cycle
  changing the human, then the six phases as the means.
- **README.md section order** — old "Why a cycle?" and "Whose cognitive
  budget?" sections are merged into a single new H2 "Why AKC" placed
  between "What is AKC?" and "What's in this repo". Three H3 subsections
  appear in theme order: *The bottleneck has moved*, *Aligned with intent,
  not just correct*, *The cycle changes the human too*.
- **README.md "Relationship to Harness Engineering"** — the
  intent-alignment paragraph is shortened to a positioning contrast and
  links back to "Why AKC → Aligned with intent".
- **llms.txt** blockquote is reordered so cognitive-resource scarcity
  leads, then intent alignment (newly written paragraph), then the cycle
  changing the human, then the six-phase mechanism.
- **llms-full.txt** opening definition is rewritten so its grammatical
  subject is the scarcity constraint, with the six-phase loop appearing
  in the same sentence as the means rather than the headline. Q&A is
  reordered: "What is AKC's central constraint?" promoted from Q9 to Q2;
  new Q3 added — "How does AKC frame intent alignment?".
- **Five language versions of README.md** (ja, es, pt-BR, zh-CN, zh-TW)
  synced to the new English structure.
- **README "What's in this repo" section trimmed.** The 50-line
  repository tree is moved to a dedicated `docs/CODEMAPS/` directory
  (matching the AAP convention: `INDEX.md` + `architecture.md`) and
  replaced in the README with a brief summary paragraph and a link.
  The Why AKC → cycle → install reading flow is no longer interrupted
  by the file-structure block.

### Added

- **`docs/adr/0012-front-load-three-core-themes.md`** — new ADR
  recording the front-door reorder decision and the verifiable
  commitments for the three themes appearing in priority order in
  README.md, llms.txt, and llms-full.txt.
- **`docs/CODEMAPS/`** — codemaps directory matching the AAP
  convention. `INDEX.md` is the navigator; `architecture.md` carries
  the full tree, document-role routing table, structural diagrams
  (three themes / six phases / three memory layers / four code-LLM
  layering patterns), invariants, citation-dependency graph,
  six-language translation convention, sibling-repo map, and
  file-count snapshot. Linked from every language version of the
  README and from llms.txt.
- **Glossary entries** in `docs/glossary.md`: *intent alignment*,
  *bottleneck*, *cognitive economy*, *cognitive resource*, *scarce
  resource*, *co-develop*, *attention and judgment* — all with five
  language renderings to keep translations in sync.
- **GitHub repo About** — description rewritten to surface theme #1
  and theme #2 alongside the preserved tagline; topics pruned of v1.x /
  v2.0.0-extraction residue (`self-improvement`, `self-improving-agent`,
  `prompt-injection`, `security-by-absence`) and extended with five
  theme-aligned topics (`agent-alignment`, `human-in-the-loop`,
  `cognitive-economy`, `human-ai-collaboration`, `signal-first`).

### Unchanged

- **Tagline.** *"A knowledge cycle for AI agents — one that grows with
  the people who shape it"* remains, per ADR-0010's preservation
  decision and ADR-0012's reaffirmation.
- **Six phases.** Research → Extract → Curate → Promote → Measure →
  Maintain are unchanged in number, name, and order.
- **Design principles.** All eight remain in effect with the same
  numbering. DP #3 (Non-destructive) and DP #8 (Cognitive economy) are
  referenced inline from "Why AKC" but not amended.
- **ADRs in effect.** ADR-0002 through ADR-0011 remain in effect as
  written. ADR-0012 is additive.
- **Reference implementation.** No code changes to
  `examples/minimal_harness/` or to `schemas/`.
- **Cycle skills.** The six external skill repositories
  (search-first, learn-eval, skill-stocktake, rules-distill,
  skill-comply, context-sync) are unchanged.

## v2.0.0 — 2026-04-19

Major positioning release. AKC declares the cycle **genre-neutral** about
the knowledge body that flows through it — behavioral patterns, domain
expertise, or constitutional values all run through the same six phases.
The security triplet that had sat in AKC through v1.x (Security by Absence,
Single External Adapter, Untrusted Content Boundary) is extracted as
genre-specific contemplative-agent content and no longer ships with AKC.

### Why v2.0.0 and not v1.9.0

AKC's identity contract changes. Prior: "a knowledge cycle for AI agents,
with Security by Absence as a first-class design principle." Current: "a
knowledge cycle for AI agents, mechanism-only, genre-neutral about what
flows through it." Academic citations resolving to v1.x will see a
different Design Principles list and a different ADR set. ADR-0009 already
established the precedent for positioning-breaking changes warranting a
version bump; the security triplet extraction completes what ADR-0009
started, and the identity-contract shift is the direct reason this is a
major bump rather than a minor one.

### Removed

- **`docs/adr/0001-security-by-absence.md`** — genre-specific to the
  contemplative-agent lineage. Extracted to local archive at
  `_archive/akc-security-triplet-2026-04/` for future re-expression.
- **`docs/adr/0006-single-external-adapter.md`** — genre-specific.
  Extracted to the same archive.
- **`docs/adr/0007-untrusted-content-boundary.md`** — genre-specific.
  Extracted to the same archive.
- **`docs/skills/llm-agent-security-principles.md`** — design-pattern
  skill that bundled the three security ADRs' concrete defense patterns.
  Extracted to the same archive.
- **Design Principle #7 (Security by Absence)** from the README —
  removed from the design principles list. Former #8 (Code-LLM Layering)
  renumbers to #7; former #9 (Human cognitive resource) renumbers to #8.

### Added

- **`docs/adr/0011-cycle-applies-to-any-knowledge-body.md`** — new ADR
  declaring genre neutrality as a first-class positioning statement, with
  three falsifiable commitments: no future AKC ADR encodes domain-specific
  content, `docs/skills/` hosts only cycle-mechanic skills, and external
  projects may cite AKC as their cycle substrate without AKC making
  claims about their content.
- **`docs/adr/0009-akc-is-a-cycle-not-a-harness.md` 2026-04-19
  addendum** — records the concrete security-triplet extraction that
  completes ADR-0009's demotion. Documents the consequences: ADR
  numbering gaps at 0001, 0006, 0007; design principles 9 → 8;
  supersession of the original "ADRs 0001–0008 unchanged" claim.
- **`examples/constitution_amend/`** — new examples entry that points
  at contemplative-agent's Constitution-amend workflow as a concrete
  instance of the AKC cycle applied to constitutional values.
  Descriptive only; the directory ships no implementation. Paired with
  ADR-0011's "Concrete instance in the wild" section, this makes
  genre neutrality observable: `minimal_harness/` shows the mechanism
  on behavioral patterns, `constitution_amend/` shows the same
  mechanism on values.

### Changed

- **ADR numbering**: gaps at 0001, 0006, 0007 are intentional and
  permanent. ADR numbers are identifiers, not positions in a sequence.
- **README.md / README.ja.md** — repo tree, counts (8 ADRs, 8 design
  principles, 3 design-pattern skills), "Related Work" section (no
  longer mentions security-by-absence as prior-art inheritance).
- **`docs/adr/README.md`** — index updated; note explaining the
  numbering gaps added.
- **`docs/skills/README.md`** — design-pattern skill table shrunk from
  4 to 3 entries.
- **`docs/inspiration.md`** — "What AKC does not carry over" extended
  with the security triplet; prior-art table narrowed to ADR-0002
  through ADR-0005 and the minimal_harness reference.
- **`examples/minimal_harness/README.md`** — "What is not implemented"
  section collapsed around the one remaining stance (Layer 3 gated on
  human review). Footnote explains that the forbidden-substring
  validation pattern in `knowledge_store.py` is inherited from upstream
  genre work even though the ADR pointers no longer live in this repo.
- **`examples/minimal_harness/knowledge_store.py`** — comment and
  docstring references to ADR-0007 replaced with a neutral description
  of the defensive pattern. Behavior is unchanged.
- **`llms.txt` / `llms-full.txt`** — all counts, ADR lists, and
  skill lists updated to the v2.0.0 state. A new Q&A section in
  `llms-full.txt` ("What knowledge bodies can run through the AKC
  cycle?") replaces the former "What does AKC deliberately not
  implement?" section, reflecting the genre-neutrality shift.
- **`CITATION.cff`** — version 2.0.0; abstract rewritten; the
  `security-by-absence` keyword removed and `genre-neutrality` added.

### Migration notes for v1.x citations and downstream repositories

- External links pointing at `docs/adr/0001-security-by-absence.md`,
  `docs/adr/0006-single-external-adapter.md`, or
  `docs/adr/0007-untrusted-content-boundary.md` at `main` HEAD will
  404. Commit-pinned links (via GitHub permalinks) continue to resolve.
  The content is preserved locally at
  `_archive/akc-security-triplet-2026-04/` on the author's machine;
  future re-expression is expected in the contemplative-agent lineage.
- Academic citations pinned to v1.x continue to describe the state at
  that version. No action is required for prior citations.
- Downstream projects that adopted AKC's security-by-absence design
  principle may continue to do so — the principle itself is sound —
  but should no longer cite AKC as its source. Contemplative-agent is
  the upstream.

## v1.8.1 — 2026-04-18

Patch release. Completes the three-layer structure introduced by v1.8.0
(principle → pattern → implementation) by adding the design-pattern skill
paired with ADR-0010, records the self-referential origin loop in
ADR-0010's Notes, and extends `inspiration.md` with the daily-research
upstream that preceded Contemplative Agent.

### Added

- **`docs/skills/signal-first-research.md`** — design-pattern skill
  paired 1:1 with ADR-0010. Covers the define-signal-before-search rule,
  the search-wide / intake-narrow asymmetry, three abstract worked
  examples (daily digest, session-scoped filter, exploration mode), and
  a diagnostic checklist. Written as a generic pattern guide — personal
  project references live in `docs/inspiration.md`, not in the skill
  body.
- **`docs/inspiration.md` new "Upstream: a daily signal filter"
  section** — documents that AKC's origin chain extends one hop further
  back than Contemplative Agent, to the daily-research pipeline that
  surfaced Laukkonen et al. (2025) in the first place and later
  generated the report that triggered ADR-0010.

### Changed

- **`docs/adr/0010-...md` Notes** — extended with an "Origin loop"
  observation: the pipeline that named the signal-first principle had
  been practicing it for months. The principle was lived before it was
  stated.
- **`README.md` / `README.ja.md`** — design-pattern skill count 3 → 4
  in the repo tree and opening summary.
- **`docs/skills/README.md`** — index table extended with
  signal-first-research ↔ ADR-0010 pairing.
- **`CITATION.cff`** bumped to v1.8.1.
- **`llms.txt`** — ADR-0010 entry cross-references the new pattern
  skill; design-pattern skills list extended.

## v1.8.0 — 2026-04-18

Architectural depth release. AKC surfaces the implicit design philosophy
that has shaped every phase since inception: **human cognitive resources
are the central constraint**. The Research phase is redefined as
signal-first, a new design principle is added, and "Why a cycle?" is
extended with the cognitive-economy paragraph. No code changes; this is
a documentation release.

See [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md)
for the full rationale.

### Added

- **ADR-0010 Human Cognitive Resource as Central Constraint** —
  articulates the implicit philosophy driving every AKC phase: as agent
  capability grows, the scarce resource shifts from compute to human
  attention and judgment. Names three concrete mechanisms: signal-first
  Research, cognitive economy as Design Principle #9, and pre-implementation
  dialogue as investment.
- **Design Principle #9 "Human cognitive resource is the bottleneck"**
  added to the README. Nine principles total now.
- **"Whose cognitive budget is the cycle protecting?" subsection** in
  the README "Why a cycle?" section — explicit statement that the
  cycle's target resource is human attention, with one line per phase
  tying the design back to that target.
- **v1.8.0 geo-writer snapshot** — baseline and post-change scores on
  README are recorded in ADR-0010 as a self-application of the Measure
  phase to AKC's own documentation.

### Changed

- **docs/akc-cycle.md Research phase** — retitled from "Search before
  building" to "Search broadly, filter by signal". A new step 0 asks
  the agent to define the signal (what information would change the
  next action) before searching. An intake paragraph clarifies that
  signal-first is the default stance; exploration phases are legitimate
  exceptions when named explicitly.
- **README Research summary rows** — both the cycle table and the rules
  table restate Research as "Search broadly, filter by signal".
- **CITATION.cff** — bumped to v1.8.0. Abstract extended with the
  cognitive-economy framing. Added keywords: `signal-first`,
  `cognitive-economy`.
- **llms.txt** — opening summary extended with the cognitive-resource
  axis. ADR-0010 added to the index.
- **docs/adr/README.md** — ADR-0010 added to the index table.

### Not changed

- The six phases. Research → Extract → Curate → Promote → Measure →
  Maintain remain unchanged in number, order, and composition.
- ADR-0001 through ADR-0009. All prior decisions remain in effect.
- Reference implementation (`examples/minimal_harness/`). No code
  changes.
- Tagline. "A knowledge cycle for AI agents — one that grows with the
  people who shape it" is retained. ADR-0010 adds depth beneath the
  ADR-0009 framing rather than replacing it.

## v1.7.0 — 2026-04-11

Conceptual repositioning. AKC is no longer described as a "self-improving
harness." It is now a **knowledge cycle for AI agents — one that grows
with the people who shape it**. No code changes; this is a positioning
release with significant documentation updates.

See [ADR-0009](docs/adr/0009-akc-is-a-cycle-not-a-harness.md) for the
full rationale.

### Added

- **ADR-0009 AKC is a Cycle, Not a Harness** — articulates why the
  "self-improving harness" framing was wrong (layer confusion with ECC,
  two-pillar drift, missing bidirectional growth) and how AKC is now
  positioned. Catalogues the three concrete changes: cycle as the sole
  defining characteristic, Security by Absence demoted to a design
  principle, bidirectional growth made explicit.
- **README "Acknowledgments" section** — explicit recognition that AKC
  grew out of daily use of Everything Claude Code (ECC). Without ECC as
  the practical baseline, AKC would not exist.
- **README "References" section** — post-hoc theoretical resonances
  noticed after the fact: Thompson's *Mind in Life* (structural
  coupling) and Laukkonen, Friston, & Chandaria's *A Beautiful Loop*
  (recursive self-modeling). AKC was built from practice, not theory;
  these references are listed for readers who might find the resonance
  interesting.
- **README bidirectional growth language** — the cycle is not a
  one-directional optimization loop. The human side changes too:
  judgment about what to keep and discard, intuition about when to adopt
  versus build, sensitivity to what makes a rule good versus vague.

### Changed

- **README tagline** — "A memory-centric, self-improving harness for
  AI agents" → "A knowledge cycle for AI agents — one that grows with
  the people who shape it."
- **README "What is AKC?"** — removed Security by Absence as a co-equal
  pillar. The cycle is now the sole defining characteristic. Security
  by Absence remains in Design Principles #7 and ADR-0001.
- **docs/akc-cycle.md** — removed the Security by Absence section.
  Security remains as a design principle and as ADR-0001; it is no
  longer presented as a phase-equivalent rule in the rules file.
- **CITATION.cff** — bumped to v1.7.0. Abstract rewritten to match the
  new positioning. Removed `harness` keyword; added `bidirectional-growth`
  and `human-ai-collaboration` keywords.
- **llms.txt** — opening summary rewritten. ADR-0009 added to the index.
- **README BibTeX note** — updated to match new tagline.
- **GitHub repository description** — updated to match new tagline.

### Not changed

- The six phases (Research → Extract → Curate → Promote → Measure →
  Maintain). The cycle skills (`search-first`, `learn-eval`,
  `skill-stocktake`, `rules-distill`, `skill-comply`, `context-sync`).
- ADRs 0001–0008. Schemas. Reference implementation
  (`examples/minimal_harness/`). Design-pattern skills.
- Security by Absence as a design principle and as a load-bearing
  guarantee. Only its rhetorical position changed, not its content.
- The repository name, the abbreviation AKC, and the project identifier.

### Why a minor bump

Pure semver would call a docs-only change a patch. v1.7.0 is a minor
bump because the README is part of the project's identity contract:
what AKC *is* changed in this release, even though no code did. The
distinction matters for academic citation — work referencing AKC v1.6
encounters the harness framing, while v1.7 onward encounters the cycle
framing.

## v1.6.0 — 2026-04-09

Additive release. The eighth ADR and a new category of skills
(design-pattern skills) — long-form "how" guides paired 1:1 with ADRs,
shipped inside the repository alongside the ADRs they correspond to.

### Added

- **ADR-0008 Code and LLM Collaboration** — names the principle behind
  ADR-0004 (two-stage distill), ADR-0005 (approval gate), and ADR-0007
  (untrusted boundary): code owns determinism and control flow, LLMs
  own meaning. Catalogues four layering patterns (LLM→Code guard,
  Code filter→LLM, LLM judge + Code enforce, Code orchestrator + LLM
  worker).
- **docs/skills/** — new directory for design-pattern skills:
  - `when-code-when-llm.md` — per-task decision framework (structural
    vs semantic) with worked examples in both directions
  - `code-and-llm-collaboration.md` — per-pipeline layering patterns
    with composition rules and a diagnostic checklist
  - `llm-agent-security-principles.md` — concrete defense patterns for
    ADR-0001 / ADR-0006 / ADR-0007 including HTTP, credential, and
    LLM-host hardening
- **README Design Principle #8** — Code-LLM Layering.
- **README "two kinds of skills"** — explicit distinction between cycle
  skills (six external repositories, one per phase) and design-pattern
  skills (in-repo, paired with ADRs).

### Changed

- **ADR-0001 Security by Absence** — added an Audit test section with
  a ready-to-run `git grep` compliance check and a pointer to the
  `llm-agent-security-principles` skill for the full "how" reference.
- **docs/adr/README.md** — ADR-0008 added to the index.
- **llms.txt** — ADR-0008 entry and a design-pattern-skills section
  added.
- **CITATION.cff** — bumped to v1.6.0, date updated.

### Relationship to contemplative-agent

The three design-pattern skills are adapted from skills accumulated
during contemplative-agent research work. The contemplative-agent
repository itself is unchanged and remains an independent research
project.

## v1.5.0 — 2026-04-09

Additive release. The six-phase cycle, the six skills, and the rules
install path are unchanged. v1.5 adds a second foundational principle
(Security by Absence), seven ADRs, JSON schemas, and a dependency-free
Python reference implementation adapted from the contemplative-agent
research repository.

### Added

- `docs/adr/` — seven new architecture decision records:
  - ADR-0001 Security by Absence as a First-Class Principle
  - ADR-0002 Immutable Episode Log as Source of Truth
  - ADR-0003 Three-Layer Distillation (Raw → Knowledge → Identity/Rules)
  - ADR-0004 Two-Stage Distill Pipeline (Free-form → Format)
  - ADR-0005 Human Approval Gate for Behavior-Modifying Changes
  - ADR-0006 Single External Adapter per Agent Process
  - ADR-0007 Untrusted Content Boundary
- `schemas/episode-log.schema.json` and `schemas/knowledge.schema.json` —
  JSON Schema definitions for the two persistent layers, usable
  independently of any implementation.
- `examples/minimal_harness/` — a dependency-free Python reference
  implementation (~300 lines) demonstrating the three-layer memory
  architecture and the two-stage distill pipeline. Runs with a
  deterministic fake LLM; no network or API keys required.
- `docs/inspiration.md` — prior-art credit to the contemplative-agent
  research repository.
- `docs/akc-cycle.md` — new 7th principle: **Security by Absence**.
  Loaded as a rule, so the principle applies to every session that
  installs the rules file.

### Changed

- `README.md` — rewritten intro. AKC is now described as a
  "memory-centric, self-improving harness" built on two complementary
  principles (the cycle, and Security by Absence). The six-skill table,
  rules install path, harness-engineering comparison, and scaffold
  dissolution links are preserved. Design Principles gain a 7th entry.
- `CITATION.cff` — bumped to v2.0.0, abstract updated to match the new
  positioning, `date-released` updated.

### Archived

- `docs/history/README-v1.4.md` — the v1.4.0 README is preserved verbatim
  for citation integrity.

### Not changed

- The six-phase cycle (Research → Extract → Curate → Promote → Measure →
  Maintain) and the six external skill repositories.
- The Design Principles 1–6 (composable, observable, non-destructive,
  tool-agnostic, evaluation-scales, scaffold-dissolution).
- `docs/akc-cycle.md` phases — only an additional principle is appended.

### Relationship to contemplative-agent

AKC v2.0 absorbs specifications and reference code from
[contemplative-agent](https://github.com/shimo4228/contemplative-agent),
which remains an independent research repository. AKC does not depend on
contemplative-agent; contemplative-agent does not depend on AKC. See
`docs/inspiration.md`.

## v1.4.0 — 2026-02-22

Initial Zenodo release. DOI: 10.5281/zenodo.19200727.
