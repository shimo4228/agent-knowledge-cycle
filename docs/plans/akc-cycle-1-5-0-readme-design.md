# README 入口の設計（readme-writer Step 1）— akc-cycle / AKC

as-of 2026-10-08。plan: [akc-cycle-1-5-0-release.html](akc-cycle-1-5-0-release.html) の claim 2・3。
決定済み: tagline は ADR-0021 のまま、ADR-0020 には注記、収載の 1 行は Published 確認後、akc-cycle の引用は README の Cite 節だけ。

## A. akc-cycle `README.md`（英語のみ）

**読者**: plugin directory か AKC から来た Claude Code 利用者。問いは「何か / 自分の harness に入るか / どう入れるか」。

### 情報の割り振り

| 置き場 | 内容 |
|---|---|
| 見える本文 | 何をするものか（1 段落）/ 2 つの入れ方のコマンド / 前提（plugin の一部 skill は同梱 Python script を `uv` と Python 3.11+ で走らせる）/ plugin が足さないもの（hook・MCP・設定なし）/ 各 phase で何が起きるかの表 / Cite / More from the author / License |
| 畳んだ節 `For tools and AI assistants` | identity 文、2 層の理由（常時ロードの rules file と、必要時に読まれる skill の信頼性の差）、Scaffold Dissolution、2 つの edition（self-contained / pointer）、companion skill の一覧と接地する AKC ADR、sync の仕組み（harness が正本・一方向・allowlist）、link map（AKC repo・llms.txt・llms-full.txt・claude-harness の pointer edition） |
| 外へ | なし（repo が小さいので docs/ は作らない） |

### 節構成案

| 節 | 読者の問い |
|---|---|
| H1 + lead | これは何で、自分向けか |
| （収載の 1 行） | 信用できる配布元か — Published 確認後に置く |
| Install | どう入れるか（rules file: `curl` 1 行で取れる形にする。今は clone が前提で書かれていない / plugin: `/plugin marketplace add` + `/plugin install`）。前提と「足さないもの」を 1 行ずつ |
| What each phase does | 入れると何が起きるか（phase / skill / いつ動くか の表。companion は 1 行ずつの list） |
| How to cite | 引用するなら何を（AKC の concept DOI） |
| More from the author | ほかに何があるか（現行の 2 件 + AKC） |
| License | |
| `<details>` For tools and AI assistants | 上の表の畳んだ節 |

「Syncing from the harness」節（保守者向け）と「Two editions」の blockquote は畳んだ節へ移す。

### 造語

| 語 | 扱い |
|---|---|
| rules file / plugin | 残す（一般語） |
| companion skills | 残す。初出に「AKC の概念を回す skill で、特定の phase に属さない」と 1 行 |
| floor / skill layer | 本文では平易に言い換える（「最小の入れ方」「phase ごとの手順」） |
| self-contained edition / pointer edition | 畳んだ節へ |
| Scaffold Dissolution | 畳んだ節へ（本文では 1 句の言い換えだけ） |

### 図

置かない（2 つの入れ方は list で足りる）。

### tagline

置かない（lead が担う）。欲しければ headline-craft で 3〜6 本出す。

## B. AKC `README.md` / `README.ja.md`

**読者**: 研究 repo を見に来た人（引用・概念を知りたい）と、cycle を試したい harness 運用者。

### 拘束

- tagline を変えない（ADR-0021）、en / ja の H2・H3 を揃える（CLAUDE.md）
- 先頭 30 行に 3 themes の語（ADR-0020 の検証条件 1）: lead に intent alignment の 1 句を足して満たす
- 3 themes の唯一の full presentation（ADR-0020）は畳んだ節へ移る。これを ADR-0020 に日付つき注記で残す（plan の決定）
- 接地リンク（ADR-0027）は畳んだ節に残る（README の中にあるので front-door のまま）

### 情報の割り振り

| 置き場 | 内容 |
|---|---|
| 見える本文 | 言語切替 / H1 / badge 2 / tagline / lead（3 themes の語を含む）/ Try it（rules file と plugin のコマンド）/ The cycle（mermaid + phase 表）/ Why AKC の 3 行版 / How to Cite / More from the author / License |
| 畳んだ節 `For tools and AI assistants` | identity、Why AKC の全文（3 themes）、What a running AKC looks like（4 層の表と接地リンク）、Limitations、Positioning、Origin & Acknowledgments、What's in this repo（link map）、Related Work、core concept 定義（six phases / harness alignment・drift / human approval gate / scaffold dissolution / three-role loop） |
| 外へ | Positioning の詳細は ADR-0013 / ADR-0017 / llms-full.txt にあるので、畳んだ節では 2〜3 文に縮めてリンク |

### 節構成案（en / ja 共通）

| 節 | 読者の問い |
|---|---|
| H1 + tagline + lead | これは何で、何が他と違うか |
| Try it（現 Install を上げて改名） | どう試すか。rules file と plugin。「各 phase の skill は plugin に入っている」を 1 行 |
| The cycle | 何が回るのか（図と表）。表の skill 列は単独 repo へのリンクを保ち、plugin に全部入ると 1 行 |
| Why AKC | なぜ要るのか（3 themes を 1 行ずつ。全文は畳んだ節） |
| How to Cite | 引用するなら何を |
| More from the author | Zenn / Dev.to と hub（現 Related Work 末尾の 1 文を独立させる） |
| License | |
| `<details>` For tools and AI assistants | 上の表の畳んだ節 |

H2 は 11 個 → 6 個 + 畳んだ節になる。ADR-0020 の行数目標（約 120〜140 行）は、見える本文で満たし、総量（畳んだ節を含む）は readme-writer の約 1.5 万字で見る。

### 古くなっている事実

| 箇所 | 今 | 直し方 |
|---|---|---|
| README.md:62-66 | 「Seven months of daily operation (February to September 2026)」「the newest three from September 2026」 | as-of 日付で書くか、期間を書かない |
| README.md:174-176 | 「roughly two weeks of single-operator practice (from 2026-08-17)」 | 「since 2026-08-17」に変える（期間は書かない） |
| README.md:128-146 | Install が rules file のみ | plugin を足す |
| README.md:140-143 | 「add the phase skills above」 | plugin で一括に入ると書く |

### 図

既存の mermaid（cycle のループ）を残す。新しい概要図は作らない。

## C. 変わる事実の持ち主

| 事実 | 持ち主 |
|---|---|
| AKC の version・version DOI・BibTeX | release-doi |
| concept DOI badge | 固定 |
| akc-cycle の version | plugin.json（README に書かない） |
| skill の数 | 書かない |
| 収載の状態 | README に as-of 日付と version つきの 1 行。release ごとに見直す |
| 運用の期間・ADR の数 | 書かない（ADR の数は llms-full.txt が持つ） |

## D. About（Step 6 で案を出す）

- akc-cycle の description は「single behavioral rules file — install all six phases without the six standalone skills」のままで、plugin に触れていない。lead と同じ主張に直す
- AKC の description・homepage（concept DOI）はそのまま使える見込み

## E. 確認してほしいこと

1. A・B の節構成と割り振りでよいか
2. akc-cycle に tagline を置くか（既定: 置かない）
3. 訪問者役の読み（初見の訪問者 3 人の読み、sonnet 3 体）を akc-cycle で回すか（既定: 回す。install が目的の repo なので）。AKC は回さない
