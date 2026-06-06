Language: [English](README.md) | 日本語

# Agent Knowledge Cycle (AKC)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19200726.svg)](https://doi.org/10.5281/zenodo.19200726)

<details>
<summary>AI 向け推奨読み順</summary>

1. [`graph.jsonld`](graph.jsonld) — 機械可読な関係マップ正本（6 フェーズ、phase-skill bindings、3 メモリ層、code-LLM パターン）
2. [`llms.txt`](llms.txt) — コンパクトなナビゲーション索引
3. [`llms-full.txt`](llms-full.txt) — 統合された事実参照
4. README およびリポジトリ固有 docs — narrative と詳細

shimo4228 全体の研究エコシステムの関係マップは https://github.com/shimo4228/shimo4228/blob/main/graph.jsonld を参照。

</details>

AI エージェントのための知識サイクル — それを形作る人とともに成長する。

## AKC とは何か

AKC は単一の観察から出発する: エージェントの能力が向上するにつれ、希少な資源はもはや計算資源やコンテキストではなく、ループを回している **人間の注意と判断** になる。AKC はその希少性を中心に据えている。[ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md) を参照。

その予算を守るという発想は、サイクルの目的を組み替える。目指すのは「エージェントが個別に正しい出力を出すこと」ではなく、「エージェントの振る舞いがセッションを越えて運用者の意図とアラインし続けること」だ。正しさはテストで確認できるが、アラインは確認できない — 運用者の判断が使い込みのなかで研ぎ澄まされていくにつれ、意図そのものが動くからだ。

したがってアラインは一度の設定ではなく、時間をかけて維持される。**サイクルは人間も変える**: Curate / Promote / Measure を繰り返すうちに、運用者の「良いエージェント挙動とは何か」の判断は、セッションごとに鋭くなっていく — タグライン「それを形作る人 *とともに* (ために、ではなく) 成長する」が指しているのはそのことだ。技術用語で言えば、これはエージェント挙動と人間判断が共に育つ双方向成長ループ (bidirectional growth loop) である。

それを実装するのが、Research → Extract → Curate → Promote → Measure → Maintain という 6 つの合成可能なフェーズだ。このループがなければ、エージェントの知識は劣化していく — スキルは陳腐化し、ルールは互いに矛盾し、ドキュメントはコードから乖離する。各フェーズがどう注意の予算を守るかは、後述の [なぜ AKC か](#なぜ-akc-か) で展開する。

AKC は仕様書・スキーマ・ADR・最小リファレンス実装として出荷される。LLM とアダプタは各自で持ち込む。

## なぜ AKC か

### ボトルネックは移動した

競合するフレームワークはどれもエージェント側を最適化する — より多くのツール、より多くのメモリ、より多くのコンテキスト、より多くの自動化。AKC は逆を問う: ループにいる人間が一日に費やせる注意と判断の予算が固定されているとして、その予算が無駄遣いされないように、サイクルはどう形作られるべきか？

AKC の各フェーズはその希少性のまわりに形作られている。Research は signal-first で、取り込み量が消化量を超えないようにする。Promote は繰り返される判断をルール化し、同じ判断を毎回下し直さないようにする。Measure は手動の再監査を観測可能な遵守チェックに置き換える。実装前の対話を厚くするのは、レビュー段階で意図のずれが発覚したときのコストが、それを防ぐための対話よりも高くつくからだ。サイクルを回すこと自体は無料ではない — しかしそれが、モデルとともにスケールしない唯一の資源を守る方法だ。[ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md) を参照。

| メンテナンス問題 | AKC の応答 |
|------|-----------|
| スキルが陳腐化する | skill-stocktake が品質を定期的に監査 |
| ルールが実態と一致しない | skill-comply が実際の行動遵守率を測定 |
| 知識が散在する | rules-distill が繰り返しパターンを原則へ昇格 |
| ドキュメントがドリフトする | context-sync が役割重複と陳腐化を検出 |
| 車輪が再発明される | search-first が既存解を先に確認 |
| 学びが失われる | learn-eval が品質ゲート付きでパターンを抽出 |

各行は、本来人間が手作業で背負うはずだったメンテナンスタスクをサイクルが置き換えている。サイクルは無料ではないが、同じ監査を毎回やり直すよりは安い。

### 正しさではなく、意図とのアラインを目指す

正しさは自動化できる — テスト、型、リンタ、レビューツールが、出力が特定の基準を満たすかを確認する。アラインメントは同じ程度には自動化できない。意図そのものが、運用者の判断が使い込みのなかで研ぎ澄まされていくにつれ動くからだ。エージェントはあらゆる正しさチェックを満たしながら、意図からは外れ続けることがある。この行動レベルの区別が [intent alignment](https://ai-alignment.com/clarifying-ai-alignment-cec47cd69dd6) (Christiano, 2018) — エージェントが運用者の望むことをしようとすること — であり、AKC はこれを時間軸の上へ、そして行動を形作る artifact の中へと拡張する。

AKC の設計選択はこの区別を反映している。設計原則 #3 (Non-destructive) — 提案して、確認を待つ — は、各変更を意図の言い直しが効くチェックポイントに置く。実装前の対話は、摩擦ではなく **認知経済への投資** として扱われる。この区別はまた、AKC がハーネスエンジニアリングと何が違うのかを説明する: ハーネスは初回の正しさを最適化するが、AKC はその意図が変化していくのに合わせて、ハーネス自体を意図とアラインし続けさせる — この活動を AKC は **harness alignment** と名づける ([ADR-0017](docs/adr/0017-harness-alignment-and-drift.md))。階層比較は [ハーネスエンジニアリングとの関係](#ハーネスエンジニアリングとの関係) を参照。

### サイクルは人間も変える

Curate と Promote を繰り返すことで、ユーザは「残すに値する知識は何か」の判断を鋭くしていく。Research を通じて、既存解を採るか自作するかの直感が磨かれる。Measure を通じて、良いルールと曖昧な願望の違いを学ぶ。AKC はエージェントが孤立して改善する一方向最適化ループではない — エージェントの振る舞いと人間の判断が、持続的な相互作用を通じて共に育つ。タグラインの「それを形作る人とともに成長する」は、まさにこの性質を指している。

## このリポジトリの中身

14 の ADR、9 の設計原則、3 の設計パターンスキル、2 の JSON スキーマ、1 つの約 500 行の実行可能リファレンス実装、そしてサイクル全体を `cp` 一行でインストールできるルールファイル。AKC は 3 つのメモリ層と 4 つのコード–LLM レイヤリングパターンを定義している。以下に挙げる 6 つのサイクルスキルは、各フェーズの「フルスペック版」実装として引き続き提供される。

AKC は **2 種類のスキル** を出荷する:

- **Cycle skills** (外部リポジトリ) — サイクルの各フェーズに 1 つ: `search-first`, `learn-eval`, `skill-stocktake`, `rules-distill`, `skill-comply`, `context-sync`。
- **Design-pattern skills** ([`docs/skills/`](docs/skills/)) — ADR と 1:1 対応する長文の「how」ガイド。横断的で、複数フェーズに適用される。

リポジトリ全体のツリーと document-role routing は [`docs/CODEMAPS/architecture.md`](docs/CODEMAPS/architecture.md) を参照。

## サイクル

AKC はサイクルの各フェーズを担う 6 つの合成可能なスキルで構成される:

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
| Promote | 繰り返し現れるパターンをルール層へ昇格 |
| Measure | 主観ではなく定量的に行動変化を検証 |
| Maintain | ドキュメントの役割を清潔に、内容を新鮮に保つ |

### Skills vs Rules

- **Skills** は各フェーズの深く段階的なワークフローを提供する。ガイド付き実行を望むときに導入する。
- **Rules** は原則とトリガー条件を提供する。サイクルを対話から自然に立ち上がらせたいときに導入する。
- 両者は共存可能。Rules はスキルがトリガーされない場合でもサイクルが回ることを保証する。

## 設計原則

1. **Composable** — 各スキルは独立して動作する。1 つでも 6 つ全部でも使える。
2. **Observable** — skill-comply は主観的評価ではなく定量的遵守率を出す。遵守の測定計器はツール呼び出しだけでなく、エージェントの **推論** — テキストで述べられる verdict や plan — を観測しなければならない。さもないと thinking-centric なフェーズ (Research, Curate) の遵守率が系統的に過小報告される。[ADR-0016](docs/adr/0016-measuring-thinking-centric-phases.md) を参照。
3. **Non-destructive** — 各スキルは変更案を提示して確認を待つ。自動適用はない。
4. **Tool-agnostic in concept** — Claude Code 向けに設計されているが、アーキテクチャは永続設定を持つ任意のエージェントに適用できる。
5. **Evaluation scales with model capability** — 小型モデルにはルーブリック採点が効き、推論モデル (Opus クラス) は完全な文脈と質的判断で評価する。AKC は単一の手法を強制しない — モデルの推論能力に評価の深さを合わせる。
6. **Scaffold dissolution** — スキルは足場である。ユーザとエージェントがサイクルを内在化すると、スキルは不要になり、ルールだけでループは維持される。[docs/scaffold-dissolution.md](docs/scaffold-dissolution.md) を参照。
7. **Code-LLM Layering** — コードは決定性・監査可能性・制御フローを所有する。LLM は意味を所有する。両者を明示的にレイヤリングし、永続状態や終了判定を LLM に持たせない。[ADR-0008](docs/adr/0008-code-and-llm-collaboration.md) を参照。
8. **Human cognitive resource is the bottleneck** — エージェント能力が向上するほど、希少資源は計算資源やコンテキストではなく人間の注意と判断になる。各フェーズはその予算を守るよう形作られている — [なぜ AKC か → ボトルネックは移動した](#ボトルネックは移動した) と [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md) を参照。
9. **Genre neutrality** — サイクルはメカニズムであり、内容ではない。同じ六つのフェーズは agent knowledge の任意の首尾一貫した body — behavioral patterns、domain expertise、constitutional values — に対して動作し、AKC は下流プロジェクトがどれを扱うかについて立場を取らない。ジャンルごとに変わるのは評価基準、プロンプトテンプレート、監査クエリであり、フェーズ自体は不変。[ADR-0011](docs/adr/0011-cycle-applies-to-any-knowledge-body.md) を参照。

## Limitations

3 つめのテーマ — *サイクルは人間も変える* — には正直な双子がいる。判断を鋭くできるループは、判断を鈍らせることもできる。双方向ループを逆向きに回す 3 つのメカニズムレベルの failure mode があり、それらを名指すことでテーマは願望ではなく反証可能なものになる。[ADR-0014](docs/adr/0014-failure-modes-of-the-bidirectional-loop.md) を参照。

- **Gate complacency (ゲートの形骸化)。** エージェントが信頼できるようになるにつれ、たいてい正しい提案の流れが運用者を反射的な承認へと訓練していく。クリックは依然起こるが、その背後の判断は薄まる。これは注意が最も希少なところ (テーマ 1) でこそ最悪になる: デフォルト承認が最も安い行動であり、信頼できるエージェントがその安さを安全に感じさせる。
- **Deskilling (技能の喪失)。** 監督に必要な能力 — 提案されたルールが微妙に間違っていると気づく力 — は行使によって維持される。基礎的な作業をやめてエージェントの出力をレビューするだけになった人間は、その能力を萎縮させ、やがて良い提案ともっともらしい提案の区別がつかなくなる。
- **Delegation-feedback divergence (委任とフィードバックの乖離)。** 成長ループは人間の判断とエージェントの振る舞いが結合し続けることを前提とする。Divergence とは、委任は続くのにその結合が壊れたときに起こる事態だ: エージェントは行動し続けるが、それを正すはずのフィードバックが、それを使える位置にいる人間にもはや届かない。乖離したループも出力は出し続ける — ただ、誰も意味のある舵取りをしていない出力を出すだけだ。

AKC はこれらの failure に対して運用者を免疫化できると主張しない。その防御は訓戒ではなく構造的なものだ。Human Approval Gate ([ADR-0005](docs/adr/0005-human-approval-gate.md)) は遅延ではなく **circuit-breaker (回路遮断器)** である: 「N 日後に自動承認」も「LLM 自身による承認」も経路が存在しないため、ループには divergence を常に止められる地点があり、ゲートの *存在* はループ自身によっては侵食されえない — 人間が注意を払わないことを選んだときだけ侵食される。Curate と Promote は能動的な判断行為であり、サイクルの通常運用そのものが deskilling に抗う行使になっている。これらの limitation は上述のポジティブな framing の正直な双子であり、その撤回ではない。

## ハーネスエンジニアリングとの関係

AKC は [harness engineering](https://mitchellh.com/writing/my-ai-adoption-journey) (Mitchell Hashimoto, 2025) — プロンプト改善 (例: AGENTS.md 更新) とプログラム可能なツール (スクリプト、検証コマンド) の組み合わせで、エージェントが同じ誤りを繰り返さないよう仕組みを作る実践 — と共通の地平を持つ。両者ともエージェントをより信頼できるものにすることを目指すが、焦点が異なる。

| 階層 | 問い | 対応者 |
|------|------|-------|
| Harness | 「この出力は正しいか？」 | 個別のリンタ、テスト、スクリプト |
| AKC | 「ハーネス自体がまだ有効か？」 | skill-comply, skill-stocktake, context-sync |

**Harness optimization vs harness alignment。** ハーネス層には今や独自の自動改善ループがある: [Meta-Harness](https://arxiv.org/abs/2603.28052) はハーネスを「何の情報を保存し、取り出し、モデルに提示するかを決めるコード」と定義し、ベンチマークスコアを最大化するようハーネスのコードを探索する — 自律的・スコア駆動の **harness optimization** (正しさの軸)。AKC の活動はその human-gated な対応物 (意図の軸) だ: **harness alignment** — ハーネスを運用者の進化する意図にアラインし続けること。その failure mode が **harness drift** — スキルが陳腐化し、ルールが実践と一致しなくなり、ドキュメントがコードから乖離する — であり、architectural drift (Perry & Wolf, 1992)、practical drift (Snook, 2000)、agent drift ([arXiv:2601.04170](https://arxiv.org/abs/2601.04170)) の系譜に連なる。2 つの活動は競合ではなく相補的だ: ハーネスは固定ベンチマークでスコアを上げながら、運用者がいま望むものから滑り落ちていくことがありうる。完全な導出は [ADR-0017](docs/adr/0017-harness-alignment-and-drift.md) を参照。

**正しさ vs 意図のアラインメント。** ハーネスエンジニアリングは、一度で正しい結果を得ること — 改善された指示と自動チェックで既知のエラーを防ぐこと — に焦点を合わせる。AKC が気にするのはむしろ別の問いだ: エージェントの振る舞いは運用者の変化していく意図とアラインし続けているか？ 主張の単独な展開は [なぜ AKC か → 正しさではなく、意図とのアラインを目指す](#正しさではなく意図とのアラインを目指す) を参照。

**リアクティブ vs プロアクティブ。** ハーネスエンジニアリングは本質的にリアクティブ — ミスが起こるたびに新しいハーネスを作る。AKC の skill-comply と skill-stocktake はプロアクティブに動き、スキルとルールが実際に従われているか、まだ妥当かを定期的に監査する。設計原則 #5 はこの評価をモデル能力に合わせてスケールさせる — 小型モデルにはルーブリック、フロンティアモデルには包括的判断。

**自律昇格のデフォルト vs 人間所有の昇格。** self-evolving-agent 系の研究、そして過去セッションを自動的に consolidate するプラットフォーム側のメモリ機能における支配的なパターンは、エージェント自身が何を残すかを決めるというものだ — 人間の介在はオプションであり、付け足してもよい guardrail にすぎない。AKC はこれを反転させる: クロスレイヤーの昇格 (確率的な skills/memory 層から決定的な rules 層へパターンを移すこと) には *名前付きの人間 sign-off* を要求する。プラットフォームのメモリ機能は Extract と Curate の取り込みフェーズを自動化するが、その出力はファイルベースのメモリ層に着地するだけで、rules・identity・weights には届かない。AKC のゲートは欠けている自動化機能ではない — それは load-bearing な貢献であり、運用者の変化していく意図がループに入る edge そのものだ。[ADR-0005 addendum](docs/adr/0005-human-approval-gate.md) を参照。

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
  version      = {2.2.0},
  doi          = {10.5281/zenodo.20565806},
  url          = {https://doi.org/10.5281/zenodo.20565806},
  note         = {A knowledge cycle for AI agents — one that grows with the people who shape it}
}
```

あるいは文中で:

> Shimomoto, T. (2026). Agent Knowledge Cycle (AKC). doi:10.5281/zenodo.20565806

## 関連プロジェクト

- [Contemplative Agent](https://github.com/shimo4228/contemplative-agent) —
  ローカル 9B モデル上で Contemplative Constitutional AI を探索する独立研究リポジトリ。
  3 層メモリ、2 段階蒸留といったエンジニアリング基盤は AKC の ADR に
  種を蒔いた先行研究である。詳細は [`docs/inspiration.md`](docs/inspiration.md) を参照。
- [Agent Attribution Practice (AAP)](https://github.com/shimo4228/agent-attribution-practice) —
  姉妹ジャンルライブラリ (DOI [10.5281/zenodo.19652013](https://doi.org/10.5281/zenodo.19652013))。
  AKC v2.0.0 で抽出されたセキュリティ三部作 (ADR-0001, ADR-0006, ADR-0007) が、
  7 つの ADR を追加したうえで AAP の harness-neutral な 10 本の ADR として再表現されている —
  自律 AI エージェントにおけるアカウンタビリティの分配について。
  AKC は cycle (メカニズム)、AAP は practice (content)。
- [Zenn の記事](https://zenn.dev/shimo4228) — 開発日誌 (日本語)
- [Dev.to の記事](https://dev.to/shimo4228) — 英語版

## 謝辞

AKC は [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code) ([@affaan-m](https://github.com/affaan-m)) という基盤の上に立っている。ECC は私が毎日使っていたベースラインハーネスであり、そのスキルとルールは豊かな出発点を与えてくれた。数ヶ月の日常使用の中で、ECC の上に自作のスキルとルールを積み上げていったが、それらは私が追いつけない速さで増殖した — スキルは陳腐化し、ルールは矛盾を始め、ドキュメントはコードから乖離した。散らかりを監査し、何を残すか・何を統合するか・何を永続的なルールへ昇格させるかを判断し続けるしかなかった。6 フェーズのサイクルは、この反復的なメンテナンス作業の形に気づいた結果、その形を名指したものだ。

ECC という立ち場所がなければ AKC は存在しない。affaan-m と ECC のすべてのコントリビュータに深い感謝を。

## References

AKC は理論ではなく実践から作られた — 6 フェーズの形は、文献から導出されたのではなく、実際のハーネスの日々のメンテナンスの中で気づかれたものだ。その epistemic な立場はここでも保持するが、それはプロジェクトが overlap する仕事を名指す義務を免除しない。このセクションは 2 つのことをする: AKC の operation が共有する agent-memory の precedent を concede し、construction 中に本当に参照しなかった哲学的共鳴を挙げる。完全な positioning は [ADR-0013](docs/adr/0013-positioning-within-agent-memory-literature.md) に記録されている。

### Agent-memory 文献 — concede した overlap、locate した delta

AKC の個々の operation は、孤立したメカニズムとしては novel ではない。それぞれが agent-memory / skill-learning 文献に名前付きの precedent を持っており、そうでないふりをすることは false novelty claim になる。正直な手は、各 operation の precedent を名指したうえで、何が新しく、何が新しくないかを述べることだ。

| AKC operation | Named precedent | precedent がやっていること |
|---|---|---|
| Extract → Promote (skill induction) | Voyager (Wang et al., 2023); Agent Workflow Memory (Wang et al., 2024) | trajectory から再利用可能・実行可能な skill/workflow を induce し、それを feed back する |
| Curate (prune / refine memory) | ReMe (Cao et al., 2025); LangMem (LangChain, 2025) | procedural memory を継続的に refine する; 何を保存するか制御する; prompt 更新で挙動を更新する |
| Extract (reflection / distillation) | Generative Agents (Park et al., 2023); MemGPT (Packer et al., 2023) | observation を higher-level な inference へ reflect する; memory hierarchy を page する |
| (framework vocabulary) | CoALA (Sumers et al., 2023); *Externalization in LLM Agents* (Zhou et al., 2026) | modular memory・action space・decision procedure を formalize する; externalization 領域を map する |

孤立した operation として走らせれば — 「このセッションから skill を induce する」「stale な memory を prune する」「これらの episode を pattern へ reflect する」 — AKC のフェーズは *新しい* メカニズムではない; 文献が先に、しばしばより成熟した engineering で到達している。AKC の delta は operation にではなく、それらのシステムが定義する共通の軸 — *エージェントがどう自身の経験を durable で再利用可能な知識に変えるか* — の上にあり、それはまさに 3 つの core theme を literature delta として言い直したものだ:

1. **構造的な human approval gate、prior art が autonomous に回るところで。** Voyager・AWM・ReMe・LangMem は人間を介さずにループを閉じる。AKC の Promote フェーズ ([ADR-0005](docs/adr/0005-human-approval-gate.md)) は、未来の挙動を書き換えるいかなる変更にも名前付きの人間 sign-off を要求し、auto-approve の escape hatch はない。prior art は unattended なループを最適化し、AKC は human-owned なループを最適化する。
2. ***双方向* の human-judgment 成長を target にする、prior art がエージェントやコンテキストを最適化するところで。** それらのシステムは成功をエージェント側で測る; AKC の target ([ADR-0009](docs/adr/0009-akc-is-a-cycle-not-a-harness.md)) は双方向だ — Curate と Promote はエージェントを鋭くすると同時に *人間の* 判断を鋭くする。人間の発達していく判断を最適化すべき output として名指す memory システムは存在しない。
3. **希少資源を *人間の注意* として framing する、prior art がエージェント能力・コンテキスト・情報量を binding と扱うところで。** MemGPT の制約はコンテキストウィンドウ; ReMe と LangMem は memory consistency; Voyager は task capability だ。AKC ([ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md)) は別の天井を名指す — 人間の注意と判断で、エージェント能力が向上するほど *相対的に* 希少になる。文献は情報側の希少性を解き、AKC は注意側の希少性を解く。どちらも valid であり、binding する資源が異なる。

これらのシステムは positioning の *ための* prior art として identify されたものであり、AKC の construction 中に参照されたものではない; この区別は上述の practice-first な立場から保持されている。

### Software-evolution / alignment 文献 — 語彙の系譜

AKC が自身の活動を指す語彙 — **harness alignment** とその failure mode **harness drift** — は、新規の造語ではなく確立された術語から導出されている。各構成要素は参照関係を持ち、AKC の delta はどの単一 source もカバーしないものだけだ: アラインの target が operator intent でありそれ自体が進化すること、human-gated なループであること、ループが人間も変えること。完全な導出は [ADR-0017](docs/adr/0017-harness-alignment-and-drift.md) に記録されている。

| 借用した構成要素 | Source | source が確立していること |
|---|---|---|
| Intent alignment (correctness ≠ alignment) | Christiano (2018), ["Clarifying 'AI alignment'"](https://ai-alignment.com/clarifying-ai-alignment-cec47cd69dd6) | アラインされたエージェントは "is trying to do what H wants it to do" — 動機であって能力ではない |
| 継続的適応; feedback としての進化 | Lehman (1980), ["Programs, Life Cycles, and Laws of Software Evolution"](https://users.ece.utexas.edu/~perry/education/SE-Intro/lehman.pdf), *Proc. IEEE* 68(9) | E-type プログラムは "undergoes continual change or becomes progressively less useful" (Law I); 進化はソフトウェアに内在する feedback 駆動の性質 |
| 鈍感さによる乖離としての drift | Perry & Wolf (1992), ["Foundations for the Study of Software Architecture"](https://users.ece.utexas.edu/~perry/work/papers/swa-sen.pdf), *ACM SIGSOFT SEN* 17(4) | "Architectural drift is due to insensitivity about the architecture" — 破局ではなく適応不能を招く |
| 成文化されたルールからの実践の drift | Snook (2000), *Friendly Fire*, Princeton UP | Practical drift: 実践が成文化された手順から緩やかに uncouple していくこと (二次文献での特徴づけ) |
| Harness; harness optimization | Lee et al., [Meta-Harness](https://arxiv.org/abs/2603.28052) (arXiv:2603.28052) | ハーネスは「何の情報を保存し、取り出し、モデルに提示するかを決めるコード」であり、ベンチマークスコアに対して自律的に改善される |
| LLM agent における行動 drift | Rath, [Agent Drift](https://arxiv.org/abs/2601.04170) (arXiv:2601.04170) | Semantic drift = "progressive deviation from original intent" — 2026 年に古典 SE 系譜を引かずに再導出された |

上の agent-memory 表と異なり、これらの source は *語彙の導出そのもののために* 参照された (2026-06-06)。引用文は一次テキストに対して照合済み — Snook を除く (二次文献での特徴づけとして引用)。

### 哲学的共鳴 — construction 中に参照していない

以下の著作は上述のプロセスで本当に参照されたものではないが、結果として生まれたサイクルはそれらのアイデアと何かを共有しているように見える。その共鳴に興味を持つ読者のためにここに挙げておく。

- [Mind in Life](https://www.hup.harvard.edu/books/9780674057517) (Evan Thompson, 2007) —
  人間とエージェントの双方向ループは、エナクティビズムの構造的カップリングという
  考えと何か通じるものを持っている。
- [A Beautiful Loop: An Active Inference Theory of Consciousness](https://www.sciencedirect.com/science/article/pii/S0149763425002970)
  (Laukkonen, Friston, & Chandaria, 2025) — エージェントが実際に何をするかを観察して
  人間がルールやスキルを更新していく様子は、ぼんやりと再帰的自己モデリングループに
  似ている気がする。

## License

MIT
