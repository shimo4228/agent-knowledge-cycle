Language: [English](README.md) | 日本語

# Agent Knowledge Cycle (AKC)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19200727.svg)](https://doi.org/10.5281/zenodo.19200727)

AI エージェントのための知識サイクル — それを形作る人とともに成長する。

## AKC とは何か

AKC はエージェントの知識を **生きた資産** として扱う。エピソードは不変ログとして記録され、パターンへと蒸留され、ルールへと昇格し、継続的に監査される。Research → Extract → Curate → Promote → Measure → Maintain という 6 つの合成可能なフェーズがスキル・ルール・ドキュメントを現実と整合させ続ける。メンテナンスループがなければエージェントの知識は劣化する — スキルは陳腐化し、ルールは互いに矛盾し、ドキュメントはコードから乖離する。

これは一方向の最適化ループではない — サイクルは人間側も変えていく。下の [なぜサイクルなのか？](#なぜサイクルなのか) を参照。

AKC は仕様書・スキーマ・ADR・最小リファレンス実装として出荷される。LLM とアダプタは各自で持ち込む。

## このリポジトリの中身

```
agent-knowledge-cycle/
├── docs/
│   ├── akc-cycle.md              # 行動ルール — サイクル全体を 1 ファイルに
│   ├── scaffold-dissolution.md   # スキルは足場である — その溶解の仕方
│   ├── inspiration.md            # 先行研究
│   ├── adr/
│   │   ├── 0002-immutable-episode-log.md         # JSONL, append-only, umask 0600
│   │   ├── 0003-three-layer-distillation.md      # Raw → Knowledge → Identity/Rules
│   │   ├── 0004-two-stage-distill-pipeline.md    # 自由記述 → 構造化フォーマット
│   │   ├── 0005-human-approval-gate.md           # ルール昇格の自動化は禁止
│   │   ├── 0008-code-and-llm-collaboration.md    # コードが制御、LLM が意味
│   │   ├── 0009-akc-is-a-cycle-not-a-harness.md  # サイクルこそが唯一の定義特性
│   │   ├── 0010-human-cognitive-resource-as-central-constraint.md  # Signal-first Research と認知経済
│   │   └── 0011-cycle-applies-to-any-knowledge-body.md  # サイクルは流れる知識のジャンルに対して中立
│   └── skills/                   # ADR と 1:1 対応する設計パターンスキル
│       ├── when-code-when-llm.md                 # タスク単位: 構造 vs 意味
│       ├── code-and-llm-collaboration.md         # パイプライン単位: 4 つのレイヤリングパターン
│       └── signal-first-research.md              # ADR-0010 の intake フィルタ設計
├── schemas/
│   ├── episode-log.schema.json   # Layer 1 レコード形
│   └── knowledge.schema.json     # Layer 2 パターン形
└── examples/
    ├── minimal_harness/          # メカニズム demo — 行動パターンに対するサイクル
    │   ├── episode_log.py        # Layer 1
    │   ├── knowledge_store.py    # Layer 2 + 時間減衰 + 禁止文字列検証
    │   ├── distill.py            # 2 段階パイプライン、LLM 非依存
    │   └── demo.py               # python3 -m examples.minimal_harness.demo
    └── constitution_amend/       # downstream 参照 — 憲法的価値に対するサイクル
        └── README.md             # AKC フェーズを contemplative-agent の amend ワークフローにマップ
```

8 の ADR、8 の設計原則、3 の設計パターンスキル、2 の JSON スキーマ、1 つの約 300 行の実行可能リファレンス実装、そしてサイクル全体を `cp` 一行でインストールできるルールファイル。AKC は 3 つのメモリ層と 4 つのコード–LLM レイヤリングパターンを定義している。以下に挙げる 6 つのサイクルスキルは、各フェーズの「フルスペック版」実装として引き続き提供される。

AKC は **2 種類のスキル** を出荷する:

- **Cycle skills** (外部リポジトリ) — 自己改善ループの各フェーズに 1 つ: `search-first`, `learn-eval`, `skill-stocktake`, `rules-distill`, `skill-comply`, `context-sync`。
- **Design-pattern skills** ([`docs/skills/`](docs/skills/)) — ADR と 1:1 対応する長文の「how」ガイド。横断的で、複数フェーズに適用される。

## サイクル

AKC は閉じた自己改善ループを形成する 6 つの合成可能なスキルで構成される:

```
Experience → learn-eval → skill-stocktake → rules-distill → Behavior change → ...
               (extract)    (curate)          (promote)            ↑
                                                            skill-comply
                                                              (measure)
                                              context-sync ← (maintain)
```

各スキルは知識ライフサイクルの 1 フェーズを担う:

| Skill | Phase | 役割 |
|-------|-------|------|
| [search-first](https://github.com/shimo4228/claude-skill-search-first) | Research | 広く探索し、信号で絞り込む — 次の行動を変える情報のみを取り込む |
| [learn-eval](https://github.com/shimo4228/claude-skill-learn-eval) | Extract | セッションから再利用可能なパターンを品質ゲート付きで抽出 |
| [skill-stocktake](https://github.com/shimo4228/claude-skill-stocktake) | Curate | インストール済みスキルの陳腐化・矛盾・冗長性を監査 |
| [rules-distill](https://github.com/shimo4228/claude-skill-rules-distill) | Promote | スキルから横断原則を蒸留してルール化 |
| [skill-comply](https://github.com/shimo4228/claude-skill-comply) | Measure | エージェントが実際にスキルとルールに従っているかをテスト |
| [context-sync](https://github.com/shimo4228/claude-skill-context-sync) | Maintain | ドキュメントの役割重複・陳腐化・決定記録の欠落を監査 |

## Rules — スキルなしでサイクルを導入する

サイクルを回すのに 6 つのスキルすべては不要。[`docs/akc-cycle.md`](docs/akc-cycle.md) は 6 フェーズを、自然な対話を通じて任意の AI エージェントが従える行動原則に蒸留したものだ。

### クイックインストール

```bash
# エージェントのルールディレクトリにコピー
cp docs/akc-cycle.md ~/.claude/rules/common/akc-cycle.md
```

これだけ。サイクルは対話を通じて回る — スキルもプラグインも CLI ツールも不要。

### ルールがカバーする内容

| Phase | ルール要約 |
|-------|-----------|
| Research | 広く探索し、信号で絞り込む — 次の行動を変える情報のみを取り込む |
| Extract | セッションから再利用可能なパターンを品質評価付きで捕捉 |
| Curate | 冗長性・陳腐化・沈黙を定期監査 |
| Promote | 3 回以上繰り返されるパターンをルール層へ昇格 |
| Measure | 主観ではなく定量的に行動変化を検証 |
| Maintain | ドキュメントの役割を清潔に、内容を新鮮に保つ |

### Skills vs Rules

- **Skills** は各フェーズの深く段階的なワークフローを提供する。ガイド付き実行を望むときに導入する。
- **Rules** は原則とトリガー条件を提供する。サイクルを対話から自然に立ち上がらせたいときに導入する。
- 両者は共存可能。Rules はスキルがトリガーされない場合でもサイクルが回ることを保証する。

## なぜサイクルなのか

静的な設定は必ずドリフトする。スキルは追加されるが見直されない。ルールは蓄積されるが遵守は測定されない。ドキュメントは陳腐化する。

AKC はエージェントの知識を、継続的なメンテナンスを必要とする生きたシステムとして扱う — 一度きりのセットアップではなく。

| 問題 | AKC の応答 |
|------|-----------|
| スキルが陳腐化する | skill-stocktake が品質を定期的に監査 |
| ルールが実態と一致しない | skill-comply が実際の行動遵守率を測定 |
| 知識が散在する | rules-distill が繰り返しパターンを原則へ昇格 |
| ドキュメントがドリフトする | context-sync が役割重複と陳腐化を検出 |
| 車輪が再発明される | search-first が既存解を先に確認 |
| 学びが失われる | learn-eval が品質ゲート付きでパターンを抽出 |

サイクルは人間側も変える。Curate と Promote を繰り返すことで、ユーザは「残すに値する知識は何か」の判断を鋭くしていく。Research を通じて、既存解を採るか自作するかの直感が磨かれる。Measure を通じて、良いルールと曖昧な願望の違いを学ぶ。AKC はエージェントが孤立して改善する一方向最適化ループではない — 人間とエージェントが持続的な相互作用を通じて共に発達する双方向成長ループだ。

### サイクルは誰の認知予算を守っているのか

人間のそれだ。エージェント能力が向上するほど、希少資源は計算資源やコンテキストではなく **人間の注意と判断** に移っていく。AKC の各フェーズはその希少性の周りに形作られている: Research は signal-first で、取り込み量が消化量を超えないようにする。Promote は繰り返される判断をルール化し、同じ判断を毎回下し直さないようにする。Measure は手動の再監査を観測可能な遵守チェックに置き換える。そして実装前の対話を厚くするのは、レビュー段階で意図のずれが発覚したときのコストが、それを防ぐための対話よりも高くつくからだ。サイクルを回すこと自体は無料ではない — しかしそれが、モデルとともにスケールしない唯一の資源を守る方法だ。[ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md) を参照。

## 設計原則

1. **Composable** — 各スキルは独立して動作する。1 つでも 6 つ全部でも使える。
2. **Observable** — skill-comply は主観的評価ではなく定量的遵守率を出す。
3. **Non-destructive** — 各スキルは変更案を提示して確認を待つ。自動適用はない。
4. **Tool-agnostic in concept** — Claude Code 向けに設計されているが、アーキテクチャは永続設定を持つ任意のエージェントに適用できる。
5. **Evaluation scales with model capability** — 小型モデルにはルーブリック採点が効き、推論モデル (Opus クラス) は完全な文脈と質的判断で評価する。AKC は単一の手法を強制しない — モデルの推論能力に評価の深さを合わせる。
6. **Scaffold dissolution** — スキルは足場である。ユーザとエージェントがサイクルを内在化すると、スキルは不要になり、ルールだけでループは維持される。[docs/scaffold-dissolution.md](docs/scaffold-dissolution.md) を参照。
7. **Code-LLM Layering** — コードは決定性・監査可能性・制御フローを所有する。LLM は意味を所有する。両者を明示的にレイヤリングし、永続状態や終了判定を LLM に持たせない。[ADR-0008](docs/adr/0008-code-and-llm-collaboration.md) を参照。
8. **Human cognitive resource is the bottleneck** — エージェント能力が向上するほど、希少資源は計算資源やコンテキストではなく人間の注意と判断になる。各フェーズはその予算を守るよう形作られている: Research の signal-first 取り込み、同じ判断を下し直さないためのルール昇格、人間が毎回再監査しないための遵守測定、ずれた実装はそれを防いだ対話より高くつくための対話先行。[ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md) を参照。

## ハーネスエンジニアリングとの関係

AKC は [harness engineering](https://mitchellh.com/writing/my-ai-adoption-journey) (Mitchell Hashimoto, 2025) — プロンプト改善 (例: AGENTS.md 更新) とプログラム可能なツール (スクリプト、検証コマンド) の組み合わせで、エージェントが同じ誤りを繰り返さないよう仕組みを作る実践 — と共通の地平を持つ。両者ともエージェントをより信頼できるものにすることを目指すが、焦点が異なる。

| 階層 | 問い | 対応者 |
|------|------|-------|
| Harness | 「この出力は正しいか？」 | 個別のリンタ、テスト、スクリプト |
| AKC | 「ハーネス自体がまだ有効か？」 | skill-comply, skill-stocktake, context-sync |

**正しさ vs 意図のアラインメント。** ハーネスエンジニアリングは、一度で正しい結果を得ること — 改善された指示と自動チェックで既知のエラーを防ぐこと — に焦点を合わせる。AKC はむしろ別の問いを気にする: 「これは所有者の意図とアラインしているか？」 エージェントは既知のミスをすべて避けても、設計意図からはずれ続けることがある。設計原則 #3 (Non-destructive) はこれを反映している — 提案してから確認を待つ。意図のアラインメントは完全に自動化しがたいからだ。

**リアクティブ vs プロアクティブ。** ハーネスエンジニアリングは本質的にリアクティブ — ミスが起こるたびに新しいハーネスを作る。AKC の skill-comply と skill-stocktake はプロアクティブに動き、スキルとルールが実際に従われているか、まだ妥当かを定期的に監査する。設計原則 #5 はこの評価をモデル能力に合わせてスケールさせる — 小型モデルにはルーブリック、フロンティアモデルには包括的判断。

## カスタマイズ

上記のリファレンス実装は出発点だ。フォークし、書き換え、自身のエージェントとワークフローに合わせて適応させてほしい。AKC が定義するのはサイクルであって、実装ではない。重要なのは各フェーズ (extract → curate → promote → measure → maintain) が閉じたループを形成していることであり、各フェーズをどう作るかではない。

## 出自

このアーキテクチャは 2026 年 2 月に Tatsuya Shimomoto ([@shimo4228](https://github.com/shimo4228)) によって最初に提案・実装された。

最初の 5 つのスキルは 2026 年 2 月から 3 月にかけて [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code) に貢献された。context-sync は独立して開発された。

## 引用方法

Agent Knowledge Cycle アーキテクチャを利用・参照する場合は、以下のように引用してほしい:

```bibtex
@software{shimomoto2026akc,
  author       = {Shimomoto, Tatsuya},
  title        = {Agent Knowledge Cycle (AKC)},
  year         = {2026},
  doi          = {10.5281/zenodo.19200727},
  url          = {https://doi.org/10.5281/zenodo.19200727},
  note         = {A knowledge cycle for AI agents — one that grows with the people who shape it}
}
```

あるいは文中で:

> Shimomoto, T. (2026). Agent Knowledge Cycle (AKC). doi:10.5281/zenodo.19200727

## 関連プロジェクト

- [Contemplative Agent](https://github.com/shimo4228/contemplative-agent) —
  ローカル 9B モデル上で Contemplative Constitutional AI を探索する独立研究リポジトリ。
  3 層メモリ、2 段階蒸留といったエンジニアリング基盤は AKC の ADR に
  種を蒔いた先行研究である。詳細は [`docs/inspiration.md`](docs/inspiration.md) を参照。
- [Zenn の記事](https://zenn.dev/shimo4228) — 開発日誌 (日本語)
- [Dev.to の記事](https://dev.to/shimo4228) — 英語版

## 謝辞

AKC は [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code) ([@affaan-m](https://github.com/affaan-m)) という基盤の上に立っている。ECC は私が毎日使っていたベースラインハーネスであり、そのスキルとルールは豊かな出発点を与えてくれた。数ヶ月の日常使用の中で、ECC の上に自作のスキルとルールを積み上げていったが、それらは私が追いつけない速さで増殖した — スキルは陳腐化し、ルールは矛盾を始め、ドキュメントはコードから乖離した。散らかりを監査し、何を残すか・何を統合するか・何を永続的なルールへ昇格させるかを判断し続けるしかなかった。6 フェーズのサイクルは、この反復的なメンテナンス作業の形に気づいた結果、その形を名指したものだ。

ECC という立ち場所がなければ AKC は存在しない。affaan-m と ECC のすべてのコントリビュータに深い感謝を。

## References

AKC は理論ではなく実践から作られた。以下の著作は上述のプロセスで参照されたものではないが、結果として生まれたサイクルはそれらのアイデアと何かを共有しているように見える。その共鳴に興味を持つ読者のためにここに挙げておく。

- [Mind in Life](https://www.hup.harvard.edu/books/9780674057517) (Evan Thompson, 2007) —
  人間とエージェントの双方向ループは、エナクティビズムの構造的カップリングという
  考えと何か通じるものを持っている。
- [A Beautiful Loop: An Active Inference Theory of Consciousness](https://www.sciencedirect.com/science/article/pii/S0149763425002970)
  (Laukkonen, Friston, & Chandaria, 2025) — エージェントが実際に何をするかを観察して
  人間がルールやスキルを更新していく様子は、ぼんやりと再帰的自己モデリングループに
  似ている気がする。

## License

MIT
