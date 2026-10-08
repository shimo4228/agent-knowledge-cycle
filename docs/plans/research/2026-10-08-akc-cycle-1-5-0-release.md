kind: external
# akc-cycle 1.5.0 と AKC の DOI release を、何を編入し、どの順で、README をどう変えて出すか

as-of 2026-10-08。統合元: 外部 notes（`~/.cache/claude-research-notes/2026-10-08-akc-cycle-directory/external.md`）、内部 notes（`.../2026-10-08-akc-cycle-selection/internal.md`）、lead の追加確認（2026-10-08、下記「lead 確認」）、README 証拠（scratchpad `readme/` 3 ファイル）、readme-writer SKILL.md、AKC の ADR-0012 / 0020 / 0021 本文。notes に無い主張は足していない。推論は「推論」と明記した。

## 問いと結論

- 問い（著者原文）: akc-cycle が Anthropic の plugin library に収録されたので、harness に増えた skill から AKC に取り入れるものを選び、akc-cycle に編入し、akc-cycle 1.5.0 と AKC の DOI を release したい。両 repo の README 改善も plan に入れる。
- 収録は一次確認が取れていない。出典は著者の申告のみで、公開側の 4 経路（official / community の marketplace.json、claude.com の listing URL、claude.ai/directory）はすべて該当なし。portal（claude.ai/directory/manage）で status が Published か、tracked branch/tag は何かを著者が確かめることが plan の前提になる。
- 編入の材料は揃った。既存 17 skill は harness 正本と内容差分ゼロ。Include 条件付きは 4（skill-creator / verify-bootstrap / loop-design-check / measurement-discipline）、Hold 2、Exclude は残り。日本語を含む候補は英訳が必須で、英訳を harness 正本へ戻すかは著者判断。
- 順序は akc-cycle 1.5.0 を先、AKC v2.9.0（DOI）を後。AKC 側に akc-cycle の記述が古い箇所が 10 件あり、Zenodo は release 時点の repo を archive するので、release 前に直す。
- README は、readme-writer の ADR-0091（floor は README 末尾の畳んだ節）と AKC の ADR-0020（floor は llms-full.txt、README は pointer）が逆を言う。ADR-0012 / 0021 とは両立できる範囲が広いが、ADR-0020 との衝突は著者が決める。

## Scope searched

- 外部 notes の範囲: Anthropic 公式 docs（claude.com/docs/directory/publish, /plugins/submit, /plugins/pre-submission-checklist, /directory/submission-status, /connectors/building/after-publishing; code.claude.com/docs/en/plugins/publish, /manifest-reference）、Software Directory Terms と Trademark Guidelines（要約器経由）、official / community registry、akc-cycle の README / CHANGELOG / plugin.json / commits。公式の収載表記規定・バッジは見つからなかった。出典: external.md:8-17。
- 内部 notes の範囲: `~/MyAI_Lab/akc-cycle`（sync script、CHANGELOG、payload 17 skill）、harness 正本（payload 外 shimo4228 origin 29 skill + loop-design-check）、AKC repo の docs / llms / graph。Bash 不可のため dry-run は未実行だった（internal.md:3-5）。
- lead 確認（2026-10-08、lead が実行）:
  - `~/MyAI_Lab/akc-cycle/scripts/sync-from-local.sh --dry-run` の出力はヘッダ行のみ = 既存 17 skill は harness 正本と内容差分ゼロ。
  - anthropics/claude-plugins-official（315 件）と anthropics/claude-plugins-community（2,284 件）の `.claude-plugin/marketplace.json`（main）を jq で "akc" / "shimo4228" 検索 → 該当 0 件。
  - https://claude.com/ja/marketplace/plugins/akc-cycle は "Nothing to see here"。https://claude.ai/directory（未ログイン）で "akc" 検索 → 該当なし（未ログインで plugin が出る画面かは不明）。
- README 材料: scratchpad の readme_evidence 出力 3 件、`~/.claude/skills/readme-writer/SKILL.md`（全文）、AKC の `docs/adr/0012-front-load-three-core-themes.md` / `0020-readme-minimal-floor.md` / `0021-replace-growth-tagline.md`（全文）、AKC README.md:1-60,120-150 と H2 一覧。readme-judge の checklist、`references/about.md`、akc-cycle README 本文、現在の GitHub About は読んでいない。

## Found

### 1. 収載の事実と更新経路

確認できた事実

- directory の実体は claude.ai/directory で、登録は portal `claude.ai/directory/manage` から。claude.com/marketplace に別の submission はない。出典: https://claude.com/docs/directory/publish （2026-10-08）
- `claude-plugins-official` は portal 経由の submission を受けない。`claude-plugins-community` は read-only mirror で、Anthropic の review pipeline から nightly sync。出典: https://code.claude.com/docs/en/plugins/publish , https://github.com/anthropics/claude-plugins-community （2026-10-08）
- akc-cycle 自身の記録は「submit し validation を通した」までを裏づける: CHANGELOG 1.4.0「ahead of the Claude directory submission」、1.4.1「Fixes from the Claude directory validation report」、1.4.2 は icon 修正。commits は 2026-10-07 まで。「approved / published」を示す文言はない。出典: https://raw.githubusercontent.com/shimo4228/akc-cycle/main/CHANGELOG.md （2026-10-08）
- portal の状態は Draft / Scanning / Needs changes / In review / Approved / Published / Not live yet / Delisted / Withdrawn。「Approved は install 可能を意味しない。Published になって初めて installable」。出典: https://claude.com/docs/directory/submission-status （2026-10-08）
- 収載後の更新に再 submit は要らない。tracked branch/tag に merge すると directory が commit を拾い、scan し、publish する。検出は schedule のポーリング + 任意の GitHub push webhook（repo の admin 権限が要る）。即時反映は portal の「Check for new commits」。出典: https://claude.com/docs/plugins/submit#update-a-published-plugin , https://claude.com/docs/connectors/building/after-publishing
- scan された version（commit）ごとに自動 validation + security scan。新規 listing のみ人が審査し、既存 listing の新 version は passing なら publish 設定に従う（設定は 3 種: 全 version を reviewer が publish / 初回のみ reviewer / 初回を自分で publish して以降自動）。失敗・hold した version は live を落とさず最後の publish 版を配り続けるが、security scan が fail すると reviewer が clear するまで以降の version も待たされる。出典: https://claude.com/docs/directory/publish#prepare-for-review
- `plugin.json` に `version` があるなら毎 release で上げる。akc-cycle は version を持つ（現在 1.4.2、plugin.json:5）ので 1.5.0 への bump は必須。出典: external.md:67-68
- tracked は branch または tag。空欄 = repo の default branch。submission 後に repo / folder は変更不可。出典: https://claude.com/docs/plugins/submit
- akc-cycle の版は plugin.json の `version` だけで刻まれている。`.git/refs/tags` が空で、CHANGELOG 1.0.0〜1.4.2 に対応する tag がローカルに無い。出典: internal.md:132-133

未確認

- akc-cycle が Published か。lead 確認の 4 経路はすべて該当なしで、公開側から Published を示す証拠は 0 件。「該当なし」は未収載の証明にもならない: community は nightly sync で反映遅延がありうる、official は portal を受けない、claude.ai/directory は未ログインの画面が plugin を出すか不明、listing の slug が `akc-cycle` でない可能性がある。出典: external.md:34-41 と lead 確認。
- 掲載エントリの source 形態（tracked branch の最新を都度配るのか、publish 時点の SHA に固定か）、掲載 version、tracked branch/tag の実値、Auto-publish 設定、listing URL と slug。
- portal の validation report 全項目（icon の 512×512、skill description の英訳要求の出所）。pre-submission checklist 本文に icon と「英語必須」の行は無く、根拠は author の CHANGELOG だけ。出典: external.md:78,82
- Directory Terms の原文。要約器は「listed という主張自体が承認なしでは禁止」とも書いたが、原文は「suggests partnership / sponsorship / endorsement」。事実としての収載記述に事前承認が要るかは未確定。出典: external.md:99

前提条件（plan の最初に置く）

1. 著者が portal で status = Published を確認し、tracked branch/tag、Auto-publish 設定、listing URL、掲載 version を記録する。Approved では不足。
2. 「main の全 commit が scan 対象」は外部 notes の推論（external.md:70）。公式文は「scan された commit ごとに」と書く。検出はポーリング + 任意の webhook なので、webhook を設定していなければ途中の commit は拾われない可能性がある。tracked が main のままなら、1.5.0 までの途中状態を main に積まない運用（task branch で作業し、完成後に ff-only で取り込む）が安全側。推論。
3. security scan が fail すると以降の version も待たされる（上記）。新 skill の追加は scan の再実行になる。

### 2. 1.5.0 で skill を足すときに引っかかりうる要件

出典はすべて https://claude.com/docs/plugins/pre-submission-checklist と manifest-reference（external.md:74-92、2026-10-08）。

- unpinned launcher（`npx` `bunx` `uvx` `pipx run` `uv run` 等）は Blocks。pin 済みでも常に reviewer hold。akc-cycle は 1.4.1 で `uv run --frozen` と `pyld==3.3.0` pin を入れた実績がある。
- 本調査では、Include 候補 4 skill の SKILL.md と同梱ファイルに launcher が無いかを grep していない（どちらの notes にも無い）。verify-bootstrap は `references/ci-verify.yml` を同梱し、`uv run` を含むかは未確認。編入前に grep が要る。
- skill front matter の description は単一テキスト。folder 名 = `name`。非画像ファイルは各 256 KiB 未満、512 files 以下、text / 画像 / font 以外の binary は hold。現状は余裕あり（blob 89、最大 uv.lock 45,802 B）。
- README は listing description として表示される。skill 数（"seventeen" 等）を README と plugin.json description で揃える。
- 新 skill が外部 fetch や送信を指示するなら README に書く（security scan 準備）。

### 3. 編入候補の選定表（内部 notes §A を圧縮）

凡例: JP = SKILL.md の日本語行数 / 全行数（harness 正本）。file:line は internal.md の引用で、harness 正本側。判断は著者。

| 区分 | skill | 根拠（接地 AKC concept / ADR） | 編入前に要る作業 | payload 内の参照（強度） |
|---|---|---|---|---|
| Include（条件付き） | skill-creator | Extract→Promote の行き先（learn-eval:38,212 が hand-off）。ADR-0005 の sign-off が §1 `⏸`（:16）と §7（:131）にある。JP 106/141 | 英訳。harness 固有行の整理: `hooks/skill-create-notice.sh` と「Fable」（:3）、`harness_lint.py`（:57,126,141）、`claude plugin eval`（:111）、harness ADR 番号（:48-58, :135）。`references/portability.md`（JP）の同梱 | 強・10 skill（learn-eval, skill-stocktake, rules-stocktake, agent-stocktake, skill-health, skill-comply, rules-distill, generation-audit, harness-boundary, llm-as-judge）。AKC の ADR に名指しは無い |
| Include（条件付き） | verify-bootstrap | ADR-0025 の機械ゲート（lint 選定の 4 軸 :85-99）。AKC README.md:72 が Enforcement 層の running instance として claude-harness 経由で名指し済み。JP 157/243 | 英訳。Step 4 は harness の hook 契約（:150,185,225、`verify_allow.py`、`~/.claude/.claude/verify.md` :86、harness ADR 0056/0075）なので「verify.sh の契約を満たす hook がある環境向け」と再定式化。`references/ci-verify.yml` 同梱 | 例示のみ（skill-stocktake:84, usage_stats.py:24）。参照切れではない |
| Include（条件付き） | loop-design-check | ADR-0024（plan/build/judge :3,96,134,171）、ADR-0005（機械 + 人間の 2 段フィードバック :24-31）。英語（JP 1/171） | origin が `ECC-customized`（:5）で sync script の `require`（sync-from-local.sh:52-61）が ABORT する（判断 D2）。`architect` agent、`/claude-api hillclimb`（:43）、`AC-NNN`、harness ADR 参照を言い換え | 弱・1（harness-boundary:3,105,120） |
| Include（候補） | measurement-discipline | Measure に隣接（ADR-0016 / 0022 :43,:50）。どの AKC ADR も名指ししない。SKILL.md 単体、道具依存なし。JP 83/115 | 英訳。事例の出所が作者の他 repo（CA RFC-0045/0046/0047、jev-research-pipeline :78,103）、`:3` の NOT-for が CA の skill を指す、`:6 replaces:` が CA の memory を列挙 | 弱・1（author-calibrated-eval:3） |
| Hold | task-triage | 接地は最強（ADR-0024 / 0028、README.md:73、graph.jsonld:776 で接地済み）。JP 26/424 | skill 外の harness 資産に実行依存: `claims.py`（:54,56,140,302）、`cloud-dispatch.sh`（:133,174）、`notify-slack.sh`（:106）、`verify_allow.py`（:311）、launchd、`spawn-session`、harness ADR 8 本。`references/first-cycle-2026-08-17.md` は作者 repo 名入り。概念版への書き直しが要る | 弱・1（generation-audit:31） |
| Hold | session-judgment-mining | Extract の遡及版（learn-eval:3 が NOT-for で対置）。JP 69/117 | Step 2 が別 repo の helper に依存（`~/MyAI_Lab/zenn-content/.claude/skills/session-theme-mining/scripts/session_catalog.py` :34-35,114）。自己完結の抽出器に置き換えるまで動かない | 弱・1（learn-eval:3） |
| Exclude | review-when-watch | ADR-0026 の読む側の自動化だが ADR-0026 は watcher を要求しない（:31,33）。launchd / Slack / TypeSafe 前提。`disable-model-invocation: true`（:9-10）で skill でなく運用手引き | — | なし |
| Exclude | implementation-chain, harness-sync, readme-writer, release-doi, llms-txt-writer, jsonld-knowledge-graph, rfc-writer, task-stocktake, repair-discipline, authorship-strategy, collect-context, headline-craft, x-draft, prose-translation, public-comment, mono-figure, prompt-perturb, wiki-query, wiki-harvest, hf-sync, spawn-session | 接地が無いか、作者の執筆・公開・台帳運用 genre（ADR-0011）、または harness 資産・Herdr・Obsidian 前提。jev-skill-router と spawn-session は別 plugin（`jev-skill-router`、`herdr-toolkit`）で配布済み（harness-sync:216-217） | — | 下の言い換え一覧 |
| Exclude（編入不可） | grill-me, wait-what | mattpocock-customized（本文は読んでいない）。origin guard で ABORT | — | — |

4 skill 全部入れると 17 → 21。ただし skill 数を README / plugin.json に書く限り drift が再発する（harness-sync:68 は集約カウントを書かない方針）。

payload の参照切れと、言い換えで潰す参照（内部 notes §E。Include の編入が決まれば skill-creator 分は解消し、決まらなければ全部言い換え）

- skill-creator（強・約 25 箇所）: Include なら同梱で解消。skill-health/SKILL.md:95 の `~/.claude/skills/skill-creator/references/portability.md` は sync の rewrite で `${CLAUDE_PLUGIN_ROOT}/...` に直り、同梱されれば解決する（sync-from-local.sh:102-111）。代替案: 参照を「skill 作成 skill（例: 公式 skill-creator）」へ言い換える。Anthropic 公式 `skill-creator` は anthropics/skills に在る（2026-10-08、小モデル要約）。
- implementation-chain: search-first:3,79（「依存追加の取り込み手順」へ一般語化）/ context-sync:281 / harness-boundary:3。
- harness-sync（6 skill）: rules-stocktake:185 / agent-stocktake:255,301 / skill-health:162 / skill-stocktake:402 / repo-asset-stocktake:143 / llm-as-judge:176 →「公開 repo への同期」。
- readme-writer / release-doi / llms-txt-writer / jsonld-knowledge-graph（context-sync:53,110,144,167,249,250,264,284 ほか）、review-to-lint:12,96,111、author-calibrated-eval:3。
- rfc-writer: harness-boundary:98 →「台帳に draft で残す」。
- `html-plan`（adr-writer:158 / search-first:86）、`architect`（context-sync:19,33,68,69,145,265 ほか）: 所在未確認。
- 既存の harness 内部リンク切れ（1.5.0 の対象外だが同じ sync で目に入る）: agent-stocktake/SKILL.md:85,170、learn-eval/SKILL.md:46、rules-distill/SKILL.md:57,58（plugin 形で解決しない harness ADR への相対リンク）。

編入の機械的手順（候補が決まった後）: `SKILLS=` 配列（sync-from-local.sh:33-36）への追加、frontmatter の origin 検査（:57-59）、JP→EN 後の YAML 検証（:136-160）、secret scan（:162-168）。script は commit しない（:12-13）ので `git diff` が review gate になる。

### 4. AKC 側の drift 一覧（akc-cycle plugin の記述が古い、または plugin が現れない箇所）

出典: internal.md §C（file:line は AKC repo）。今回の README 読みで追加した行は「追加」と付けた。

| file:line | 内容 | 状態 |
|---|---|---|
| docs/akc-cycle.md:32-36 | 「Since v1.1.0 the same repository also ships the nine cycle-phase skills」 | 古い（現在 17、1.4.0 で 9→17。版差語も残る） |
| docs/akc-cycle.md:9 | 「without installing the six standalone cycle skills」 | six / ten の食い違い |
| graph.jsonld:1277 | akc-cycle ノート「bundling the nine cycle-phase skills and their two subagents」 | 古い（subagent は 1.3.0 で撤去、skill は 17） |
| llms-full.txt:124 | 「additionally install the cycle skills as external repositories (…10 skill 名…)」「No skills, no plugins…」 | plugin 経路が出ない。10 skill 列挙も companion 7 を欠く |
| llms-full.txt:31, :81, :113 | akc-cycle を rules file の standalone repo としてのみ記述 | plugin 経路・17 skill の言及なし |
| llms.txt:67 | 「AKC Cycle Rules」= rules file のみ | plugin 経路なし |
| llms.txt:133-149 | 「Optional: the phase-scaffolding skills … available as external repositories」 | plugin 一括経路が出ない |
| README.md:22-25, :128-146 / README.ja.md:21-24, :125-134 | 「Try it first」と Install 節は rules file のみ。:140-143「add the phase skills above」 | plugin への言及なし（en/ja の H2 対応は CLAUDE.md の不変条件） |
| README.md:106-113 | phase 表の列名「Current external skill」= 単独 repo リンク | 17 skill の plugin 経路は表に無い |
| graph.jsonld:776 | claude-harness ノート「some 58 skills (the six AKC cycle skills among them…)」 | six / 10 の食い違い。集計値 58 は harness-sync:68 の No-volatile-state に反する形 |
| 追加: README.md 全体 | evidence script は 261 行 / 17,374 字。ADR-0020 は目標 ≈120–140 行、200 行超を再監査の signal とする（ADR-0020:68,85）。readme-writer は約 1.5 万字超で docs/ 移動を問う（SKILL.md:148） | 既に ADR-0020 の再監査 signal を超過 |
| 追加: README.md:1-30 | grep で `intent alignment` / `aligned with intent` の唯一の出現は :40（Why AKC 内）。ADR-0020 の検証条件 1（先頭 30 行に 3 cluster 各 1 語）は、cluster 2 について文字どおりには満たしていない | ADR の検証条件との不整合（cluster 1, 3 は :14-15 に「attention and judgment」「changes the human too」） |

偽陽性: docs/scaffold-dissolution.md:58, :70 の「nine」は skill 数ではない。`.zenodo.json` に akc-cycle の記載は無く（`related_identifiers` の 1 件が唯一のヒット）、CITATION.cff:6 の abstract は plugin に触れない。

akc-cycle 側で 1.5.0 時に個数・名前を直す箇所: README.md:8,30,51 / llms.txt:3,10,14,20 / llms-full.txt:3,14,24,36,40,48 / `.claude-plugin/plugin.json:3`（version は :5）/ `.claude-plugin/marketplace.json:11` / `scripts/sync-from-local.sh:5-6`（コメント）と :33-36（配列）。harness 側の `~/.claude/skills/harness-sync/SKILL.md:158` も「AKC cycle phase binding の skill 群」と書いており、17 skill と合わない。

### 5. README 改善（両 repo）

証拠（readme_evidence、2026-10-08）

| | AKC README.md | AKC README.ja.md | akc-cycle README.md |
|---|---|---|---|
| 規模 | 261 行 / 17,374 字 | 253 行 / 20,454 字 | 69 行 / 6,647 字 |
| `<details>` | 0 | 0 | 0 |
| em-dash | 23 | 23 | 22 |
| 第一画面 | H2 まで 26 行、prose 16 行、新語 1 | 25 行、15 行、1 | 9 行、prose 1 行、新語 2（Rules file / Claude Code plugin）|
| 内部参照 | ADR 19（unique 13）、github repo 25 | 同 | ADR 7（unique 5）、github repo 5 |
| DOI / how-to-cite | あり / あり | あり / あり | DOI あり / **how-to-cite なし** |
| 造語候補 | 11 | 4 | 33 |

出典: scratchpad `readme/*.txt`。akc-cycle の install は自前 marketplace（`/plugin marketplace add shimo4228/akc-cycle`）のみで、directory 経路の記述はない（lead 材料 4）。akc-cycle の slop 0、壊れた local ref 0、alt 欠落 0。

readme-writer の Rewrite モード（SKILL.md:190-238）は 7 step。人間ゲートは Step 1（入口設計: 情報の割り振り、節構成案、造語の表、変わる事実の持ち主、tagline 候補）と Step 6（著者通読 GO: README 全文 + 判定結果 + About 案 + 描画 PNG の前後比較）。判定は fresh context の `readme-judge`（draft → recheck → final → recheck の 2〜4 回、上限 2 ラウンド）。描画証拠は `readme_render.py`（desktop / mobile、light / dark）。Step 6 は About（description / topics）の「現状 → 提案」で、DOI repo の homepage・CITATION・release metadata は `release-doi` が持つ（SKILL.md:106-108）。見える本文は「冒頭で何をするものか + 使い始めの摩擦の解消」、why・設計・比較は畳んだ節か docs/ へ（SKILL.md:69-75）。LLM-read フロアは末尾の `<details>` に文で置き、DOI repo は DOI + how-to-cite + core concept 定義 3–6 個を含める（:84-95）。

### 6. ADR-0012 / 0020 / 0021 と readme-writer（ADR-0091）の衝突

AKC 側の拘束（本文を読んだ）

- CLAUDE.md の不変条件: tagline を README en/ja 両方で保つ（ADR-0021）、README en/ja の H2/H3 構造を揃える、3 themes を front-door で先に登場させる（ADR-0012）。
- ADR-0012（2026-05-08）: README の最初の 30 行に 3 theme 各 1 語、themes は six-phase mechanism より前。ただしその README-internal 部分は ADR-0020（2026-07-07）が修正済み: 「Why AKC」に 3 themes の唯一の full presentation を置き、先頭 30 行の検証条件 1 と themes が mechanism の前、は維持（ADR-0020:25,29,82-83）。llms.txt / llms-full.txt の約束（blockquote 順序、Q2 = central constraint、Q3 = intent alignment）は不変（ADR-0020:31,80）。
- ADR-0021（2026-07-08）: tagline は「A knowledge cycle for AI agents — agent behavior compounds, human judgment sharpens.」。変更時は README.md / README.ja.md / llms.txt / llms-full.txt / CITATION.cff / .zenodo.json / codemeta.json の同時更新が要る（ADR-0021:33。同 ADR の docs/CODEMAPS/architecture.md は 2026-09-26 に削除済み）。

両立する部分

- tagline: ADR-0091 は tagline を禁じない。Step 1 の tagline 候補は著者が選ぶので、現行 tagline を残せば ADR-0021 と衝突しない。変えるなら ADR-0021 の supersede と上の同時更新が要る。
- en/ja の構造対応: readme-writer Step 3 は「同じフロア・見出し階層・アンカー・例で揃える」（SKILL.md:211-213）で CLAUDE.md の不変条件と同方向。現状も両言語の H2 は 11 個で一致（README.md と README.ja.md の H2 一覧）。
- 先頭 30 行の 3 themes: lead 段落（README.md:10-17）に theme 1 と 3 の語が既にある。intent alignment の 1 句を lead に足せば ADR-0020 の検証条件 1 を満たしたまま、「Why AKC」本文を畳める。これは構成案であって推奨ではない。
- 長さ: ADR-0020 の 200 行超 signal と readme-writer の 1.5 万字超の問いは同じ方向（肥大の是正）。
- 識別情報（DOI、how-to-cite、author identifiers）: ADR-0020:25 の (g)(h) と readme-writer フロア 3 は一致。

判断を要する部分

- floor の置き場所が逆: ADR-0020 は「README が full information floor を持つ前提」を誤りとして訂正し、floor を llms.txt / llms-full.txt / graph に置いて README は pointer にした（ADR-0020:19,27）。readme-writer は「load-bearing な情報は README 末尾の畳んだ節に置き、llms.txt や graph は補助にとどめる」（SKILL.md:43-45）。根拠は、URL を取得した AI の経路が `<details>` の中も末尾も読み、llms.txt は読まれたり読まれなかったりする、という実験（各条件 1 回、as-of 2026-10-08、SKILL.md:41-43）。AKC の証拠基準（memory: 観測された痛み / 反復実践のみ ADR に値する）に照らすと、n=1 の取得実験が新 ADR（次番号は 0029）の根拠になるかは著者判断。ADR-0020 の該当節に注記で済ませる道（rules/common/akc-cycle.md の ADR の扱い）もある。
- 「Why AKC」を見える本文に残すか: ADR-0012 / 0020 は「themes は mechanism の前、唯一の full presentation」。ADR-0091 は why を畳んだ節か docs/ へ（SKILL.md:73）。lead への theme 句の追加（上記）か、ADR-0020 の検証条件の読み替えか、現状維持か。
- ADR-0012 の README 側検証条件（ADR-0020 が置換）は、畳んだ節に themes を置くと機械的に（先頭 30 行の語として）は満たせなくなる。畳んだ節は ADR-0091 の下でも LLM は読むが、ADR-0020 の条件は「先頭 30 行」を文字どおり要求している。
- 行数目標: ADR-0020 の ≈120–140 行目標は、readme-writer の 1.5 万字目安（SKILL.md:148）と別の尺度。畳んだ節を含めた総量が 261 行から減るとは限らない（floor を README に戻すと増える方向）。

## Contradictions

1. 収載の有無。著者の申告（収録済み）と、公開側 4 経路の「該当なし」。外部 notes の「truncated の可能性」（external.md:36-37）は lead の jq（315 + 2,284 件）で解消した。ただし community は nightly sync、official は portal を受けない、未ログインの claude.ai/directory が plugin を出すか不明のため、「該当なし」は未収載を証明しない。強い根拠は portal の status だけで、著者の画面にしかない。申告を覆す証拠もない。
2. 内部 notes の「行数一致 = 内容一致の証明でない」（internal.md:83-84）は、lead の dry-run（ヘッダのみ）で解消。dry-run の比較対象と粒度は本統合では確認していない。
3. 「main の全 commit が scan 対象」（external.md:70、lead の依頼文も同旨）は推論。公式文は「scan された commit」で、検出はポーリング + 任意の webhook。webhook が無ければ途中の commit は拾われない可能性があり、tracked を tag にすれば release 時点を固定できる。どちらが実態かは portal の設定次第で未確認。
4. ADR-0020（floor は llms-full.txt、README は pointer）と readme-writer（floor は README の畳んだ節）が直接逆。後者の根拠は n=1 の取得実験、前者の根拠は 2026-07-07 の operator の density 苦情（観測された痛み）。重みの比較は著者判断で、本調査は決められない。
5. 内部 notes の skill-creator 評価（Include 条件付き）と、Anthropic 公式 skill-creator の存在（internal.md:43）。矛盾ではなく選択肢の併存: 同梱するか、参照を公式 skill-creator へ言い換えるか。

## Still unknown

- akc-cycle の directory status（Published か）、tracked branch/tag、Auto-publish 設定、listing URL と slug、掲載 version、source 形態。
- 収載の事実を書くことへの Directory Terms 原文上の制約。公式の収載表記・バッジ規定は見つからなかった。plugin の listing URL の形は未確認。
- 1.4.0 が verify-bootstrap と task-triage を外した理由（CHANGELOG.md:31-48 に記述なし。移植性か接地の弱さかで 1.5.0 の線引きが変わる）。
- Include 候補 4 skill に launcher（`uv run` 等）が含まれるか、`uv.lock` / `pyproject.toml` が hold 対象か、scan が SKILL.md 本文中の launcher をどこまで拾うか（1.4.1 の実績は 1 件）。
- loop-design-check の ECC 由来部分の範囲と再配布上の帰属。`license: MIT`（:4）はあるが、ECC 文面とのどこが重なるかは未確認。
- 英訳を harness 正本へ戻したとき、日本語 trigger 語（skill-creator §1 :21 は著者の発話例を description に入れると定める）を失ってよいか。payload と正本の description が分岐する可能性。
- measurement-discipline を Measure に接地する AKC 側の根拠（ADR）を著者が持つか。現状は隣接のみ。
- akc-cycle の GitHub 側 Zenodo webhook の有無、remote tag の有無（`gh` 不可）。akc-cycle の現在の GitHub About（description / topics）。
- readme-judge の checklist 内容と akc-cycle README 本文は本統合で読んでいない。akc-cycle README が実際に何を言い、何を畳むべきかは readme-writer Step 1 で決まる。
- `html-plan` / `architect` の所在（参照切れの総量に入る）。
- AKC v2.9.0 の版番号は lead 案。minor か patch かは未確認（release-doi が決める）。
- 収載の表記が listing の description に与える影響: listing の name / short description は live version の plugin.json と README から取られる（reviewer が編集した場合は reviewer の文面が残る）。README 改訂が listing 表示をどう変えるかは portal の表示で確認するまで未確認。

## 判断が要る分岐（著者が決める）

前提: D0 が先。以降は D0 の結果で変わる。

- D0 収載の事実確認（前提条件）。portal で status、tracked branch/tag、Auto-publish、listing URL、掲載 version を確認して記録する。
- D1 編入する skill の集合。4 全部（21 skill）/ 一部 / Hold 2 を含める / 0（言い換えのみ）。Hold の 2 つは概念版への書き直しか、claude-harness への接地リンクで足りるか（task-triage は README.md:73 で既に接地、ADR-0027 の grounding expectation は満たされている、internal.md:47）。
- D2 loop-design-check の origin 扱い。(a) 自作に書き直し `replaces:` で系譜を残して origin を反転（rules/common/skills.md の運用）、(b) sync script に skill ごとの許容 origin を足す（script 変更）、(c) 編入せず harness-boundary の 3 箇所（:3,105,120）を言い換える。ECC 文面の再配布の帰属表記も含めて著者判断。
- D3 英訳を harness 正本へ戻すか。CHANGELOG.md:24 の運用は「同じ編集を harness 正本にも適用する」。skill の変更は boundary.md で人間に渡す操作で、正本が英語化されると日本語 trigger 語を失う。戻さない場合は payload と正本が分岐し、以後の sync が毎回上書きするため sync script 側に翻訳段が要る（既存の JP→EN 工程 :136-160 がどこまで担うかは本統合で未確認）。
- D4 AKC の接地リンク先。現状は `claude-harness/tree/main/skills/<name>`（README.md:70-73, llms.txt:119,167,170, graph.jsonld:776）。claude-harness のまま / akc-cycle/skills/<name> に替える / 併記。ADR-0027 は「links follow running state」で、どちらも running instance。
- D5 ADR-0012 / 0020 / 0021 と ADR-0091 の扱い。(i) 現行 tagline を残すか（残せば ADR-0021 は無傷）、(ii) floor の置き場所（ADR-0020 の訂正を再訂正するか、現状維持か）、(iii) 「Why AKC」を見える本文に残すか、lead への intent alignment の 1 句追加で畳むか、(iv) 新 ADR（0029）か ADR-0020 への注記か（証拠基準: 観測された痛み / 反復実践）。(v) README.md の行数目標（≈120–140）を維持するか、再定義するか。
- D6 akc-cycle に Zenodo / CITATION を付けるか。現状は CITATION.cff も .zenodo.json も無く、AKC の concept DOI `10.5281/zenodo.19200726` を引くだけ（internal.md:129-131）。release-doi は CITATION.cff が無ければ skip（release-doi/SKILL.md:20-22）。案: (a) 付けず、README に AKC DOI の how-to-cite を足す（readme-writer のフロア 3 を満たす最小）、(b) CITATION.cff のみ、(c) Zenodo 連携まで。収載 version（tracked branch の最新 passing commit）と Zenodo release が指す commit は別物になりうる（external.md:107）。
- D7 収載の書き方。公式の表記規定は無く、Terms 原文は未確認。案: Published 確認後に「Anthropic の plugin directory に listed（as of YYYY-MM-DD、version X）」と日付つきで書き、portal が示す listing URL にリンクする。Anthropic / Claude のロゴ、「公式」「Anthropic-approved」「Verified」は使わない。Terms の読みを確定するなら directory@anthropic.com か marketing@anthropic.com に問い合わせる（external.md:105）。書かない選択肢もある。
- D8 akc-cycle の tracked 運用。main のまま（sync commit が積まれる運用なら、途中状態を main に置かない）か、tag を追うか（tracked の変更は Settings から可能で live version は維持される）。webhook の設定可否も含む。
- D9 akc-cycle README の install に directory 経路を書くか。directory 経由の install コマンドは未確認（external.md:72 は claude.ai 側 install が `<name>@synced` で同期されると書くのみ）。Published と listing の表示を著者が確認するまで書かない、が安全側。
- D10 AKC の drift 修正を v2.9.0 に含めるか。含めないと snapshot に誤りが焼き付く（internal.md:140-141）。README の plugin 経路（Try it first / Install）をどう書くかは D5 と D9 に連動する。

## release の順序と依存

1. D0 の確認と D1〜D9 の決定（Step 1 の人間ゲートと同時に回せる）。
2. akc-cycle 1.5.0（task branch で作業）:
   1. `SKILLS=` 配列に追加、origin 処理（D2）、英訳（D3）、payload 内の参照切れを言い換え（上の一覧）。launcher / binary / 256 KiB を編入前に grep。
   2. sync-from-local.sh を実行し `git diff` を著者が通読（script は commit しない）。secret scan。
   3. 個数・名前の更新（上の akc-cycle 側一覧）、plugin.json `version` を 1.5.0 に、CHANGELOG。
   4. akc-cycle README 改善（readme-writer Rewrite）をここで行う。README は listing description として表示される（external.md:86）ので、main に入る時点で完成していること。
   5. main へ ff-only 取り込み → directory が検出（ポーリング / webhook / 「Check for new commits」）→ scan → Auto-publish 設定に従って publish。reviewer publish 設定なら著者の portal 作業が要る。
   6. Published を portal で確認。失敗・hold ならここで止まり、以降の AKC release の記述（D7）は据え置く。
3. AKC v2.9.0:
   1. drift 修正（上の AKC 側一覧）。akc-cycle の記述（skill 数、skill 名、plugin 経路）が akc-cycle の main の実態と一致していること。Zenodo は release 時点の repo を archive するので、リンクと個数は release 前に確定する（internal.md:140-141）。
   2. AKC README 改善（readme-writer Rewrite、en/ja を揃える）を drift 修正と同じ編集で行う。両方が README.md:22-25,128-146 と README.ja.md の同じ箇所に触るため。D5 で新 ADR を作るなら、その ADR を先に main に入れる。
   3. release-doi の 4 phase: CHANGELOG / CITATION.cff / llms* を揃える（release-doi/SKILL.md:81-103）→ release commit・tag・`gh release create`（Release object が Zenodo の発火源 :192-200）→ 版 DOI を CITATION.cff / README に反映し SWHID を記録（:228-269）。直近の実例は commit `47243d5`。DOI 欄は release commit では据え置き（:89,397）。
4. 依存の向き（内部 notes §D）:
   - akc-cycle → AKC: concept DOI と ADR 番号（0008, 0022–0026）だけを引き、AKC の version DOI にも版にも依存しない。新 skill が引く ADR が既存範囲（0008〜0028）なら AKC の新 release を待たない。例外: v2.9.0 が ADR-0029 以降を作り akc-cycle が引くなら、その ADR を AKC の main に先に push する。
   - AKC → akc-cycle: 上の drift 一覧。AKC が「directory に listed」と書くなら、1.5.0 の Published 確認（D0, 手順 6）が先。推論: listing は mutable（Anthropic はいつでも delist できる、external.md:106）ので、AKC の Zenodo snapshot に焼く記述には取得日・version・portal status を併記する。
5. README 改善の位置: 各 repo の release commit より前。どちらの README も release 時点で凍結され（akc-cycle は listing 表示、AKC は Zenodo snapshot）、release 後の修正は次の release まで反映されない。readme-writer の 2 つの人間ゲート（Step 1, Step 6）は各 repo に 1 組ずつ。About（description / topics / homepage）の変更は Step 6 の成果物で、AKC の homepage・CITATION・release metadata は release-doi が持つ（SKILL.md:106-108）。`gh repo edit` による About 更新は外部可視なので著者承認の後。
6. validation / security scan が走る点: akc-cycle の tracked branch に入った commit（検出されたもの）は 1 つずつ validation + security scan を受ける（上の「前提条件」2, 3）。途中状態の commit を main に積まず、README と skill 編入を task branch で完成させてから ff-only で取り込めば、scan される version は完成形に近づく。fail した場合も最後の publish 版は live のまま。ただし security scan の fail は以降の version を reviewer の clear まで止める。
7. boundary.md 上、DOI release・public repo への push・skills の変更（英訳の harness 正本への適用を含む）は人間に渡す操作。plan の「実行者の決定」で明示する。

## 出典一覧（as-of 2026-10-08）

- https://claude.com/docs/directory/publish , /docs/plugins/submit , /docs/plugins/pre-submission-checklist , /docs/directory/submission-status , /docs/connectors/building/after-publishing
- https://code.claude.com/docs/en/plugins/publish , /plugin-marketplaces , /plugins/manifest-reference
- https://github.com/anthropics/claude-plugins-official , https://github.com/anthropics/claude-plugins-community
- https://raw.githubusercontent.com/shimo4228/akc-cycle/main/CHANGELOG.md
- https://support.claude.com/en/articles/13145338-anthropic-software-directory-terms（要約器経由）、https://www.anthropic.com/legal/trademark-guidelines（Last Updated 2024-08-01、要約器経由）
- `~/.cache/claude-research-notes/2026-10-08-akc-cycle-directory/external.md` , `.../2026-10-08-akc-cycle-selection/internal.md`
- `~/.claude/skills/readme-writer/SKILL.md` ; AKC `docs/adr/0012-front-load-three-core-themes.md` , `0020-readme-minimal-floor.md` , `0021-replace-growth-tagline.md` ; AKC `README.md`（1-60, 120-150, H2 一覧）, `README.ja.md`（H2 一覧）
- scratchpad `.../scratchpad/readme/{agent-knowledge-cycle_README.md,agent-knowledge-cycle_README.ja.md,akc-cycle_README.md}.txt`
