# Glossary

Key terms used across the ADRs, the cycle documentation, and the
companion paper. Definitions here are navigation summaries; **the ADRs
are canonical** — when a definition and an ADR diverge, the ADR wins.
For the English ↔ Japanese rendering table, see
[translation-glossary.md](translation-glossary.md).

Several terms are shared with the sibling repository
[agent-attribution-practice](https://github.com/shimo4228/agent-attribution-practice)
(AAP), whose [glossary](https://github.com/shimo4228/agent-attribution-practice/blob/main/docs/glossary.md)
treats the accountability side of the same vocabulary. Cross-references
are marked inline; the two glossaries are written to be consistent.

## Agent Knowledge Cycle (AKC)

Six composable phases — Research, Extract, Curate, Promote, Measure,
Maintain — by which an agent's experience becomes durable,
behavior-shaping knowledge, with human approval required on every change
to the agent's future behavior. A cycle, not a harness: it is what you
do *to* a harness over time, portable across harnesses (ADR-0009).
Genre-neutral: the same six phases run on behavioral patterns, domain
expertise, or constitutional values (ADR-0011). The one-page installable
form is [akc-cycle.md](akc-cycle.md).

## Signal-first

The Research-phase intake discipline: search broadly, admit only what
would change the next action. Information that does not change an action
does not deserve to be held — intake is where human attention is spent.
See ADR-0010.

## Attention ceiling

The limit the operator's attention and judgment place on a human-agent
loop — a budget that does not grow with the model, and that grows
*relatively* scarcer as agent capability does. AKC's organizing design
axis: every phase is shaped to spend the budget only where judgment is
irreplaceable. The repository hedges the constraint as "a contemporary
claim about 2026-era human-agent work, not an eternal law" (ADR-0010).

## Line of approval

The boundary separating what an agent may write freely from what
requires human approval. It runs not between skills and rules but
between **records** (transcripts, distilled notes — disposable,
regenerable, free to write) and **the artifacts that shape future
behavior** (skills, rules, identity prose — approval required). See
ADR-0005's decision table. The position paper presents this boundary as
the cycle's load-bearing structural commitment — the place where the
human-gated property becomes architecture: what can be verified without
the operator runs unattended; every behavior-shaping change passes the
gate ([position paper](https://doi.org/10.5281/zenodo.20578272), §5).

## Rules (layer)

The layer of persistent instructions a coding agent loads
unconditionally at the start of every session — a rules directory in
Claude Code or Cursor, whatever the implementation calls it. Skills and
memory load probabilistically; rules load every session, which makes a
misjudged rule the extreme of binding strength: it shapes every session
that follows (ADR-0003). AKC's Promote writes to this layer.

## The gate (human approval gate)

The structure that enforces the line of approval: before any change to
future behavior, the harness stops and does not proceed until a named
human passes it. **Approval is the act; the gate is the structure that
enforces it.** The approval is *continuing* (every change, for the life
of the install), *human* (a named operator, not an automated validator),
and *structural* (no path routes around it) — no "auto-approve after N
days" escape hatch, no self-approval path. The commit history of gated
artifacts becomes an audit trail of every intentional behavioral change.
See ADR-0005. AAP's glossary carries the sibling entry *approval gate*
for its genre; both descend from the same Contemplative Agent decision.

## Promote

The cycle phase that elevates a recurring pattern to the rules layer,
through the gate — the highest-stakes instance of the line of approval,
not its only one. See ADR-0005.

## Harness

The configuration layer an agent runs on: skills, rules, prompts,
scripts, documentation. AKC is not a competitor to harnesses but an
activity performed on them over time (ADR-0009). The term follows the
harness-engineering discourse (Hashimoto 2026; the externalization
survey, Zhou et al. 2026, maps the field).

**The same non-weights layer is called *scaffolding* in the AI-safety
and accountability discourse** (Davidson et al. 2023). AAP's glossary
treats the two terms' connotations at length — *scaffolding* emphasizes
the inspectable-artifact axis and carries a dissolution trajectory;
*harness* emphasizes the operational-capability axis and implies
durability — and chooses scaffolding as its primary term because
inspectability is load-bearing for accountability distribution. AKC
chooses **harness** as its primary term because its positioning runs
against harness engineering and harness optimization (ADR-0017), and the
shared noun is what makes that contrast statable in one sentence.

For retrieval: readers arriving under either term are in the right
place. The layer is the same whichever name is used.

## Scaffolding

AAP's primary term for the non-weights layer this repository calls the
harness — see [Harness](#harness) and AAP's glossary for the full
treatment of the connotation split. In AKC's own documents, *scaffold*
usually appears in a second, narrower sense: the cycle's install skills
as transient support (see [Scaffold dissolution](#scaffold-dissolution)).
The senses share the Vygotskian root — structure meant to fade — but
apply at different levels: scaffolding-as-layer names where agent
behavior lives; scaffold-as-install names AKC's own packaging.

## Scaffold dissolution

AKC's skills are scaffolding in the Vygotskian sense: as operator and
agent internalize the cycle through practice, the explicit skill files
become unnecessary and the rules alone sustain the loop. Dissolution is
the **intended end state, not a fallback**; what is built to persist is
the judgment lineage in the decision records. See
[scaffold-dissolution.md](scaffold-dissolution.md) and ADR-0003 (the
distilled layers are disposable by construction).

AAP's glossary distinguishes **two senses of dissolution that must not
be conflated**: *healthy dissolution into human cognitive patterns*
(this one — which AAP attributes to AKC) and *unhealthy internalization
into model weights* (rules absorbed by training: the rule still "runs,"
but probabilistically — it cannot be read, diffed, or reverted without
retraining). AAP also carries a provisional five-criterion checklist for
telling the two apart (external inspectability, locus of agency, failure
visibility, causal recoverability, reversibility). AKC's dissolution is
the healthy sense, and the gate plus the decision records are what keep
it inspectable while it proceeds.

## Harness alignment

The continuous, human-gated activity of keeping an agent's harness
(skills, rules, prompts, documentation) aligned with the operator's
evolving intent.
Three properties hold simultaneously, and no single prior term covers
all three: **(a)** the target is operator intent, *itself evolving* —
labeled *bidirectional*, because the loop's own running is what moves
the target; **(b)** the loop is *human-gated*; **(c)** the alignment is
*continuous* — sustained through a recurring cycle, not configured once.
The position paper derives all three from a single root: intent has no
verifier outside the operator, and verifying intent sharpens the
judgment doing the verifying, so the loop moves its own target
([position paper](https://doi.org/10.5281/zenodo.20578272), §3).
Extends intent alignment (Christiano 2018) from behavior to the
artifacts that shape behavior, and across time (Lehman 1980's law of
continuing change). Contrast: autonomous, score-driven *harness
optimization* (Meta-Harness). See ADR-0017.

## Harness drift

Harness alignment's failure mode: the gradual uncoupling of the harness
from operator intent when the cycle does not run. Named in lineage with
architectural drift (Perry & Wolf 1992), practical drift (Snook 2000,
secondary-verified), and agent drift (Rath 2026). See ADR-0017.

The artifact-side layer of harness alignment's failure; its human-side
twin is the [failure twin](#failure-twin-experimental) (ADR-0014). The
two compound — a complacent gate accelerates harness drift — but are
distinct failures, recorded separately. The position paper's pre-deposit
audit extended the lineage check to three further 2026 drift coinages
(constraint drift, memory drift, belief deviation) and found the same
absence of the classical software-evolution lineage; it also found the
term "harness drift" used once elsewhere in a different sense — a
benchmark-comparability defect (Moghadasi & Ghaderi 2026), not a
configuration layer's uncoupling from operator intent
([position paper](https://doi.org/10.5281/zenodo.20578272), §6 and
notes).

## Intent alignment

Christiano's (2018) sense: an agent that "is trying to do what H wants
it to do." Correctness can be automated — tests, types, linters check
stated criteria; intent alignment cannot be automated to the same
degree, because intent moves as the operator's judgment sharpens through
use. An agent can pass every correctness check and still drift from what
its operator now wants. The position paper carries the structural
argument for why the asymmetry is not a tooling artifact: any automated
intent-check must freeze intent into a stated criterion; a frozen
criterion is a specification, and checking against a specification is
correctness work — so the automatable part of intent alignment reduces,
piece by piece, to correctness work, and the moving criterion is the
residue that harness alignment works on
([position paper](https://doi.org/10.5281/zenodo.20578272), §3). See
ADR-0017 for AKC's two-direction extension.

## Bidirectional growth loop

The loop's stated target: agent behavior and operator judgment
co-develop. Through repeated Curate, Promote, Research, and Measure
decisions, the operator's judgment is named as an output the loop is
shaped to produce — not an acknowledged side effect. "The cycle grows
*with* the people who shape it, not *for* them." See ADR-0009 and
ADR-0012; kept falsifiable by the failure twin (ADR-0014).

## Failure twin (experimental)

The named failure modes that keep the bidirectional claim falsifiable —
recorded as structural inferences, not measured phenomena (ADR-0014,
experimental):

- **Gate complacency** — a stream of reliable proposals trains the
  operator to approve by default; the click remains, the judgment behind
  it thins to a reflex. The agent-knowledge instance of automation
  complacency (Parasuraman & Manzey 2010).
- **Deskilling** — the supervisory faculty is maintained by exercise; an
  operator who only reviews agent output loses the ability to tell a
  good proposal from a plausible one (Bainbridge 1983's irony of
  automation).
- **Delegation-feedback divergence** — delegation continues while the
  judgment-behavior coupling breaks; the loop still produces output, but
  output no human is meaningfully steering.

The defenses are structural, not exhortative: the gate is a
circuit-breaker, Curate and Promote are active judgment acts, and the
gate forces articulation rather than a one-bit click. AKC does not claim
immunity — "a human determined to stop attending will diverge from the
loop regardless of structure" (ADR-0014).

These three modes are the human-side layer of harness alignment's
two-layer failure; the artifact-side layer is
[harness drift](#harness-drift). The two compound but are recorded
separately ([position paper](https://doi.org/10.5281/zenodo.20578272),
§6).

## Self-reingestion (experimental)

The cycle feeds on its own output: distillation reads both records of
what happened and the agent's own earlier writing. Two degradations
follow when the self-written share grows unchecked — **echo** (a framing
the agent invented becomes a rule and teaches itself as observed fact)
and **grounding loss** (summaries of summaries drift abstraction hops
away from events). The decisions: only the observed record is ground;
the self-generated share of approved artifacts stays visible (Measure);
the gate is the circuit-breaker before the always-loaded layer.
Generalized from one production observation (the Contemplative Agent
substrate) — experimental; "an expectation, not yet a measured
dose-response." See ADR-0015 and ADR-0002.

AAP's glossary records the same underlying judgment from the security
side as *untrusted content*: self-authored distillation inherits the
taint of the external input it summarized — there a trust boundary, here
a knowledge-quality boundary.

## Text-observability (Measure)

ADR-0016's requirement on Measure instruments: an instrument that
ignores agent text (stated reasoning, verdicts, plans) systematically
under-reports compliance for judgment-phase work, which lives in text
rather than tool calls. Instruments must treat agent text as first-class
evidence.

## Mechanism vs content

AKC carries the **mechanism** only — the cycle, phases, layers, decision
records, and patterns. Concrete use cases, domain knowledge, and
populated threat models are **content**, owned by downstream projects
and confined to `examples/`. The boundary case: an empty-default
parameterized check (a structural guard / validation seam) is mechanism;
the populated list that fills it is content. See ADR-0011 and the
inclusion rule in `CLAUDE.md`.

## Judgment lineage

What AKC is built to persist: the chain of recorded decisions (the ADRs)
explaining why the mechanism is shaped as it is. Model evolution is
expected to dissolve implementations; the lineage of judgments is the
durable artifact. **Implementation dissolves; judgment persists.** See
ADR-0009 and [scaffold-dissolution.md](scaffold-dissolution.md).
