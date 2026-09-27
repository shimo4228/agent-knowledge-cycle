# graph.jsonld — implements 辺 backfill (ADR-0027 open obligation)

## Context

ADR-0027 (mental model / instance) の Decision 2 が grounding expectation を導入し、Consequences の Negative 3 項が「既存 Concept ノードの implements 辺 backfill は named open obligation」と明記している。v2.7.0 で新設 3 Concept は claude-harness からの implements 辺を持つが、既存 Concept の大半は groundedIn（ADR 方向）のみ。本作業は EcosystemRepo / 標準 skill repo ノードから既存 Concept への implements 辺を、README/description から明確に言える組だけ保守的に追加する。

前提照合済み: ADR-0027 は想定どおり。全候補の source ノード・target Concept ノードは graph.jsonld に実在する。

## 変更（graph.jsonld のみ、1 ファイル）

`implements` は `@context` で `@type: @id` 定義済み。配列も既に使用例あり（claude-harness ノード）。

| Source node | 現在の implements | 追加する implements 先 | 根拠（node description より） |
|---|---|---|---|
| `search-first` (L545) | `akc-phase/research` | + `akc/concept/signal-first` → 配列化 | Research phase 定義が「Signal-first intake … scaffolded by the search-first skill」 |
| `signal-first-research` (L1254) | なし | `akc/concept/signal-first` | 「Operationalizes the signal-first principle」、ADR-0010 と 1:1 |
| `when-code-when-llm` (L1240) | なし | `akc/concept/code-llm-layering` | 「operationalize the code-vs-LLM choice」、ADR-0008 と 1:1 |
| `code-and-llm-collaboration` (L1247) | なし | `akc/concept/code-llm-layering` + pattern 4 ノード（`akc/pattern/guard` / `filter` / `judge` / `orchestrator`）の配列 | 「Realizes the four code-LLM layering patterns (guard, filter, judge, orchestrator)」— 4 パターンを明示的に名指し |
| `akc-mcp` (L780) | なし | `akc/concept/two-stage-distill` | 「memory distillation … re-implements its cognitive layer」— CA の distill 層（ADR-0004 の原典）の再実装 |

追加しない（保守的判断）:
- ResearchLine 型（contemplative-agent 等）— 指示どおり触らない
- `akc-cycle` → six-phase-loop 等、description から一段推論が要る組 — ADR-0027 は「無ければ無いと書く」を許すため無理に埋めない
- 既存 field は一切変更しない（追記のみ。search-first のみ既存値を配列先頭に保持して配列化）

## Verify

```bash
python3 - <<'EOF'
import json
g = json.load(open('graph.jsonld'))['@graph']
ids = {n['@id'] for n in g}
edges = ['implements','groundedIn','extends','appliesTo','hasFailureMode','derivesFrom','siblingOf','definesConcept','contrastsWith','about']
dangling = [(n['@id'],k,v) for n in g for k in edges if k in n
            for v in (n[k] if isinstance(n[k],list) else [n[k]])
            if v.startswith('https://shimo4228.github.io') and v not in ids]
print('dangling:', dangling)
assert not dangling
EOF
```

- JSON valid（json.load が通る）
- 全辺の参照先ノード実在（dangling 0）— 内部 vocab URI のみ対象（外部 URL は除外）
- `git diff` で追記のみ（削除行が implements 単一値→配列化の 1 箇所以外に無いこと）を目視

## Commit

commit のみ、push しない。message に premise（ADR-0027 Negative 3 の backfill obligation）と verify 証拠（JSON valid + dangling 0）を記載。CHANGELOG・他ファイルは触らない。
