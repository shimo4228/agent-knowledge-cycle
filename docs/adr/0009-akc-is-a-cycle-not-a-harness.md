# ADR-0009: AKC is a Cycle, Not a Harness

> **Summary.** AKC is a knowledge cycle that runs on top of harnesses (like ECC), not a harness itself. The "self-improving harness" framing put AKC in the wrong layer — competing with the very harnesses it was meant to sustain. AKC's defining characteristic is the cycle, and the cycle's distinguishing feature is that it grows agent knowledge alongside the people who shape it.

## Status
accepted

## Date
2026-04-11

## Context

From v1.0 through v1.6, AKC was described as "a memory-centric, self-improving harness for AI agents." That framing was technically defensible — the repository ships ADRs, schemas, and a reference implementation that together describe how an agent's memory and skills should be organized — but it created two persistent problems.

**Problem 1: layer confusion.** Calling AKC a *harness* put it in the same conceptual layer as Everything Claude Code (ECC), Claude Code's built-in skills system, and similar agent scaffolds. Readers assumed AKC was a competitor to those systems, an alternative harness to install in their place. But AKC was never built that way. It grew out of daily use of ECC as a baseline, by accumulating skills and rules on top of ECC and then needing a way to keep that accumulation coherent. AKC is what you do *to* a harness over time, not a replacement for one.

**Problem 2: two-pillar drift.** The v1.5/v1.6 framing presented AKC as built on "two complementary principles": the self-improvement loop and Security by Absence. Treating these as co-equal pillars made the identity of AKC harder to state. Readers had to hold both ideas simultaneously to understand what AKC was, and the cycle — which is the actual defining contribution — got diluted by the security framing. Security by Absence is load-bearing as a *design principle*, but it is not what makes AKC AKC.

A third issue surfaced as the project matured: the cycle does not just improve the agent. It also changes the human running it. Curate and Promote sharpen judgment about what knowledge is worth keeping. Research develops intuition for when to adopt versus build. Measure teaches what makes a good rule versus a vague aspiration. None of this was articulated in the v1.6 README, even though it was the lived experience of running AKC.

These three problems share a root cause: the harness framing pointed at the wrong center of gravity.

## Decision

AKC is reframed as **a knowledge cycle for AI agents — one that grows with the people who shape it**.

The repositioning has three concrete elements:

### 1. Cycle as the sole defining characteristic

AKC is a cycle. The six phases (Research → Extract → Curate → Promote → Measure → Maintain) are the definition. Everything else — ADRs, schemas, the reference implementation, the eight design principles — exists to support or instantiate the cycle. AKC is no longer described as having "two pillars."

### 2. Security by Absence demoted to a design principle

Security by Absence remains in the repository. ADR-0001 is unchanged. It is listed as Design Principle #7. But it is no longer presented as a co-equal definitional element of AKC. A future fork that ignored Security by Absence would be a *less safe* implementation of AKC, not a different thing entirely. The cycle is what would make it AKC.

### 3. Bidirectional growth made explicit

The README now states that AKC is not a one-directional optimization loop. The cycle changes the human too. This is not a metaphysical claim; it is a description of what running the cycle actually does. The "Why a cycle?" section spells out the human-side changes; the tagline ("one that grows with the people who shape it") signals it on first contact.

### What does not change

- Identifier: AKC. The repository name, the abbreviation, and the six phases are unchanged.
- ADRs 0001–0008: unchanged.
- Schemas, reference implementation, cycle skills (search-first, learn-eval, etc.): unchanged.
- Security guarantees: unchanged. The ADR remains; only its rhetorical position changes.
- Relationship to ECC: unchanged in substance, but now made explicit through a new Acknowledgments section.

## Alternatives Considered

- **Keep "harness" framing.** Rejected. The ECC competition reading was too persistent, and the two-pillar phrasing kept diluting the cycle.
- **"Meta-harness."** Rejected. The Meta-Harness paper (Lee et al., 2026) coined this term for an automated harness optimizer. Borrowing it would conflate two very different ideas — AKC is not automated, and it specifically depends on human judgment in the loop.
- **"Cognitive framework" / "Joint cognitive system."** Rejected. Both are existing terms with established meanings in cognitive science, and overclaiming kinship would create more confusion than clarity. AKC is closer to "knowledge cycle" because that is literally what the abbreviation has always stood for.
- **Drop Security by Absence entirely from the README.** Rejected. It is a load-bearing design principle and a real safety guarantee. Demoting it to one of eight principles is the right level — visible, but not definitional.
- **Add a separate "human side" section to the README.** Rejected as insufficient. The bidirectional growth is structural to AKC, not a sidebar. It belongs in the tagline and the opening section, not in an appendix.

## Consequences

### Positive

- AKC's position relative to ECC, Claude Code, and similar systems is no longer ambiguous. AKC is what you run *on top of* a harness, to keep the harness alive as your understanding evolves.
- The cycle is unobstructed. Readers encountering AKC for the first time meet the six phases as the central idea, not as one of two competing themes.
- The contrast with harness engineering (Hashimoto, 2025) and Meta-Harness (Lee et al., 2026) becomes sharper. Both of those focus on the agent side. AKC focuses on the human-agent loop. The "Relationship to Harness Engineering" section now lands more clearly because the framings no longer collide.
- Bidirectional growth becomes citeable. Future work that wants to reference AKC as an example of human-AI co-development has explicit language to point to.

### Negative

- Citations to v1.6 and earlier carry the old framing. Anyone reading AKC at the older DOI will see "self-improving harness" and may not realize the project has been repositioned. The CITATION.cff and Zenodo record need to be updated for the v1.7 release, and the old version remains in the version history.
- Some external references to AKC (blog posts, README mentions in other repos) may still describe AKC as a harness. There is no fix for this except to update them as they are noticed.

### Neutral

- No code changes. The reference implementation is untouched. The ADR set 0001–0008 is untouched. This is a positioning change, not a structural one — but the positioning change is significant enough to warrant a minor version bump.

## Relationship to other ADRs

- **ADR-0001 Security by Absence** — unchanged in content, demoted in rhetorical position. Still load-bearing, still a design principle, still listed in the README.
- **ADR-0008 Code-LLM Layering** — unaffected. The four layering patterns remain the canonical pipeline vocabulary.
- All other ADRs (0002–0007) — unaffected. They describe how the cycle is built, and the cycle itself is unchanged.

---

### Addendum — 2026-04-19: security triplet extracted

ADR-0009's demotion of Security by Absence was a necessary step but not a sufficient one. Through v1.8.x the security triplet (ADR-0001 Security by Absence, ADR-0006 Single External Adapter, ADR-0007 Untrusted Content Boundary), together with the `docs/skills/llm-agent-security-principles.md` skill, remained inside AKC as demoted-but-still-present concerns. Continued use revealed that the triplet is **genre-specific**: it encodes a stance appropriate to autonomous agents making side effects in the world (the contemplative-agent lineage), not a universal requirement of any knowledge cycle. An AKC user building, say, a pure documentation-distillation agent does not need Security by Absence as an AKC-level principle. The triplet belongs upstream with the genre that requires it.

In v2.0.0 the security-triplet files were removed from this repository:

- `docs/adr/0001-security-by-absence.md`
- `docs/adr/0006-single-external-adapter.md`
- `docs/adr/0007-untrusted-content-boundary.md`
- `docs/skills/llm-agent-security-principles.md`

Consequences of the extraction:

- The original "What does not change" list in this ADR stated that ADRs 0001–0008 were unchanged and that Security by Absence would remain in the repository as Design Principle #7. Both claims are now superseded by the v2.0.0 extraction; they accurately describe ADR-0009 at the time it was written (2026-04-11) but no longer describe current state.
- AKC's Design Principles shrink from nine to eight; numbers #8 (Code-LLM Layering) and #9 (Human cognitive resource) renumber to #7 and #8.
- The ADR numbering gaps at 0001, 0006, 0007 are intentional. ADR numbers are permanent identifiers; reusing a gap would mask the historical record.
- The cycle itself — the sole defining characteristic established by this ADR — is unchanged.

ADR-0011 (2026-04-19) generalizes this extraction into a positioning statement about genre neutrality. Read ADR-0011 together with this addendum: ADR-0009 established "cycle is the center," the addendum records the concrete act, and ADR-0011 records the principle that makes the act coherent.

---

**Notes.** This ADR was prompted by a single question from the project author: *"Calling AKC a harness is awkward — that puts it in competition with ECC, doesn't it?"* The answer turned out to require unwinding the two-pillar framing that had quietly accumulated since v1.5, and replacing it with a single sentence: AKC is a cycle that grows with the people who shape it.
