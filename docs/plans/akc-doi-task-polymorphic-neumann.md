# AKC v2.7.0 — ecosystem 刷新 + 3 worldview/運用形の昇格 + DOI リリース

## Context

AKC は v2.6.0（2026-07-28）以降、ハーネス側の進化（harness ADR-0043〜0059: 公開 rfcs/ 台帳統一、状態語彙標準化、task-triage 三役ループ、judge-tier dispatch 既定）を反映していない。graph.jsonld の claude-harness ノードは「6 cycle skills の同梱配布」という古い記述のまま、llms-full.txt の daily-research URL は旧名 (`claude-skill-daily-research`)、CODEMAPS の freshness header は 1 ヶ月stale、8 月の commit（rfcs/ 台帳、AI-native SDLC）は CHANGELOG 未収載。

grill-me 面接での決定（著者確認済み）:

1. **スコープ = 事実更新 + 選択的昇格 + README 全面刷新**（README は当初「骨格維持」だったが著者指示で上書き 2026-09-01）。刷新の軸: cycle の運用形が skill 単層でなく **skills / rules（worldview 層）/ 機械ゲート / 三役ループの多層**になった現実を反映する。ADR-0020（minimal floor / theme 単一箇所提示）の規律は維持した内容刷新 — readme-writer の judge loop が破れを要求した場合のみ supersede 候補として著者に提示
2. **昇格は 3 本**（著者確認済み）: (a) judge/build/human **三役ループ**（harness ADR-0043/0045/0057、~2 ヶ月の反復実践）を Theme 1（human cognitive resource scarcity）の運用形として昇格。rfcs 台帳・claims/lease 等の具体機構は claude-harness ノードの記述更新（関係の事実）に留める。旧 TASKS.md T5 の却下は日付つき仮説として ADR 内で注記 — 却下時点に三役ループは存在せず前提が変わった。(b) **llm-first-code worldview**（読者は次セッションの LLM / 検証可能性を保存 / 執行者は機械ゲート）— Theme 1 の可読性予算への適用形、ADR-0008 隣接。(c) **knowledge-staleness worldview**（LLM 界隈 1 週間陳腐化 / as-of 日付 / 失効条件付き推奨）— cycle の intake（Search）と保存された judgment（ADR = 日付つき仮説）に失効規律を与える mechanism
3. **新規 repo は herdr-toolkit のみ追加**（三役ループの build-dispatch 基盤としての関係 1 辺。配布・周辺層 = graph + llms-full のみ、README には出さない）。frontier 系 / contemplative_alignment は見送り（interest-driven citation 原則）
4. **バージョン = v2.7.0**（additive minor）。DOI は Zenodo 自動採番の new version

## 変更内容

### 0. 事前参照（CLAUDE.local.md 規約）

- research wiki（非公開）の AKC ページを read-only 参照（ADR 候補マーク・矛盾節・外部出典の確認）。wiki パスは公開成果物に引用しない

### 1. 新 ADR 3 本（docs/adr/0024〜0026）

- **ADR-0024** — 題目案: "The Judge/Build/Human Three-Role Loop as the Operational Form of Attention Scarcity"。judge 層が台帳の全 open task を判定・dispatch、build 層が実装、human は最後のスイッチ（merge）のみ — human approval gate（ADR-0005）を attention-scarcity 制約下でスケールさせる運用形。T5 却下との関係を "Relationship to other ADRs" で日付つき注記
- **ADR-0025** — 題目案: "LLM-First Artifact Readability"。artifact の読者・編集者は次セッションの LLM。可読性でなく検証可能性を保存（型・テスト・golden = 保存層、説明は derived）、基準の執行者は機械ゲート、人間可読性の予算は README と出力の文面のみ。Theme 1 の可読性予算への適用形、ADR-0008（code-LLM layering）の隣接。証拠: verify-bootstrap 4 軸選定・golden 凍結層・readme-writer 投資前提の反復実践
- **ADR-0026** — 題目案: "Expiry-Conditioned Knowledge"（knowledge-staleness）。LLM 分野の外部知識は ~1 週間スケールで陳腐化する。intake は検索時点照合（as-of 日付）、保存された推奨・判断は失効条件（valid-until / 無効化イベント）を持つ — 「ADR は日付つき仮説」の一般化。**帰結として AKC ADR format に optional `Review-when` section を導入**（harness ADR-0044 の輸入。新 3 本自身が持つ。既存 ADR は遡及しない）
- 共通: mechanism のみ記述、実装詳細（claims.py / lease / launchd / lint コマンド等）は書かず harness ADR を external evidence として引用。必須 section（Status / Date / Context / Decision / Alternatives Considered / Consequences / Relationship to other ADRs）+ Review-when。`/adr-writer` で起草 → agent: adr-reviewer でレビュー。ADR index と CLAUDE.md の ADR format 節（Review-when 追記）を更新

### 2. graph.jsonld（skill: jsonld-knowledge-graph の規約に従う）

- Concept ノード 3 本新設（三役ループ / LLM-first readability / expiry-conditioned knowledge）+ ADR-0024〜0026 ノード。辺: Theme 1 / human-approval-gate (ADR-0005) / ADR-0008 / claude-harness（implements 方向）
- claude-harness ノードの description 刷新: 「6 cycle skills 同梱」→ 現状（58 skills / worldview rule 層 / 公開 rfcs 台帳 / 三役 triage 運用を含む harness）の関係の事実
- herdr-toolkit を EcosystemRepo として追加（build-dispatch 基盤の関係 1 辺、DOI なし）
- citation_audit.py で検証（既知残差: Bainbridge 括弧入り DOI は意図的）

### 3. 既存ドキュメントの事実同期

- **llms-full.txt**: daily-research URL を `shimo4228/daily-research` に修正、herdr-toolkit 追加、ADR count 更新（正本）、新 Concept 3 本の Q&A エントリ追加
- **llms.txt**: ADR 参照系の更新 + phase 節の skill-centric な提示を多層運用形に整合（herdr-toolkit は配布層なので載せない）
- **README.md / README.ja.md**: **skill: readme-writer で全面刷新**（en 正本 → ja mirror、evidence script + readme-judge 草稿ゲート + panel（readme-reviewer / readme-clarity-reviewer）+ binding 最終判定 + 著者通読 GO、上限 2 ラウンド）。核となる内容転換: 「6 phase ↔ 6 skill の binding」中心の提示から、skills / rules（worldview 層）/ 機械ゲート / 三役ループの**多層運用形**へ。three themes の順序固定（ADR-0012）と Related Work 表の research-lines-only 規約は維持。新 Concept 3 本（三役 / LLM-first / expiry-conditioned）を theme との接続で言及
- **docs/CODEMAPS/architecture.md**: ecosystem 表に herdr-toolkit、daily-research URL 修正、rfcs/ 行の確認、freshness header 更新（2026-08-25 以降 2 回の編集で header 未更新の残差も解消）
- glossary（存在すれば）: 三役 / LLM-first readability / expiry condition の用語エントリ

### 4. リリース（skill: release-doi の 5 phase + post-release）

- CHANGELOG.md に v2.7.0 エントリ（8 月の未収載作業 — rfcs/ 台帳導入、AI-native SDLC doc、rfcs README 縮小 — も含める）
- CITATION.cff / .zenodo.json の version・日付更新
- tag `v2.7.0` push → Zenodo 自動採番 → 新 version DOI を反映 → Software Heritage archive + SWHID 記録
- **HF mirror sync**: skill: hf-sync で `Shimo4228/agent-knowledge-cycle` へ graph.jsonld/jsonl を upload（webhook は tag push で発火しないため必須手順）

## 修正対象ファイル

- `docs/adr/0024-*.md`, `0025-*.md`, `0026-*.md`（新規）
- `CLAUDE.md`（ADR format 節に optional Review-when を 1 行追記）
- `graph.jsonld`
- `llms-full.txt`, `llms.txt`
- `docs/CODEMAPS/architecture.md`
- `CHANGELOG.md`, `CITATION.cff`, `.zenodo.json`
- `README.md` / `README.ja.md`（count 整合のみ、骨格不変）

## Verification

1. `python3 scripts/citation_audit.py`（あるいは repo の verify entrypoint）が pass
2. graph.jsonld が JSON として valid（`python3 -c "import json; json.load(open('graph.jsonld'))"`）+ jsonld-knowledge-graph skill の整合チェック
3. daily-research / herdr-toolkit の URL 生存確認（`gh repo view`）
4. release-doi Phase 1（整合検査）が全項目 green になってから tag push
5. リリース後: Zenodo 新 DOI がバッジ/CITATION に反映、HF dataset の graph 更新を確認
6. README: readme-judge の binding 最終判定（Publishable）+ 著者通読 GO
7. Human gate: ADR 3 本・README・CHANGELOG は著者通読 sign-off 後に commit（AKC ADR-0005 / release-doi の gate）

## 実行順序

1. wiki 参照 → ADR 3 本（0024〜0026）+ CLAUDE.md format 追記
2. graph.jsonld（Concept / ADR ノード + claude-harness 刷新 + herdr-toolkit）
3. README 全面刷新（readme-writer loop — 新 Concept を参照するため ADR/graph の後）
4. llms.txt / llms-full.txt / CODEMAPS / glossary の同期
5. release-doi 5 phase（CHANGELOG / CITATION.cff / tag / Zenodo / SWH）+ hf-sync

## Non-goals

- rfcs 台帳・claims/lease の Concept 化（関係の事実のみ）
- frontier 系 repo・contemplative_alignment の追加
- mechanism-only rule 自体の見直し
