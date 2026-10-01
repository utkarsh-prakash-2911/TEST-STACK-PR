"""Baseline smoke test so CI has something green to run on every PR in the stack.

Real coverage (models, store, CLI) arrives in PR 3 of the stack.
"""

import tasklib


def test_package_imports():
    assert tasklib.__version__ == "0.1.0"
