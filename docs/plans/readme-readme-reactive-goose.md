# AKC README 全面改稿 — 最小フロア型への移行 + ADR-0012 改訂

## Context

現行 README.md（302 行・表 8 個）は情報密度が過多で、同一概念が反復している:
intent alignment ×3 箇所、bidirectional loop ×2、harness drift ×4、6 phase 列挙 ×3、skill 一覧が 3 つの表に分散。
反復の最大源は **ADR-0012 自身が命じた「3 themes の二重提示」**（What is AKC? 4 段落 + Why AKC H3×3）と、
「README が情報フロア全体を抱える」構造。repo には llms.txt / llms-full.txt / graph.jsonld という機械可読層が既にあり、
フロアの二重保持は不要（llms-full.txt が design principles 一覧・harness engineering 対比・references をカバー済みと確認済み）。

## grill-me で確定した決定（ユーザー承認済み）

1. **最小フロア型** — README は「cycle 定義 + 3 themes + install + cite」の最小フロアのみ。詳細は llms-full.txt / ADR へのポインタ
2. **ポインタ化で十分** — 新規 doc は作らない。カバー漏れが見つかった項目のみ llms-full.txt に補充
3. **skill 表は phase→skill 表のみ残す** — maintenance-pressure 表は削除（prose 1-2 文に圧縮）、3 レベル採用表は Install 節の 2-3 文に畳む。design-pattern skills 3 つは phase 表の下に 1 行言及
4. **ADR-0012 を新 ADR（0020）で改訂** — ただし射程は **README 構造のみ**。themes front-load 原則と llms.txt / llms-full.txt の既存 commitment（blockquote 順序、Q2/Q3）は効力維持

## タスク種別

`writing`（README 自体が一次成果物）→ Writing Chain、orchestrator = **readme-writer**。
付随して ADR 新設（adr-writer）+ doc-sync（graph.jsonld / CODEMAPS 両面更新）。

## 変更ファイル

| ファイル | 変更 |
|---|---|
| `docs/adr/0020-*.md` | 新設。「README を最小フロア型 + themes 単一箇所提示に移行、ADR-0012 の README 構造 commitment を改訂」。llms.txt 系 commitment は不変と明記。検証条件を新構造用に書き直す |
| `README.md` | 全面改稿（~120-140 行目標、下のスケルトン） |
| `README.ja.md` | 英語正本確定後に同じ diff でミラー改稿 |
| `graph.jsonld` | ADR-0020 ノード追加（既存 ADR ノード規約に従う） |
| `docs/CODEMAPS/architecture.md` | ADR-0020 言及 + README 役割記述の鮮度更新 |
| `llms.txt` | 61 行目の README 説明（"design principles" を含む）を新構造に合わせ微修正のみ。構造は不変 |
| `llms-full.txt` | 原則不変。ポインタ化でカバー漏れが判明した項目のみ補充 |

## 新 README スケルトン

1. **Lead** — Language 行 / H1 / badges 3 個 / tagline / 定義 2-3 文 + companion paper DOI 1 行。冒頭 30 行内に 3 theme の語句を各 1 回含める（front-load 原則は維持）
2. **Why AKC** — 3 themes の**唯一の**本格提示。theme 順固定（cognitive resource → intent alignment → changes the human too）、各 1 短段落。maintenance-pressure 表はここの prose 1-2 文に吸収。harness alignment / drift は ADR-0017 + paper へのリンクで 1 文
3. **The cycle** — mermaid 図 + text equivalent 1 文 + **phase→skill 表**（唯一の skill 表）+ design-pattern skills 1 行 + ADR-0019 provisional 注 1 行
4. **Install** — akc-cycle quick install ブロック + 3 レベル採用の畳み込み 2-3 文（rules だけで入る / skills は段階導入 / dissolution へのポインタ）
5. **Fact table** — 現行のまま維持（project type / author / release / DOI / license / audience / AI navigation）
6. **What's in this repo** — 現行表を維持または微トリム（ナビゲーション役）
7. **Limitations** — 2-3 文 + ADR-0014 / harness drift ポインタ
8. **Positioning** — 旧 Relationship to Harness Engineering を表なし 2-3 文に圧縮 + ADR-0009 / 0017 ポインタ
9. **Origin & Acknowledgments** — 2 節をマージして短段落 1 つ（ECC への謝辞は保持）
10. **How to Cite** — bibtex 維持
11. **Related Work** — compact 表 + hub ポインタ維持（ecosystem federation 規約）。Related Publication 節は Lead の paper 言及に統合して削除
12. **License**

**削除（ポインタ化）**: What is AKC? の theme 4 段落（Why AKC に一本化）、Design principles 9 項目（llms-full.txt 24 行目 + 各 ADR が正本）、References 3 小節（ADR-0013 / 0017 + llms-full.txt）、Customization 節（Install に 1 文吸収）、maintenance-pressure 表、3 レベル採用表。

## 実行チェーン（Writing Chain）

1. **Wiki 参照（read-only）** — CLAUDE.local.md 規約: ADR 起草前に research wiki `AKC.md` の「オープンクエスチョン / 矛盾・論争」節を確認
2. **ADR-0020 起草** — adr-writer agent。6 必須 section + Relationship to other ADRs（0012 との系譜）。Status: accepted
3. **README.md 改稿** — readme-writer skill 準拠でドラフト
4. **Parallel Group 1（レビュー）**: [readme-reviewer, codex-review (prompt-driven — 公開 repo README = 高 stakes)]
5. **README.ja.md ミラー** — 英語正本のレビュー通過後
6. **doc-sync** — graph.jsonld + CODEMAPS + llms.txt 微修正を同じ diff に含める
7. **Verify（writing 版）** — `readme_lint.py`（`~/.claude/skills/readme-writer/scripts/readme_lint.py`）を README.md / README.ja.md に実行、ADR-0020 の新検証条件を目視チェック、`git status` 確認
8. **人間 gate** — commit 前 diff 承認（第 2 介入点）

早期停止: readme-reviewer MAJOR ISSUES / codex CRITICAL / readme_lint exit 1 → 停止して報告。

## Verification

- readme_lint.py が README.md / README.ja.md 両方で PASS
- 冒頭 30 行に 3 theme クラスタの語句が各 1 以上（front-load 原則の存続確認）
- README 内で intent alignment / bidirectional loop / 6 phase 列挙 / skill 一覧の登場が各 1 箇所になっている（grep で確認）
- 削除した各節の内容が llms-full.txt または ADR に存在することを個別確認（漏れは llms-full.txt に補充）
- graph.jsonld が `python -m json.tool`（または既存の検証手段）で valid
- git status に意図外ファイルなし

commit はユーザーの diff 承認後のみ。
