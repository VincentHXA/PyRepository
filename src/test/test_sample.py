
import pytest


def inc(x):
    if x > 0:
        return x + 1
    else:
        raise SystemExit(1)


def test_answer():
    with pytest.raises(SystemExit):
        assert inc(3) == 4
        assert inc(-2) == -1
