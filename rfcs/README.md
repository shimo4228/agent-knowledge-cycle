# RFCs

この repo の提案と作業項目の公開台帳（1 エントリ 1 ファイル、`NNNN-slug.md`、ID は
`RFC-NNNN`）。フル RFC の提案から小さな作業項目まで**同居する** — 別置き場を作らない。
様式・状態語彙・規約の正本は skill
[`task-stocktake`](https://github.com/shimo4228/claude-harness/blob/main/skills/task-stocktake/SKILL.md)、
判断は
[claude-harness ADR-0049](https://github.com/shimo4228/claude-harness/blob/main/docs/adr/0049-unify-task-ledger-into-public-rfcs.md)。

状態は各ファイルの frontmatter `state:` が**唯一の正本**（`candidate` / `ready` /
`in_progress` / `blocked` / `done` / `decided` / `dropped` / `retired`。この index には
複製しない — 二重記録は drift する）。終端エントリも削除・退避せずここに残る —
却下理由ごと残るのが公開判断記録の価値。状態別の列挙は
`python3 ~/.claude/scripts/claims.py ready [--state <state>]`。

この repo は小さいので、**提案性・未決の起票だけをここへ置く**。完了記録と運用行は
非公開の単一表（`.notes/TASKS.md`、gitignored）に残る — 形は 2 つのままでよい
（ADR-0049 の「単一表だけの小 repo は移行必須ではない」）。

| # | Title |
|---|---|
| [0001](0001-conflict-cost-local-metric.md) | conflict cost のローカル metric を設計する |
