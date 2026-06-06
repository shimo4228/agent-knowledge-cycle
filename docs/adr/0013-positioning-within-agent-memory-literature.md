# ADR-0013: Positioning Within the Agent-Memory Literature

> **Summary.** AKC's individual operations — Promote (skill/memory induction), Curate (memory pruning and refinement), Extract (turning episodes into reusable patterns) — are not novel as isolated mechanisms. Each has named precedent in the agent-memory and skill-learning literature: Voyager and Agent Workflow Memory induce reusable skills; ReMe and LangMem refine procedural memory; Generative Agents, MemGPT, and CoALA formalize memory hierarchies and the reflection that distills experience. ADR-0013 concedes this directly and locates AKC's delta on the *shared axis* those systems define. The delta is not a new operation. It is (1) a structural human approval gate where the prior art runs the operations autonomously, (2) a target of *bidirectional* human-judgment growth where the prior art optimizes the agent or its context, and (3) a framing of the scarce resource as *human attention* where the prior art treats agent capability, context window, or information volume as the binding constraint. Those three are exactly the three core themes (ADR-0012). This ADR is the project's explicit Related-Work positioning, written once so it does not have to be re-argued in each front-door document.

## Status
accepted

## Date
2026-06-06

## Context

Through v2.1.x, AKC's README listed "Related Work" as three sibling projects (contemplative-agent, AAP, the author's article feeds) and a "References" section of resonance-only works (Thompson 2007; Laukkonen, Friston & Chandaria 2025) that were explicitly *not consulted during construction*. Neither section situates AKC against the body of work it most obviously overlaps: the agent-memory and skill-learning literature. A reader arriving from that literature — someone who knows Voyager's skill library, MemGPT's paged memory, or LangMem's procedural-memory refinement — has no place in the repository that answers the obvious question: *isn't this just another memory system with a six-phase coat of paint?*

The gap became concrete from three signals.

**Signal 1: the operations are independently named in the literature.** AKC's phases are not inventions. Several are well-established operations with their own papers:

- **Extract / Promote (induce reusable skills from experience).** Voyager (Wang et al., 2023) maintains an "ever-growing skill library of executable code" induced from gameplay. Agent Workflow Memory (Wang et al., 2024) induces "commonly reused routines, i.e., workflows" from agent trajectories and feeds them back into subsequent generations. Both are, in AKC vocabulary, Extract-then-Promote run end to end.
- **Curate (prune and refine accumulated memory).** ReMe — *Remember Me, Refine Me* (Cao et al., 2025, arXiv:2512.10696) — is a "dynamic procedural memory framework" whose entire premise is moving "beyond static memory approaches" by continuously refining what is stored. LangMem (LangChain, 2025) ships memory tools that "control what gets stored," maintain "memory consistency," and "optimize agent behavior through prompt updates." Both are Curate-and-Promote loops by another name.
- **Extract / reflection (distill episodes into durable patterns).** Generative Agents (Park et al., 2023) introduced a reflection step that synthesizes observations into higher-level inferences stored for later retrieval. MemGPT (Packer et al., 2023) formalizes a memory hierarchy with paging between context and external store. CoALA — Cognitive Architectures for Language Agents (Sumers et al., 2023) — provides the framework vocabulary (modular memory, structured action space, decision procedure) that makes all of the above commensurable.

A 2026 survey, *Externalization in LLM Agents* (Zhou et al., 2026, arXiv:2604.08224), frames the whole field as four coupled forms of externalization — memory, skills, protocols, and harness engineering — in which "capabilities that earlier systems expected the model to recover internally are now externalized." AKC is squarely inside that frame. Pretending otherwise would be a false novelty claim, the kind ADR-0011 was written to prevent.

**Signal 2: the silence reads as either ignorance or evasion.** A repository that overlaps a well-cited literature and never names it invites one of two unflattering readings: the author does not know the prior art, or the author is hiding it to inflate originality. Both are corrosive to the authenticity the project is built on. The honest move is to name the precedent for each operation and then state plainly what is and is not new.

**Signal 3: the delta is real but lives in the ADRs, not in a positioning statement.** AKC's actual contribution is already decided — ADR-0005 (human approval gate), ADR-0009 (bidirectional growth), ADR-0010 (human cognitive resource as the constraint), ADR-0012 (the three themes front-loaded). What was missing is a single ADR that *locates* that contribution on the same axis the literature defines, so the delta is legible as a delta rather than as a parallel vocabulary. Without it, every front-door document re-argues the positioning from scratch, and AI search engines excerpting any one of them surface the mechanism overlap without the distinction.

The common diagnosis: AKC has a defensible position relative to the agent-memory literature, but the position has never been written down as a position. ADR-0013 writes it down.

## Decision

AKC adopts an explicit positioning statement against the agent-memory and skill-learning literature, structured in two moves: **concede, then locate**.

### 1. Concede: the operations are not novel in isolation

For each phase whose mechanism has named precedent, AKC concedes the precedent by name rather than implying invention:

| AKC operation | Named precedent | What the precedent does |
|---|---|---|
| Extract → Promote (skill induction) | Voyager (Wang et al., 2023); Agent Workflow Memory (Wang et al., 2024) | Induce reusable, executable skills/workflows from trajectories and feed them back |
| Curate (prune / refine memory) | ReMe (Cao et al., 2025); LangMem (LangChain, 2025) | Continuously refine procedural memory; control what is stored; update behavior via prompts |
| Extract (reflection / distillation) | Generative Agents (Park et al., 2023); MemGPT (Packer et al., 2023) | Reflect observations into higher-level inferences; page a memory hierarchy |
| (framework vocabulary) | CoALA (Sumers et al., 2023); *Externalization in LLM Agents* (Zhou et al., 2026) | Formalize modular memory, action space, decision procedure; map the externalization field |

Conceded plainly: an AKC phase run as an isolated operation — "induce a skill from this session," "prune stale memories," "reflect these episodes into a pattern" — is *not* a new mechanism. The literature got there first, repeatedly, with implementations more mature than AKC's reference harness.

### 2. Locate: AKC's delta on the shared axis

The shared axis the literature defines is *how an agent turns its own experience into durable, reusable knowledge*. AKC sits on that axis and differs in three load-bearing ways — the same three core themes ADR-0012 front-loads:

1. **A structural human approval gate, where the prior art runs autonomously.** Voyager, AWM, ReMe, and LangMem are designed to close the loop *without a human in it*: the agent induces, refines, and re-applies skills on its own. AKC's Promote phase does the opposite by design (ADR-0005): any change that modifies future behavior is proposed and waits for explicit human sign-off, with no "auto-approve after N days" escape hatch. This is not a missing automation feature; it is the defining structural choice. The prior art optimizes for an unattended loop; AKC optimizes for a human-owned one.

2. **A target of *bidirectional* human-judgment growth, where the prior art optimizes the agent or its context.** Every system above measures success on the agent side — higher task success, better skill reuse, longer effective context. AKC's stated target (ADR-0009) is bidirectional: Curate and Promote sharpen the *human's* judgment about what knowledge is worth keeping, even as they sharpen the agent's. The loop grows the operator, not only the model. No system in the agent-memory literature names the human's developing judgment as an output to optimize for; for them the human is, at most, an annotator.

3. **A framing of the scarce resource as *human attention*, where the prior art treats agent capability, context, or information volume as binding.** MemGPT's constraint is the context window; ReMe's and LangMem's is memory consistency and retrieval quality; Voyager's and AWM's is task-completion capability. AKC (ADR-0010) names a different ceiling: human attention and judgment, which become *relatively* scarcer as agent capability grows. The memory literature solves information-side scarcity (the agent can't hold or recall enough); AKC solves attention-side scarcity (the human's fixed judgment budget is the ceiling). Both are valid; they bind on different resources and can coexist.

These three are not three positioning tricks; they are the three core themes (ADR-0012) restated as a literature delta. The positioning and the identity are the same statement seen from two sides.

### 3. This is orthogonal to ADR-0009's harness positioning

ADR-0009 positioned AKC against *harness* systems (ECC, Claude Code's skills, Meta-Harness) along the axis "is this a harness or something that runs on one?" ADR-0013 positions AKC against *memory and skill-learning* systems along a different axis: "how does experience become durable knowledge, and who owns the loop?" The two positionings are orthogonal and both required. A reader can accept ADR-0009 (AKC is not a harness) and still ask ADR-0013's question (isn't AKC just a memory system?). ADR-0013 answers the second without disturbing the first. Where ADR-0009 contrasts AKC with the layer *below* it (the harness), ADR-0013 contrasts AKC with the layer it is most often *confused for* (the memory/skill store).

### What does not change

- **The six phases.** Research → Extract → Curate → Promote → Measure → Maintain are unchanged in number, name, and order. ADR-0013 names their precedents; it does not redefine them.
- **The three core themes.** ADR-0012's themes are unchanged. ADR-0013 re-expresses them as a literature delta; it does not add a fourth.
- **ADRs in effect.** ADR-0002 through ADR-0012 remain in effect. ADR-0013 cites them; it amends none.
- **Reference implementation.** No code changes to `examples/minimal_harness/` or the JSON schemas.
- **Mechanism-only scope.** The cited systems are named as precedent and contrast only. No genre-specific threat model, domain content, or concrete instance enters the core from this ADR (ADR-0011).

## Alternatives Considered

- **Leave Related Work as sibling-projects-only and never name the literature.** Rejected. Silence against an obvious, well-cited overlap reads as ignorance or evasion (Signal 2) and undercuts the authenticity the project depends on. Conceding precedent costs nothing and sharpens the delta.

- **Claim the phases as novel and not cite the literature.** Rejected as false. Voyager, AWM, ReMe, and LangMem implement AKC's operations as isolated mechanisms, several with more mature engineering. A novelty claim here would be exactly the kind of inflated positioning ADR-0011's falsifiable commitments exist to prevent. AKC's honesty about *what is borrowed* is what makes its claim about *what is new* credible.

- **Write the positioning as a README "Related Work" expansion only, with no ADR.** Rejected. The positioning is a judgment — *the delta is the human gate, the bidirectional target, and the attention framing, not the operations* — and judgments belong in an ADR so they survive README rewrites. A README section without an ADR behind it drifts; the ADR is the artifact a future reviewer checks the README against (the same discipline ADR-0012 applied to the three themes).

- **Fold this into ADR-0009 as an addendum.** Rejected. ADR-0009 positions against harnesses; this positions against memory systems. They are orthogonal axes (Decision §3). Merging them would re-create the "two-pillar drift" ADR-0009 itself diagnosed — forcing readers to hold two unrelated positionings as one. Separate axes get separate ADRs.

- **Position against the full *Externalization* taxonomy (memory, skills, protocols, harness) point by point.** Deferred. AKC overlaps the memory and skills quadrants directly; protocols and harness are adjacent but not the confusion AKC most needs to dispel. Naming the survey as the field map is enough here; a four-quadrant treatment, if ever needed, is a separate ADR.

## Consequences

### Positive

- A reader arriving from the agent-memory literature finds AKC's relationship to Voyager / AWM / ReMe / LangMem / MemGPT / Generative Agents / CoALA stated plainly, with the delta located on the shared axis rather than asserted as parallel vocabulary.
- The three core themes gain a second articulation — as a literature delta — that is legible to readers who think in terms of prior work rather than in terms of AKC's internal vocabulary. The positioning and the identity reinforce each other.
- The honesty of conceding precedent strengthens, rather than weakens, the novelty claim. "These operations are not new; this loop ownership and this scarce-resource framing are" is a more credible and more defensible statement than an unqualified originality claim.
- Front-door documents (README "Related Work", llms-full.txt) now have a single ADR to point at instead of re-arguing the positioning. AI search engines excerpting the positioning surface the delta, not just the overlap.

### Negative

- The cited literature moves quickly. ReMe, LangMem, and the *Externalization* survey are recent; newer systems will appear that also implement AKC's operations, and the concession table will read as incomplete over time. The mitigation is that ADR-0013 concedes the *category* of precedent (skill induction, memory refinement, reflection), not an exhaustive list; new entrants strengthen the concession rather than invalidating it.
- Naming specific systems dates the ADR, the same risk ADR-0010 flagged for naming the LLM-Wiki wave. Accepted here because the concession is the point — it must name names to be honest — and the delta (human gate, bidirectional target, attention framing) is the durable claim that outlives any specific citation.

### Neutral

- No code changes. No schema changes. The six phases, three themes, nine design principles, and reference implementation are unchanged. ADR-0013 is a positioning decision, not an architectural one — the same shape as ADR-0009 and ADR-0012.

## Relationship to other ADRs

- **ADR-0005 (Human Approval Gate).** ADR-0005 is the mechanism that makes delta #1 real: the structural gate is *why* AKC's loop is human-owned where the prior art's is autonomous. ADR-0013 cites ADR-0005 as the concrete instantiation of its first distinction from the literature.
- **ADR-0009 (AKC is a Cycle, Not a Harness).** Orthogonal positioning. ADR-0009 separates AKC from the harness *below* it; ADR-0013 separates AKC from the memory/skill store it is *confused for*. Both are required; neither subsumes the other (Decision §3).
- **ADR-0010 (Human Cognitive Resource as Central Constraint).** ADR-0010 names the attention-side scarcity that is delta #3. ADR-0013 contrasts that framing against the literature's information-side and capability-side constraints, making ADR-0010's claim legible as a difference rather than a restatement.
- **ADR-0012 (Front-load the Three Core Themes).** ADR-0013 re-expresses ADR-0012's three themes as a literature delta. ADR-0012 makes the themes visible in the front door; ADR-0013 makes them defensible against the prior art. The two are the inward-facing and outward-facing views of the same three claims.

---

**Notes.** ADR-0013 is a positioning ADR in the lineage of ADR-0009 and ADR-0012: it introduces no new principle and no new mechanism. It records a single judgment — that AKC's operations are borrowed but its loop ownership, bidirectional target, and scarce-resource framing are not — so the project never has to re-argue its relationship to the agent-memory literature from scratch. The cited works (CoALA, Voyager, Generative Agents, MemGPT, ReMe, Agent Workflow Memory, LangMem, and the *Externalization in LLM Agents* survey) were identified as prior art *for positioning*, not consulted during AKC's construction; the distinction matters and is preserved from the README's "References" framing.
