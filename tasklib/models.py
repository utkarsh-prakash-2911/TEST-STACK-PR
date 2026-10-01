"""Core data model for tasklib."""

from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass
class Task:
    """A single to-do item."""

    id: int
    title: str
    done: bool = False

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> Task:
        return cls(id=data["id"], title=data["title"], done=data.get("done", False))
