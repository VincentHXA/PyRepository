
import pytest
import sys

from .pytest_markers import minversion

@minversion
def test_skipif():
    assert False

