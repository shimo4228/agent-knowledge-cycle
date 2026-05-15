<!-- Generated: 2026-05-08 | Total codemaps: 1 | Token estimate: ~250 -->
# Codemaps Index

Architectural documentation for **agent-knowledge-cycle (AKC)** — a DOI-registered knowledge-cycle specification + reference implementation (9 ADRs + 8 design principles + 3 design-pattern skills + 1 ~500-line Python reference, six README languages).
**Last Updated**: 2026-05-08 | **Repo**: 60+ markdown / Python / schema files; primary audience is LLM-mediated channels.

---

## Quick Navigation

### 1. [architecture.md](architecture.md) — Document Architecture

**Read first.** Top-level layout, document-role index, three-themes / six-phases / three-memory-layers structure, citation-dependency graph, six-language translation convention, sibling-repo relationships.

**Topics**:
- Top-level layout (`docs/`, `docs/adr/`, `docs/skills/`, `docs/CODEMAPS/`, `schemas/`, `examples/`)
- Document roles (which document answers which question — for citation routing)
- Three-themes ordering invariant (per ADR-0012: cognitive resource → intent alignment → cycle changes the human → mechanism)
- Six-phase cycle (Research → Extract → Curate → Promote → Measure → Maintain)
- Three memory layers (Raw episodes → Knowledge store → Identity/Rules)
- Four code-LLM layering patterns (guard, filter, judge, orchestrator)
- Citation-dependency graph (README → ADR-N → glossary → skills triangulation paths)
- LLM-facing artifacts (llms.txt, llms-full.txt) and how they relate to source docs
- Two-language README convention (English primary, ja mirror; zh-CN / zh-TW / pt-BR / es mirrors retired 2026-05-15 — git history preserves prior content)
- Sibling-repo map (contemplative-agent / agent-attribution-practice)
- File-count snapshot

**Use when**: Citing AKC from an LLM-mediated channel; deciding which document is canonical for a given question; navigating the ADR ↔ design-principle ↔ skill ↔ glossary web; understanding what the cycle is vs what flows through it (ADR-0011 genre neutrality).

---

## Maintenance

Regenerate when: (a) new ADR / design principle / top-level doc added, (b) sibling-repo relationships change, (c) translation language set changes, (d) reference implementation grows beyond `examples/minimal_harness/`. Stale codemaps lie about the structure — date-stamp them and treat them as decaying.
