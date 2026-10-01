"""Tests for the Task model (PR 1 code)."""

from tasklib.models import Task


def test_round_trip():
    task = Task(id=1, title="write docs", done=True)
    assert Task.from_dict(task.to_dict()) == task


def test_default_not_done():
    assert Task(id=2, title="read docs").done is False
