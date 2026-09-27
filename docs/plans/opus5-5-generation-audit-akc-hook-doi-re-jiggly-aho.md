# Plan: 新しくハーネスに入ったスキル・ルールを AKC のコンセプトに配置 → v2.8.0 DOI release

## Context

- Opus 5.5 の generation-audit は今朝（2026-09-25、harness ADR-0078）実施済み。これで AKC の最終 release
  （v2.7.0、2026-09-01）以降、ハーネスの中身が変わった
- 依頼: 09-01 以降にハーネスへ入ったスキル・Hook・ルールのうち、AKC のコンセプト（graph.jsonld の Concept /
  Phase / Pattern ノード）に当たるものを AKC に配置する。そのあと DOI release する
- 配置の規約は AKC ADR-0027: graph の `implements` 辺と front door のリンクで接地し、本文は複製しない。
  既存の慣例では、集約 repo（claude-harness）に入っているものは graph では claude-harness ノードの
  `implements` に足し、README では path 単位でリンクする。単独 repo を持つものは、その repo へリンクする
- 著者の決定（2026-09-25）: ADR-0024 は新しい ADR-0028 で一部を置き換える。公開 copy は集約 repo と
  generation-audit の単独 repo を同期する

## 配置表（09-01 以降に入ったもの — `git log --diff-filter=A` で全件）

| 入ったもの | 当たるコンセプト | 配置先 |
|---|---|---|
| `rules/common/boundary.md`（09-15） | human-approval-gate（ADR-0005）。「人間に渡す」の列挙が、Concept の定義（skills・rules に加え hooks・permissions・scheduled task・verify.sh まで届く）と一致する | graph: claude-harness の `implements` に追加 / README の「through-line」段落（:70–75）にリンク / llms-full の claude-harness 項 |
| `skills/author-calibrated-eval`（09-25） | intent-alignment（Theme 2）。読む価値の正解は著者の読みで、LLM 判定役は忠実さ（正しさ側）の足切りだけを受け持ち、形式はコードが見る — 「correctness と alignment は別物」をそのまま役割分担にしている | graph: claude-harness の `implements` に追加 / README の Theme 2 段落（:40–47）に running instance として 1 句 / llms-full |
| `skills/jev-judgment-design`（09-23） | code-LLM pattern: judge（ADR-0008）。「Jev が答え、コードが決める」— 閉じた判定を型付きの判定器へ移し、採否はコードが持つ | graph: claude-harness の `implements` に `akc/pattern/judge` を追加 / docs/skills/README.md の表に running instance として追記 / llms-full |
| `skills/jev-skill-router`（09-21、単独 repo `shimo4228/jev-skill-router` あり） | 同じく judge pattern。skill の名簿という有限の選択肢を Jev が確率で判定し、shadow か inject かはコードが決める | 同上。リンク先は単独 repo（`gh repo view` で公開を確かめる） |
| `skills/growth-astra` / `growth-fable`（09-08） | **配置しない** — GitHub follower という外部指標を追う目標ループで、知識を代謝する cycle のコンセプトに当たらない。front door に載せると utility / growth 側に立場を取ることになる | — |
| `output-styles/signal-first.md`（09-19） | **配置しない** — 公開されていない（harness-sync の SUBTREES に output-styles/ が無い）うえに、style が `default` のままで動いていない | — |
| `hooks/ask-one-question.sh` | **配置しない** — 09-25 に退役 | — |
| `agents/Explore.md`、`skills/archify`、`skills/typesafe-ai` | **配置しない** — built-in の override と外部 origin。typesafe-ai は退役済み | — |

既存の配置のうち、09-01 以降の変化で事実と合わなくなったもの（ここも直す）:
- generation-audit（scaffold-dissolution に配置済み）→ graph ノードの記述を v2 にする（runtime 照合 +
  vendor が保守する dated pattern エンジンを写さずに使う）
- Attention topology の行（README:68 / README.ja.md:66、llms-full:13,160）→ dispatch の既定は cloud session
  （harness ADR-0075）、local pane なら herdr-toolkit
- Maintain phase（graph:161）→ 「CLAUDE.md / CODEMAPS / ADR / README」から CODEMAPS を外す（harness ADR-0062）

## 実行順

### 1. 公開 copy の同期（skill `harness-sync`）— リンク先を先に揃える

- `~/.claude/docs/adr/README.md` には別 session の未 commit の変更がある。dry-run でこれが diff に入るか
  確かめ、入るなら報告してから進める
- 集約 repo `~/MyAI_Lab/claude-harness`: dry-run の要約 → sync → commit → push
- 単独 repo `~/MyAI_Lab/generation-audit` を v2 にする。script 同期か手動 curation かは、harness-sync の
  repo-mapping 表で確かめる。公開 README は skill `readme-writer` で v2 に書き直す（harness の path と、
  同梱の `/claude-api prompt-audit` への依存を明記する）。version はその repo の慣例に合わせる

### 2. 配置（上の表の 4 件と既存の 3 件の更新）

- graph.jsonld: claude-harness ノードの `implements` に 3 つを足す — human-approval-gate、intent-alignment、
  `akc/pattern/judge`。description には該当 path の関係の記述を足す。jev-skill-router は単独 repo なので、
  既存の単独 skill repo と同じ形の EcosystemRepo ノードを足し、`implements` judge と `isPartOf` claude-harness
  を付ける（形は skill `jsonld-knowledge-graph` の規約に合わせる）
- README.md と README.ja.md は同じ箇所を対で直す。docs/skills/README.md、llms.txt、llms-full.txt も直す
- 検証: JSON として parse できること、追加した辺が jq で見えること、README のリンク先が `gh api` で
  解決すること

### 3. ADR-0028（skill `adr-writer`、AKC の ADR 様式）— boundary.md の配置と整合させる

boundary.md を human-approval-gate の running instance として置くと、README の「authority stays with the
human」「human keeps the final merge switch」と食い違う（boundary.md では判断役が取り込む）。これを解く:
- 決定: 権限を artifact の種類で分けて置く
  - behavior-shaping artifact（skills・rules・control plane）は ADR-0005 のまま人間が持つ
  - admitted task の出力は、決定論ゲートと独立した判断役の検収で閉じる
  - 人間の権限は admission（起票・drop）と、revert 数による失効条件へ移る
  - ADR-0024 Decision 1 の「gate は merge の地点で人間」を、この範囲に限って置き換える
- 材料（operator-harness の記録であり、この repo からは再現できないと明記する）:
  - harness ADR-0069 の D3・D4・Review-when
  - ADR-0075 の注記
  - ADR-0076（build の提案は再現手順つき。起票は人間）
  - `~/.claude` と contemplative-agent の main で `git log --since=2026-09-15 --grep='^Revert'` の件数
- ADR-0024 に `> **Note (2026-09-25, ADR-0028)**` を付ける（AKC の既存の注記の形を grep して合わせる）
- `adr-reviewer` agent で 1 回見る
- 追従: README:68–75（en/ja）、graph.jsonld（ADR-0028 ノード、330 と 494 の記述）、llms.txt:97、
  llms-full（Q&A と ADR 数 24→25）、README / codemeta の「twenty-four」

### 4. v2.8.0 release（skill `release-doi`）

1. Pre-flight:
   - `gh api repos/shimo4228/agent-knowledge-cycle/hooks` で Zenodo webhook を確かめる
   - `v2.7.0..HEAD` が空でないことを確かめる
2. Phase 2（`/context-sync` から始める）で揃えるもの:
   - CHANGELOG の v2.8.0 項
   - CITATION.cff の version と date（DOI は据え置き）
   - `uvx cffconvert -f codemeta -o codemeta.json` で codemeta を再生成
   - README en/ja の BibTeX の version
   - llms.txt と llms-full.txt の Version
   - CLAUDE.md
   - docs/CODEMAPS/architecture.md の件数
3. Phase 3 verify:
   - `uvx cffconvert --validate`
   - graph.jsonld と codemeta.json の JSON parse
   - `2.7.0` が残っていないか grep
   - `git status`
4. **確認点（1 回だけ）**: diff stat と CHANGELOG 項を示し、OK を得る。そのあと main と tag `v2.8.0` を
   push → `gh release create v2.8.0`
5. Post-release:
   - Zenodo API から version DOI を取る
   - CITATION.cff、codemeta、README の BibTeX、llms-full の Citation を更新する
   - SWH の Save Code Now を実行し、SWHID を append する
   - commit → push
   - `/hf-sync Shimo4228/agent-knowledge-cycle`
   - Wayback snapshot

AKC の commit は 4 つに分ける: ① 配置 ② ADR-0028 ③ release-prep ④ DOI 反映。git は skill `git-workflow` の
作法に従う（`git -C`、commit message はファイル経由）。

## 範囲外（報告の末尾に 1 行ずつ）

- 09-01 より前から在って、09-01 の backfill でも配置されなかったもの（今回は入れない）:
  - harness-boundary → scaffold-dissolution
  - review-to-lint → pattern: guard / llm-first-readability
  - llm-as-judge → pattern: judge
  - adr-writer → expiry-conditioned-knowledge
- `skills/loop-design-check/SKILL.md:138`「the human flips the last switch」は `boundary.md` と食い違う
  （設計の選択を含むので直さない）
