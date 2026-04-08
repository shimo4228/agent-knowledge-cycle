# Adapted from contemplative-agent
# (https://github.com/shimo4228/contemplative-agent) at commit 2dbde9d.
# Stripped of project-specific content. This file is an independent,
# harness-neutral reference for AKC. See docs/adr/0002-immutable-episode-log.md.
"""Layer 1: EpisodeLog — append-only daily JSONL episode storage.

One record per line: {"ts": ISO8601, "type": str, "data": dict}

Design notes:
- Files are written with umask(0o177) so they are created mode 0600.
- Daily partitioning: one file per UTC day, named YYYY-MM-DD.jsonl.
- No in-place mutation. Recovery = re-read the log.
"""

from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class EpisodeLog:
    """Append-only episode log stored as daily JSONL files."""

    def __init__(self, log_dir: Path) -> None:
        self._log_dir = Path(log_dir)

    def _path_for_date(self, date_str: str) -> Path:
        return self._log_dir / f"{date_str}.jsonl"

    def _today_path(self) -> Path:
        return self._path_for_date(
            datetime.now(timezone.utc).strftime("%Y-%m-%d")
        )

    def append(self, record_type: str, data: dict[str, Any]) -> None:
        """Append a record immediately to today's log file."""
        self._log_dir.mkdir(parents=True, exist_ok=True)
        record = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "type": record_type,
            "data": data,
        }
        path = self._today_path()
        old_umask = os.umask(0o177)
        try:
            with path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
        except OSError as exc:
            logger.warning("Failed to write episode log: %s", exc)
        finally:
            os.umask(old_umask)

    def read_range(
        self, days: int = 1, record_type: str | None = None
    ) -> list[dict[str, Any]]:
        """Read records from the last N days (inclusive of today)."""
        records: list[dict[str, Any]] = []
        now = datetime.now(timezone.utc)
        for i in range(days):
            date_str = (now - timedelta(days=i)).strftime("%Y-%m-%d")
            records.extend(self.read_file(self._path_for_date(date_str)))
        if record_type is not None:
            records = [r for r in records if r.get("type") == record_type]
        return records

    @staticmethod
    def read_file(path: Path) -> list[dict[str, Any]]:
        """Read all JSON lines from a single JSONL file."""
        if not path.exists():
            return []
        records: list[dict[str, Any]] = []
        try:
            with path.open("r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        records.append(json.loads(line))
                    except json.JSONDecodeError:
                        logger.warning(
                            "Skipping malformed log line in %s", path.name
                        )
        except OSError as exc:
            logger.warning("Failed to read log file %s: %s", path.name, exc)
        return records
