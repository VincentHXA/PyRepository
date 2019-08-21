
import time
import functools


def logger(func):
    """
    1. 无参函数装饰器 - 日志
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        print("before func")
        res = func(*args, *kwargs)
        print("after func")
        return res
    return wrapper


def timer(func):
    """
    2. 无参函数装饰器 - 计时
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        time.sleep(1)
        end = time.time()
        print('timing: %ss' % (end - start))
        return res
    return wrapper


def logger_with_level(level='info'):
    """
    3. 带参函数装饰器
    :param level:
    :return:
    """
    def wrapper(func):
        @functools.wraps(func)
        def deco(*args, **kwargs):
            print('%s: before func' % level)
            res = func(*args, **kwargs)
            print('%s: after func' % level)
            return res
        return deco
    return wrapper


class logger_for_cls(object):
    """
    4. 无参类装饰器
    """
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('before func')
        res = self.func(*args, *kwargs)
        print('after func')
        return res


class logger_for_cls_with_level(object):
    """
    5. 带参类装饰器
    """
    def __init__(self, level='info'):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('%s: before func' % self.level)
            res = func(*args, **kwargs)
            print('%s: after func' % self.level)
            return res
        return wrapper



# =========================================


import unittest


class TestDecorators(unittest.TestCase):

    def setUp(self) -> None:  print('====================')

    def test_logger(self):
        @logger
        def f():
            print('I am f')
            print(f.__name__)
            return True

        print(f())

    def test_timer(self):
        @timer
        def f():
            print('I am f')
            print(f.__name__)
            return True

        print(f())

    def test_logger_with_level(self):
        @logger_with_level('error')
        def f():
            print('I am f')
            print(f.__name__)
            return True

        print(f())

    def test_logger_for_cls(self):
        @logger_for_cls
        def f():
            print('I am f')
            return True

        print(f())

    def test_logger_for_cls_with_level(self):
        @logger_for_cls_with_level(level='warn')
        def f():
            print('I am f')
            return True

        print(f())



    def tearDown(self) -> None: pass



if __name__ == '__main__':
    unittest.main()
