# Changelog

All notable changes to AKC are recorded here. AKC follows semantic
versioning; breaking changes to positioning or public interfaces bump the
major version.

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
