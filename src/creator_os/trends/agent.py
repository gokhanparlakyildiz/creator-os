"""Trend Agent orchestration and ranking logic."""

from dataclasses import dataclass

from creator_os.trends.models import RankedTrend, TrendCandidate
from creator_os.trends.source import TrendSource


@dataclass(frozen=True, slots=True)
class TrendAgent:
    """Discover and rank content opportunities from a trend source."""

    source: TrendSource

    def discover(self, niche: str, *, limit: int = 5) -> list[RankedTrend]:
        """Return the strongest trend opportunities for a creator niche."""
        if not niche.strip():
            raise ValueError("niche must not be empty")
        if limit < 1:
            raise ValueError("limit must be at least 1")

        ranked = [self._rank(candidate) for candidate in self.source.fetch(niche)]
        ranked.sort(key=lambda trend: trend.score, reverse=True)
        return ranked[:limit]

    @staticmethod
    def _rank(candidate: TrendCandidate) -> RankedTrend:
        score = (
            candidate.relevance * 0.50
            + candidate.velocity * 0.30
            + candidate.engagement * 0.20
        )
        return RankedTrend(candidate=candidate, score=round(score, 4))
