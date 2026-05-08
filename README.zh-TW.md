Language: [English](README.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md) | 繁體中文 | [Português (Brasil)](README.pt-BR.md) | [Español](README.es.md)

# Agent Knowledge Cycle (AKC)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19200726.svg)](https://doi.org/10.5281/zenodo.19200726)

為 AI 代理打造的知識週期 —— 與塑造它的人一同成長。

## 什麼是 AKC

AKC 起於一個觀察：隨著代理能力的提升，稀缺資源已經不再是運算或上下文 —— 而是讓循環得以持續運作的 **人的注意力與判斷**。AKC 正是圍繞這份稀缺而打造的。請參閱 [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md)。

守護這份預算，會重新定義週期的目的。目標並不是「代理產出單次正確的輸出」 —— 而是「代理的行為在不同會話之間，持續與運營者的意圖保持對齊」。正確性可以由測試檢查；對齊則無法，因為意圖本身會隨著運營者在使用中磨練出的判斷而移動。

因此，對齊是在時間中維持，而不是一次性完成設定。**週期同樣會改變人**：在一次次 Curate / Promote / Measure 的決策之後，運營者關於「什麼算是好的代理行為」的判斷，會一場會話比一場會話更鋒利 —— 這正是標語所說的「與塑造它的人 *一同* (而非 *為* 它) 成長」。用技術語言說，這是一個代理行為與人類判斷共同成長的雙向循環 (bidirectional growth loop)。

把這一切落地的，是六個可組合的階段 —— Research → Extract → Curate → Promote → Measure → Maintain。signal-first 的吸收，讓注意力不被花在不會改變下一步行動的資訊上；將反覆出現的判斷提升為規則，讓同一份判斷不必反覆重做；可觀測的遵循檢查，讓人不必在每次會話中再做手動審計。沒有這樣的循環，代理的知識就會退化 —— 技能陳舊、規則互相矛盾、文件與程式碼漸行漸遠。

AKC 以規範、schema、ADR 與最小參考實作的形式發布。LLM 與 adapter 請自行準備。

## 為什麼是 AKC

### 瓶頸已經移動

隨著代理能力提升，稀缺資源已經不再是運算或上下文，而是人的注意力與判斷。每一個與之競爭的框架都在最佳化代理一側 —— 更多的工具、更多的記憶、更多的上下文、更多的自動化。AKC 反過來問：既然處於循環中的人，每天可投入的注意力與判斷是固定預算，那麼週期應該如何塑造，才不會讓這份預算被白白浪費？

AKC 的各階段都圍繞這份稀缺打造。Research 採用 signal-first，讓吸收量不超過消化量。Promote 把重複出現的判斷轉化為規則，避免每次會話重做同樣的決定。Measure 用可觀測的遵循檢查取代手動重新審計。實作前的對話之所以被提前，是因為在審查時才發現意圖錯位，其代價會高於本可預防它的那場對話。運轉週期並非免費 —— 但這正是週期守護那個唯一不會隨模型規模擴展的資源的方法。請參閱 [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md)。

| 維護問題 | AKC 的回應 |
|------|------------|
| 技能陳舊 | skill-stocktake 定期審計品質 |
| 規則與實際脫節 | skill-comply 測量真實的行為遵循率 |
| 知識散落各處 | rules-distill 將重複出現的模式提升為原則 |
| 文件漂移 | context-sync 偵測角色重疊與陳舊內容 |
| 重複造輪子 | search-first 先確認是否已有現成方案 |
| 經驗流失 | learn-eval 以品質關卡擷取模式 |

每一行都是週期接管了原本應由人手動承擔的維護工作。運轉週期並非免費，但比起每次都重做同一份審計，仍要便宜得多。

### 與意圖對齊，不只是正確

正確性可以自動化 —— 測試、型別、lint、評審工具都能檢查輸出是否滿足特定條件。對齊則無法以同樣的程度自動化，因為意圖本身會隨著運營者在使用中磨練出的判斷而移動。一個代理可以滿足所有正確性檢查，卻仍然偏離意圖。

AKC 的設計選擇反映了這份區別。設計原則 #3（Non-destructive）—— 先提議、再等待確認 —— 把每一次變更都置於一個可以重新陳述意圖的檢查點。實作前的對話被視為 **認知經濟的投資**，而非摩擦。這份區別也說明了 AKC 與 harness engineering 的差異：harness 最佳化的是首次的正確性，而 AKC 讓 harness 自身隨著意圖的變化而保持與意圖對齊。分層比較請參閱 [與 Harness Engineering 的關係](#與-harness-engineering-的關係)。

### 週期同樣會改變人

在反覆進行 Curate 與 Promote 的決策過程中，使用者會磨練出「什麼知識值得保留」的判斷力。透過 Research，使用者會培養出「該採用現成方案還是自行打造」的直覺。透過 Measure，使用者能學到好規則與模糊願望之間的差異。AKC 並不是一個讓代理獨自改進的單向最佳化循環 —— 代理的行為與人類的判斷在持續互動中共同成長。標語 —— *與塑造它的人一同成長* —— 命名的正是這項性質。

## 儲存庫內容

九個 ADR、八條設計原則、三個設計模式技能、兩個 JSON schema、一份約 500 行的可執行參考實作，以及只需一行 `cp` 就能裝入完整週期的規則檔。AKC 定義了三層記憶與四種程式碼–LLM 分層模式。下列的六個 cycle skills 仍然是各階段「完整版」且帶有立場的實作。

AKC 發布 **兩類技能**：

- **Cycle skills**（外部儲存庫）—— 週期的每個階段對應一個：`search-first`、`learn-eval`、`skill-stocktake`、`rules-distill`、`skill-comply`、`context-sync`。
- **Design-pattern skills**（[`docs/skills/`](docs/skills/)）—— 與 ADR 一一對應的長篇「how」指南，橫跨多個階段。

完整的儲存庫樹與文件角色路由請參閱 [`docs/CODEMAPS/architecture.md`](docs/CODEMAPS/architecture.md)。

## 週期

AKC 由六個可組合的技能構成，週期的每個階段對應一個：

```
Experience → learn-eval → skill-stocktake → rules-distill → Behavior change → ...
               (extract)    (curate)          (promote)            ↑
                                                            skill-comply
                                                              (measure)
                                              context-sync ← (maintain)
```

每個技能負責知識生命週期中的一個階段：

| Skill | Phase | 作用 |
|-------|-------|------|
| [search-first](https://github.com/shimo4228/claude-skill-search-first) | Research | 廣泛搜尋，以訊號篩選 —— 僅吸收能改變下一步行動的資訊 |
| [learn-eval](https://github.com/shimo4228/claude-skill-learn-eval) | Extract | 從會話中提取可重用模式，附帶品質關卡 |
| [skill-stocktake](https://github.com/shimo4228/claude-skill-stocktake) | Curate | 審計已安裝技能的陳舊、衝突與冗餘 |
| [rules-distill](https://github.com/shimo4228/claude-skill-rules-distill) | Promote | 將技能中的跨領域原則蒸餾為規則 |
| [skill-comply](https://github.com/shimo4228/claude-skill-comply) | Measure | 測試代理是否真的遵循其技能與規則 |
| [context-sync](https://github.com/shimo4228/claude-skill-context-sync) | Maintain | 審計文件的角色重疊、陳舊內容與缺失的決策記錄 |

## Rules —— 不安裝技能也能裝入週期

並不需要六個技能全部都有才能讓週期運作。[`docs/akc-cycle.md`](docs/akc-cycle.md) 將六個階段蒸餾為任何 AI 代理都能透過自然對話遵循的行為原則。

### 快速安裝

```bash
# 複製到代理的 rules 目錄
cp docs/akc-cycle.md ~/.claude/rules/common/akc-cycle.md
```

就這樣。週期會透過對話運轉 —— 不需要技能、外掛或 CLI 工具。

### 規則所涵蓋的內容

| Phase | 規則要點 |
|-------|----------|
| Research | 廣泛搜尋，以訊號篩選 —— 僅吸收能改變下一步行動的資訊 |
| Extract | 從會話中以品質評估方式擷取可重用模式 |
| Curate | 定期審計冗餘、陳舊與沉默 |
| Promote | 將重複出現 3 次以上的模式提升至規則層 |
| Measure | 以量化方式驗證行為變化，而非主觀感受 |
| Maintain | 保持文件角色清晰、內容新鮮 |

### Skills vs Rules

- **Skills** 提供各階段深入、逐步的工作流程。想要被引導式執行時安裝它們。
- **Rules** 提供原則與觸發條件。想讓週期從對話中自然浮現時安裝它們。
- 兩者可以並存。即使技能未被觸發，Rules 也能確保週期持續運轉。

## 設計原則

1. **Composable** —— 每個技能都能獨立運作。可以只用一個，也可以六個一起用。
2. **Observable** —— skill-comply 輸出的是量化遵循率，而非主觀評價。
3. **Non-destructive** —— 每個技能都是提議變更並等待確認。沒有任何事情會自動套用。
4. **Tool-agnostic in concept** —— 為 Claude Code 設計，但其架構適用於任何擁有持久設定的代理。
5. **Evaluation scales with model capability** —— 小型模型受惠於 rubric 式的評分；推理型模型（Opus 等級）則以完整上下文與質性判斷進行評估。AKC 不強制單一方法 —— 它依模型的推理能力調整評估深度。
6. **Scaffold dissolution** —— 技能是鷹架。當使用者與代理將週期內化後，技能就不再必要，僅靠規則即可維持這個循環。請參閱 [docs/scaffold-dissolution.md](docs/scaffold-dissolution.md)。
7. **Code-LLM Layering** —— 程式碼掌握決定性、可審計性與控制流。LLM 掌握語意。兩者要明確分層；永遠不要讓 LLM 持有持久狀態或終止判斷。請參閱 [ADR-0008](docs/adr/0008-code-and-llm-collaboration.md)。
8. **Human cognitive resource is the bottleneck** —— 隨著代理能力提升，稀缺資源已不再是運算或上下文，而是人類的注意力與判斷。每個階段都被塑造為守護這份預算：Research 的 signal-first 吸收、以規則提升避免重做同一決策、以遵循度測量避免人工重新審計，以及前置對話 —— 因為錯位實作的代價高於本可預防它的那場對話。請參閱 [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md)。
9. **Genre neutrality** —— 循環是機制，而非內容。同樣的六個階段在代理知識的任何連貫主體上運作 —— 行為模式、領域專長或憲法性價值 —— AKC 不對下游專案關心哪一種採取立場。每種類型變化的是評估標準、提示範本和稽核查詢；階段本身保持不變。請參閱 [ADR-0011](docs/adr/0011-cycle-applies-to-any-knowledge-body.md)。

## 與 Harness Engineering 的關係

AKC 與 [harness engineering](https://mitchellh.com/writing/my-ai-adoption-journey)（Mitchell Hashimoto, 2025）—— 透過改良提示（例如 AGENTS.md 更新）與可程式化工具（腳本、驗證指令）的組合，讓代理不再重複同一錯誤的工程實踐 —— 共享同一片土壤。兩者都希望讓代理更可靠，但關注的焦點不同。

| 層 | 問題 | 由誰回應 |
|----|------|---------|
| Harness | 「這個輸出對嗎？」 | 單獨的 lint、測試、腳本 |
| AKC | 「這些 harness 本身還有效嗎？」 | skill-comply、skill-stocktake、context-sync |

**正確性 vs 意圖對齊。** harness engineering 關注「一次就得到正確結果」—— 以更好的指令與自動化檢查預防已知錯誤。AKC 關心的是另一個問題：代理的行為是否與運營者不斷變化的意圖保持對齊？這項論點的獨立展開請參閱 [為什麼是 AKC → 與意圖對齊](#與意圖對齊不只是正確)。

**反應式 vs 主動式。** harness engineering 本質上是反應式 —— 每出現一次錯誤就新增一個 harness。AKC 的 skill-comply 與 skill-stocktake 採取主動姿態，定期審計技能與規則是否仍被遵循、是否仍然適用。設計原則 #5 讓評估隨模型能力延伸 —— 小型模型用 rubric，前沿模型用整體性判斷。

## 自訂

上述參考實作只是起點。請儘管 fork、改寫，依你的代理與工作流程調整它們。AKC 定義的是週期，不是實作。重要的是各階段（extract → curate → promote → measure → maintain）構成一個封閉循環，而不是各階段如何打造。

## 出處

這套架構由 Tatsuya Shimomoto（[@shimo4228](https://github.com/shimo4228)）於 2026 年 2 月首次提出並實作。

最初的五個技能於 2026 年 2 月至 3 月間貢獻給 [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code)。context-sync 則是獨立開發的。

## 引用方式

若你使用或引用 Agent Knowledge Cycle 架構，請引用：

```bibtex
@software{shimomoto2026akc,
  author       = {Shimomoto, Tatsuya},
  title        = {Agent Knowledge Cycle (AKC)},
  year         = {2026},
  version      = {2.1.0},
  doi          = {10.5281/zenodo.20076396},
  url          = {https://doi.org/10.5281/zenodo.20076396},
  note         = {A knowledge cycle for AI agents — one that grows with the people who shape it}
}
```

或在文中：

> Shimomoto, T. (2026). Agent Knowledge Cycle (AKC). doi:10.5281/zenodo.20076396

## 相關專案

- [Contemplative Agent](https://github.com/shimo4228/contemplative-agent) ——
  一個獨立的研究儲存庫，在本地 9B 模型上探索 Contemplative Constitutional AI。
  其工程底層（三層記憶、兩階段蒸餾）正是為 AKC 的 ADR 播下
  種子的先行研究。詳情請見 [`docs/inspiration.md`](docs/inspiration.md)。
- [Agent Attribution Practice (AAP)](https://github.com/shimo4228/agent-attribution-practice) ——
  姊妹類型庫 (DOI [10.5281/zenodo.19652014](https://doi.org/10.5281/zenodo.19652014))。
  AKC v2.0.0 抽出的安全三件套（ADR-0001、ADR-0006、ADR-0007）
  在那裡與另外五條 ADR 一起被重新表述為八條 harness-neutral 的 ADR ——
  關於自主 AI 代理中問責分配的判斷。
  AKC 是循環（機制），AAP 是實踐（內容）。
- [Zenn 上的文章](https://zenn.dev/shimo4228) —— 開發日誌（日文）
- [Dev.to 上的文章](https://dev.to/shimo4228) —— 英文版

## 致謝

AKC 站立在 [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code)（[@affaan-m](https://github.com/affaan-m)）的基礎之上。ECC 是我每天使用的基礎 harness，其技能與規則給了我一個豐富的起點。在數個月的日常使用中，我在 ECC 之上堆疊了自己的技能與規則，而它們增殖的速度快到我追不上 —— 技能陳舊、規則開始互相矛盾、文件與程式碼漸行漸遠。我不得不持續審計這片混亂，決定保留什麼、合併什麼、把什麼提升為持久的規則。六階段的週期，就是我一旦看清這件反覆進行的維護工作的形狀之後，對那個形狀的命名。

若沒有 ECC 這個立足點，AKC 不會存在。向 affaan-m 與每一位 ECC 貢獻者致上深深的謝意。

## References

AKC 源自實踐而非理論。以下著作並未在上述過程中被參考，但所形成的週期似乎與其中的想法之間存在某種共鳴。這裡列出，供有興趣的讀者品味這份共鳴。

- [Mind in Life](https://www.hup.harvard.edu/books/9780674057517)（Evan Thompson, 2007）——
  人與代理之間的雙向循環，與生成論（enactivism）裡的「結構耦合」
  概念有某種共通之處。
- [A Beautiful Loop: An Active Inference Theory of Consciousness](https://www.sciencedirect.com/science/article/pii/S0149763425002970)
  （Laukkonen, Friston, & Chandaria, 2025）—— 人類透過觀察代理的實際行為
  來更新規則與技能的過程，隱約讓人聯想到一個遞迴自我建模循環。

## License

MIT
