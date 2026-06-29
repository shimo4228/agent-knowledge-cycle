# AKC Rules (moved to a standalone repository)

The cycle-as-a-single-rules-file lives in its own repository:
**[shimo4228/akc-cycle](https://github.com/shimo4228/akc-cycle)**.

It distills the six AKC phases (Research, Extract, Curate, Promote, Measure,
Maintain) plus Scaffold Dissolution into one behavioral rules file you can drop
into an agent's rules directory — the lightweight install path for the whole
cycle, without installing the six standalone [cycle skills](../README.md#the-cycle).

## Installing

```bash
# clone, then copy the rule into your global rules directory
cp rules/common/akc-cycle.md ~/.claude/rules/common/akc-cycle.md
```

The repository's README covers the per-phase trigger table and the one-way
sync model.

## Why it moved

This file previously held the full rules text, but the same content also lives
as a live rule in the author's harness — and the two copies drifted. Publishing
the rule as its own repository gives it a single source of truth (the harness
copy, mirrored one-way), the same distribution model as the cycle skills and the
[design-pattern skills](skills/README.md). The decision records that motivate the
cycle (the "why") stay here in [`docs/adr/`](adr/).
