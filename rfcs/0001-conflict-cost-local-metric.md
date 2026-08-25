---
state: candidate
---

## タスク

conflict cost のローカル metric を設計する。「矛盾する指示の解決に費やされる推論」は現在
ベンダーが自社 eval について主張したものを引用しているだけで、AKC 側に計器がない。
generation review が 4 つの証拠クラス中ただ 1 つ instrument を持たない状態（ADR-0023）。
ADR-0022 が held-out transfer の reference construction を欠くのと同型の open question。

## 着手条件

AKC の Measure フェーズを触るとき、計器を作るかを決める（採否未定なので candidate）。

## 詳細

[ADR-0023](../docs/adr/0023-generation-review-as-a-fourth-evidence-class.md)
（"What this decision does not add" 節が「conflict cost の local instrument は open」を
明記している）。同型の欠落は
[ADR-0022](../docs/adr/0022-transfer-as-completion-test-for-dissolution.md) の held-out transfer。

旧 ID: T-003（`.notes/TASKS.md` から 2026-08-25 移送。元は harness 台帳から 2026-08-17 に移設）。
