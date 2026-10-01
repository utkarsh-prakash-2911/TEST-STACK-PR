"""Command-line front-end for tasklib, wired to the TaskStore from PR 1."""

from __future__ import annotations

import argparse

from tasklib.store import TaskStore


def _cmd_add(store: TaskStore, args: argparse.Namespace) -> None:
    task = store.add(args.title)
    print(f"Added #{task.id}: {task.title}")


def _cmd_list(store: TaskStore, args: argparse.Namespace) -> None:
    tasks = store.list()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        mark = "x" if task.done else " "
        print(f"[{mark}] #{task.id} {task.title}")


def _cmd_done(store: TaskStore, args: argparse.Namespace) -> None:
    task = store.complete(args.id)
    print(f"Completed #{task.id}: {task.title}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tasklib", description="A tiny to-do manager.")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="add a task")
    add.add_argument("title")
    add.set_defaults(func=_cmd_add)

    ls = sub.add_parser("list", help="list tasks")
    ls.set_defaults(func=_cmd_list)

    done = sub.add_parser("done", help="mark a task complete")
    done.add_argument("id", type=int)
    done.set_defaults(func=_cmd_done)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    store = TaskStore()
    args.func(store, args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
