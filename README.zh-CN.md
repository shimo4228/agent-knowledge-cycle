Language: [English](README.md) | [日本語](README.ja.md) | 简体中文 | [繁體中文](README.zh-TW.md) | [Português (Brasil)](README.pt-BR.md) | [Español](README.es.md)

# Agent Knowledge Cycle (AKC)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19200726.svg)](https://doi.org/10.5281/zenodo.19200726)

为 AI 代理构建的知识周期 —— 与塑造它的人共同成长。

## 什么是 AKC

AKC 起于一个观察：随着代理能力的提升，稀缺资源已经不再是算力或上下文 —— 而是让循环持续运转的 **人的注意力与判断**。AKC 正是围绕这一稀缺而构建。请参阅 [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md)。

守护这份预算，会重新定义周期的目的。目标并不是「代理产出单次正确的输出」 —— 而是「代理的行为在不同会话之间，始终与运营者的意图保持对齐」。正确性可以由测试检查；对齐则不能，因为意图本身会随着运营者在使用中磨砺出的判断而移动。

因此，对齐是在时间中维持，而非一次性配置完成。**周期同样改变着人**：在一次次 Curate / Promote / Measure 决策之后，运营者关于「什么算好的代理行为」的判断，会一会话比一会话更锋利 —— 这正是标语所说的「与塑造它的人 *一同* (而非 *为* 它) 成长」。用技术语言说，这是一个代理行为与人类判断共同成长的双向循环 (bidirectional growth loop)。

把这一切落地的，是六个可组合的阶段 —— Research → Extract → Curate → Promote → Measure → Maintain。signal-first 的吸收，让注意力不被花在不会改变下一步行动的信息上；将反复出现的判断提升为规则，让同一判断不必反复重做；可观测的遵循检查，让人不必每次会话再做手动审计。没有这样的循环，代理的知识就会退化 —— 技能陈旧、规则相互矛盾、文档与代码逐渐脱节。

AKC 以规范、模式、ADR 与最小参考实现的形式发布。LLM 与适配器请自备。

## 为什么是 AKC

### 瓶颈已经移动

随着代理能力提升，稀缺资源已经不再是算力或上下文，而是人的注意力与判断。每一个与之竞争的框架都在优化代理一侧 —— 更多的工具、更多的内存、更多的上下文、更多的自动化。AKC 反过来问：既然处在循环中的人，每天可投入的注意力与判断是固定预算，那么周期应该如何塑造，才不至于让这份预算被白白浪费？

AKC 的各个阶段都围绕这份稀缺塑造。Research 采用 signal-first，让吸收量不超过消化量。Promote 把反复出现的判断转化为规则，避免每次会话重新做同样的决断。Measure 把人工再审计替换为可观测的遵循检查。实施前的对话被前置，是因为在评审阶段才发现意图错位的代价，会高于本可预防它的对话。运行周期并非免费 —— 但它正是周期保护那唯一不会随模型规模扩展的资源的方式。请参阅 [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md)。

| 维护问题 | AKC 的回应 |
|------|------------|
| 技能陈旧 | skill-stocktake 周期性审计质量 |
| 规则与实际脱节 | skill-comply 测量真实的行为遵循率 |
| 知识散落 | rules-distill 把反复出现的模式提升为原则 |
| 文档漂移 | context-sync 检测角色重叠与陈旧内容 |
| 重复造轮子 | search-first 先确认是否已有现成方案 |
| 经验流失 | learn-eval 在质量门下提取模式 |

每一行都是周期接管了本应由人手工承担的维护任务。运行周期并非免费，但比起每次都重做同一份审计，仍要便宜得多。

### 与意图对齐，而不只是正确

正确性可以自动化 —— 测试、类型、lint、评审工具都能检查输出是否满足特定标准。对齐则无法以同样的程度自动化，因为意图本身会随着运营者在使用中磨砺出的判断而移动。一个代理可以满足所有正确性检查，却仍偏离意图。

AKC 的设计选择反映了这一区别。设计原则 #3 (Non-destructive) —— 先提议、再等待确认 —— 把每一次变更都置于一个可以重新陈述意图的检查点。实施前的对话被视为 **认知经济的投资**，而非摩擦。这一区别也解释了 AKC 与 harness engineering 的不同：harness 优化的是首次的正确性，而 AKC 让 harness 自身随着意图的变化而保持与意图对齐。分层比较请参阅 [与 Harness Engineering 的关系](#与-harness-engineering-的关系)。

### 周期同样改变着人

在反复进行 Curate 与 Promote 决策的过程中，使用者会磨砺出「什么知识值得保留」的判断力。在 Research 中，他们对「采用现成方案还是自己实现」会培养出更好的直觉。在 Measure 中，他们学到良规则与含糊愿景之间的区别。AKC 不是一个代理孤立改进的单向优化循环 —— 代理的行为与人类的判断在持续互动中共同成长。标语 —— *与塑造它的人共同成长* —— 命名的正是这一性质。

## 仓库内容

九个 ADR、八条设计原则、三个设计模式技能、两个 JSON 模式、一个约 500 行的可执行参考实现，以及只需一行 `cp` 即可装入完整周期的规则文件。AKC 定义了三层记忆与四种代码–LLM 分层模式。下方列出的六个 cycle skills 仍然是各阶段「全功能版」的有主张的实现。

AKC 发布 **两类技能**：

- **Cycle skills**（外部仓库）—— 周期的每个阶段对应一个：`search-first`、`learn-eval`、`skill-stocktake`、`rules-distill`、`skill-comply`、`context-sync`。
- **Design-pattern skills**（[`docs/skills/`](docs/skills/)）—— 与 ADR 一一对应的长篇「how」指南。横切多个阶段。

完整的仓库树与文档角色路由请参阅 [`docs/CODEMAPS/architecture.md`](docs/CODEMAPS/architecture.md)。

## 周期

AKC 由六个可组合的技能构成，周期的每个阶段对应一个：

```
Experience → learn-eval → skill-stocktake → rules-distill → Behavior change → ...
               (extract)    (curate)          (promote)            ↑
                                                            skill-comply
                                                              (measure)
                                              context-sync ← (maintain)
```

每个技能负责知识生命周期中的一个阶段：

| Skill | Phase | 作用 |
|-------|-------|------|
| [search-first](https://github.com/shimo4228/claude-skill-search-first) | Research | 广泛搜索，按信号筛选 —— 仅吸收能改变下一步行动的信息 |
| [learn-eval](https://github.com/shimo4228/claude-skill-learn-eval) | Extract | 从会话中提取可复用模式，附带质量门 |
| [skill-stocktake](https://github.com/shimo4228/claude-skill-stocktake) | Curate | 审计已安装技能的陈旧、冲突与冗余 |
| [rules-distill](https://github.com/shimo4228/claude-skill-rules-distill) | Promote | 将技能中的横切原则蒸馏为规则 |
| [skill-comply](https://github.com/shimo4228/claude-skill-comply) | Measure | 测试代理是否真的遵循其技能与规则 |
| [context-sync](https://github.com/shimo4228/claude-skill-context-sync) | Maintain | 审计文档的角色重叠、陈旧内容与缺失的决策记录 |

## Rules —— 不安装技能也能装入周期

并不需要全部六个技能才能让周期运转。[`docs/akc-cycle.md`](docs/akc-cycle.md) 把六个阶段蒸馏成任何 AI 代理都能通过自然对话遵循的行为原则。

### 快速安装

```bash
# 复制到代理的 rules 目录
cp docs/akc-cycle.md ~/.claude/rules/common/akc-cycle.md
```

仅此而已。周期将通过对话运转 —— 无需技能、插件或 CLI 工具。

### 规则覆盖的内容

| Phase | 规则要点 |
|-------|----------|
| Research | 广泛搜索，按信号筛选 —— 仅吸收能改变下一步行动的信息 |
| Extract | 从会话中以质量评估捕获可复用模式 |
| Curate | 定期审计冗余、陈旧与沉默 |
| Promote | 将出现 3 次以上的模式提升至规则层 |
| Measure | 用定量方式而非主观感受验证行为变化 |
| Maintain | 保持文档角色清晰，内容新鲜 |

### Skills vs Rules

- **Skills** 提供每个阶段深入、分步的工作流。当你想要被引导执行时安装它们。
- **Rules** 提供原则与触发条件。当你希望周期自然地从对话中浮现时安装它们。
- 两者可以并存。Rules 确保即使技能未被触发，周期也能运转。

## 设计原则

1. **Composable** —— 每个技能独立工作。可以只用一个，也可以六个全用。
2. **Observable** —— skill-comply 输出定量遵循率，而非主观评价。
3. **Non-destructive** —— 每个技能都是先提议变更并等待确认。没有任何东西会被自动应用。
4. **Tool-agnostic in concept** —— 为 Claude Code 设计，但其架构适用于任何具有持久配置的代理。
5. **Evaluation scales with model capability** —— 小模型受益于规则化打分；推理模型（Opus 级）则用完整上下文与质性判断进行评估。AKC 不强制单一方法 —— 它将评估深度与模型的推理能力相匹配。
6. **Scaffold dissolution** —— 技能是脚手架。当用户与代理把周期内化后，技能不再必要，仅靠规则即可维持循环。请参阅 [docs/scaffold-dissolution.md](docs/scaffold-dissolution.md)。
7. **Code-LLM Layering** —— 代码拥有确定性、可审计性与控制流。LLM 拥有语义。明确地分层；永远不要让 LLM 持有持久状态或决定终止条件。请参阅 [ADR-0008](docs/adr/0008-code-and-llm-collaboration.md)。
8. **Human cognitive resource is the bottleneck** —— 随着代理能力提升，稀缺资源已不是算力或上下文，而是人的注意力与判断。每个阶段都被塑造为守护这份预算：Research 中的 signal-first 吸收、用规则提升以避免重做同一决策、用遵循度测量以避免人工再审计，以及前置对话 —— 因为错位实现的代价高于本可预防它的对话。请参阅 [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md)。
9. **Genre neutrality** —— 循环是机制，而非内容。同样的六个阶段在代理知识的任何连贯主体上运作 —— 行为模式、领域专长或宪法性价值 —— AKC 不对下游项目关心哪一种采取立场。每种类型变化的是评估标准、提示模板和审计查询；阶段本身保持不变。请参阅 [ADR-0011](docs/adr/0011-cycle-applies-to-any-knowledge-body.md)。

## 与 Harness Engineering 的关系

AKC 与 [harness engineering](https://mitchellh.com/writing/my-ai-adoption-journey)（Mitchell Hashimoto, 2025）—— 通过改良提示（如 AGENTS.md 更新）与可编程工具（脚本、验证命令）的组合，让代理不再重复同一错误的工程实践 —— 共享共同地基。两者都旨在让代理更可靠，但关注点不同。

| 层 | 提问 | 由谁回应 |
|----|------|---------|
| Harness | 「这个输出对吗？」 | 单独的 lint、测试、脚本 |
| AKC | 「这些 harness 本身仍然有效吗？」 | skill-comply、skill-stocktake、context-sync |

**正确性 vs 意图对齐。** harness engineering 关注一次性获得正确结果 —— 通过更好的指令与自动检查防止已知错误。AKC 更在意另一个问题：代理的行为是否与运营者不断变化的意图保持对齐？这一论点的独立展开请参阅 [为什么是 AKC → 与意图对齐](#与意图对齐而不只是正确)。

**反应式 vs 主动式。** harness engineering 本质上是反应式的 —— 每出现一次错误就新增一个 harness。AKC 的 skill-comply 与 skill-stocktake 采取主动姿态，定期审计技能与规则是否仍被遵循、是否仍然适用。设计原则 #5 让评估随模型能力扩展 —— 小模型用 rubric，前沿模型用整体性判断。

## 自定义

上述参考实现只是起点。请尽情 fork、改写、按你的代理与工作流调整。AKC 定义的是周期，不是实现。重要的是各阶段（extract → curate → promote → measure → maintain）形成一个闭合循环，而非各阶段如何构建。

## 出处

这一架构由 Tatsuya Shimomoto（[@shimo4228](https://github.com/shimo4228)）于 2026 年 2 月首次提出并实现。

最初的五个技能于 2026 年 2 月至 3 月间贡献给了 [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code)。context-sync 则是独立开发的。

## 引用方式

如果你使用或引用 Agent Knowledge Cycle 架构，请引用：

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

## 相关项目

- [Contemplative Agent](https://github.com/shimo4228/contemplative-agent) ——
  一个独立研究仓库，在本地 9B 模型上探索 Contemplative Constitutional AI。
  其工程基础（三层记忆、两阶段蒸馏）正是为 AKC 的 ADR
  播下种子的先行研究。详情见 [`docs/inspiration.md`](docs/inspiration.md)。
- [Agent Attribution Practice (AAP)](https://github.com/shimo4228/agent-attribution-practice) ——
  姐妹类型库 (DOI [10.5281/zenodo.19652014](https://doi.org/10.5281/zenodo.19652014))。
  AKC v2.0.0 抽出的安全三件套（ADR-0001、ADR-0006、ADR-0007）
  在那里与另外五条 ADR 一起被重新表达为八条 harness-neutral 的 ADR ——
  关于自主 AI 代理中问责分配的判断。
  AKC 是循环（机制），AAP 是实践（内容）。
- [Zenn 上的文章](https://zenn.dev/shimo4228) —— 开发日记（日文）
- [Dev.to 上的文章](https://dev.to/shimo4228) —— 英文版

## 致谢

AKC 站立在 [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code)（[@affaan-m](https://github.com/affaan-m)）的地基之上。ECC 是我每天使用的基础 harness，其技能与规则给了我一个丰富的起点。在数月的日常使用中，我在 ECC 之上叠加了自己的技能与规则，它们以我跟不上的速度增殖 —— 技能陈旧、规则开始相互矛盾、文档与代码渐行渐远。我不得不持续审计这片混乱，决定保留什么、合并什么、把什么提升为持久的规则。六阶段周期，正是我一旦看清这件反复进行的维护工作的形状之后，对那个形状的命名。

没有 ECC 这个立足点，AKC 不会存在。向 affaan-m 与每一位 ECC 贡献者致以深深的谢意。

## References

AKC 来自实践，而非理论。下列著作并未在上述过程中被参考，但所形成的周期似乎与其中的观念之间存在某种共鸣。这里列出，供有兴趣的读者品味这种共鸣。

- [Mind in Life](https://www.hup.harvard.edu/books/9780674057517)（Evan Thompson, 2007）——
  人与代理之间的双向循环，与生成主义中的「结构耦合」
  概念有某种共通之处。
- [A Beautiful Loop: An Active Inference Theory of Consciousness](https://www.sciencedirect.com/science/article/pii/S0149763425002970)
  （Laukkonen, Friston, & Chandaria, 2025）—— 人类通过观察代理的实际行为
  来更新规则与技能的过程，隐约让人联想到一个递归自我建模循环。

## License

MIT
