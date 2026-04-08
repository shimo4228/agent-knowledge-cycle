"""End-to-end demo for the AKC minimal-harness reference.

Run from the repository root:

    python -m examples.minimal_harness.demo

The demo uses a fake LLM that emits deterministic output so the whole
pipeline runs without any network access, API keys, or GPU. It is
intended as a smoke test and as executable documentation of the
three-layer memory architecture (ADR-0003) and the two-stage distill
pipeline (ADR-0004).
"""

from __future__ import annotations

import json
import logging
import tempfile
from pathlib import Path

from .distill import distill
from .episode_log import EpisodeLog
from .knowledge_store import KnowledgeStore, effective_importance


def fake_llm(prompt: str) -> str:
    """Deterministic stand-in for a real LLM.

    Stage 1 receives "episodes" in the prompt and returns prose.
    Stage 2 receives "reflection" and returns a JSON array.
    """
    if "<reflection>" in prompt:
        # Stage 2 — return a fixed JSON array so parsing is exercised.
        return json.dumps(
            [
                {
                    "pattern": "The agent should summarize long user turns before responding.",
                    "importance": 0.8,
                    "category": "important",
                },
                {
                    "pattern": "Empty sessions contain no signal.",
                    "importance": 0.2,
                    "category": "noise",
                },
            ]
        )
    # Stage 1 — return free-form prose.
    return (
        "Across the session I noticed the user asked for clarification twice. "
        "The agent should summarize long user turns before responding. "
        "Otherwise the session was uneventful."
    )


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        log_dir = root / "logs"
        knowledge_path = root / "knowledge.json"

        # Layer 1 — append a few episodes.
        log = EpisodeLog(log_dir)
        log.append("session", {"user": "hello", "agent": "hi"})
        log.append("session", {"user": "can you clarify?", "agent": "sure"})
        log.append(
            "session",
            {"user": "clarify again please", "agent": "of course"},
        )

        print(f"[Layer 1] wrote {len(log.read_range(days=1))} episodes to {log_dir}")

        # Layer 2 — distill episodes into patterns.
        store = KnowledgeStore(knowledge_path)
        result = distill(log, store, generate=fake_llm, days=1)
        store.save()

        print(
            f"[Layer 2] stage1_reflection={result.stage1_reflection[:60]!r}..."
        )
        print(f"[Layer 2] added {result.added} patterns to {knowledge_path}")

        # Reload and sort by effective importance to confirm round-trip.
        reloaded = KnowledgeStore(knowledge_path)
        reloaded.load()
        ranked = sorted(
            reloaded.all(), key=effective_importance, reverse=True
        )
        print("[Layer 2] top patterns by effective importance:")
        for p in ranked:
            print(
                f"  - ({effective_importance(p):.3f}) [{p['category']}] {p['pattern']}"
            )

        print("[demo] done — no Layer 3 in this reference; see ADR-0005.")


if __name__ == "__main__":
    main()
