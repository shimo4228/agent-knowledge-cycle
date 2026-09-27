# Plan: human-gate 第 2 軸の AKC 位置づけ + 3 skill の standalone repo 化 + glossary 引用復元

## Context

harness 側で確定した human-gate 第 2 軸の成果（rule + hook + ADR-0019 追記 + 記事）の AKC 側位置づけを
検討する中で、セッション内議論により判定が 2 段階で発展した:

1. 当初の「instance は pointer page を持たない」は過剰圧縮 — phase skill 6+ 個はすべて
   ~/.claude 内部ファイルから standalone repo 化されて linkable になった。抽出が既定パターン
2. graph の実構造では全 phase node が scaffold を名指しし（"Currently scaffolded by …"）、
   skill repo node が `implements` 辺を持つのに、**human-approval-gate node にだけ binding が無い**。
   さらに **agent-stocktake / generation-audit も standalone repo 未化・graph 不在**のまま
   load-bearing に使われている（前者は Curate の第 3 semantic sibling を自認、後者は
   Scaffold Dissolution の世代交代トリガーの operationalization で ADR-0023 と直結）

T7（旧称 T-009）の恒久却下は「concept page + paired ADR」に対するもので**有効のまま**。
binding 層は AKC ADR-0019（cycle-structure-is-provisional）が定義する可変 snapshot 層で
paired ADR を要しない — T7 のフレーム外の別チャネル。

## 確定済み判定（一次資料検証済み）

- **証拠生成物カテゴリ → 足す**: `line of approval` の基準（glossary:51-52 "artifacts that shape
  future behavior"）を満たすのに列挙に無い。前回 control plane 還元 `14c995b` と同一構造 →
  同じ glossary sharpening + graph node 更新。ADR は立てない（`14c995b` の 3 条件を同様に満たす）
- **昇格規則（第 1 軸が第 2 軸を上書き）→ 対象外**: 提示物分岐の上に乗る operator content。
  AKC の gate は常に本文 sign-off で、昇格の起点となる要約経路が存在しない
- **glossary 引用 → 原文復元**: `every behavior-shaping change passes the gate` は paper 原文
  （.notes/papers/harness-alignment.md:107）の言い換えで、"and intent enters the loop with it"
  （human-gated property の核心節）が脱落。glossary:60-62 と **llms-full.txt:100 の両方**を原文
  `What can be verified without the operator runs unattended; every change that shapes behavior
  passes the gate, and intent enters the loop with it.` に復元。graph に言い換えは無い（確認済み）
- **Zenn / Dev.to 記事への参照 → しない**: repo でも研究成果物でもない配布・解説層
- **3 skill の standalone repo 化 + binding → する**（ユーザー指示で確定）:
  - `human-gate` → `implements: vocab#akc/concept/human-approval-gate`（concept への辺・第 1 例）
  - `agent-stocktake` → `implements: vocab#akc-phase/curate`（第 4 の Curate scaffold）
  - `generation-audit` → `implements: vocab#concept/scaffold-dissolution`（concept への辺・第 2 例。
    `groundedIn` に ADR-0023 — generation review evidence class の計測器そのもの）

## 実装手順

### Phase I — AKC 側・repo 公開を待たない分（先行）

1. **wiki 参照**（CLAUDE.local.md 規約）: glossary / graph 更新前に wiki `AKC.md` を read-only 確認
2. **Commit A（引用復元・独立瑕疵)**: `docs/glossary.md` + `llms-full.txt:100` を paper 原文に復元
3. **Commit B（証拠生成物 sharpening)**: glossary `Line of approval` の control plane 文の後に追加 +
   graph `human-approval-gate` node description に同旨を追加。文体は `14c995b` に揃える。英文ドラフト:
   `The same reach covers the artifacts that produce the gate's verification evidence — tests,
   lint and CI configuration, review prompts, dependency manifests — since a change there moves
   what counts as verified: an evidence-loosening edit lets "runs unattended" expand without any
   behavior-shaping artifact appearing to change.`
4. **台帳更新**: `.notes/TASKS.md` — T7 に再訪記録（恒久却下は concept page + paired ADR に限定して
   有効、binding 層はフレーム外だった旨）+ 新タスク行「3 repo 公開後の binding 追加」
   （着手条件: 各 repo 公開）

### Phase II — repo 抽出・公開（このセッション枠で実施可。GitHub 公開 = 外部書き込みごとに承認）

既存 9 repo と同じ発行パターン（harness-sync の単独 skill repo 群。汎用化 curation は手動）。
ソースは ~/.claude 配下を**読むだけ**（Change Target 規律 — ~/.claude 側は変更しない）:

5. **`shimo4228/agent-stocktake`**: SKILL.md（本文は既に英語・汎用的）+ README。curation 軽
6. **`shimo4228/generation-audit`**: SKILL.md 本文が日本語 → 公開版は英語化
   （`ja-to-en-translation` skill）。README で dissolution の世代交代トリガー（AKC ADR-0023 /
   docs/scaffold-dissolution.md 第 4 機構）との対応を明記
7. **`shimo4228/human-gate`**: human-gate.md の公開向け curation 版（operator 固有参照の汎用化・
   英語化）+ `evidence-file-notice.sh`（hook 同梱で単独位置づけ問題は消滅）+ README

### Phase III — AKC 側 binding（repo 公開後。先例 `d050162` の面チェックリストに従う）

8. **graph.jsonld**:
   - EcosystemRepo node × 3（`implements` は上記judgment表どおり、`extends: concept DOI`。
     generation-audit は `groundedIn: ADR-0023`）
   - `human-approval-gate` node と `concept/scaffold-dissolution` node の description に
     "Currently scaffolded by … (a snapshot, mutable; ADR-0019)" 定型文を追加
   - Curate phase node: "three scaffolds" → 4 scaffold（structural 1 + semantic siblings 3:
     skills / rules / agents）に改稿
9. **glossary**: 「The gate」項に scaffold 1 文（human-gate repo）
10. **llms.txt / llms-full.txt**: cycle-skill list に agent-stocktake 追加（canonical count 9→10）。
    human-gate / generation-audit は phase skill でないので同 list に入れず、それぞれ gate /
    dissolution を述べる箇所に配置。README en/ja の Curate 行に agent-stocktake 追加
11. **CODEMAPS**: freshness bump + ADR-0019 layering 記述の更新
12. **HF mirror sync**: graph 変更をまとめて `hf-sync`（`Shimo4228/agent-knowledge-cycle`）。実行前承認

### Phase IV — harness 側への申し送り（別セッション。テキストを最終報告に含める）

- ADR-0019 の 2026-07-26 追記の引用を原文化（+ "and intent enters the loop with it"）
- 2026-07-28 追記「副産物」段落の **未対応** → 解消済み（AKC commit hash 記録）
- 「instance は pointer page を持たない」の文言修正 — 却下対象は concept page + paired ADR のみ。
  binding 層は別チャネルで、phase skill も抽出前は instance 内部ファイルだった事実を併記
- akc-cycle repo（plugin）が新 3 repo を bundle するかは akc-cycle 側の判断として follow-up
  （bundle するまで docs/akc-cycle.md:18 の "nine cycle-phase skills" は v1.1.0 plugin の事実として維持）

## 留意（数値クレーム規律）

count の正本は llms-full.txt。cycle-skill count は 9→10（agent-stocktake のみ算入）。
他所の "nine" は `d050162` の先例どおり de-number するか正本へのポインタ化。
generation-audit / human-gate は phase-bound でないため cycle-skill count に入れない。

## Human gate（この作業自体の提示）

glossary / graph / llms*.txt / README / 新 repo の SKILL.md・README はすべて behavior-shaping /
公開ドキュメント → **各 commit・各 repo 公開前に本文（diff）を提示**。GitHub repo 作成と
HF upload は外部書き込みとして個別承認。

## Verification

- Phase I 後: `grep -rn "behavior-shaping change passes"` が 0 件 / graph が valid JSON /
  `scripts/` の lint（citation_audit 等）PASS
- Phase III 後: 3 node の implements 辺が既存 skill node と同型 / llms.txt の list と
  graph の EcosystemRepo 集合が一致 / count クレームが llms-full.txt と整合 /
  HF dataset 側の graph 反映確認
- 各公開 repo: リンク到達性（AKC → repo、repo → AKC concept DOI の双方向）
