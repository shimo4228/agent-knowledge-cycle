# AKC Rules (moved to a standalone repository)

The cycle-as-a-single-rules-file lives in its own repository:
**[shimo4228/akc-cycle](https://github.com/shimo4228/akc-cycle)**.

It distills the six AKC phases (Research, Extract, Curate, Promote, Measure,
Maintain) plus Scaffold Dissolution into one behavioral rules file you can drop
into an agent's rules directory — the lightweight install path for the whole
cycle, without installing the six standalone [cycle skills](../README.md#the-cycle).

The rules file exists as **two deliberate editions** (since 2026-09-01), and which
one you want depends on whether the cycle skills are installed:

- **Self-contained edition** — [akc-cycle
  `rules/common/akc-cycle.md`](https://github.com/shimo4228/akc-cycle/blob/main/rules/common/akc-cycle.md):
  the full floor (six-phase trigger table, dissolution evidence standard, worldview
  digests). Install this when no skills are present.
- **Pointer edition** — [claude-harness
  `rules/common/akc-cycle.md`](https://github.com/shimo4228/claude-harness/blob/main/rules/common/akc-cycle.md):
  the running instance in the author's harness, where each mechanism is delegated
  to an installed skill or resident rule and the file keeps only the judgment
  content no skill owns. Use it as the reference shape once the skill layer is
  installed — a worked example of Scaffold Dissolution in progress.

## Installing

```bash
# clone, then copy the rule into your global rules directory
cp rules/common/akc-cycle.md ~/.claude/rules/common/akc-cycle.md
```

Since v1.1.0 the same repository also ships the nine cycle-phase skills as a
Claude Code plugin (`/plugin marketplace add shimo4228/akc-cycle`) — the rules
file stays the minimal floor, the plugin adds the skill layer. The repository's
README covers the per-phase trigger table, both install paths, and the one-way
sync model.

## Why it moved

This file previously held the full rules text, but the same content also lives
as a live rule in the author's harness — and the two copies drifted. Publishing
the rule as its own repository gives it a single home, the same distribution
model as the cycle skills and the [design-pattern skills](skills/README.md).
Since 2026-09-01 the akc-cycle repo owns the self-contained edition outright
(no longer mirrored from the harness), while the harness runs the pointer
edition — the drift risk was resolved by making the two editions deliberately
different rather than nominally identical. The decision records that motivate
the cycle (the "why") stay here in [`docs/adr/`](adr/).
