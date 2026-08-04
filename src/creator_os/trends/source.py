"""Contracts for Trend Agent data sources."""

from typing import Protocol

from creator_os.trends.models import TrendCandidate


class TrendSource(Protocol):
    """A provider capable of finding trend candidates for a niche."""

    def fetch(self, niche: str) -> list[TrendCandidate]:
        """Return normalized trend candidates relevant to the niche."""
        ...
