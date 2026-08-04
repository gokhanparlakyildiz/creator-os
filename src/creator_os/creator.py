"""Core creator domain models."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CreatorProfile:
    """A minimal identity used by Creator OS workflows."""

    name: str
    niche: str

    def introduction(self) -> str:
        """Return a short, deterministic creator introduction."""
        return f"{self.name} creates content about {self.niche}."
