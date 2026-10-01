# tasklib

A tiny to-do manager used to **demonstrate stacked pull requests**.

The code is deliberately built up in layers so each PR depends on the one below it:

| PR | Branch | Base | Adds |
|----|--------|------|------|
| 1 | `pr-1-core` | `main` | `models.py` + `store.py` — the `Task` model and add/list/complete storage |
| 2 | `pr-2-cli` | `pr-1-core` | `cli.py` — an argparse front-end wired to the store |
| 3 | `pr-3-tests` | `pr-2-cli` | `tests/` — real coverage for models, store, and CLI |

Each branch is cut from the previous branch (not `main`), and each PR targets the
branch below it. They merge bottom-up: merge PR 1 → PR 2 retargets to `main` → merge PR 2 → ...

## CI

`.github/workflows/ci.yml` lives on `main`, so every branch cut from the stack inherits it.
Because the `pull_request` trigger has **no `branches` filter**, CI runs on all three PRs
(a `branches: [main]` filter would skip PRs whose base is another branch in the stack).
GitHub also runs PR CI against the *merge commit*, so each PR is tested as
"main + everything below it + this PR."

## Development

```bash
pip install -e ".[dev]"
ruff check .
pytest
```
