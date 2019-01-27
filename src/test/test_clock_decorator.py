
import functools
import unittest

from src.decorators.myclock import clock

@functools.lru_cache()
@clock()
# @ClockDecoratorAsClass
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

class ClockDecoratorTests(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(10), 55)

if __name__ == "__main__":
    unittest.main()


