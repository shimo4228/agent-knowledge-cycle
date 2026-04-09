# Changelog

All notable changes to AKC are recorded here. AKC follows semantic
versioning; breaking changes to positioning or public interfaces bump the
major version.

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
