---
name: signal-first-research
description: Design guide for a research intake filter that admits only information likely to change your next action. Use when you are about to build a recurring research workflow (daily digest, news stream, topic monitor, literature feed) and the default question "what should I read?" keeps producing too much. Covers the define-signal-first rule, three worked examples, and a diagnostic checklist for telling a healthy filter from a lazy one.
user-invocable: true
---

# Signal-First Research

Most "stay current" workflows fail in one of two directions:

- **Volume bias.** You wire up ten sources, aggregate everything, and trust yourself to skim. Within weeks the backlog outruns your reading time; the system has become a guilt queue. The filter lives inside your head and degrades on tired days.
- **False-abstinence.** You give up on breadth entirely and read nothing, because sorting what matters feels more expensive than ignoring everything. You miss things you would have acted on.

A signal-first Research workflow refuses both. It searches widely — *no* source is excluded upfront — but admits each piece of information through a question the reader must answer *before* accepting it: **would this change what I do next?** If the answer is no, the filter drops the item at intake, not at read-time.

This skill is the design pattern for that filter, plus examples of three ways to shape it and a diagnostic checklist for spotting filters that have quietly broken.

---

## The core rule: define the signal before the search

Most research workflows collapse because the signal is defined *after* the search — "I'll know it when I see it." The volume of "maybes" then dominates the volume of "yeses," and the reader burns judgment budget classifying things they could have skipped.

The reversal:

1. **Name the next action** the research is meant to inform. "I am going to decide X this week" / "I want to spot weekly shifts in topic Y" / "I need to know when library Z ships a breaking change."
2. **Write the signal in terms of that action.** "A source mentions a change in Y's methodology" / "A benchmark number moves by >10%" / "Z's changelog lists a breaking change."
3. **Only admit items matching that signal.** Everything else — even interesting, even well-written — is out of scope for this pass.

Define the signal first means: the filter is a property the reader can state out loud, not a mood.

---

## The asymmetry: search wide, intake narrow

Signal-first is not "read less." It is "search more, admit less." The two behaviors have to live in different phases or the filter collapses:

- **Search phase** — generous, broad, tolerant. Cast for candidates across more sources than you think you need. Missing candidates is the expensive failure here; reading too many is cheap, because nothing has been admitted yet.
- **Intake phase** — strict, explicit, binary. Apply the signal. Each candidate is either admitted or dropped. No "maybe," no "save for later," no "I'll skim it first." Maybe-piles are the leak that kills the system.

The point of the asymmetry is that search is cheap on attention (machines can do it) and intake is expensive (only the reader can decide whether a thing matches their next action). Spending attention budget on intake is the correct use of the scarce resource; spending it on search is a misallocation.

---

## How to build yours

Before writing any code or wiring any prompt, answer these in plain language:

1. **What decision does this research inform?** If you cannot name the decision, you are building a hobby archive, not a research workflow.
2. **What item shape counts as signal?** A sentence template ("a source reports X about Y") is stronger than a topic area ("AI news").
3. **What is the minimum useful unit?** A link? A paragraph? A structured extract? Smaller units are harder to read later; larger units are cheaper to drop at intake.
4. **Where does the filter live — at intake, at archive, or at read?** Filters at read-time are imaginary filters. Filters at archive are slightly better. Filters at intake are the only ones that protect attention.
5. **What is the escape hatch?** A purely strict filter will miss novel signals. Design a deliberate exploration mode (see Example 3 below) and *name* when you enter it, so exploration does not silently become the default.
6. **How will the filter get worse?** Every filter drifts. Either the signal description gets vaguer, or the reader starts admitting "interesting but not actionable" items. Plan the recalibration ritual (monthly? after every drift event?) before the drift starts.

---

## Worked example 1 — Daily topic digest

**Goal.** One short report per day summarizing the one or two things worth acting on in a specific domain.

**Shape of the filter.**

- Search phase (automated): query 20–30 sources, collect 40–60 candidate items.
- Scoring phase (model-led): score each candidate against a named signal — e.g., "discussing a change in methodology, tooling, or benchmark that would plausibly affect what the reader builds next week."
- Intake phase (strict): admit only the top-N (N = 1 or 2). Everything else is dropped. Not stored for later, not summarized in an appendix — dropped.

**Why this shape.** Top-N with a hard cap enforces the asymmetry. If N = 5 sneaks in as "oh, just in case," the filter has lost. The hard cap is the architectural ally of the rule.

**Failure mode to watch.** Scope creep in the signal description. If the signal drifts to "anything interesting in the domain," the system becomes a volume feed again. Quarterly audit: re-read the signal description and check whether the actual admitted items match it.

---

## Worked example 2 — Session-scoped filter

**Goal.** Inside a single work session (say, deciding between two libraries), search generously but admit narrowly.

**Shape of the filter.**

- Before searching: write down the specific decision being made. "Which of library A or library B handles my use case without introducing a Python dependency."
- Search: broad — official docs, issues, changelogs, adjacent discussions.
- Intake: admit only content that names A, B, or the specific dependency constraint. Skim-drop everything else inside 30 seconds.
- No deferred reads. At end of session, the search history is discarded; anything not admitted is gone.

**Why this shape.** Session-scoped work has a natural end point (the decision). The filter can be strict because the scope is small. Deferred reads are the trap: they turn a 1-hour task into a 1-week reading project.

**Failure mode to watch.** The reader's attention sliding into adjacent-but-unrelated topics. Even a good signal cannot save a reader who keeps re-orienting to "oh, that's interesting." Set a timer or a cost cap.

---

## Worked example 3 — Exploration mode (breaking the rule on purpose)

**Goal.** Learn a new domain or deliberately widen the intake to find signals the strict filter would miss.

**Shape of the filter.**

- Named entry: the reader explicitly declares "this is an exploration pass, not a normal research pass."
- Broader intake: the signal is temporarily relaxed to "anything that seems novel in this new domain."
- Time-boxed: exploration passes have a hard duration (e.g., one week, five sessions) and convert their output into either a new strict signal or a discarded detour.
- No silent drift: at the end of the exploration pass, the reader must decide — either (a) keep the expanded signal as the new default, or (b) drop back to the prior filter. Ambiguous "I'll see" outcomes mean the filter is actually broken.

**Why this shape.** Signal-first without exploration becomes rigid and blind to new domains. The rule is "default is strict, exploration is a named exception." Forbidding exploration is as bad as having no filter at all.

**Failure mode to watch.** Exploration as a fig leaf — the reader stays in exploration mode indefinitely and calls their regular unfiltered reading "exploration." Make the exit criterion concrete and dated.

---

## Diagnostic checklist

Apply to any existing research workflow. More than two "no" answers means the filter is broken.

1. **Can you state the signal in one sentence that references a decision or action?**
2. **Is there a hard numerical cap on what gets admitted per cycle?**
3. **When an item is dropped, is it *gone* — not saved in a "later" queue?**
4. **Is exploration mode a named, time-boxed exception rather than the default?**
5. **Has the signal description been revisited in the last three months?**
6. **Does the reader actually act on admitted items at a rate higher than rejected items? (If action rates are equal, the filter is doing nothing.)**

---

## Why the naming matters: signal-first vs. archive-first

Two architecturally different systems get lumped together under "research workflow":

- **Archive-first.** Everything collected is stored; filtering happens when the reader decides to read. The filter is invisible, personal, and degrades with fatigue. Capacity is defined by storage.
- **Signal-first.** Items are either admitted or dropped at intake. The filter is explicit, external to the reader's mood, and constant across days. Capacity is defined by attention.

The two have opposite relationships to information volume. Archive-first scales badly with volume — more input, more backlog, more guilt. Signal-first is indifferent to volume — search can grow indefinitely, intake stays constant, the reader is protected from the growth.

This is not a preference. It is a decision about which resource you are optimizing: storage or attention. Most readers optimize attention accidentally, by dropping workflows when the backlog wins. Signal-first is the deliberate version.

---

## Related AKC decisions

- [ADR-0010 Human Cognitive Resource as Central Constraint](../adr/0010-human-cognitive-resource-as-central-constraint.md) — the principle this skill is the "how" counterpart to. ADR-0010 states *why* signal-first intake matters (attention is the scarce resource); this skill shows *how* to build a filter that honors that principle.
- [`docs/inspiration.md`](../inspiration.md) — for one lived instance of the pattern and the causal chain it produced.
