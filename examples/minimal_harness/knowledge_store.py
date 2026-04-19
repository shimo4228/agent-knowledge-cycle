# Adapted from contemplative-agent
# (https://github.com/shimo4228/contemplative-agent) at commit 2dbde9d.
# Stripped of project-specific content. This file is an independent,
# harness-neutral reference for AKC. See docs/adr/0003-three-layer-distillation.md.
"""Layer 2: KnowledgeStore — distilled patterns with time decay.

Each pattern: {"pattern": str, "distilled": iso8601, "importance": float,
               "category": str, "source"?: str, "last_accessed"?: iso8601}

Importance decays on read as base * 0.95 ** days_elapsed so recent evidence
dominates stale signals without destroying them.

Load-time validation against a forbidden-substring list treats accumulated
knowledge as untrusted input — a defensive pattern inherited from upstream
genre work. Operators should define their own list; the default is empty.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

logger = logging.getLogger(__name__)

# Operators replace this tuple with their own forbidden substrings.
# Matching is case-insensitive. If any substring appears in a loaded
# knowledge file, the file is treated as tainted and NOT loaded.
DEFAULT_FORBIDDEN_SUBSTRINGS: tuple[str, ...] = ()


def effective_importance(p: dict) -> float:
    """Compute importance with time decay: base * 0.95^days_elapsed."""
    base = float(p.get("importance", 0.5))
    distilled = p.get("distilled", "")
    if not distilled or distilled == "unknown":
        return base * 0.1  # unknown timestamp -> heavy penalty
    try:
        dt = datetime.fromisoformat(distilled)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        days = max(
            0.0,
            (datetime.now(timezone.utc) - dt).total_seconds() / 86400.0,
        )
    except (ValueError, TypeError):
        return base * 0.1
    return max(0.0, min(1.0, base * (0.95 ** days)))


class KnowledgeStore:
    """Manages distilled patterns as a JSON file."""

    def __init__(
        self,
        path: Path,
        forbidden_substrings: Iterable[str] = DEFAULT_FORBIDDEN_SUBSTRINGS,
    ) -> None:
        self._path = Path(path)
        self._forbidden = tuple(forbidden_substrings)
        self._patterns: list[dict] = []

    def add(
        self,
        pattern: str,
        importance: float = 0.5,
        category: str = "uncategorized",
        source: str | None = None,
    ) -> None:
        entry: dict = {
            "pattern": pattern,
            "distilled": datetime.now(timezone.utc).isoformat(
                timespec="minutes"
            ),
            "importance": importance,
            "category": category,
        }
        if source:
            entry["source"] = source
        self._patterns.append(entry)

    def all(self, category: str | None = None) -> list[dict]:
        """Return pattern dicts, optionally filtered by category."""
        if category is None:
            return list(self._patterns)
        return [
            p
            for p in self._patterns
            if p.get("category", "uncategorized") == category
        ]

    def top_context(
        self, limit: int = 50, category: str | None = None
    ) -> str:
        """Return a bullet list of top-N patterns by effective importance.

        The selected patterns have their `last_accessed` timestamp updated
        as a side effect, which downstream code can persist if desired.
        """
        pool = self.all(category)
        if not pool:
            return ""
        scored = sorted(pool, key=effective_importance, reverse=True)
        selected = scored[:limit]
        now = datetime.now(timezone.utc).isoformat(timespec="minutes")
        for p in selected:
            p["last_accessed"] = now
        return "\n".join(f"- {p['pattern']}" for p in selected)

    def load(self) -> None:
        """Load from disk. Validate against forbidden substrings (fail closed).

        If the file contains a forbidden substring anywhere, the store is
        left empty and a warning is logged. This is intentional: we prefer
        to surface tampering evidence rather than silently filter it out.
        """
        if not self._path.exists():
            return
        try:
            text = self._path.read_text(encoding="utf-8")
        except OSError as exc:
            logger.warning("Failed to read knowledge file: %s", exc)
            return
        text_lower = text.lower()
        for pat in self._forbidden:
            if pat and pat.lower() in text_lower:
                logger.warning(
                    "Knowledge file %s contains forbidden substring %r; "
                    "refusing to load.",
                    self._path,
                    pat,
                )
                return
        try:
            data = json.loads(text)
        except json.JSONDecodeError as exc:
            logger.warning("Failed to parse knowledge JSON: %s", exc)
            return
        if not isinstance(data, list):
            logger.warning("Knowledge JSON is not an array")
            return
        for item in data:
            if isinstance(item, dict) and isinstance(item.get("pattern"), str):
                self._patterns.append(
                    {
                        "pattern": item["pattern"],
                        "distilled": item.get("distilled", "unknown"),
                        "importance": float(item.get("importance", 0.5)),
                        "category": item.get("category", "uncategorized"),
                        **(
                            {"source": item["source"]}
                            if item.get("source")
                            else {}
                        ),
                        **(
                            {"last_accessed": item["last_accessed"]}
                            if item.get("last_accessed")
                            else {}
                        ),
                    }
                )

    def save(self) -> None:
        """Atomic write to disk."""
        self._path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self._path.with_suffix(self._path.suffix + ".tmp")
        content = (
            json.dumps(self._patterns, ensure_ascii=False, indent=2) + "\n"
        )
        tmp.write_text(content, encoding="utf-8")
        tmp.replace(self._path)
