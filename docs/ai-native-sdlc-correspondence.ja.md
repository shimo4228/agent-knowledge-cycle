# AKC と AI-Native SDLC Playbook

**As of 2026-08-25.** Anthropic は 2026-08-21 に *The AI-Native SDLC Playbook* を公開した。
本書は 2026-08-24 時点のアーカイブ版
（[archived copy](https://web.archive.org/web/20260824134825/https://claude.com/blog/the-ai-native-sdlc-playbook)、
2026-08-25 に live ページと記事本文が同一であることを照合済み）に対して書かれている。
playbook は予告なく live URL 上で改版されうるベンダー文書であり、以下で「playbook」に
ついて述べる主張はすべてその日付つきテキストへの主張であって、読者が読む時点の掲載内容への
主張ではない。

## 2 つのループ — 1 枚の対応表ではない

playbook は 6 つの stage — Plan, Design, Build, Test, Deploy, Maintain — を回す。
AKC は 6 つの phase — Research, Extract, Curate, Promote, Measure, Maintain — を回す。
数が一致するのは偶然であり、stage↔phase の対応表として読むと意味をなさない。
両者は**異なる対象を運ぶ異なるループ**である。

playbook のループ — 本書ではこれを **product loop** と呼ぶ。呼称は本書のもので、ループは
playbook のものだ — は、ソフトウェア変更を intent から production まで運び、また戻す。
各 stage は次の stage が読む artifact — intent、spec、plan、diff とそのテスト、PR とその
指摘、incident の記録 — を commit して終わり、production で control band が破られると
次の intent が書かれてループが再始動する。運ばれる対象はプロダクトへの変更である。

AKC のループ — 本書ではこれを **harness loop** と呼ぶ。AKC 自身の語彙では knowledge
cycle — は、経験を、将来の振る舞いを形づくる耐久的な知識（skill・rule・ドキュメント）へ、
人間の承認の下で変える。運ばれる対象は agent を操る構成であって、agent が出荷する
プロダクトではない。このループを回し続けることが harness alignment を保ち、回さなければ
同じ構成が drift する（ADR-0017）。

2 つのループは並行ではなく結合しており、結合には向きがある。product loop が 1 周する
ことが、harness loop の Research と Extract が消費する経験 — agent が 2 度した誤り、
eval の無かった incident、繰り返し出るレビュー指摘 — を生む。product loop を回せば、
置き場所があろうとなかろうと harness loop への入力は生まれる。

playbook は第二のループを含んでいる。Stage 3 では CLAUDE.md へ書き込まれる訂正と
skill として version 管理される組織知として、Stage 4 では agent 構成が変わるたびに走り、
モデルの向上で判別力を失う case を足し続けねばならない eval suite として、Stage 5 では
review policy への月次チューニングと、譲れない hook の managed settings への移動として、
Stage 6 では却下された指摘による detection band の調整として現れる。playbook は
ある一層についてこの原則を明言する: agent 構成は agent を操るのだから
「コードが受けるのと同じ回帰テストに値する」（"deserves the regression testing that
code gets"）。

playbook がしていないのは、この第二のループを**ループとして名指す**ことだ。第二のループは
自前の phase を持たず、それを表面化させた stage と別の所有者を持たず、自前の stage を
持たず、ループ全体が所有する cadence も持たない — 存在するスケジュール（月次チューニング、
夜間の eval 実行）は個々の play に属する。それは 4 つの stage に分配された良い習慣の
集まりであり、各々はそれを露呈させた product loop の瞬間に付随している。AKC はその
第二のループを明示化したものだ: 6 つの名前つき phase、各 phase が所有する資産、
走る場所。

## playbook が各 phase をどこで示唆しているか

[ADR-0013](adr/0013-positioning-within-agent-memory-literature.md) の流儀に従い、まず
譲歩（concede）から: AKC の phase がやることの大半は、playbook のどこかで既に示唆
されている。次の表は各示唆の位置を特定し、対応の強さを評定する。

| AKC phase | playbook がそれを示唆する箇所 | 強さ |
|---|---|---|
| **Research** — signal-first intake（[search-first](https://github.com/shimo4228/search-first)） | 無い。research の形をした唯一の存在は、codebase を探索して主文脈を溢れさせずに報告する subagent（Stage 3）— 内部・タスク単位・context 節約が目的で、外から到来する知識の intake 規律ではない。 | gap |
| **Extract** — reusable pattern（[learn-eval](https://github.com/shimo4228/learn-eval)） | 2 度した誤りは CLAUDE.md の訂正になるという運用則（Stage 3）と、レビュー側で指摘が 2 度目に出たときの同型（Stage 5）; 各 production incident が eval になり回帰テストとして suite に残る（Stage 4）; 却下された指摘が detection band — version 管理された設定に置かれる — を調整する（Stage 6）。 | strong — ただし 3 つの機構が 4 stage に散在し、1 つの活動として名指されない |
| **Curate** — audit what accumulated（[skill-health](https://github.com/shimo4228/skill-health) + [skill-stocktake](https://github.com/shimo4228/skill-stocktake) + [rules-stocktake](https://github.com/shimo4228/rules-stocktake) + [agent-stocktake](https://github.com/shimo4228/agent-stocktake)） | tech lead が REVIEW.md で指摘を評定し Nit 量に上限を課して review 設定を調整する月次パス（Stage 5）; 古びた記述は便益なしに context を食うので CLAUDE.md を 1 ページ以下に保つ（Stage 3）; 古い eval case が判別力を失うにつれ新しい case を足すべしという注記（Stage 4）。 | embryonic — 習慣と cadence はあるが、蓄積した集合の体系的な棚卸しは無い |
| **Promote** — human-gated behavior change（[rules-distill](https://github.com/shimo4228/rules-distill)） | ゲートは全層に存在し、よく規定されている: CLAUDE.md の変更は PR review で code owner が承認し、skill の変更は policy owner が承認し（Stage 3）、譲れない hook は個々のエンジニアが切れない managed settings へ移る（Stage 5）。skill と CLAUDE.md と prompt のどれに置くかの経験則もある（Stage 3）。 | mixed — 人間ゲートは存在する。一方、蒸留の判断 — そもそもどの経験が耐久化に値するか — は「2 度」の閾値とその配置経験則に還元されている |
| **Measure** — observable behavior（[skill-comply](https://github.com/shimo4228/skill-comply)） | CLAUDE.md・skill・hook への任意の変更時とスケジュールで走る eval suite; 構成変更は結果でゲートされ、pass rate を下げる skill 変更は merge 前にレビューされる; pass rate は経時で追跡される（Stage 4）。skill が実際に発火するかを、タスクの頼み方を変えて試す（Stage 3）。 | strongest correspondence |
| **Maintain** — docs and artifact hygiene（[context-sync](https://github.com/shimo4228/context-sync) + [repo-asset-stocktake](https://github.com/shimo4228/repo-asset-stocktake)） | playbook の Stage 6 ではない。最も近い示唆は、変更が CLAUDE.md を古びさせたことを review が指摘する（Stage 5）、read-only の pipeline step が changelog を起草する、ゲートつきの write step が生成 docs を更新する（Stage 5）。 | false friend |

明示的に旗を立てる価値があるのは最終行だ。名前の一致が誤りを誘うからである。AKC の
Maintain はドキュメントと artifact の衛生 — context ファイルの役割を清潔に保ち、消費者の
消えた資産を見つける。playbook の Stage 6 Maintain は production 監視 — agent が稼働中の
deployment を見張り、決定論的 script が control band の突破を検知し、診断が新しい intent
としてループに書き戻される。名前は一致し、指示対象は一致しない。二重ループの語彙で言えば
このずれは正確に記述できる — playbook の Maintain は product loop の再入口、新しい仕事を
**生む** stage であり、AKC の Maintain は harness loop の衛生 phase、ループ自身の記録を
読める状態に保つ側である。名前で対応させると、仕事の源泉を記録の掃除に写像してしまう。

## gap が意味するもの

弱い 2 行は Research と Curate であり、それはまさに AKC がそのために存在する 2 つの
phase である。

playbook の harness-loop 的習慣それぞれの発火条件を見ると、大半は product loop 内の
出来事 — 繰り返された誤り、incident、2 度出たレビュー指摘、却下された band 突破 — で、
残りは play ごとのスケジュール — レビュー指摘を評定する月次パス、現在の構成をテストする
夜間実行 — である。どの発火条件もしないのは、**蓄積した集合を掃くこと**だ: 積み上がった
skill・訂正・eval case のうちどれがまだそこに在るべきかを問うものは無く、組織自身の
軌跡の外から知識を持ち込むものも無い。それこそが AKC の出発点になった失敗 — skill は
古び、rule は常駐コストを蓄積し、ドキュメントは drift する — であり、どれも出来事として
自己申告しないし、集合の現状だけをテストする実行にも現れない。

これは playbook の欠陥ではなく、規模の違いである。各 play が何を配置済みと仮定しているかを
読めば役割は明示されている: platform engineer が eval suite を立ち上げ、tech lead が
REVIEW.md を月次で調整して human threshold を定め、各 policy には skill 変更を承認する
名前つき owner がいて、service owner が band 突破の queue を捌く。これらの役割が存在する
ところでは、出来事とスケジュールによる保守で足りる — 各自の play が浮かび上がらせるものに
気づくことが、誰かの職務だからだ。AKC は同じループを 1 人で回す operator のために
書かれている。そこでは上記の役割すべてが同一人物であり、保守を割り当てる先がいない
（[ADR-0010](adr/0010-human-cognitive-resource-as-central-constraint.md)）。その規模では
intake と棚卸しは名前つきの phase にしなければ、そもそも起きない。

人間の位置についても、2 つの文書はわずかに違う場所に立つ。playbook は、ボトルネックが
build phase の周囲の human-speed の工程へ移ったという観察から始まり、人間の注意は消える
のではなく移動する — ゲートに集中し、レビューすべき artifact とともに移る — と明言し、
人間の判断がループの上に立ち続けるという像で締める。その応答は、ボトルネックの工程を
自動化して除くことだ。AKC は制約については同意した上で、playbook がしない 2 つの主張を
足す: この希少性は agent の能力が伸びるほど相対的に悪化するから、予算は迂回するだけで
なく保全されねばならない（ADR-0010）こと、そして人間はループの出力の一つである — Curate
と Promote は operator に何を残す価値があるかの判断を強い、それを繰り返すことがループを
操る判断力を研ぐ — ことだ。AKC の枠組みでは、ループの上に立つことはループの中にいる
ことでもある。

## artifact の対応: intent と RFC

playbook の Plan stage は `intent.md` を生む: 発案者自身の言葉で書かれた proto-spec で、
product owner が見張る共有・version 管理された置き場に commit され、問題・望む結果・
影響を受けるユーザーとシステム・制約・未解決の問いを覆う。その load-bearing な性質は、
version 管理されていること、人間と agent の両方が読めること、merge として受理・却下
されることだ。

operator の規模では、この artifact には既に名前がある: RFC 形式の提案記録である。作業が
起きる repository 内の公開 `rfcs/` ディレクトリは忠実な intent home だ — playbook 自身の
指針も、単一プロダクトなら最も簡単な置き場は product repo 内の `intent/` フォルダで、
専用の intent repository は intent が多数の repository に跨るときだけ割に合う、という
ものである。`rfcs/` は同じ形の、より古い名前だ。

field の対応は近く、Rust RFC 系譜の RFC テンプレートは intent テンプレートの代替では
なく上位集合になる:

| intent field | RFC section |
|---|---|
| Problem | Motivation |
| Proposed outcome | Summary |
| Affected users and systems | Guide-level explanation（users）、Reference-level explanation（systems） |
| Constraints | Reference-level explanation |
| Open questions | Unresolved questions |

対応物を持たない RFC 節 — drawbacks、rationale and alternatives、prior art、future
possibilities — は有用な方向への余剰である: intent home はフル RFC より軽い文書を
受け入れつつ、重い文書を拒まないべきだ。intent に RFC 形式を採ることは新たなコストを
生まず、agent の問いより古いレビュー慣行を継承する。

## continuous evals への規模条件

Measure 行は表の中で最も強い対応であり、同時に最も明瞭な規模条件を帯びる。

playbook の continuous-evals play は、チームが持つ 2 つのものを前提にする。corpus:
直近の作業から 20〜50 件の実タスクを集め、各々に受理可能な結果を定義するチェックを
書き添えることを提案する。そして配置済みの triage: incident を所有したチームがその
eval を書き、platform engineer が suite を立ち上げ、構成変更を所有するチームが結果に
照らして承認する。どちらもチーム規模では合理的で、どちらも operator 規模ではタダでは
ない。

証拠を読む前に、1 つの分解 — playbook のものではなく本書のもの — が有用だ。書かれて
いる限りで、この play の受理チェックは決定論的である: テストが通る、lint が綺麗、
振る舞いが不変、を script が検証する。モデルが判定を下す形は playbook の別の場所に
現れる — 敵対的な reviewing agent、merge ゲートでの層状の agentic review。前者を構成
計測の**決定論 tier**、後者を **judge tier** と呼ぶことにする。

著者自身の実践からの operator 規模の証拠（2026-08 — operator 1 人、約 50 skill）は、
judge tier が先に劣化することを示唆する。LLM-judge による skill 監査の pilot は
48 skill で真の欠陥 0 を返した: 全指摘が false positive だった。skill が実際にどれだけ
発火するかを測るために建てた別の計器は定数 0 を読み、信じられる代わりに死んだ計器として
退役された。ここでの転移仮定は明示しておく: skill 監査の judge は eval suite の judge
ではない。だが両者とも operator 規模の corpus の上で LLM が判定を下す形であり、失敗が
追跡していたのは corpus の大きさだった。どちらの結果も playbook と矛盾しない。どちらも、
ある corpus 規模を下回ると judge tier は operator が triage せねばならないノイズを
生む — その計器が守るはずだった予算をまさに費やして — ことを示唆する。

決定論 tier は同じ意図を運び、その規模でも発火する: hook への回帰テストと構成 lint を
すべての構成変更で走らせ — agent を操る構成はコードが受けるのと同じ回帰テストに値する
という playbook 自身の原則 — すべての incident を恒久的な回帰テストへ変換する。playbook
自身も、最も stakes の高い場所では同じ分離を主張する: band 検知はモデルを介さず完全に
決定論的に保ち、モデルは突破の後にのみ呼ぶ。批判ではなく規模条件として読むこと:
決定論 tier はあらゆる規模で保ち、judge tier はその判定が triage に値するだけ corpus が
育ってから足す。

## 変わらないもの

- **6 つの phase。** Research → Extract → Curate → Promote → Measure → Maintain は
  数・名前・順序とも不変である。本書はそれらを外部フレームワークに写像するだけで、
  再定義はしない。playbook の Stage 6 が AKC の Maintain を改名することもない。
- **3 つの core theme。** cognitive-resource の希少性、intent alignment、cycle が人間も
  変えること、は不変である（ADR-0012）。第 4 の theme はここから入らない。
- **効力中の ADR。** どの ADR も修正・supersede されない。本書は ADR-0013 の系譜 —
  concede, then locate — に連なる Related-Work positioning を、研究文献ではなくベンダーの
  実践文書へ適用したものである。
- **Mechanism-only の範囲。** 具体的 instance・operator 固有の資産・domain content は
  本書から core に入らない（ADR-0011）。

## Dated addenda

playbook は変わりうる URL に住んでいる。本対応は 2026-08-24 のアーカイブ版に pin
されている。将来の改版は、この節に日付つきの追記 — playbook で何が変わり、それが上の
写像の何を動かし何を動かさないか — として入り、本文の静かな書き換えにはしない。
ADR-0013 が addenda を同じ形で保つのは同じ理由による: 対象が動くたびに静かに自らを
書き換える positioning は、何の記録でもない。

*追記はまだ無い。*
