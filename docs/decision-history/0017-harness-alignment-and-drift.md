# ADR-0017: Harness Alignment and Harness Drift

> **Summary.** AKC's relationship to harness engineering required a two-sentence circumlocution wherever it was explained — "harnesses optimize correctness on the first try, while AKC keeps the harnesses themselves aligned with intent as that intent evolves" — because the activity that sentence describes had no name. A four-domain literature search (software evolution, IS/organizational/safety science, ML/AI-safety, HCI/knowledge engineering) run on 2026-06-06 found no single established term that simultaneously captures (a) an alignment target that is operator intent, itself evolving; (b) a human-gated loop; and (c) continuous, not one-time, alignment. Every candidate covers at most a subset. ADR-0017 establishes two terms derived from the intersection of those vocabularies rather than coined fresh — the same "concede, then locate" move ADR-0013 made for the agent-memory literature, applied here to the software-evolution and alignment literatures. **Harness alignment** extends intent alignment (Christiano 2018) from agent behavior to the artifacts that shape behavior, and across time; **harness drift** names the failure mode in lineage with architectural drift (Perry & Wolf 1992), practical drift (Snook 2000), and agent drift (arXiv:2601.04170). A secondary finding the decision preserves: the 2026 agent-drift literature and the classical software-evolution literature are currently unconnected; harness drift, defined with explicit lineage to both, bridges that vocabulary gap by reference rather than by reinvention.

## Status

accepted

## Date

2026-06-06

## Context

Two surfaces in the README use the same concept without naming it. The sentence "harnesses optimize correctness on the first try, while AKC keeps the harnesses themselves aligned with intent as that intent evolves" appears in the "Why AKC → Aligned with intent" section. The table row "Are the harnesses themselves still valid?" appears in "Relationship to Harness Engineering." Every explanation of AKC's relationship to harness engineering requires this two-sentence circumlocution because the concept — the continuous activity of keeping an agent's harness aligned with the operator's evolving intent — has no name in the repository. An unnamed concept cannot be cited, indexed in a glossary, or encoded as a graph node.

Before establishing a name, a four-domain literature search was run on 2026-06-06 to find whether an established term already captures the concept. The three properties that must hold simultaneously are: (a) the alignment target is operator intent, which itself evolves; (b) the loop is human-gated; (c) alignment is sustained continuously, not configured once. The search covered software evolution, IS/organizational/safety science, ML/AI-safety, and HCI/knowledge engineering. No single term was found. The candidates and their disqualifying gaps follow.

**Intent alignment (Christiano 2018).** "When I say an AI A is aligned with an operator H, I mean: A is trying to do what H wants it to do" (Christiano, "Clarifying 'AI alignment'", ai-alignment.com, 2018; verified verbatim across three independent mirrors). The source also gives the correctness-versus-alignment distinction precisely: "the problem of getting your AI to try to do the right thing, not the problem of figuring out which thing is right." This is the nearest single-source anchor — but Christiano treats the operator's wants as static and says nothing about the configuration layer (skills, rules, documentation) that shapes the agent's behavior. AKC's README already uses the phrase "intent alignment" without citing Christiano; a missing reference relation this ADR repairs.

**Lehman's laws of software evolution (Lehman 1980).** "A program that is used and that as an implementation of its specification reflects some other reality, undergoes continual change or becomes progressively less useful" (Law I, Continuing Change; Lehman, "Programs, Life Cycles, and Laws of Software Evolution", *Proceedings of the IEEE* 68(9):1060–1076, Table I, p. 1068; verified directly). Lehman also frames "evolution is an intrinsic, feedback driven, property of software" (§IV.A, p. 1067) and characterizes E-programs as those where "the program has become a part of the world it models, it is embedded in it" (p. 1063). The continual-adaptation necessity and the feedback-loop framing are exact matches — but the driver of change in Lehman is the world, not the operator's intent.

**Architectural drift / erosion (Perry & Wolf 1992).** "Architectural drift is due to insensitivity about the architecture. This insensitivity leads more to inadaptability than to disasters and results in a lack of coherence and clarity of form" (Perry & Wolf, "Foundations for the Study of Software Architecture", *ACM SIGSOFT Software Engineering Notes* 17(4):40–52, p. 43; verified directly). The canonical academic name for divergence-by-insensitivity — but the intended architecture is assumed fixed; a moving alignment target is outside its frame.

**Practical drift (Snook 2000).** The slow, steady uncoupling of practice from written procedure, characterized in secondary literature as the process by which rules no longer match practice (Snook, *Friendly Fire*, Princeton University Press; book text not directly verified — cited as characterized in secondary literature). Near-verbatim match for the failure description, but names the failure process, not the counter-activity.

**Harness optimization (Meta-Harness, arXiv:2603.28052).** Defines the harness as "the code that determines what information to store, retrieve, and present to the model" and describes "an outer-loop system that searches over harness code for LLM applications" — "automated harness engineering" driven by benchmark scores (verified directly). The closest activity-side neighbor: it improves the harness, but it is autonomous and score-driven. No operator intent in the loop.

**Agent drift (arXiv:2601.04170).** Defines "the progressive degradation of agent behavior, decision quality, and inter-agent coherence over extended interaction sequences" and "semantic drift" as "progressive deviation from original intent" (Rath, "Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions"; verified directly). The reference list (12 entries) contains no classical software-engineering literature — no Lehman, no Perry & Wolf, no Parnas, no Snook (verified directly). The 2026 drift literature has re-arrived at the classical drift problem under new coinage, unconnected to the classical lineage.

Also rejected during the search: "alignment drift" (no canonical citation; informal usage only) and "configuration drift" (DevOps vendor vocabulary; the adjacent research exists under "code-documentation inconsistency detection," which is too narrow).

The common diagnosis: AKC has a defensible position at the intersection of the software-evolution and alignment literatures, the repeated circumlocution is exactly the kind of re-made judgment the Promote phase exists to eliminate, and the naming must carry reference relations rather than a free-floating coinage — or it repeats the failure ADR-0013 was written to prevent.

## Decision

AKC establishes two terms derived from the intersection of established vocabularies rather than coined fresh — the same "concede, then locate" structure ADR-0013 applied to the agent-memory literature, applied here to the software-evolution and alignment literatures.

### 1. Canonical definitions

**Harness alignment** — the continuous, human-gated activity of keeping an agent's harness (its configuration layer: skills, rules, prompts, documentation) aligned with the operator's evolving intent. It extends intent alignment (Christiano 2018) in two directions: from the agent's *behavior* to the *artifacts that shape behavior*, and across *time* — alignment is sustained through a cycle, not configured once (cf. Lehman's Law of Continuing Change). The alignment target is operator intent, not model values. This is not an AI-safety value-alignment claim.

**Harness drift** — harness alignment's failure mode: the gradual uncoupling of the harness from operator intent when the cycle does not run. Skills go stale, rules stop matching practice, documentation diverges from code. Named in lineage with architectural drift (Perry & Wolf 1992: divergence by insensitivity), practical drift (Snook 2000: practice uncoupling from written procedure), and agent drift (arXiv:2601.04170: behavioral-level degradation).

### 2. The three required properties and what no single source covers

Each component of both definitions traces to an established source. AKC's delta is confined to the gap that no source covers individually:

| Requirement | Best single-source match | What it misses |
|---|---|---|
| (a) Alignment target is operator intent, itself evolving | Christiano 2018 (intent alignment) | Treats intent as static |
| (a) continued: feedback loop changes operator's intent too | ADR-0012 Theme 3 | Not present in the alignment literature |
| (b) Human-gated loop | ADR-0005 (Human Approval Gate) | Meta-Harness (arXiv:2603.28052) runs autonomously |
| (c) Continuous alignment, not one-time configuration | Lehman 1980, Law I (Continuing Change) | Lehman's driver is the world, not operator intent |

### 3. Contrast: harness optimization vs. harness alignment

Harness optimization (Meta-Harness, arXiv:2603.28052) is the autonomous, score-driven improvement of the harness on the correctness axis. Harness alignment is the human-gated counterpart on the intent axis. The two are complementary, not competing: a harness can be optimized and drifted simultaneously — scoring better on a fixed benchmark while sliding away from what its operator now wants.

### 4. AKC's six phases in this vocabulary

The six phases are, in this vocabulary, an operationalization of harness alignment: Measure and Maintain detect harness drift; Curate and Promote correct it through the human gate; the cycle as a whole is the feedback system Lehman said evolution intrinsically is.

### 5. Vocabulary bridge as a finding

The 2026 agent-drift literature and the classical software-evolution literature are currently unconnected (verified for arXiv:2601.04170's 12-entry reference list: no Lehman, no Perry & Wolf). Harness drift, defined with explicit lineage to both, bridges that vocabulary gap by reference rather than by reinvention. The bridge is the contribution that survives implementation churn.

### 6. Roll-out (recorded for completeness; the definitions above are the decision)

README en/ja replace the existing circumlocutions with the named term and add the Christiano citation; the References section gains a second positioning table (software-evolution and alignment literature). `docs/glossary.md` gains both terms (keep-original). `llms.txt` and `llms-full.txt` gain the definitions. `graph.jsonld` gains two Concept nodes, this ADR node, and six external-reference nodes (Christiano 2018, Lehman 1980, Perry & Wolf 1992, Snook 2000, arXiv:2603.28052, arXiv:2601.04170).

## Alternatives Considered

### Adopt a single existing term

Considered adopting one of the candidate terms (intent alignment, continuing change, architectural drift, practical drift, harness optimization, agent drift) as the sole vocabulary rather than deriving a new term. Rejected after the four-domain search: every candidate covers at most a subset of the three required properties. Intent alignment lacks the temporal and artifact dimensions; Lehman's continuing change has the wrong driver (world, not intent); architectural drift assumes a fixed target; practical drift names the failure, not the activity; harness optimization is the activity but autonomous and correctness-axis; agent drift names the failure but lacks the classical lineage. Adopting any one would mislabel the concept and inherit the mismatch.

### Use "alignment drift" as the failure-mode name

Rejected: no canonical citation exists. The phrase circulates informally — topic-aggregation pages, blog usage — without a foundational source. Building a reference relation requires something to refer to.

### Use "configuration drift" as the failure-mode name

Rejected: DevOps vendor vocabulary without a canonical academic citation. The adjacent research exists under "code-documentation inconsistency detection," which is too narrow (documentation only) and misses the intent-evolution dimension.

### Keep the circumlocution and add citations without naming

Rejected: the two-sentence paraphrase is required every time AKC's relationship to harness engineering is explained, and an unnamed concept cannot be cited, indexed in a glossary, or encoded as a graph node. The repeated paraphrase is exactly the kind of re-made judgment the Promote phase exists to eliminate.

### Coin the terms without reference relations

Rejected as false novelty: the components are all named in prior literature. A free-floating coinage would repeat the failure ADR-0013 was written to prevent, and would also waste the verified finding that the 2026 drift literature lacks the classical lineage — the bridge between the two bodies is the value this ADR adds.

## Consequences

### Positive

- The two-sentence circumlocution collapses into a citable, definable, graph-encodable term; explanations of AKC's relationship to harness engineering shorten.
- The missing Christiano citation for "intent alignment" — vocabulary the README already uses without attribution — is repaired as part of the same change.
- AKC gains a second positioning axis (software-evolution and alignment literatures) symmetrical with ADR-0013's agent-memory axis, with all quotations verified against primary sources (Snook excepted, marked as secondary-verified).
- The terms bridge the verified vocabulary gap between 2026 agent-drift work and the classical SE lineage by reference relations — the kind of contribution that survives implementation churn.
- LLM-mediated discovery improves: queries shaped like "my agent's skills and rules degrade over time" gain a nameable answer path (harness drift → harness alignment → AKC).

### Negative

- "Alignment" collides with AI-safety vocabulary; readers may misread a value-alignment claim. Mitigated by the definition's explicit disclaimer (operator intent, not model values), but the risk of out-of-context quotation remains.
- Two more terms in a project whose first theme is attention scarcity. Mitigated: the terms replace existing circumlocutions rather than adding net new vocabulary, but the glossary still grows by two rows.
- External adoption is n=0 at establishment time. The terms may never be picked up; they then remain internal shorthand with citations — useful, but short of the bridging ambition.
- The cited 2026 papers (arXiv:2603.28052, arXiv:2601.04170) are recent and unreviewed; their vocabulary may shift or be superseded, dating the contrast. The classical anchors (Lehman 1980, Perry & Wolf 1992) carry the durable weight.

### Neutral

- No change to the six phases, three core themes, nine design principles, JSON schemas, or reference implementation. ADR-0017 is a vocabulary and positioning decision in the lineage of ADR-0009, ADR-0012, and ADR-0013.
- Snook 2000 is cited as characterized in secondary literature; the book text was not directly verified. If the verbatim is ever checked against the book, the citation should be upgraded or corrected.

## Relationship to other ADRs

- **[ADR-0005](./0005-human-approval-gate.md) (Human Approval Gate).** The gate is what makes harness alignment *human-gated* rather than autonomous — the load-bearing difference from harness optimization. ADR-0017 names the activity; ADR-0005 is its structural mechanism.
- **[ADR-0009](./0009-akc-is-a-cycle-not-a-harness.md) (AKC is a Cycle, Not a Harness).** Unchanged and reinforced: harness alignment is what the cycle does *to* harnesses, which presupposes the cycle/harness layer separation ADR-0009 drew. The new vocabulary makes ADR-0009's distinction expressible in one sentence.
- **[ADR-0012](./0012-front-load-three-core-themes.md) (Front-load the Three Core Themes).** The delta that justifies the new terms is the three themes restated at the harness layer. ADR-0017 does not alter the themes or their front-door ordering; the README verification conditions of ADR-0012 are preserved.
- **[ADR-0013](./0013-positioning-within-agent-memory-literature.md) (Positioning Within the Agent-Memory Literature).** ADR-0017 is the second positioning ADR, same "concede, then locate" structure, orthogonal axis: ADR-0013 answers "isn't this just a memory system?"; ADR-0017 answers "isn't this just harness engineering / maintenance?" and supplies the vocabulary the answer needs.
- **[ADR-0014](./0014-failure-modes-of-the-bidirectional-loop.md) (Failure Modes of the Bidirectional Loop).** Distinct failure layers: ADR-0014 names *human-side* failures (gate complacency, deskilling, delegation-feedback divergence); harness drift is the *artifact-side* failure. The two compound — a complacent gate accelerates harness drift — but they are not the same failure and are recorded separately.

---

**Notes.** ADR-0017 is a positioning ADR in the lineage of ADR-0009, ADR-0012, and ADR-0013: it introduces no new principle and no new mechanism. It records two vocabulary decisions — harness alignment and harness drift — so the project never has to re-argue its relationship to harness engineering from scratch, and so the verified gap between the 2026 agent-drift literature and the classical software-evolution literature is bridged by reference rather than lost. The Christiano (2018) citation is incidental to the definition but corrects a missing attribution that predates this ADR. Snook (2000) is marked as secondary-verified; all other citations (Christiano, Lehman, Perry & Wolf, arXiv:2603.28052, arXiv:2601.04170) were verified directly against their primary texts.

**Scaffolding synonymy (2026-06-06).** The non-weights layer these terms govern is named *scaffolding* in the AI-safety and accountability discourse; the sibling repository agent-attribution-practice chooses that term as primary and records the connotation split in its glossary (scaffolding emphasizes the inspectable-artifact axis; harness the operational-capability axis). This ADR keeps *harness* because the contrast it draws — against harness engineering and harness optimization — requires the shared noun. A *scaffolding alignment* rename was considered and rejected: in AKC, *scaffold* is already load-bearing in the opposite direction (scaffold dissolution — structure designed to fade), and "scaffolding alignment is sustained continuously" next to "scaffolding dissolves by design" would put contradictory predicates on one word. The synonymy is recorded on both sides — `docs/glossary.md` here, AAP's glossary there.
