"""Tests for the CLI front-end (PR 2 code)."""

from tasklib.cli import main


def test_add_then_list(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)

    assert main(["add", "buy milk"]) == 0
    assert main(["list"]) == 0

    out = capsys.readouterr().out
    assert "Added #1: buy milk" in out
    assert "[ ] #1 buy milk" in out


def test_done_marks_complete(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)

    main(["add", "buy milk"])
    main(["done", "1"])
    main(["list"])

    out = capsys.readouterr().out
    assert "[x] #1 buy milk" in out
