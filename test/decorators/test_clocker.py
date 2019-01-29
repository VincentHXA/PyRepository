
import functools

from src.decorators.clocker import clock


def test_clocker():

    @functools.lru_cache()
    @clock()
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n - 2) + fibonacci(n - 1)

    _fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    for i in range(0, 10, 1):
        assert fibonacci(i) == _fibonacci[i]

