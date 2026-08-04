import pytest

from creator_os.trends import TrendAgent, TrendCandidate


class FakeTrendSource:
    """A predictable source used to test the agent without internet access."""

    def __init__(self, candidates: list[TrendCandidate]) -> None:
        self.candidates = candidates
        self.requested_niche: str | None = None

    def fetch(self, niche: str) -> list[TrendCandidate]:
        self.requested_niche = niche
        return self.candidates


def candidate(
    topic: str,
    *,
    relevance: float,
    velocity: float,
    engagement: float,
) -> TrendCandidate:
    return TrendCandidate(
        topic=topic,
        source="test-source",
        relevance=relevance,
        velocity=velocity,
        engagement=engagement,
    )


def test_discover_ranks_candidates_and_applies_limit() -> None:
    source = FakeTrendSource(
        [
            candidate("AI video", relevance=0.9, velocity=0.8, engagement=0.7),
            candidate("Old news", relevance=0.3, velocity=0.2, engagement=0.8),
            candidate("AI agents", relevance=1.0, velocity=0.9, engagement=0.9),
        ]
    )

    trends = TrendAgent(source).discover("artificial intelligence", limit=2)

    assert source.requested_niche == "artificial intelligence"
    assert [trend.candidate.topic for trend in trends] == ["AI agents", "AI video"]
    assert trends[0].score == 0.95


def test_discover_rejects_invalid_input() -> None:
    agent = TrendAgent(FakeTrendSource([]))

    with pytest.raises(ValueError, match="niche must not be empty"):
        agent.discover("  ")

    with pytest.raises(ValueError, match="limit must be at least 1"):
        agent.discover("AI", limit=0)


def test_candidate_rejects_metric_outside_normalized_range() -> None:
    with pytest.raises(ValueError, match="velocity must be between"):
        candidate("Invalid trend", relevance=0.5, velocity=1.1, engagement=0.5)
