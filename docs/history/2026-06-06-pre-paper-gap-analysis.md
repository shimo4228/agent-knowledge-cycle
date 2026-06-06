Confirmed: highest existing ADR is 0012, next free number is 0013, gaps at 0001/0006/0007 are intentional, and exactly two READMEs (en + ja) exist. The data anchors hold. Here is the report.

---

# AKC 論文化前ギャップ分析 — 統合レポート

## 1. Executive Summary

AKC の mechanism layer は v2.0.0 で骨格が固定され、6 phases / 3 memory layers / 4 patterns / 9 ADRs の判断 lineage は安定している。だが position paper として deposit するには、現状は **mechanism の片面だけが書かれている** 状態にある。最大の構造的欠落は 2 つ — (1) three core themes のうち Theme 3 (bidirectional growth) が一方向の楽観的主張のままで failure-mode theory を持たず、reviewer の最も明白な反論 (gate は rubber stamp ではないか) を pre-empt できていない。(2) agent-memory / skill-learning literature (CoALA, Voyager, MemGPT, Generative Agents 等) に対する related-work positioning が完全に欠落し、自分の sibling しか引いていないため、Extract / Curate / Promote が既存 operation の再発明だという desk-rejection リスクを抱える。

これらは「足りない実装」ではなく「言語化されていない mechanism judgment」であり、いずれも scaffold dissolution を生き残る judgment-level の内容で、AKC の role boundary 内に収まる。加えて、Human Approval Gate を autonomous-promotion の field default に対する **central contribution** として昇格させる作業 (ADR-0005 の addendum) が、論文の novelty 主張を支える。残りは repo 完全性 (self-reingestion echo loop、demotion の不在、Measure の実証ゼロ) と boundary-audit 系の hygiene fix (principle count 8 vs 9、CODEMAPS の guard↔filter 反転、AAP ADR count drift) に分かれる。論文の骨格を埋める作業と repo hygiene は分離可能で、前者を先に走らせるのが正しい順序である。

---

## 2. 確証された gap 一覧 (優先度順)

優先度区分: **P0 = 論文の骨格に直接効く / P1 = repo 完全性 (mechanism の honest さ) / P2 = boundary hygiene (5 分で reviewer が見つける self-contradiction)**。

---

### P0-1. Theme 3 の failure-mode theory が存在しない (bidirectional loop の dark side)

**何が欠けているか** — AKC は human-changing loop を純粋に楽観的に枠づけ ("judgment sharpens session by session")、repo 全体に limitations section が一つもない。dark-side literature は逆の帰結を予測し、AKC 自身の mechanism を直撃する: (a) automation bias / complacency — 信頼できる agent が ADR-0005 の gate でまさに rubber-stamping を誘発、Theme 1 の attention load 下で最悪化する。(b) deskilling — over-delegation が supervise に必要な tacit expertise を萎縮させ、loop の human 側を崩壊させる。(c) delegation-feedback divergence — growth loop の failure-twin。

**Evidence** — repo grep で `limitation` / `failure mode` / `deskilling` / `automation bias` がゼロ match。`docs/adr/0005-human-approval-gate.md` は meaningful human evaluation を仮定し complacency theory を持たない。`README.md` の Theme 3 は positive framing のみ。`graph.jsonld` の `bidirectional-growth-loop` node も downside ゼロ。

**更新先** — 新規 `docs/adr/0013-failure-modes-of-the-bidirectional-loop.md` (Status: **experimental**) / `README.md` に `## Limitations` H2 / `llms-full.txt` に Q&A 1 件 / `graph.jsonld` に `concept/loop-failure-modes` node。

**具体的内容** — ADR は 6-section format。Context で Theme 3 が一方向に枠づけられていたことを明示し、3 つの mechanism-level failure mode を命名 (gate complacency / deskilling / delegation divergence)。Decision で AKC の構造的防御を articulate: (a) Human Approval Gate は runaway coevolution に対する **circuit-breaker** であり "auto-approve after N days" path を持たない、(b) curate / promote は passive consumption ではなく **active judgment act** — これが AKC の anti-deskilling 論証、(c) gate は yes/no click でなく **articulation を強制** する (planning.md の Step-0 user-visible-text pattern と同型)。Lineage を ADR-0005 / ADR-0010 (Theme 1 の load が complacency amplifier) に接続。**重要**: Eliav 2026 / Parasuraman & Manzey / Shen et al. の重い citation は paper-stage material。ADR は mechanism-level に留め、full citation apparatus は将来の position paper に予約する。

---

### P0-2. agent-memory / skill-learning literature への related-work positioning が皆無

**何が欠けているか** — Related Work と References が著者自身の repo (contemplative-agent, AAP)、Hashimoto の harness engineering、2 つの post-hoc philosophical resonance (Mind in Life, Laukkonen) しか引いていない。README は theory を disclaim する ("AKC was built from practice, not theory. The following works were not consulted")。だが最も近い precedent — Voyager skill library (= Extract+Promote)、Generative Agents reflection (= autonomous Promote)、CoALA の episodic/semantic/procedural taxonomy (AKC の 3 layer が最も似る構造)、MemGPT (autonomous curation)、LangMem (gate なしの self-editing rules)、ReMe (distill+reuse+utility-prune が Extract/Curate に 1:1)、AWM (workflow induction = autonomous Promote) — のいずれも acknowledge されていない。

**Evidence** — CoALA/Voyager/MemGPT/Generative Agents/LangMem/ReMe/AWM の grep が全 `.md`/`.txt`/`.jsonld` でゼロ match。`graph.jsonld` の ResearchLine node は 4 つ全て著者自身の work。一方 ADR-0009 は Meta-Harness (Lee et al.) を **名指しで** Alternatives に置いており、literature-aware delta articulation は in-scope であることが証明済み — memory/skill-learning 軸だけが blind spot。

**更新先** — 新規 `docs/adr/0013-positioning-within-agent-memory-literature.md` (Status: accepted) / README Related Work の rewrite / `llms-full.txt` に Q&A + Prior Research References table 拡張 / `graph.jsonld` に prior-art ResearchLine node + contrast edge / README.ja.md mirror / ADR index + CODEMAPS 更新。

**具体的内容** — ADR で (a) Promote / Curate / Extract は **isolated operation としては novel でない** ことを concede し operation ごとに precedent を命名、(b) AKC の真の delta を共有軸上に locate: これらは operation を **autonomous に走らせ agent/context 側を最適化** するのに対し、AKC は **structural human approval gate** を挿入し、**bidirectional human-judgment growth** を target にし、scarce resource を context-window economy でなく **human attention** と枠づける (= three core themes そのもの)、(c) ADR-0009 を cross-reference し、harness-layer positioning でなく **orthogonal な memory/skill-learning 軸** を埋めることを明示。citation format (arXiv ID / DOI consistency) は citation-formatter 経由で通す — これが repo 初の external academic citation at scale。

> **注**: P0-1 と P0-2 は両方とも「次の free number 0013」を proposedAction で要求している。**番号衝突に注意**。下の next steps で 0013 / 0014 の割り当てを確定する。

---

### P0-3. Human Approval Gate を central contribution に昇格させる (ADR-0005 modify)

**何が欠けているか** — AKC の genuine かつ rare な delta は、cross-layer promotion が **named human sign-off を要求** する点 (ADR-0005)。Voyager/Reflexion/ExpeL/Generative-Agents/A-MEM/Mem0/LangMem/AWM/ReMe は全て agent が何を keep するか決め、human-in-the-loop を optional safety guardrail 扱いする。だが ADR-0005 は gate の存在と structural である理由を述べるだけで、**autonomous-promotion norm に対する primary scientific contribution として gate を枠づけていない**。scalable-oversight literature への grounding もない。

**Evidence** — Voyager/Reflexion/ExpeL/A-MEM/Mem0/LangMem/scalable-oversight/variance-inequality/intrinsic-metacognition/HyperAgents の grep が全 corpus でゼロ。著者自身の production daily-research note (2026-05-24: Promote は external memory で埋められない / 2026-05-23: Claude Dreaming は Extract/Curate のみで Promote を持たない) が saturation limit を裏づける。

**更新先** — `docs/adr/0005-human-approval-gate.md` に "Why the gate is the contribution, not a guardrail" addendum (Consequences 後・Inspired-by footer 前)。ADR-0009 から forward link。README に autonomous-promotion default / platform memory feature への contrast entry。

**具体的内容** — 3 threads: (1) **Autonomous-promotion contrast** — self-evolving-agent corpus を命名し、AKC がこれを inverts する (promotion が named human sign-off を要求) と明示。(2) **External grounding** — scalable-oversight literature と Generator-Verifier variance-inequality (verifier noise が閾値超で recursive error amplification) を gate が load-bearing である formal/empirical 理由として引く。(3) **Extrinsic-vs-intrinsic metacognition** — AKC の Promote は設計上 refined extrinsic metacognitive mechanism (Liu & van der Schaar, ICML 2025, arXiv:2506.05109)。Dreaming は output が常に memory で rules でも weights でもないため、Promote は intrinsic-metacognition literature が予測する saturation point に達する。non-autonomy を欠落 feature でなく **deliberate architectural stance** として枠づける。

> **scoping 警告 (verdict より)**: 著者の 2026-06-04 note を wholesale で AKC ADR に lift してはならない。あの note は明示的に **contemplative-agent (CA) 向け** の ADR を提案し CCAI Mindfulness clause (substrate layer) に紐づく。AKC-located evidence は 2026-05-24 / 2026-05-23 の 2 note のみ。これらから addendum を組む。

---

### P1-1. Self-reingestion echo loop の failure-mode theory が欠如

**何が欠けているか** — 3-layer distillation は毎 iteration で下層 output を再読 (log→knowledge→skill→rule) し、promote された artifact は次 session に context として再投入される。cycle は自分の distilled output を継続的に re-ingest するが、AKC core はこれが degenerate する条件の theory を持たず、immutable episode log を pristine source として扱い、promote された各 layer が LLM-generated content の write であり input に再投入される事実を命名しない。sibling は既にこれを最深の distillation failure mode として documented: self-conditioning echo loop が "thickens from within, undilutable from outside" (CA ADR-0050)、summary-of-summary compression chain からの jargon convergence (CA ADR-0052)。

**Evidence** — `contemplative-moltbook/docs/adr/0050` (epistemic taxonomy {observed, generated})、`0052` (3-hop chain が grounding を失う)、`agent-attribution-practice/docs/adr/0003` (taint inheritance)、AKC `README.md` L48-49 (loop を純粋に corrective と枠づけ)。grep で `0050`/`0052`/`epistemic`/`echo`/`thicken` がゼロ。`untrusted` は security-triplet-extraction 文脈のみ。

**更新先** — 新規 `docs/adr/0013-loop-failure-modes-self-reingestion.md` (Status: **experimental**) / `docs/akc-cycle.md` の Measure 下に "Failure modes" subsection / `docs/adr/0003` の Consequences に 1 bullet / `graph.jsonld` に Concept node。

**具体的内容** — Decision (mechanism-level, genre-neutral): (1) immutable episode log (Layer 1) のみが observed ground、上の distilled 層は全て generated で re-read 時に fresh observation 扱いしない、(2) **observed-vs-generated composition signal** を Measure-phase concern として導入 (promoted artifact の input のうち self-generated narrative の割合を track)、(3) Human Approval Gate を self-reingestion loop を collapse 下に保つ **structural circuit-breaker** として枠づける。Lineage は CA ADR-0050/0052 + AAP ADR-0003。**重要 (verdict より)**: deep-research の "Variance Inequality" を gate の **formal foundation** として import してはならない (personal Obsidian vault、peer-reviewed でない)。言及するなら external analog として、proof としてではなく。

---

### P1-2. Promotion の dark side と inverse の不在 (demotion / rule decay / scoping)

> **著者判断 (2026-06-06): 実装後に取り下げ — WITHDRAWN**。一度 ADR-0016 として実装したが同日撤回。理由: (1) rules は実践で既に対話的に整理・退役されている (rules-stocktake、retirement-over-deletion 習慣) — 「退役手段がない」は閉じた自律ループ前提の overclaim (2) incident n=0 で、この gap の根は観測された痛みではなく対称性論証 (gap 分析 lens の示唆語「demotion」由来)。唯一の実痛み (rule leakage) は ADR 自身が unsolved と認める scope 外部分。「rules 層の整理は人間の関与なしには困難」という観察は、痛みの記録が揃った時点で ADR 化を再検討。akc-cycle.md には実践記述 (archive over delete + 同一 gate) の 1 文のみ残した — がその 1 文も後の review で削除 (git 管理下では deletion 自体が lineage を保持するため archive 句は冗長)。旧 0017 (measuring) は 0016 に繰り上げ。

**何が欠けているか** — AKC は Promote (memory→skills→rules, upward) を定義するが symmetric な downward operation を持たない。(1) **No inverse**: gate を通過した rule は、supporting evidence が再発しなくなっても weaken / expire / 下層返却する path を持たない。非対称は structural — Layer 2 (knowledge) は time-decay (importance × 0.95^days) を持つが Layer 3 (rules) は decay analogue がなく、approve されたら永久に full strength で毎 session load される。(2) **Leakage**: promote された rule は applicability と side effect の両方を広げる (zenn essay の worked example: testing.md の 80% coverage rule が常時 load され README に無意味な数値を書かせ、rule-calls-rule proliferation を起こした — unsolved need は "rules need a scoping mechanism")。

**Evidence** — `docs/adr/0003` (Layer 2 decay / Layer 3 no decay / one-directional promotion)、`docs/akc-cycle.md` (Promote は "Elevate" のみ)、`zenn-content/articles/agent-essence-is-memory.md` (leakage の worked example)、harness ADR-0004/0005 ("retirement over deletion" を実践しているが AKC core に mechanism なし)、harness ADR-0008 (rules/ が recursively full load される)。

**更新先** — 新規 `docs/adr/0013-demotion-and-rule-retirement.md` / `docs/akc-cycle.md` の Promote に dark-side caveat + Curate に demote/retire clause / `graph.jsonld` に demotion node + "rule scoping (unsolved)" honest-limitation node。

**具体的内容** — Decision: ADR-0005 の gate と parallel な demotion/retirement operation を定義 — retirement over deletion (`_archived/` に移し lineage 保持)、同じ Human Approval Gate で gate、拡張された Curate audit で surface。Consequences で **rule-scoping を explicitly UNSOLVED problem として記録** (essay の leakage example は reference のみ、inline content は core に入れない)。**scoping 注意 (verdict より)**: scaffold-dissolution.md は rules を **durable substrate** として扱う ("Cycle persistence depends on rules and memory, not skills") ため、この ADR を scaffold-dissolution thesis 経由で枠づけてはならない。dissolution は skills 層を target にする。あくまで「cycle が ratchet でなく cycle であるための inverse operation」として枠づける。

---

### P1-3. Measure phase に cycle 稼働の実証がほぼゼロ + agent text を観測する必要 (modify)

**何が欠けているか** — AKC は Measure が "quantitative compliance rates, not subjective assessments" を produce すると繰り返すが (README DP#2)、repo 内の唯一の quantitative artifact は ADR-0010 の geo-writer GEO snapshot — README の documentation-SEO 測定であって、skill/rule が実際に follow されているかの測定ではない。さらに akc-cycle.md と llms-full.txt は Measure を action-observable signal のみで定義 ("tool call sequences, outputs, test results") するが、skill-comply は **thinking-centric phase (Research, Curate) が tool call のみ観測すると systematically under-score される** ことを発見した (search-first を 8% と測定、実際は scout + 18 searches + adopt/implement/test を完了済みだった)。fix (text を pseudo-event に昇格 + observability constraint) が 8%→56% に lift。

**Evidence** — `docs/adr/0010` の geo-writer snapshot / `README.md` L194 (compliance rate の claim, in-repo data なし) / `docs/akc-cycle.md:58` / `llms-full.txt:65` / `claude-skill-comply/CHANGELOG.md` v0.2.0 (8%→56% text-observability fix)。

**更新先** — `docs/akc-cycle.md` Measure section (text 観測 clause 追加) / 新規 `docs/adr/0013-measuring-thinking-centric-phases.md` / `graph.jsonld:116` Measure node + `llms-full.txt:65` 更新 / README DP#2 sharpen。

**具体的内容 (verdict による reframe)** — text-observability refinement を **mechanism-level Measure constraint** として採用するが、"evidence" 部分は in-repo case study でなく **descriptive pointer** に格下げ。akc-cycle.md に「Measure instrument は tool call だけでなく agent text (reasoning, verdicts, plans) も observable にしなければならない。text-only な instrument は thinking-centric phase を systematically under-report する。scoring 前に text を observable event に昇格せよ」を追加。ADR は falsifiable claim として枠づけ、Theme 2 (reasoning 内の intent alignment vs tool call 経由の correctness) に明示的に紐づける。**DROP (verdict より)**: `examples/measure_case_study/` に 8%→56% before/after table を複製する案は drift-prone duplication なので採用しない。skill-comply の CHANGELOG を canonical worked-measurement record として pointer する。

---

### P1-4. Stale-input precondition の不在 (audit/measurement phase は input freshness を先に検証すべき)

> **著者判断 (2026-06-06): 実装後に取り下げ — DROPPED**。rules file の存在資格は「毎セッション行動を変える行か」。この precondition は知恵ではあるが context-sync Phase 0 が既に実装しており、rules での再記述は乗客。akc-cycle.md の blockquote と graph.jsonld の InputFreshnessPrecondition node を削除。

**何が欠けているか** — stale snapshot に対して audit/promote する phase は fiction を生む — 現在を out-of-date な picture と比較し、もう存在しない世界向けの変更を提案する。context-sync skill (Maintain の bijective binding) はこれを具体的に発見し Phase 0 pre-check を追加した (codemap freshness を verify してから他の audit を走らせる)。これは cross-cutting mechanism principle: accumulated state を読む全 phase (Curate は skill corpus、Measure は rules、Maintain は docs) が、input が stale なら fiction の上で動く脆弱性を持つ。AKC core は general な "verify input freshness first" precondition を述べていない。

**Evidence** — `.claude/skills/context-sync/SKILL.md` (Phase 0 freshness pre-check L53-92) / harness `ADR-0010` (cascade は stale codemap が fictional migration proposal を生んだため追加) / AKC `docs/akc-cycle.md` (Curate/Measure/Maintain が accumulated state を読むが input-freshness precondition なし、staleness check は content check であって input-source check ではない)。

**更新先 (modify)** — `docs/akc-cycle.md` に Curate/Measure/Maintain をカバーする shared precondition note (~3 文) / `graph.jsonld` に 1 concept triple (`InputFreshnessPrecondition`)。

**具体的内容** — 「全 audit/measurement phase は accumulated state を読む。走る前に input source が current か verify せよ。stale snapshot に対して audit する phase は stale content を **見つける** のでなく stale content に **なる**。staleness は audit するものの中に見つかるだけでなく、audit が始まる前に audit を poison しうる」。**DON'T (verdict より)**: 新規 docs/skills/ entry を作らない (one-paragraph principle に over-scaffolding)。CA ADR-0042 silent-truncation と comply v0.3 inference-budget は **別の failure class** (LLM call boundary の length/budget distortion) なので core に lift しない。concrete codemap example は skill 内に留める。

---

### P1-5. Quality/importance score を Extract phase の output として定義する (modify)

> **著者判断 (2026-06-06): AKC には反映しない — WON'T DO**。この judgment (distill 時 rate / immutable store / lazy decay / post-hoc re-scoring 拒否) は substrate-level の設計詳細であり、まず Contemplative Agent 側で問題提起・議論する。AKC core への昇格は CA 側の議論が落ち着いてから再判断。

**何が欠けているか** — Extract は "evaluate quality before saving" と言い、Layer 2 は importance score (0.0–1.0) を time-decayed retrieval に使う (ADR-0003) が、AKC core は score を Extract phase の **defined mechanism output** として specify しない (いつ・何が assign し、Curate/Promote にどう propagate するか)。CA corpus が欠落 judgment を供給: importance は episode context がまだ available な **distill 時に一度 rate**、immutable に store、read 時に lazy decay — post-hoc re-scoring は original context なしでは unreliable だから。

**Evidence** — `docs/adr/0003` (importance 0.0-1.0 は Layer 2 field だが assignment mechanism / phase ownership 未指定) / `contemplative-moltbook/docs/adr/0009-importance-score.md` (distill 時 rate / immutable store / lazy decay / post-hoc re-scoring を低精度で reject) / `.claude/skills/learn-eval/SKILL.md` (Verdict-gate)。
**更新先 (modify, 新 ADR でない)** — `docs/adr/0003-three-layer-distillation.md` の Layer 2 section に 2-3 文 / `docs/akc-cycle.md` Extract に 1 文。

**具体的内容** — importance は distill 時に一度 assign、base score として immutable に store、read 時のみ decay (× 0.95^days)、**post-hoc re-scoring は行わない** (original episode context なしで rating quality が落ちるため)。さらに Extract の save/drop **quality gate** (binary admit) と Layer-2 **importance score** (graded retrieval weight) を disambiguate — related だが distinct。AKC 自身の "immutable judgment + time-varying view" thesis に紐づける。**DON'T (verdict より)**: retain-as-seed / noise-as-seed policy、salience/REVELATION_THRESHOLD、Yogacara/FEP framing は CA substrate なので import しない。新 ADR でなく ADR-0003 の clarification に留める。

---

### P1-6. Trigger-altitude と execution model の不在 (modify)

> **著者判断 (2026-06-06): 実装後に取り下げ — DROPPED**。trigger-altitude bullet と Cadence/execution-model 節を akc-cycle.md から、ordinal=reading-order の言い換えを llms-full.txt から除去 (元の文面に復元)。

**何が欠けているか** — 6 phase は ordinal 1–6 + circular figure で sequence を示唆するが、各 phase は独立した event-based trigger で発火し、graph.jsonld は ordinal を encode するが transition edge を持たない (= order は presentation であって execution ではない)。(A) **Trigger altitude**: Extract は "capture reusable patterns" と言うが、抽出された trigger が generalize する mechanism を与えない — transient identifier (username, post ID, timestamp) で studded された auto-extracted trigger は exact past episode にしか match せず future case で発火しない。(B) **Execution model**: phase が sequential pass か asynchronous event-loop かが unstated。

**Evidence** — `graph.jsonld` L65-128 (phase は ordinal を持つが precedes/follows edge なし) / `docs/akc-cycle.md` (各 phase に独立 Trigger 行、altitude/generaliz の match なし) / CA `ADR-0048` (trigger generalization + monotonic growth + no numeric caps)。

**更新先 (modify, scope down)** — `docs/akc-cycle.md` Extract に trigger-altitude bullet 1 つ + "Cadence and execution model" note / `graph.jsonld` に transition edge (または `llms-full.txt` L103 の over-claim 修正)。

**具体的内容** — Extract に「trigger が transient identifier で studded されているとき structural altitude に generalize せよ — exact past episode にしか match しない trigger は reusable pattern ではない」。phase が独立 event-based trigger で発火 (strict 1→6 pass ではない)、ordinal は reading order であって execution sequence ではない、と明示。**EXCLUDE (verdict より)**: cadence の具体数値 ("1 layer / 10 items"、"15 days / 3 stocktakes")、no-numeric-cap anti-pattern を AKC rule として、34,198/46.3% の Skills-in-the-Wild stats — これらは instance/substrate-unresolved (CA ADR-0048 L74 自身が cadence を "separate ADR territory" と defer) なので core に入れない。

---

### P1-7. Cold-start / bootstrapping の不在 (modify)

> **著者判断 (2026-06-06): 実装後に取り下げ — DROPPED**。scaffold-dissolution の Bootstrapping 節 (en/ja) と akc-cycle.md の pointer 行を全削除。実装は (a) トリガー (目安) を機械的ゲートと誤読した「自己起動不能」論証 (b) Layer-N 語彙の漏出 (「ルール」と「Layer 3 の蒸留物」の二重計上) で崩壊。実観察 (ECC continuous-learning-v2 の records-only) は将来必要になれば 2〜3 文で再導入可。

**何が欠けているか** — 全 phase が accumulated material を前提とする (Curate は既存 skill、Promote は "3+ recurrence"、Measure は既存 rules、Extract は populated episode log)。AKC core は、空の episode log・skill なし・rules なしの fresh harness で cycle がどう始まるかを describe しない。layer が下層の pure function として定義される (ADR-0003) ため、空の Layer 1 では Layer 2,3 が空、promotion threshold は十分な session が走るまで発火できない。

**Evidence** — `docs/akc-cycle.md` L43 (Promote が "3 or more places" 要求 — fresh harness で発火不能) / `docs/adr/0003` (layer は pure function) / `docs/scaffold-dissolution.md` L63 (rebuild need は命名するが mechanism 不在) / `zenn-content/articles/ecc-journey-part3.md` (continuous-learning-v2: records-only, 0 extracted — cycle は self-start しない)。

**更新先 (modify, 新 ADR でない)** — `docs/scaffold-dissolution.md` に "Bootstrapping — how the loop starts turning" section / `docs/akc-cycle.md` から cross-link 1 行。

**具体的内容** — (1) fresh harness では Layer 2,3 と rules 層が construction 上 空、threshold-gated phase は発火不能、cycle は self-start しない。(2) bootstrap-first phase は **Extract** — single productive session で発火し prior accumulation を要さない、唯一 Layer 1→2 path に material を inject する。(3) 6 つの scaffold skill が bootstrap apparatus であり、rules が self-emerge するだけの history が貯まる前に各 phase を deliberately 走らせ、その後 dissolve する (Phase 1 ↔ Phase 3 を既存 file 内で接続)。(4) bootstrap が対抗する failure mode を命名: records-only system は observation を貯めるが Extract を deliberately 走らせないと一つも distilled pattern を produce しない。**DON'T**: 新 ADR を mint しない (judgment は ADR-0003 + scaffold-dissolution.md に既に記録済み、これは clarifying surfacing)。

---

### P2-1. Design-principle count が自己矛盾 (8 vs 9) — しかも係争中の principle が genre-neutrality

**何が欠けているか** — README L120 が "nine design principles"・L201 が #9 Genre neutrality・CODEMAPS/INDEX.md L4 が "9"。だが ADR-0009 addendum L97 ("shrink from nine to eight")・ADR-0012 L70/L101 ("eight design principles")・CHANGELOG L95/L139-141/L154 ("9 → 8")・llms-full.txt L23 ("8") は 8 と言う。原因は boundary event: v2.0.0 が Security by Absence (#7) を削除し 9→8 に renumber、その後 ADR-0011 が Genre neutrality を追加、README は #9 として戻したが prose は "eight" のまま。係争中の principle が **mechanism/content boundary marker そのもの** であるため、reviewer が principle を数えると repo が自分の boundary marker の番号で自己矛盾する。さらに深い問題: llms-full.txt L23 は 8 個を列挙しその中に Genre neutrality を **含めない** (= 載せない立場)。count 矛盾の下に分類の不一致がある。

**更新先 (modify)** — canonical count を 9 に統一して伝播。`llms-full.txt` L23 (8→9、Genre-neutrality 追加) / `ADR-0012` L70/L101 (eight→nine、ADR-0012 は ADR-0011 より後なので誤り) / CHANGELOG・ADR-0009 addendum は **historical record として非破壊** にし注記のみ / ADR-0011 に canonical 宣言 1 行 ("Genre neutrality is Design Principle #9")。README/README.ja/INDEX.md は既に 9 で正しいので改変不要。

---

### P2-2. CODEMAPS architecture.md が 4 patterns のうち guard ↔ filter を反転 + 全 surface 不整合

**何が欠けているか** — CODEMAPS architecture.md L96-100 が `guard = code precondition, rejects before LLM` / `filter = code post-condition, validates LLM output` と定義。これは canonical ADR-0008 / code-and-llm-collaboration skill (guard = LLM→Code guard = output を AFTER validate / filter = Code filter→LLM = input を BEFORE narrow) と反転。CODEMAPS は "citation を route する時に最初に読む index" (llms.txt L58) かつ primary LLM-facing surface なので、AI search engine が誤定義を emit する。

**更新先 (modify — 単純 typo fix ではない)** — verdict が repo を直接検査した結果、**3 surface が不一致** であることが判明: skill/ADR-0008 (guard=POST-LLM)、graph.jsonld L305 (guard=PRE-LLM input exclusion、別概念)、CODEMAPS L97 (guard=PRE-LLM、graph と一致)。CODEMAPS の `filter` (post-LLM) が唯一どことも match しない anomaly。**naively CODEMAPS を skill に sync すると graph.jsonld と矛盾する**。著者が canonical 定義を決定 (guard = post-LLM-output validator OR pre-LLM-input excluder、orchestrator = code-owns-loop OR LLM-owns-selection) し、不一致な全 surface (skill / ADR-0008 / graph.jsonld L297-326 / llms-full.txt / CODEMAPS) を統一。CODEMAPS Invariants list に 4-pattern 定義を追加し context-sync が future drift を flag するように。

---

### P2-3. AAP cross-reference の ADR count が stale (8 → 10)

**何が欠けているか** — verdict が candidate の 2 sub-claim を検査: **DOI 部分は FALSE** (19652013 は AAP の concept DOI で正しい — AAP 自身の llms-full.txt / CHANGELOG / README badge が確認、sibling cross-reference は version-agnostic concept DOI を指すのが正しい)。**ADR-count 部分は GENUINE**: AAP は v0.1.0 で 8 ADR だったが v0.2.0 で ADR-0009/0010 を追加し **10 ADR**。AKC は依然 "eight" / "five additional" と 5 箇所で言う。AAP 自身は既にこの drift を self-correct 済み (v0.5.0 CHANGELOG: "eight ADRs → ten")。

**更新先 (modify — count のみ、DOI は触らない)** — `README.md` L256 / `graph.jsonld` L419 / `llms.txt` L114 / `llms-full.txt` L45 (および L99 の enumeration) / `CLAUDE.md` L37。"five additional ADRs as eight" → "seven additional ADRs as ten"。**DROP**: candidate の DOI-update と "federation-DOI convention を CLAUDE.md に追加" は inverted reading なので採用しない。これは routine な Maintain-phase numeric-freshness fix。

---

### P2-4. ADR-0008 / skill に genre-specific security threat model が残留 (ADR-0011 commitment #1 と矛盾)

**何が欠けているか** — ADR-0011 commitment #1 は "no future ADR encodes domain-specific content beyond what the six phases require" と言い、v2.0.0 extraction の根拠は security/threat-model が genre-specific だったこと。だが ADR-0008 の canonical skill が prompt-injection defense を prescribe (forbidden-pattern check、"wrap both documents as untrusted content"、"every LLM input wrapped as untrusted content")。これは AAP ADR-0003 (Untrusted Content Boundary) に extract された threat model と同じ。reviewer は問える: untrusted-content handling が ADR-0008 に残すほど mechanism-neutral なら、なぜ ADR-0007 は genre-specific として extractable だったのか。

**更新先 (modify — demarcation + dangling-ref cleanup, 削除でない)** — (1) **最高価値の objective defect**: `docs/adr/0008` L121 が "Existing ADRs-0004/0005/**0007**" を dangling reference (ADR-0007 は v2.0.0 で extract 済み) → "ADRs-0004/0005" に修正。(2) ADR-0008 に 1-paragraph demarcation: guard の **structural discipline** (schema + parameterized check で validate、empty default forbidden list で ship) は mechanism、**specific threat model** (どの payload が forbidden か、adversary の姿) は content (downstream / AAP 所有)。knowledge_store.py L13-15 が既に line を operationalize していることを cite。(3) CLAUDE.md の Mechanism-only rule に 1 clause: structural guard/validation seam (empty-default, parameterized) は security control に似ても mechanism、populated threat model のみ content。**DON'T**: guard pattern を ADR-0008 から削除しない (genuine に mechanism)、concrete forbidden-pattern list を core に import しない。

---

### P2-5. CODEMAPS file-count snapshot が retired README mirror を 5 つ数えている

**何が欠けているか** — CODEMAPS architecture.md L135 (prose) は es/pt-BR/zh-CN/zh-TW mirror が 2026-05-15 に retire され README.md + README.ja.md のみ残ると document (`ls` で確認済み: 正に 2 file)。だが同 file の File-Count Snapshot L163 は依然 "README files (en + 5 mirrors) | 6"、Total (L168=38) と layout caption も retired state を反映。snapshot header は 2026-05-08 付 (= 2026-05-15 retirement より前)。直近 commit 915ec2f が同 file の retired language ref を sweep したが File-Count Snapshot 行を見逃した residual。

**更新先 (modify — chore-grade Maintain fix)** — `docs/CODEMAPS/architecture.md` File-Count Snapshot L163 "6" → "README files (en + ja mirror) | 2"、Total を recompute (README 行が 4 減)、snapshot header date を regeneration date に更新。**update-codemaps skill を re-run** して hand-patch でなく generated snapshot を current tree に合わせる。

---

## 3. 棄却された候補 (1 行ずつ — 「あれは検討したか」参照用)

- **Theme 3 が bidirectional-alignment literature (Shen et al.) を引かない** — lens mismatch: repo は paper でなく navigator/spec、"must-cite" pressure は spec repo を縛らない。Shen et al. positioning は paper-time decision。README の "not consulted" honesty posture とも衝突。
- **3 themes を falsifiable prediction として formalize** — 著者が ADR-0010 L80-81 で themes を **deliberately non-empirical** ("contemporary claim, not eternal law") と枠づけ。paper draft が repo に存在しない。Measure を meta-thesis の proof に流用すると mechanism/content boundary を侵す。
- **generalizability が single example に依存 (second instantiation なし)** — ADR-0011 が既に contemplative-agent の amend_constitution を real cross-genre instance として cite 済み。提案の fix は CA を downstream proof として surface し substrate direction を inverts (role-boundary violation) + Obsidian vault 等の private path を core に持ち込む (mechanism-only violation)。
- **conflict resolution mechanism の不在** — false: resolution mechanism は missing でなく Promote gate の human に deliberately 配置済み (ADR-0005)。提案の mechanical precedence rule は Theme 1 / ADR-0011 が禁じる value-adjudication を automate する。
- **cross-harness / multi-operator cycle** — multi-operator promotion / whose-approval は AAP ADR-0008 (One Agent One Human) の canonical territory (role-boundary)。artifact portability の Measure instrumentation 化は ADR-0009 line を侵す。residue は ADR-0010 L81 で既にカバー。
- **graph.jsonld の sibling-federation edge が非対称** — research-program-hub convention が既にこれを deliberately 解決済み (siblingOf=symmetric peer / derivesFrom=AAP→CA の named exception)。提案の fix は著者の recorded judgment (inspiration.md: CA は prior art であって downstream でない) と逆。唯一の real drift は AKC L48 の AKC→CA derivesFrom 除去だが、これは小さな graph-hygiene。

---

## 4. 論文化 readiness 評価

**現状で position paper を書き始められるか** — 部分的に Yes、だが related-work positioning (P0-2) と Theme 3 limitations (P0-1) を埋める前に書き始めるのは推奨しない。理由は 3 点。

1. **Novelty 主張が unsupported のまま**。repo は "first proposed and implemented" の novelty claim (llms-full.txt L49, README L222) を持つが、dominant な agent-memory literature に対する articulated delta がない。Extract/Curate/Promote が CoALA/Voyager/MemGPT の再発明だという最も明白な reviewer charge を pre-empt できていない。これは desk-rejectable。**P0-2 が single highest-leverage paper-readiness gap**。

2. **Limitations section が repo 全体に存在しない** (P0-1)。position paper に limitations / failure-mode theory は hard requirement。Theme 3 が 3 つの load-bearing theme の 1 つでありながら unfalsifiable な one-sided claim のまま、v2.0.0 後に成熟した deskilling/automation-bias counter-literature に丸腰で露出している。

3. **Empirical validation がほぼゼロ** (P1-3)。Measure を headline property (DP#2) として主張しながら cycle 自身の測定を一つも供給していない。ただしこれは pointer (skill-comply CHANGELOG) で緩和可能で、in-repo case study の複製は不要。

**related work positioning の状態** — 現状は著者自身の sibling (CA, AAP) + harness engineering (Hashimoto) + 2 つの post-hoc philosophical resonance のみ。ADR-0009 が Meta-Harness (Lee et al.) を名指しで Alternatives に置く前例があるため literature-aware delta articulation は in-scope と証明済みだが、**memory/skill-learning 軸が完全な blind spot**。Theme 1 の theoretical anchor (Simon 1971 / CLT / scalable-oversight) も欠落するが、これは著者の "operationalization, not philosophical novelty" stance により **resonance-style entry に留めるべき** で、"Theoretical Grounding" section を ADR-0010 に bolt するのは ADR の practice-first epistemic narrative を腐敗させる (棄却された Theme 1 anchor 候補が modify 判定なのはこの理由)。

**gap 埋めと paper 執筆のどちらが先か** — gap 埋めが先。P0-1/P0-2/P0-3 は paper の Related Work と Limitations section の骨格を直接構成する mechanism-level judgment であり、これらを ADR/README/graph に先に固定してから paper-writing に入ると、paper は repo を引くだけで Related Work が組める。逆順 (paper draft → repo backfill) は同じ judgment を 2 度書く。

---

## 5. 推奨 next steps (作業順序)

**Step 0 — ADR 番号の割り当てを確定** (作業前の 1 分)
P0-1 / P0-2 / P0-3-companion / P1-1 / P1-2 が全て "次の free number 0013" を要求しており衝突する。次の free 番号は 0013 から連番。提案する割り当て:
- `0013` = Positioning within agent-memory literature (P0-2) — paper Related Work の骨格、最優先
- `0014` = Failure modes of the bidirectional loop (P0-1) — Theme 3 dark side
- `0015` = Loop failure modes / self-reingestion echo loop (P1-1)
- `0016` = Demotion and rule retirement (P1-2)
- `0017` = Measuring thinking-centric phases (P1-3)

P0-3 (gate as contribution) は **新 ADR でなく ADR-0005 の addendum** (verdict 判定)、P1-5/P1-6/P1-7 も新 ADR でなく既存 file の modify。

**Step 1 — paper 骨格 gap (P0-1, P0-2, P0-3)**
adr-writer / citation-formatter convention 経由で 0013 (related-work) と 0014 (failure modes) を起こし、ADR-0005 に gate-as-contribution addendum を追加。3 つは README Related Work / Limitations / References に伝播する。P0-2 は repo 初の external academic citation at scale なので citation-formatter を必ず通す。番号衝突回避のため逐次。

**Step 2 — mechanism 完全性 gap (P1-1〜P1-7)**
0015/0016/0017 の新 ADR + ADR-0003/akc-cycle.md/scaffold-dissolution.md の modify 群。互いに独立なので並列可。各々で graph.jsonld の dual-update convention (concept node + edge) を守る。**重要な scoping ガード**: P1-1 で Variance Inequality を formal proof として import しない、P1-2 で scaffold-dissolution thesis 経由で枠づけない、P1-3 で 8%→56% を複製せず pointer、P1-5 で noise-as-seed を import しない、P1-6 で cadence 数値を core に入れない。

**Step 3 — boundary hygiene fix (P2-1〜P2-5)**
context-sync / update-codemaps skill で機械的に処理可能なものが多い。P2-1 (count 統一 9)、P2-3 (AAP ADR count 8→10)、P2-5 (CODEMAPS file-count) は単純 modify。P2-2 (4-pattern reconciliation) は著者が canonical 定義を決定する必要があるため human judgment 1 点が入る — 並列の他 fix と切り離す。P2-4 (ADR-0008 dangling ref + demarcation) は L121 の "0007" 除去が objective defect なので即修正可。

**Step 4 — release + paper 着手**
全 gap 埋め後、release-doi で new version DOI を mint し hf-sync で graph mirror を同期。その後 paper-ecosystem → paper-writing → paper-deposit の chain に入る。この時点で Related Work は repo の 0013 を引くだけで組め、Limitations は 0014/0015 を引くだけで組める。

**並列化サマリ**
```
Sequential: Step 0 (番号確定) → Step 1 (P0 群, 番号衝突回避で逐次)
Parallel Group A (Step 2): P1-1 | P1-2 | P1-3 | P1-5 | P1-6 | P1-7
Parallel Group B (Step 3): P2-1 | P2-3 | P2-5 | P2-4  (P2-2 は human judgment 待ちで分離)
Sequential: Step 4 (release-doi → hf-sync → paper chain)
```

**関連ファイル (絶対パス)**
- 新規 ADR 配置先: `/Users/shimomoto_tatsuya/MyAI_Lab/agent-knowledge-cycle/docs/adr/`
- modify 対象: `/Users/shimomoto_tatsuya/MyAI_Lab/agent-knowledge-cycle/docs/adr/0005-human-approval-gate.md`、`docs/adr/0003-three-layer-distillation.md`、`docs/adr/0008-code-and-llm-collaboration.md`、`docs/adr/0011-cycle-applies-to-any-knowledge-body.md`、`docs/adr/0012-front-load-three-core-themes.md`、`docs/akc-cycle.md`、`docs/scaffold-dissolution.md`、`docs/CODEMAPS/architecture.md`、`docs/CODEMAPS/INDEX.md`、`README.md`、`README.ja.md`、`llms.txt`、`llms-full.txt`、`graph.jsonld`、`CHANGELOG.md`、`CITATION.cff`、`CLAUDE.md`
- sibling lineage 参照元 (read-only): `/Users/shimomoto_tatsuya/MyAI_Lab/contemplative-moltbook/docs/adr/0050,0052,0009.md`、`/Users/shimomoto_tatsuya/MyAI_Lab/agent-attribution-practice/docs/adr/0003.md`、`/Users/shimomoto_tatsuya/MyAI_Lab/claude-skill-comply/CHANGELOG.md`
