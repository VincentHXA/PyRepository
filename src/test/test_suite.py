
import unittest
from src.test.test_clock_decorator import ClockDecoratorTests

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ClockDecoratorTests))

    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')