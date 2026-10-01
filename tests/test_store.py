"""Tests for TaskStore persistence and operations (PR 1 code)."""

import pytest

from tasklib.store import TaskStore


def test_add_assigns_sequential_ids(tmp_path):
    store = TaskStore(tmp_path / "tasks.json")
    first = store.add("a")
    second = store.add("b")
    assert (first.id, second.id) == (1, 2)


def test_complete_marks_done_and_persists(tmp_path):
    path = tmp_path / "tasks.json"
    store = TaskStore(path)
    task = store.add("ship it")
    store.complete(task.id)

    reloaded = TaskStore(path)
    assert reloaded.list()[0].done is True


def test_complete_unknown_id_raises(tmp_path):
    store = TaskStore(tmp_path / "tasks.json")
    with pytest.raises(KeyError):
        store.complete(999)
