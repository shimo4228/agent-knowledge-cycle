# AKC Glossary

Terminology mapping for the two languages supported by AKC's README
(English primary + Japanese mirror). Use this as the canonical reference
when translating or updating either version of `README.md`.

(The es / pt-BR / zh-CN / zh-TW mirrors were retired on 2026-05-15
after traffic data showed statistically zero unique human viewers;
LLM crawlers translate from the English source on demand. Glossary
entries are preserved as historical reference for the original
translation discipline and for any future re-introduction of mirrors.)

## Translation policy

- **Skill names and AKC-coined terms stay in English.** Names like
  `search-first`, `learn-eval`, `skill-stocktake`, `rules-distill`,
  `skill-comply`, `context-sync`, `signal-first`, `harness`, and the six
  phase names (Research / Extract / Curate / Promote / Measure /
  Maintain) remain in their original English form across all languages.
  Translating them would break searchability and create divergent
  vocabularies across the ecosystem.
- **General-purpose technical terms are localized.** Words like
  *cycle*, *skill*, *rule*, *audit*, *layer*, *pattern* are translated
  using the natural local equivalent — never transliterated or
  romanized.
- **Phase names appear bilingually in body text** when first introduced
  (e.g., 「Research（研究）」), then English alone afterwards.

## Terminology table

| English | 日本語 | 简体中文 | 繁體中文 | Português (Brasil) | Español | Keep original |
|---------|--------|----------|----------|---------------------|---------|:-------------:|
| cycle | サイクル | 周期 | 週期 | ciclo | ciclo | |
| phase | フェーズ | 阶段 | 階段 | fase | fase | |
| Research | Research | Research | Research | Research | Research | ✓ |
| Extract | Extract | Extract | Extract | Extract | Extract | ✓ |
| Curate | Curate | Curate | Curate | Curate | Curate | ✓ |
| Promote | Promote | Promote | Promote | Promote | Promote | ✓ |
| Measure | Measure | Measure | Measure | Measure | Measure | ✓ |
| Maintain | Maintain | Maintain | Maintain | Maintain | Maintain | ✓ |
| signal-first | signal-first | signal-first | signal-first | signal-first | signal-first | ✓ |
| skill | スキル | 技能 | 技能 | habilidade | habilidad | |
| rule | ルール | 规则 | 規則 | regra | regla | |
| pattern | パターン | 模式 | 模式 | padrão | patrón | |
| episode | エピソード | 片段 | 片段 | episódio | episodio | |
| layer | 層 | 层 | 層 | camada | capa | |
| distill / distillation | 蒸留 | 蒸馏 | 蒸餾 | destilar / destilação | destilar / destilación | |
| audit | 監査 | 审计 | 審計 | auditar / auditoria | auditar / auditoría | |
| compliance | 遵守 | 遵循 | 遵循 | conformidade | cumplimiento | |
| immutable | 不変 | 不可变 | 不可變 | imutável | inmutable | |
| intake | 取り込み | 吸收 | 吸收 | ingestão | ingesta | |
| drift | ドリフト | 漂移 | 漂移 | desvio | desviación | |
| scaffold / scaffolding | 足場 | 脚手架 | 腳手架 | andaime | andamio | |
| dissolution | 溶解 | 溶解 | 溶解 | dissolução | disolución | |
| harness | ハーネス | harness | harness | harness | harness | ✓ |
| knowledge body | 知識体 | 知识体 | 知識體 | corpo de conhecimento | cuerpo de conocimiento | |
| knowledge cycle | 知識サイクル | 知识周期 | 知識週期 | ciclo de conhecimento | ciclo de conocimiento | |
| reference implementation | リファレンス実装 | 参考实现 | 參考實作 | implementação de referência | implementación de referencia | |
| three memory layers | 3 つのメモリ層 | 三层内存 | 三層記憶 | três camadas de memória | tres capas de memoria | |
| intent alignment | 意図のアライン | 意图对齐 | 意圖對齊 | alinhamento de intenção | alineación de intención | |
| bottleneck | ボトルネック | 瓶颈 | 瓶頸 | gargalo | cuello de botella | |
| cognitive economy | 認知経済 | 认知经济 | 認知經濟 | economia cognitiva | economía cognitiva | |
| cognitive resource | 認知資源 | 认知资源 | 認知資源 | recurso cognitivo | recurso cognitivo | |
| scarce resource | 希少資源 | 稀缺资源 | 稀缺資源 | recurso escasso | recurso escaso | |
| co-develop | 共に育つ / 共進化する | 共同发展 | 共同發展 | co-desenvolver | co-desarrollar | |
| attention and judgment | 注意と判断 | 注意力与判断 | 注意力與判斷 | atenção e julgamento | atención y juicio | |

## Skill names (always English)

- `search-first` — Research
- `learn-eval` — Extract
- `skill-stocktake` — Curate
- `rules-distill` — Promote
- `skill-comply` — Measure
- `context-sync` — Maintain

## Notes

- *Harness* is left in English because it carries a specific meaning in
  the Mitchell Hashimoto / harness-engineering literature that local
  translations do not yet stably encode.
- *Signal-first* stays in English to preserve its connection to the
  AKC vocabulary and to ADR-0010.
- The phase verbs (Extract, Curate, Promote, Measure, Maintain,
  Research) are kept English even when the surrounding body text is
  localized, because they are also the names of the cycle skills and
  must be searchable across languages.

## Maintenance

When updating `README.md` (English source), keep this table in sync if
you introduce a new AKC-coined term. The Japanese mirror translator
(currently the author) consults this table before choosing a rendering.
