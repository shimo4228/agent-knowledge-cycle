# Architecture Decision Records

AKC records design decisions as ADRs. Each ADR is short, dated, and
self-contained: it states the context, the decision, the alternatives
considered, and the consequences. ADRs are dated hypotheses, not
permanent constraints: from ADR-0024 onward each carries a
`## Review-when` section naming its expiry conditions (ADR-0026);
earlier ADRs are read by their Context premises and Date — lint
reports of a missing Review-when on 0002–0023 are expected, not debt.

## Index

| # | Title |
|---|-------|
| [0002](0002-immutable-episode-log.md) | Immutable Episode Log as Source of Truth |
| [0003](0003-three-layer-distillation.md) | Three-Layer Distillation (Raw → Knowledge → Identity/Rules) |
| [0004](0004-two-stage-distill-pipeline.md) | Two-Stage Distill Pipeline (Free-form → Format) |
| [0005](0005-human-approval-gate.md) | Human Approval Gate for Behavior-Modifying Changes |
| [0008](0008-code-and-llm-collaboration.md) | Code and LLM Collaboration |
| [0009](0009-akc-is-a-cycle-not-a-harness.md) | AKC is a Cycle, Not a Harness |
| [0010](0010-human-cognitive-resource-as-central-constraint.md) | Human Cognitive Resource as Central Constraint |
| [0011](0011-cycle-applies-to-any-knowledge-body.md) | Cycle Applies to Any Knowledge Body |
| [0012](0012-front-load-three-core-themes.md) | Front-load the Three Core Themes in Front-door Documentation |
| [0013](0013-positioning-within-agent-memory-literature.md) | Positioning Within the Agent-Memory Literature |
| [0014](0014-failure-modes-of-the-bidirectional-loop.md) | Failure Modes of the Bidirectional Loop *(experimental)* |
| [0015](0015-loop-failure-modes-self-reingestion.md) | Self-Reingestion — When the Cycle Feeds on Its Own Output *(experimental)* |
| [0016](0016-measuring-thinking-centric-phases.md) | Measuring Thinking-Centric Phases |
| [0017](0017-harness-alignment-and-drift.md) | Harness Alignment and Harness Drift |
| [0018](0018-record-downstream-applications-as-first-class-context.md) | Record Downstream Applications as First-Class Context |
| [0019](0019-cycle-structure-is-provisional.md) | The Cycle's Structure Is Provisional — Skills, Bindings, and Phases Held Lightly |
| [0020](0020-readme-minimal-floor.md) | Minimal-floor README with Single-location Theme Presentation |
| [0021](0021-replace-growth-tagline.md) | Replace the Growth Tagline |
| [0022](0022-transfer-as-completion-test-for-dissolution.md) | Transfer as the Completion Test for Dissolution *(experimental)* |
| [0023](0023-generation-review-as-a-fourth-evidence-class.md) | Generation Review as a Fourth Retirement Evidence Class |
| [0024](0024-judge-build-human-three-role-loop.md) | The Judge/Build/Human Three-Role Loop as the Operational Form of Attention Scarcity |
| [0025](0025-llm-first-artifact-readability.md) | LLM-First Artifact Readability |
| [0026](0026-expiry-conditioned-knowledge.md) | Expiry-Conditioned Knowledge |

ADR numbers are permanent identifiers. Gaps (0001, 0006, 0007) reflect
ADRs that were extracted from this repository in v2.0.0 as
genre-specific content; see the ADR-0009 addendum for the reasoning.

Several remaining ADRs are adapted from the [contemplative-agent](https://github.com/shimo4228/contemplative-agent)
research repository, which served as prior art. Credit is given at the
bottom of each ADR where applicable.
