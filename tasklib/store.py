"""JSON-backed storage for tasks."""

from __future__ import annotations

import json
from pathlib import Path

from tasklib.models import Task

DEFAULT_PATH = Path("tasks.json")


class TaskStore:
    """Load, mutate, and persist a list of tasks as JSON."""

    def __init__(self, path: Path = DEFAULT_PATH) -> None:
        self.path = Path(path)
        self._tasks: list[Task] = self._load()

    def _load(self) -> list[Task]:
        if not self.path.exists():
            return []
        raw = json.loads(self.path.read_text())
        return [Task.from_dict(item) for item in raw]

    def _save(self) -> None:
        self.path.write_text(json.dumps([t.to_dict() for t in self._tasks], indent=2))

    def _next_id(self) -> int:
        return max((t.id for t in self._tasks), default=0) + 1

    def add(self, title: str) -> Task:
        task = Task(id=self._next_id(), title=title)
        self._tasks.append(task)
        self._save()
        return task

    def list(self) -> list[Task]:
        return list(self._tasks)

    def complete(self, task_id: int) -> Task:
        for task in self._tasks:
            if task.id == task_id:
                task.done = True
                self._save()
                return task
        raise KeyError(f"No task with id {task_id}")
