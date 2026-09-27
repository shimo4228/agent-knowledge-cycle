# Plan — `line of approval` に control plane を追記する

## Context

2026-07-25、harness 側（`~/.claude`）で ADR-0019 を立て、ゲートの「第 2 軸」を規定する常駐 rule
`rules/common/human-gate.md` を新設した。その軸（artifact 層は機械 / intent 層は人間）を AKC に
昇格すべきか、pointer page を置くべきかを grill セッションで検証した。

**結論: 昇格しない。** 検証で判明した事実:

- 層軸そのものは AKC に既出 — position paper §5「what can be verified without the operator runs
  unattended; every behavior-shaping change passes the gate」、`docs/glossary.md:46-57`
  (line of approval)、`docs/adr/0005:86-90`（generator–verifier gap / no approved-by-the-LLM path）。
  ADR-0019 は新しい判断ではなく、論文 §5 が "first instance"（著者の日常運用）と呼ぶものの実装記録。
- pointer page（`docs/akc-cycle.md` / `docs/skills/README.md`）は「why は AKC の ADR / how は配布 repo」
  という役割分割の片側であり、既存 4 件はすべて paired ADR を持つ。今回は埋めるべき why が AKC 側に無い。
- ADR-0019 の残りの内容（実装コードは意図の要約で提示する）は operator content であり、
  mechanism-only inclusion rule により AKC には入らない。加えて論文 §2.1(b)/§6.2 が gate complacency
  防御として "a diff reviewed... under the operator's name" を挙げているため、限定文脈なしに配布すると
  衝突して読まれる。

**ただし 1 点だけ実質的な穴が見つかった。** `hook` / `permission` / `allowedTools` / `control plane` は
`docs/adr/0005` にも `docs/glossary.md` にも **1 回も出現しない**（grep 実測）。ADR-0005 の decision table は
episode log / knowledge store / rule / skill / identity / ADR・README の 6 行で、ハーネス自身の control plane
（hooks、permission 付与、scheduled task 定義）を列挙していない。これらは records ではないが、
**ゲートを執行する層それ自体**であり、無警戒だと agent がゲートを迂回する代わりに**ゲートを書き換えられる**。

この追記は新しい judgment ではなく **enumeration の穴埋め**である — line of approval の判定基準は
「artifacts that shape future behavior」であり、hooks / permissions はその基準を満たすのに列挙から漏れていた。
基準からの導出であって基準の変更ではないため、ADR テスト（不可逆 / 文脈なしで驚く / 実在するトレードオフ）を
通らず、ADR ではなく glossary の sharpening として着地させる。

意図した結果: line of approval の承認必須側が、自身の判定基準に対して閉じた列挙になること。

## 変更する物

### 1. `docs/glossary.md` — `## Line of approval`（46-57 行）

承認必須側の列挙に control plane を加え、理由を 1 文添える。

- 現状: 境界を「**records**（transcripts, distilled notes）↔ **the artifacts that shape future
  behavior**（skills, rules, identity prose）」で引き、「See ADR-0005's decision table.」で締める。
- 追記の要件:
  - control plane を**第 3 の項目として並べず**、承認必須側の内部で扱う（軸を増やさない。
    境界は 2 分割のまま、承認必須側の内訳が広がるだけ）。
  - 「ハーネス自身の control plane（hooks、permission 付与、scheduled task 定義）」を明示。
  - 理由を 1 文: この層への変更はゲート自身を動かすため、緩める変更がゲートを通らずに入りうる。
  - **ADR-0005 の内容として書かない。** 既存の「See ADR-0005's decision table」は残しつつ、
    control plane は同 table が列挙していない導出項であることが読者に分かる書き方にする
    （table を後から書き換えたように読ませない — ADR は歴史的記録）。

### 2. `graph.jsonld` — human approval gate ノード（435 行付近）

同じ列挙が `"description": "...every change to the artifacts that shape future behavior — skills,
rules, identity — requires named human sign-off. Codified as ADR-0005."` として存在する。
glossary だけ直すと graph が drift するため、同じ内訳に揃える。ADR-0005 への帰属表現は
glossary と同じ扱いにする（table の中身を偽らない）。

### 3. `.notes/TASKS.md` — 判断の記録

Done 節に 1 行追加: 「ゲート層軸の AKC 昇格 — 却下（層軸は §5 / glossary / ADR-0005 に既出、
pointer は paired ADR を要する）。control plane の列挙欠落のみ glossary へ還元」＋ 再訪トリガー
「CA または第三者ハーネスで、gate の提示物に関する同型の判断が独立に必要になったとき」。

既存 T3（rules 層整理の human 依存性観察）は**別テーマ**なので上書きしない。deferred のまま残す。

### 4.（別 change target）`~/.claude` 側の後始末 — **別コミット**

放置すると「AKC 昇格待ち」という誤った状態が残るため、今回で閉じる。

- **`~/.claude/.notes/TASKS.md:14`** — T-009（pending）を Done 節へ移す。結論を 1 行で:
  層軸は AKC に既出（paper §5 / glossary line of approval / ADR-0005）のため昇格せず、
  ADR-0019 は "first instance" の実装記録として harness 側に留まる。control plane の
  列挙欠落のみ AKC glossary + graph へ還元。
- **`~/.claude/docs/adr/0019-human-gate-layer.md`** — Consequences / Negative の
  「AKC への昇格が未了…drift しうる」を、確定した結論に差し替える。Alternatives (d)
  （AKC 側に先に concept / ADR を立てる案）の却下理由も、当時の「証拠が足りない」から
  検証後の「AKC に既出であり新しい judgment ではない」へ更新する。**Status / Date /
  Decision は変更しない**（受理済み判断は動かさない — Consequences の事実更新に限る）。

AKC repo とは変更先が異なるため、コミットは分ける。

## 触らない物（明示）

- **`llms-full.txt:100`** — position paper の要約段落。論文本文は control plane に言及していないため、
  ここに足すと source fidelity 違反になる。**編集しない**。
- **`docs/adr/0005-human-approval-gate.md`** — 受理済みの歴史的判断記録。後から行を足さない。
- **新規 ADR / 新規 pointer page / 新規 standalone repo** — いずれも作らない（上記 Context の理由）。
- `README.md` / `README.ja.md` / `docs/akc-cycle.md` / `docs/skills/README.md` / `CHANGELOG.md`
  （リリース時に扱う）。

## 語彙の制約（決定済み）

- **"value layer" は使わない** — `docs/adr/0017:41,106` が "The alignment target is operator intent,
  not model values. This is not an AI-safety value-alignment claim." として意図的に排除している。
- **新語を coin しない** — authorship-strategy ADR-0010（Coin Sparingly, Anchor Densely）。
  `line of approval` / `the gate` / `harness alignment` の既存 anchor だけを使う。

## Verification

docs 変更のためビルド・テストは無い。以下で足りる。

1. `python3 -c "import json; json.load(open('graph.jsonld'))"` — JSON-LD が壊れていないこと。
2. `grep -n "control plane\|hook\|permission" docs/glossary.md graph.jsonld` — 両面に入り、
   かつ `docs/adr/0005*` と `llms-full.txt` には入っていないこと（意図的な非対称の確認）。
3. `docs/glossary.md` の Line of approval 全文と graph の該当 description を読み比べ、
   ADR-0005 の table を偽って引用していないことを目視確認。
4. `git status` — `docs/glossary.md` / `graph.jsonld` / `.notes/TASKS.md` の 3 ファイルのみ。

## 人間ゲート

`docs/glossary.md` と `graph.jsonld` は DOI 登録 repo の公開ドキュメント = behavior-shaping artifact。
`human-gate.md` の規定どおり、コミット直前に**差分の本文**を提示して承認を得る（意図の要約では済ませない）。
