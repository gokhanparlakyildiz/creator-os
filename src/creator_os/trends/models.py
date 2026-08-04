"""Domain models used by the Trend Agent."""

from dataclasses import dataclass


def _validate_metric(name: str, value: float) -> None:
    if not 0.0 <= value <= 1.0:
        msg = f"{name} must be between 0.0 and 1.0"
        raise ValueError(msg)


@dataclass(frozen=True, slots=True)
class TrendCandidate:
    """A trend observed by an external data source.

    Metrics use a normalized 0.0-to-1.0 scale so candidates from different
    sources can be compared consistently.
    """

    topic: str
    source: str
    relevance: float
    velocity: float
    engagement: float

    def __post_init__(self) -> None:
        if not self.topic.strip():
            raise ValueError("topic must not be empty")
        if not self.source.strip():
            raise ValueError("source must not be empty")

        _validate_metric("relevance", self.relevance)
        _validate_metric("velocity", self.velocity)
        _validate_metric("engagement", self.engagement)


@dataclass(frozen=True, slots=True)
class RankedTrend:
    """A trend candidate with its final ranking score."""

    candidate: TrendCandidate
    score: float
