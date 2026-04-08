# Changelog

All notable changes to AKC are recorded here. AKC follows semantic
versioning; breaking changes to positioning or public interfaces bump the
major version.

## v2.0.0 — 2026-04-09

Scope expansion: AKC is now positioned as a **memory-centric,
self-improving harness** rather than solely a cyclic self-improvement
architecture. The six-phase cycle remains unchanged; the v2.0 release
adds a second foundational principle (Security by Absence) and absorbs
engineering decisions from the contemplative-agent research repository
as harness-neutral specifications.

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
