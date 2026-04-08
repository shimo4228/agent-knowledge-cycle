# Adapted from contemplative-agent
# (https://github.com/shimo4228/contemplative-agent) at commit 2dbde9d.
# Stripped of project-specific content. This file is an independent,
# harness-neutral reference for AKC. See docs/adr/0004-two-stage-distill-pipeline.md.
"""Two-stage distill pipeline: free-form reasoning → structured format.

Stage 1 is exploratory: the LLM reads raw episodes and thinks out loud.
Stage 2 is strict: the Stage-1 prose is rewritten as structured patterns.

This module is LLM-agnostic. Callers pass a `generate` callable with the
signature (prompt: str) -> str. For local development, pass a fake that
echoes deterministic output. For production, wire it to your model of
choice.

Templates are just strings. Swap them to change what the distillation
looks for without rewriting the pipeline.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import Callable

from .episode_log import EpisodeLog
from .knowledge_store import KnowledgeStore

logger = logging.getLogger(__name__)

GenerateFn = Callable[[str], str]


# Stage 1 — minimal, exploratory. No schema, no length limit.
DEFAULT_STAGE1_TEMPLATE = """\
Below is a batch of agent episodes. Read them carefully and write a
reflection: what patterns recur, what surprised you, what the agent should
remember next time. Think out loud. Do not format as JSON.

<untrusted_content>
{episodes}
</untrusted_content>
"""

# Stage 2 — strict. Full schema, no semantic discovery.
DEFAULT_STAGE2_TEMPLATE = """\
Rewrite the following reflection as a JSON array of pattern objects. Each
object must have exactly these fields:
  - "pattern": a concise, actionable statement (string)
  - "importance": a number in [0.0, 1.0]
  - "category": one of "important", "uncategorized", "noise"

Return only the JSON array, no prose.

<reflection>
{reflection}
</reflection>
"""


@dataclass
class DistillResult:
    stage1_reflection: str
    stage2_patterns: list[dict]
    added: int


def _format_episodes(records: list[dict]) -> str:
    return "\n".join(
        json.dumps(r, ensure_ascii=False) for r in records
    )


def _parse_stage2(raw: str) -> list[dict]:
    """Parse Stage 2 output. Tolerant of surrounding whitespace."""
    text = raw.strip()
    # Strip common code fences if the model insists on them.
    if text.startswith("```"):
        text = text.strip("`")
        # Drop an optional language tag on the first line.
        first_newline = text.find("\n")
        if first_newline != -1:
            text = text[first_newline + 1 :]
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        logger.warning("Stage 2 output is not valid JSON: %s", exc)
        return []
    if not isinstance(data, list):
        logger.warning("Stage 2 output is not a JSON array")
        return []
    return [item for item in data if isinstance(item, dict)]


def distill(
    log: EpisodeLog,
    store: KnowledgeStore,
    generate: GenerateFn,
    days: int = 1,
    stage1_template: str = DEFAULT_STAGE1_TEMPLATE,
    stage2_template: str = DEFAULT_STAGE2_TEMPLATE,
) -> DistillResult:
    """Run the two-stage distill pipeline and update the knowledge store.

    Returns a DistillResult describing what happened. Does NOT save the
    store to disk — the caller decides when to persist (so dry runs are
    cheap).
    """
    records = log.read_range(days=days)
    episodes = _format_episodes(records)

    # Stage 1 — free-form reflection.
    stage1_prompt = stage1_template.format(episodes=episodes)
    reflection = generate(stage1_prompt)

    # Stage 2 — structured rewrite.
    stage2_prompt = stage2_template.format(reflection=reflection)
    raw = generate(stage2_prompt)
    parsed = _parse_stage2(raw)

    added = 0
    for item in parsed:
        pattern = item.get("pattern")
        if not isinstance(pattern, str) or not pattern.strip():
            continue
        store.add(
            pattern=pattern.strip(),
            importance=float(item.get("importance", 0.5)),
            category=str(item.get("category", "uncategorized")),
        )
        added += 1

    return DistillResult(
        stage1_reflection=reflection,
        stage2_patterns=parsed,
        added=added,
    )
