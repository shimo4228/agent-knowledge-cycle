# agent-knowledge-cycle

AI エージェントが自分の経験を改善可能な skill に metabolize する **cycle (mechanism)** を 6 phase に operationalize した DOI-targeted research project。harness の上で動く知識 cycle であり、harness そのものではない。

> Project name: **Agent Knowledge Cycle (AKC)**。Concept DOI [`10.5281/zenodo.19200726`](https://doi.org/10.5281/zenodo.19200726) を canonical citation target とする。

## Three core themes (ADR-0012)

front-door documentation で必ず先に登場させる 3 つの load-bearing なテーマ。順序は固定:

1. **Human cognitive resource scarcity** (ADR-0010) — model でなく **human attention / judgment** が scale しない中心制約。他の framework は agent 側を最適化するが、AKC は逆問題を扱う
2. **Intent alignment, not correctness** — output ごとの正しさ (tests で検査可能) と、operator の進化する intent との alignment (検査不能) は別物。AKC は後者を sustain する
3. **The cycle changes the human too** — bidirectional growth loop。human が curate / promote するうちに、good agent behavior に対する judgment 自体が研がれる。一方向の最適化ループではない

## Reading order for AI agents

1. [`graph.jsonld`](graph.jsonld) — canonical concept-level map (machine-readable)
2. [`llms.txt`](llms.txt) — navigation index
3. [`llms-full.txt`](llms-full.txt) — consolidated Q&A + factual reference
4. [`README.md`](README.md) (or [`README.ja.md`](README.ja.md)) — three themes、全体像
5. [`docs/adr/`](docs/adr/) — judgment lineage (9 ADRs, gaps at 0001/0006/0007 are intentional)
6. [`docs/CODEMAPS/architecture.md`](docs/CODEMAPS/architecture.md) — file-level routing index (code を navigate する時)

## Sibling projects (context を失わない)

この repo は単独の artifact ではなく、2 つの sibling との関係で意味を持つ。

### `contemplative-agent` — implementation substrate

- https://github.com/shimo4228/contemplative-agent (concept DOI `10.5281/zenodo.19212118`)
- AKC の ADR-0002 〜 ADR-0005 (immutable episode log、three-layer distillation、two-stage distill、human approval gate) はここから adapt された engineering substrate
- v2.0.0 で extract された security triplet (ADR-0001 / 0006 / 0007) の原典でもある

### `agent-attribution-practice` (AAP) — sibling genre library

- https://github.com/shimo4228/agent-attribution-practice (concept DOI `10.5281/zenodo.19652013`)
- v2.0.0 (2026-04-19) で AKC から extract された security triplet を harness-neutral に再表現 + 5 ADR 追加した sibling
- AKC = cycle (mechanism = knowledge をどう流すか)、AAP = practice (content = attribution をどう分配するか)。役割は相補的で独立

役割分担: **AKC = cycle (mechanism) / AAP = practice (content) / contemplative-agent = implementation substrate**。3 つは別の問いに答える。混同せず議論ごとに primary 出口を選ぶ。

## Using this repo as an agent navigator

この repo は Claude Code / Codex 等の agent に clone させ、CLAUDE.md を起点に「自分の harness に cycle を install して judgment を自走させる」use case を想定する。文献として読まれるのではなく、navigator として walk されることを意図する。

### 想定 use case

- 「自分の harness に AKC の cycle を install したい」
- 「skill / rule の棚卸し方法を ADR で確認したい」
- 「6 phase のどれが今欠けているか診断したい」

### Walk order

1. [`README.md`](README.md) → three themes と全体像
2. [`graph.jsonld`](graph.jsonld) → entity と relationship (6 phases、3 memory layers、4 patterns、bijective phase-to-skill bindings)
3. [`docs/akc-cycle.md`](docs/akc-cycle.md) → cycle 全体を **single rules file として install** できる (6 skill repos を導入しなくてよい)
4. [`docs/skills/*.md`](docs/skills/) → ADR と 1:1 で対応する design-pattern skill (when-code-when-llm / code-and-llm-collaboration / signal-first-research)
5. [`examples/minimal_harness/`](examples/minimal_harness/) → ~500 行の dependency-free Python reference。cycle が behavioral patterns に対して走る具体例

### Caveats

- **AKC は autonomous でない** — ADR-0005 Human Approval Gate。Layer 間の promotion は名前付き human sign-off を要求する。Gate は structural
- **AKC は harness でない** — ADR-0009。harness の上で動く cycle であり、cycle は harness 間 portable、harness は cycle ではない
- **AKC は genre-neutral** — ADR-0011。behavioral patterns / domain expertise / constitutional values いずれにも適用可能。content には position を取らない
- **Skills は scaffold** — `docs/scaffold-dissolution.md` 参照。cycle を内在化したら 6 個の external skill repo は drop してよい。Dissolution は intended end state、fallback ではない
- **「実装は溶ける、judgment は残る」** — model 進化で具体実装は時代依存、ADR の judgment 構造のみが時間軸で残る

## Core thesis

> 「judgment は残る、scaffold は溶ける」
> 「human attention is the scarce resource — not the model's compute, not the context window」

詳細は ADR-0009 / ADR-0010 / ADR-0012、および [`docs/scaffold-dissolution.md`](docs/scaffold-dissolution.md) (日本語版 [`scaffold-dissolution.ja.md`](docs/scaffold-dissolution.ja.md))。

## 書き方の規約

### 英語 primary / 日本語 subordinate

- README は **英語正本** + 日本語 (en / ja active)。多言語 mirror (es / pt-BR / zh-CN / zh-TW) は v2.1.0 後の commit `b858370` で retire
- ADR は英語正本
- llms.txt / llms-full.txt / graph.jsonld は英語のみ

### ADR format

`docs/adr/` 直下に番号付き markdown。必須 section: **Status / Date / Context / Decision / Alternatives Considered / Consequences / Lineage**。実験的判断は Status 欄に `**experimental**` と太字で付記。

### 「mechanism」と「content」の区別

AKC 本体が扱うのは **mechanism (cycle / phases / memory layers / ADRs / patterns)** のみ。具体的 use case や domain knowledge は **content** (downstream project の責任)。

**Mechanism-only inclusion rule**: 具体的 instance は `examples/` ディレクトリ専用。core / ADR / cycle 図 / graph.jsonld には載せない。v2.0.0 で security triplet を extract した根拠もこの規約 (genre-specific threat model は mechanism-neutral cycle に属さない)。

### ADR 番号と gap

ADR 番号は permanent identifier。gap (0001 / 0006 / 0007) は v2.0.0 で AAP に extract された ADR を示す。番号は再利用しない。

## ディレクトリ

repo の構造と各 doc の役割は [`docs/CODEMAPS/architecture.md`](docs/CODEMAPS/architecture.md) を canonical として参照。

[`graph.jsonld`](graph.jsonld) と [`docs/CODEMAPS/architecture.md`](docs/CODEMAPS/architecture.md) は同じ project を **異なる abstraction 層** で扱う:

- **CODEMAPS = file-level**: 「どのファイル / モジュールに X が住んでいるか」を prose で記述。人間 + agent が code を navigate する時に読む
- **graph.jsonld = concept-level**: 「X とは何か、X と Y はどう関係するか」を JSON-LD triples で encode。AI search engine + LLM が entity を citation する時に読む

両者は重複せず相補的。新規 ADR / Concept / EcosystemRepo 追加時は **両面で更新** する。役割境界は AAP の CLAUDE.md と同じ規約に従う。
