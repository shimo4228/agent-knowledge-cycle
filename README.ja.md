Language: [English](README.md) | 日本語

# Agent Knowledge Cycle (AKC)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19200726.svg)](https://doi.org/10.5281/zenodo.19200726)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/shimo4228/agent-knowledge-cycle)

**AI エージェントのための知識サイクル — エージェントの振る舞いは積み上がり、人間の判断は研がれる。**

Agent Knowledge Cycle (AKC) は、永続的な AI エージェントのための 6 フェーズ
の成長サイクルです。反復されるエージェント経験を、再利用可能な知識 —
スキル・ルール・ドキュメント — へ人間の承認の下で変換し、希少資源である
**人間の注意と判断**を本当に必要な場所にだけ使いながら、エージェントを
運用者の変化し続ける意図（intent）にアラインさせ続けます。サイクルは人間も
変えます: 回すことで、それを舵取りする判断力自体が研がれていきます。coding
agent や永続的 AI harness を日常的に運用する人のために作られており、
Claude Code をはじめ同等の harness の上で動きます。

関連論文: *Harness Alignment and Harness Drift: Why Intent, Unlike
Correctness, Resists Automation* — doi:[10.5281/zenodo.20578272](https://doi.org/10.5281/zenodo.20578272)

**まず試すなら**: 単独リポジトリ
[akc-cycle のルールファイル](https://github.com/shimo4228/akc-cycle)を `cp`
1 回コピーするだけで、任意の AI エージェントに 6 フェーズの振る舞いが入ります —
詳細は[サイクルを導入する](#サイクルを導入する)へ。

## なぜ AKC か

**ボトルネックは移動しました。** 多くの agent framework はエージェント側を
最適化します — より多くのツール、メモリ、コンテキスト、自動化。AKC は逆の
制約から出発します: エージェント能力が伸びるほど、希少資源はループを
舵取りするための人間の注意と判断になります
([ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md))。
スキルは陳腐化し、ルールは常駐コストを溜め込み、ドキュメントはドリフトします
— サイクルの各フェーズは、その maintenance が運用者の固定予算を食い潰さ
ないために存在します。

**正しさだけでなく、意図とのアライン。** テストやリンタは、ある出力が仕様を
満たすかを確認できます。しかし、変わり続ける harness が運用者の意図に今も
沿っているかまでは確認できません — 使い込みのなかで判断が研がれるにつれて、
意図そのものが動くからです。AKC はこの configuration layer での活動を
**harness alignment** と呼び、その failure mode を **harness drift** と
呼びます。導出は [ADR-0017](docs/adr/0017-harness-alignment-and-drift.md) と
関連論文にあります。

**サイクルは人間も変えます。** Curate と Promote は、どの知識を残すべきかを
運用者に判断させます。Measure は、その判断が実際に振る舞いを変えたかを検査
します。時間が経つにつれ、エージェントはより一貫し、人間はその一貫性を判断
する力を上げていきます — エージェントの振る舞いは積み上がり、人間の判断は
研がれます。

## サイクル

AKC は経験を 6 つのフェーズで durable behavior に変換します。Research が
intake を絞り、Extract が再利用可能パターンを捕捉し、Curate が蓄積物を
監査し、Promote が選ばれたパターンを振る舞いを形成するルールへ移し、
Measure が振る舞いの変化を検査し、Maintain がドキュメントと artifact を
整合させます。

```mermaid
flowchart TD
  E[Experience] --> R[Research<br/>signal-first intake]
  R --> X[Extract<br/>reusable pattern]
  X --> C[Curate<br/>structural + semantic audit]
  C --> P[Promote<br/>human-gated rule or skill change]
  P --> M[Measure<br/>observable behavior]
  M --> T[Maintain<br/>docs and artifact hygiene]
  T --> E
```

| Phase | 現在の外部スキル | 目的 |
|---|---|---|
| Research | [search-first](https://github.com/shimo4228/search-first) | 広く探索し、次の行動を変える signal だけを取り込む |
| Extract | [learn-eval](https://github.com/shimo4228/learn-eval) | セッションの再利用可能パターンを品質ゲート付きで抽出する |
| Curate | [skill-health](https://github.com/shimo4228/skill-health) + [skill-stocktake](https://github.com/shimo4228/skill-stocktake) + [rules-stocktake](https://github.com/shimo4228/rules-stocktake) + [agent-stocktake](https://github.com/shimo4228/agent-stocktake) | 構造的負債の検査の後に、スキル・常駐ルール・agent 定義を意味的にレビューする |
| Promote | [rules-distill](https://github.com/shimo4228/rules-distill) | 反復パターンを durable rule に変換する |
| Measure | [skill-comply](https://github.com/shimo4228/skill-comply) | エージェントが実際にスキルとルールに従うかをテストする |
| Maintain | [context-sync](https://github.com/shimo4228/context-sync) + [repo-asset-stocktake](https://github.com/shimo4228/repo-asset-stocktake) | 文書役割を清潔にし、consumer が消えた非コード資産を監査する |

3 つの design-pattern skills —
[when-code-when-llm](https://github.com/shimo4228/when-code-when-llm),
[code-and-llm-collaboration](https://github.com/shimo4228/code-and-llm-collaboration),
[signal-first-research](https://github.com/shimo4228/signal-first-research) —
がサイクルの再利用可能な設計判断を担います。さらに 2 つの repo は、phase
ではなくサイクルが依拠する概念を scaffold しています。
[human-gate](https://github.com/shimo4228/human-gate) は、**人間承認ゲート**
（振る舞いを形成するすべての変更が通る確認点 —
[ADR-0005](docs/adr/0005-human-approval-gate.md)）で人間に何を見せるかを
固定します: 将来の振る舞いを形成する変更（何をもって合格とするかを決める
テストや検査を含む）は本文を、通常の実装コードは短い固定形式の意図の要約を
見せます。[generation-audit](https://github.com/shimo4228/generation-audit)
は、新しいモデル世代が出たときにルールとスキルを再監査します — 旧世代の
弱いモデルに合わせて書いた足場が、摩擦に転じる時点です。これは **Scaffold
Dissolution**（スキルは足場であり、サイクルが内在化されたら溶けることを
意図している、という原則 —
[docs/scaffold-dissolution.md](docs/scaffold-dissolution.md)）を実行可能な
検査にしたものです。

フェーズ集合と phase-to-skill binding は、それ自体が可変なスナップショット
であり、AKC の固定された本質ではありません
([ADR-0019](docs/adr/0019-cycle-structure-is-provisional.md))。

## サイクルを導入する

最も軽い導入経路は、単独リポジトリ
[**shimo4228/akc-cycle**](https://github.com/shimo4228/akc-cycle) のルール
ファイルです。フェーズ別スキルを入れなくても、AI エージェントに 6
フェーズの振る舞いを渡せます:

```bash
# github.com/shimo4228/akc-cycle のクローンから、ルールを
# エージェントのルールディレクトリにコピーする。
cp rules/common/akc-cycle.md ~/.claude/rules/common/akc-cycle.md
```

導入は段階的で構いません。ルールファイルだけで、通常の対話の中からサイクルが
自然に立ち上がります。特定フェーズの段階的な実行ガイドが必要になったら、上の
phase skills を追加してください。どれも fork して構いません — AKC が定義する
のは実装ではなくサイクルです。スキルは足場であり、サイクルが内在化されたら
溶けることを意図しています（Scaffold Dissolution,
[docs/scaffold-dissolution.md](docs/scaffold-dissolution.md)）。

## このリポジトリの中身

| 領域 | 内容 |
|---|---|
| 決定記録 | [`docs/adr/`](docs/adr/) の ADR カタログ。0001, 0006, 0007 は v2.0.0 extraction 由来の恒久 gap（その内容は sibling repo の Agent Attribution Practice に移管済み） |
| AI navigation | [`graph.jsonld`](graph.jsonld) が concept map、[`llms.txt`](llms.txt) が routing、[`llms-full.txt`](llms-full.txt) が自己完結した事実参照（設計原則の一覧を含む） |
| 仕様 | [`schemas/episode-log.schema.json`](schemas/episode-log.schema.json), [`schemas/knowledge.schema.json`](schemas/knowledge.schema.json) |
| リファレンス実装 | [`examples/minimal_harness/`](examples/minimal_harness/): 3 メモリ層と 2 段階 distill pipeline の dependency-free Python demo |
| routing map | [`docs/CODEMAPS/architecture.md`](docs/CODEMAPS/architecture.md): canonical file-level navigation index |

## Limitations

双方向ループは人間側にも失敗しえます —
[ADR-0014](docs/adr/0014-failure-modes-of-the-bidirectional-loop.md) は
**gate complacency**（承認が時とともに形骸化する）、**deskilling**（運用者
自身の判断力が衰える）、**delegation-feedback divergence**（委譲は増えるのに
結果を読む量は減っていく）を名づけています — そして artifact 側の失敗が
harness drift です。両者は複合しうるため、AKC は maintenance を一度限りの
設定ではなく cycle として扱います。AKC はこれらのリスクを明示し、人間承認
ゲートを構造的な防御として残します。リスクを消せるとは主張しません。

## 位置づけ

Harness engineering は、出力が初回で正しくなるように scaffold を改善します。
AKC は、運用者の意図が変化するなかで scaffold をその意図にアラインさせ
続けます ([ADR-0009](docs/adr/0009-akc-is-a-cycle-not-a-harness.md),
[ADR-0017](docs/adr/0017-harness-alignment-and-drift.md))。AKC の個別操作は
Voyager, Agent Workflow Memory, ReMe, MemGPT などの先行 agent-memory 研究
と重なります。差分は loop ownership — 構造的な人間承認ゲート
([ADR-0005](docs/adr/0005-human-approval-gate.md))、双方向の判断力の成長、
attention 側の希少性 — にあります。完全な引用経路は
[ADR-0013](docs/adr/0013-positioning-within-agent-memory-literature.md),
ADR-0017, [`llms-full.txt`](llms-full.txt) にあります。

## 出自と謝辞

このアーキテクチャは 2026 年 2 月に Tatsuya Shimomoto
([@shimo4228](https://github.com/shimo4228), ORCID
[0009-0002-6168-4162](https://orcid.org/0009-0002-6168-4162)) によって最初に
提案・実装されました。土台は [@affaan-m](https://github.com/affaan-m) による
[Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code)
— 日常運用の baseline harness — です。そこに著者自身が追加したスキルと
ルールが増え、陳腐化したスキル、矛盾するルール、ドリフトするドキュメントが
それ自体の maintenance problem になったときに、AKC が生まれました。最初の
5 つの cycle skills は 2026 年 2 月から 3 月にかけて ECC に貢献されました。
`context-sync` は独立に開発されたものです。

## 引用方法

AKC は 2 つの DOI を持ちます。Concept DOI
[10.5281/zenodo.19200726](https://doi.org/10.5281/zenodo.19200726)（badge が
使用）は常に最新版に解決され、各 archived release は個別の DOI を持ちます —
引用には下の release DOI を使ってください。

AKC を利用・参照する場合は、[`CITATION.cff`](CITATION.cff) の archived
release metadata を引用してください。同じメタデータは
[`codemeta.json`](codemeta.json) としても提供しています:

```bibtex
@software{shimomoto2026akc,
  author       = {Shimomoto, Tatsuya},
  title        = {Agent Knowledge Cycle (AKC)},
  year         = {2026},
  version      = {2.6.0},
  doi          = {10.5281/zenodo.21644565},
  url          = {https://doi.org/10.5281/zenodo.21644565},
  note         = {A knowledge cycle for AI agents -- agent behavior compounds, human judgment sharpens}
}
```

文中では: Shimomoto, T. (2026). *Agent Knowledge Cycle (AKC)*.
doi:[10.5281/zenodo.21644565](https://doi.org/10.5281/zenodo.21644565).

## 関連プロジェクト

研究エコシステムの hub は
[`shimo4228/shimo4228`](https://github.com/shimo4228/shimo4228) です。より
広い研究ライン群の canonical relationship map を持ちます。

| Repository | AKC との関係 |
|---|---|
| [Contemplative Agent](https://github.com/shimo4228/contemplative-agent) | AKC 初期 ADR の upstream engineering substrate であり、6 フェーズ cycle の downstream operational re-implementation |
| [Agent Attribution Practice](https://github.com/shimo4228/agent-attribution-practice) | ジャンル違いの sibling library。AKC はサイクル（mechanism）を、AAP は attribution の実践（content）を定義する |
| [Authorship Strategy](https://github.com/shimo4228/authorship-strategy) | 同じ日常運用から結晶化した独立の DOI 付き研究ライン。output が operator-agent pair の外へどう拡散するかを扱う |
| [Attention, Not Self](https://github.com/shimo4228/attention-not-self) | sibling 研究ライン。共有 hub repo 経由で相互リンクされ、この repo には統合しない |
| [doctrine-corpus](https://github.com/shimo4228/doctrine-corpus) | AKC を source line の 1 つに含む bilingual judgment-eliciting Q&A corpus |
| [existence-proof](https://github.com/shimo4228/existence-proof) | Authorship Strategy を補完する作業リポジトリ。独立の研究ラインにはまだ結晶化していない |

日本語の開発ノートは [Zenn](https://zenn.dev/shimo4228)、英訳は
[Dev.to](https://dev.to/shimo4228) にあります。

## License

MIT
