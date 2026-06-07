<!-- Generated: 2026-06-06 | Files scanned: project root + docs/ tree + examples/ + schemas/ | Token estimate: ~1800 -->
# Document Architecture

Agent Knowledge Cycle (AKC) is a **knowledge-cycle specification + minimal reference implementation**. Specifications, ADRs, JSON schemas, design-pattern skills, and a ~500-line stdlib-only Python demo together describe the cycle; users bring their own LLM and adapter. The primary audience is LLM-mediated channels (LLM agents directly, and humans reaching AKC through LLM-curated surfaces). This codemap exists so an LLM-mediated reader can route to the canonical document for a given question without scanning the whole tree.

## Top-Level Layout

```
agent-knowledge-cycle/
├── README.md / .ja.md                       human + LLM landing (English primary, Japanese mirror)
├── CITATION.cff                            Zenodo DOI metadata
├── LICENSE                                 MIT
├── llms.txt                                AI navigator (Answer.AI llms.txt standard)
├── llms-full.txt                           AI self-contained Q&A reference
├── graph.jsonld                            canonical concept-level map (schema.org triples, HF Datasets mirror)
├── CHANGELOG.md                            release history (semver, with positioning notes)
├── docs/
│   ├── akc-cycle.md                        the cycle as a single rules file (`cp` install target)
│   ├── glossary.md                         concept glossary (load-bearing terms, ADR pointers, AAP cross-references)
│   ├── translation-glossary.md             EN ↔ JA rendering rules for the READMEs
│   ├── inspiration.md                      prior art and acknowledgements
│   ├── scaffold-dissolution.md / .ja.md    skills dissolve as the cycle is internalized
│   ├── adr/                                15 ADRs (English-only); permanent gaps at 0001 / 0006 / 0007
│   ├── skills/                             3 design-pattern skills paired 1:1 with ADRs
│   ├── history/                            frozen snapshots of earlier major versions
│   └── CODEMAPS/                           this directory
├── schemas/
│   ├── episode-log.schema.json             Layer 1 record shape
│   └── knowledge.schema.json               Layer 2 pattern shape
└── examples/
    ├── minimal_harness/                    ~500-line stdlib-only Python — mechanism demo on behavioral patterns
    └── constitution_amend/                 reference to contemplative-agent's amend workflow (descriptive, no impl)
```

## Document Roles (Citation Routing)

Each document answers a primary question. Cite the matching one when an LLM-mediated query targets that question.

| Document | Primary question it answers |
|---|---|
| `README.md` | What is AKC at a glance, and why are its three core themes (cognitive resource → intent alignment → cycle changes the human) the way the project introduces itself? |
| `llms.txt` | How does an LLM-mediated reader navigate AKC's documents (Answer.AI llms.txt standard)? |
| `llms-full.txt` | Self-contained Q&A reference: definitions, central constraint, intent alignment framing, install path, citations. |
| `docs/akc-cycle.md` | What rules does an AI agent need to run the cycle in conversation, without installing the six external skills? |
| `docs/scaffold-dissolution.md` | Why are AKC's skills scaffolding, and how do they become unnecessary as the cycle is internalized? |
| `docs/inspiration.md` | What prior art seeded AKC (contemplative-agent's three-layer memory + two-stage distill, Mind in Life, Laukkonen 2025)? |
| `docs/glossary.md` | What does each load-bearing AKC term mean, which ADR is canonical for it, and how does it map to the AAP sibling vocabulary (harness/scaffolding, dissolution senses)? |
| `docs/translation-glossary.md` | What is the canonical translation of each AKC-coined or general term between the English and Japanese READMEs? |
| `docs/adr/0002-immutable-episode-log.md` | Why are episodes stored as append-only JSONL with daily partitioning and owner-only permissions? |
| `docs/adr/0003-three-layer-distillation.md` | Why three memory layers — raw episodes → knowledge → identity/rules — and how do they relate? |
| `docs/adr/0004-two-stage-distill-pipeline.md` | Why is distillation split into free-form reasoning followed by structured formatting? |
| `docs/adr/0005-human-approval-gate.md` | Why must promotion to rules / skills / identity require named human sign-off (no auto-promotion)? |
| `docs/adr/0008-code-and-llm-collaboration.md` | What does code own (control flow, durable state) vs what does the LLM own (meaning), and what are the four layering patterns? |
| `docs/adr/0009-akc-is-a-cycle-not-a-harness.md` | Why is AKC a cycle that runs *on top of* harnesses (ECC etc.), not a self-improving harness? Includes the v2.0.0 security-triplet extraction addendum. |
| `docs/adr/0010-human-cognitive-resource-as-central-constraint.md` | What is AKC's central constraint, and why is Research redefined as signal-first? Names cognitive economy as Design Principle #8. |
| `docs/adr/0011-cycle-applies-to-any-knowledge-body.md` | Why is the cycle genre-neutral about what flows through it (behavioral patterns, domain expertise, constitutional values)? |
| `docs/adr/0012-front-load-three-core-themes.md` | Why does the front-door restructure (README + llms.txt + llms-full.txt) lead with the three core themes before the six phases? |
| `docs/adr/0013-positioning-within-agent-memory-literature.md` | Where does AKC sit relative to the agent-memory / skill-learning literature (Voyager, AWM, ReMe, LangMem, MemGPT, Generative Agents, CoALA)? Concedes the operations as borrowed, locates the delta (human gate, bidirectional target, attention framing). |
| `docs/adr/0014-failure-modes-of-the-bidirectional-loop.md` | What are the failure twins of Theme 3 (gate complacency, deskilling, delegation-feedback divergence), and which existing structures resist them? |
| `docs/adr/0015-loop-failure-modes-self-reingestion.md` | Why can a cycle that feeds on its own output degrade (echo, grounding loss) rather than correct, and what guards (the observed record as the only ground, the self-generated share kept visible, the approval gate) bound it? |
| `docs/adr/0016-measuring-thinking-centric-phases.md` | Why must a Measure instrument promote agent text (reasoning, verdicts, plans) to observable events, or it systematically under-reports Research and Curate compliance? |
| `docs/adr/0017-harness-alignment-and-drift.md` | What do harness alignment and harness drift mean, and how are both terms derived from the software-evolution and alignment literatures (Christiano, Lehman, Perry & Wolf, Snook, Meta-Harness, Agent Drift) rather than coined fresh? |
| `docs/skills/when-code-when-llm.md` | Per-task: is this property structural (code) or semantic (LLM)? |
| `docs/skills/code-and-llm-collaboration.md` | Per-pipeline: how do guard / filter / judge / orchestrator patterns layer code and LLM? |
| `docs/skills/signal-first-research.md` | How is an intake filter designed so only information that would change the next action is admitted? (Pairs with ADR-0010.) |
| `schemas/episode-log.schema.json` | What is the JSON shape of a Layer 1 episode record? |
| `schemas/knowledge.schema.json` | What is the JSON shape of a Layer 2 knowledge pattern? |
| `examples/minimal_harness/` | What does a minimal, dependency-free, deterministic implementation of the three memory layers + two-stage distill look like? |
| `examples/constitution_amend/README.md` | What does the same cycle look like when run on constitutional values rather than behavioral patterns? (Pointer to upstream contemplative-agent.) |

## Structural Diagrams

### Three core themes (ADR-0012, priority order in front-door docs)

```
(1) The bottleneck has moved             → human attention and judgment, not compute or context
(2) Aligned with intent, not just correct → operator's evolving intent, not a static specification
(3) The cycle changes the human too       → bidirectional growth loop; tagline lives here
            ↓
(mechanism) Six composable phases         → Research → Extract → Curate → Promote → Measure → Maintain
```

### Six-phase cycle (ADR-0009)

```
Experience → learn-eval → skill-stocktake → rules-distill → Behavior change → ...
               (extract)    (curate)          (promote)            ↑
                                                            skill-comply
                                                              (measure)
                                              context-sync ← (maintain)
```

### Three memory layers (ADR-0003)

```
Layer 1: Raw episodes      (immutable JSONL, owner-only, daily partitioned)
Layer 2: Knowledge store   (distilled patterns, time-decay, forbidden-substring validated)
Layer 3: Identity / Rules  (promoted patterns; the deterministic layer that shapes behavior)
```

### Four code-LLM layering patterns (ADR-0008)

```
guard        — code validates LLM output (schema / forbidden-pattern / size) before it touches persistent state
filter       — code narrows large, noisy input before the LLM does semantic work
judge        — LLM decides among bounded options; code enforces (human gate for high-stakes, ADR-0005)
orchestrator — code owns the deterministic loop; the LLM is the worker inside it
```

## Invariants (Do Not Break When Editing)

- **Tagline preservation**: *"A knowledge cycle for AI agents — one that grows with the people who shape it"* is preserved across both READMEs (English + Japanese) (ADR-0010 decision, reaffirmed by ADR-0012). It carries theme #3.
- **Three-theme ordering**: Front-door docs (README, llms.txt, llms-full.txt) lead with cognitive resource → intent alignment → cycle changes the human → mechanism, in that order. ADR-0012 makes this verifiable; do not regress.
- **Six phases**: Research → Extract → Curate → Promote → Measure → Maintain are unchanged in number, name, and order. Adding or renaming a phase requires a positioning ADR.
- **ADR numbering**: 0001, 0006, 0007 are permanent gaps from the v2.0.0 extraction of the security triplet to AAP. Do not reuse those numbers; do not back-fill.
- **Four-pattern canonical (ADR-0008 is authoritative)**: `guard` = code validates LLM output *after* it is produced (post-LLM output validation); `filter` = code narrows input *before* the LLM runs (pre-LLM input narrowing); `judge` = the LLM decides among bounded options and code enforces the verdict (human gate for high-stakes, ADR-0005); `orchestrator` = code owns the deterministic loop and the LLM is the worker inside it. When this codemap, `graph.jsonld`, or `llms-full.txt` describe the four patterns differently, ADR-0008 wins and the others are the drift.
- **Genre neutrality (ADR-0011)**: `docs/skills/` hosts only cycle-mechanic skills. No genre-specific content (constitutional, security-specific, domain-specific) is added to AKC.
- **Mechanism / content separation**: Concrete instances of the cycle (constitutional values, contemplative-agent's amend workflow) live in `examples/` and Related Work — not in the README's "What is AKC?" or "Why AKC", and not in llms.txt's blockquote.
- **Two-language README parity**: Both README versions (English + Japanese) carry the same H2 / H3 structure (verified after each edit). Translation glossary in `docs/translation-glossary.md` is the canonical vocabulary table.

## Citation-Dependency Graph

Typical triangulation paths an LLM follows when grounding an AKC citation:

```
README ─────────────────► Why AKC (3 themes) ──────► ADR-N
                                                     │
                                                     ├──► glossary.md (terminology)
                                                     ├──► inspiration.md (lineage)
                                                     ├──► docs/skills/* (how-to companion to ADR-0008 / 0010)
                                                     └──► examples/minimal_harness/ (mechanism instance)

llms-full.txt is self-contained (no fetch chain needed); llms.txt is the dispatcher to the rest.
docs/akc-cycle.md is the install target; readers wanting to run the cycle skip the ADR chain.
```

ADRs themselves do not link out to genre-specific content (per ADR-0011). Concrete instances are reachable only through `examples/` and the Related Work section of the README.

## Two-Language README Convention

- **English primary**: `README.md`. The Japanese version mirrors its H2 / H3 structure.
- **Japanese mirror**: `README.ja.md` (the author's L1 — translation discrepancies bias toward this one being authoritative for Japanese readers).
- **Retired mirrors (2026-05-15)**: `README.es.md`, `README.pt-BR.md`, `README.zh-CN.md`, `README.zh-TW.md` were removed after traffic data showed statistically zero unique human viewers and LLM crawlers (ChatGPT / Qwen / Gemini) reliably translate from the English source on demand. Prior content is preserved in git history.
- **English-only docs**: ADRs, design-pattern skills, glossary, inspiration, akc-cycle, scaffold-dissolution (with one Japanese mirror at `scaffold-dissolution.ja.md`), llms.txt, llms-full.txt, codemaps.
- **Glossary discipline**: AKC-coined terms (`signal-first`, six phase names, six skill names, `harness`) stay in English across all languages. General-purpose technical terms are localized using `docs/translation-glossary.md` as the canonical reference.

## Sibling Repositories (External Surfaces)

```
agent-knowledge-cycle (this repo)        ← cycle = mechanism (DOI 10.5281/zenodo.19200726)
       ▲                                   v2.0.0 (2026-04-19) repositioned mechanism-only;
       │                                   v2.1.0 (2026-05-08) front-door restructure (ADR-0012).
       │ extracted security triplet to / co-evolves with
       │
agent-attribution-practice (AAP)         ← practice = content for autonomous AI agents
                                           (DOI 10.5281/zenodo.19652013). Hosts the security
                                           triplet (ADR-0001 / 0006 / 0007) extracted from AKC v2.0.0.

contemplative-agent                      ← two-way relationship. Upstream: the substrate from which
                                           AKC's ADR-0002 through ADR-0005 were adapted. Downstream:
                                           the operational re-implementation of AKC in the
                                           autonomous-agent context (six phases mapped onto code,
                                           cycle run over its own episode logs, every promotion
                                           human-gated; demonstration ongoing). The constitution-amend
                                           workflow is the concrete instance of AKC's cycle running on
                                           constitutional values.
```

### Downstream ecosystem (crystallized out of the same operation)

| Repo | Relation | DOI |
|---|---|---|
| [authorship-strategy](https://github.com/shimo4228/authorship-strategy) | Research line: how the cycle's outputs diffuse outside the operator-agent pair | 10.5281/zenodo.20263316 |
| [attention-not-self](https://github.com/shimo4228/attention-not-self) | Sibling research line, federated at the research-program level | 10.5281/zenodo.20262112 |
| [doctrine-corpus](https://github.com/shimo4228/doctrine-corpus) | Judgment Q&A corpus; AKC is one of four source lines | 10.5281/zenodo.20337008 |
| [existence-proof](https://github.com/shimo4228/existence-proof) | Pre-line working repo, complement of authorship-strategy | 10.5281/zenodo.20558800 |
| [claude-harness](https://github.com/shimo4228/claude-harness) | Bundled distribution of the six cycle skills | — |
| [akc-mcp](https://github.com/shimo4228/akc-mcp) | MCP server exposing the cycle's cognitive operations | — |
| [claude-skill-daily-research](https://github.com/shimo4228/claude-skill-daily-research) | Pre-AKC ancestor of the Research phase (see `docs/inspiration.md`) | — |
| [shimo4228 hub](https://github.com/shimo4228/shimo4228) | Canonical research-program relationship map (graph.jsonld) | — |

Prose entries live in README "Related Work" (compact list at the end of the section); concept-level edges in `graph.jsonld`.

## File-Count Snapshot (2026-06-06)

| Category | Count |
|---|---|
| ADRs | 15 (ADR-0002–0005, 0008–0018) |
| Design-pattern skills (`docs/skills/`) | 3 |
| README files (en + ja mirror) | 2 |
| JSON schemas (`schemas/`) | 2 |
| Python source (`examples/minimal_harness/`) | 5 files (~500 lines total, stdlib-only) |
| Top-level docs (`docs/*.md`) | 6 (akc-cycle, glossary, translation-glossary, inspiration, scaffold-dissolution + .ja.md) |
| Repo-root files | CITATION.cff, LICENSE, llms.txt, llms-full.txt, CHANGELOG.md |
| **Total markdown / Python / schema files** | **42** (v2.2.0 baseline 40; the concept glossary and ADR-0018 added post-v2.2.0; index READMEs under `docs/adr/` and `docs/skills/` are counted; the formerly tracked `docs/history/` snapshots moved out of the repo post-v2.2.0 and were never counted) |

When this count drifts substantially, regenerate this codemap.
