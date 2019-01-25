# coding: utf-8

'''
a decorator with parameters for adding a common clock
'''

import time
import functools

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({arg_str}) -> {result}'

def clock(fmt = DEFAULT_FMT):
    """
    时耗装饰器，参数为时间格式
    :param fmt:
    :return:
    """
    def decorate(func):
        @functools.wraps(func)
        def clocked(*_args, **_kwargs):
            t_start = time.time()
            _result = func(*_args, **_kwargs)
            elapsed = time.time() - t_start
            name = func.__name__
            arg_lst = []
            if _args:
                arg_lst.append(', '.join(repr(arg) for arg in _args))
            if _kwargs:
                pairs = ['%s=%r' % (k, w) for k, w in sorted(_kwargs.items())]
                arg_lst.append(', '.join(pairs))
            arg_str = ', '.join(arg_lst)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate

class ClockDecoratorAsClass:
    """
    使用类修饰器。
    只是一个尝试，尚未理想完成。
    """

    def __init__(self, function, fmt = DEFAULT_FMT):
        self.function = function
        self.fmt = fmt

    def __call__(self, *args, **kwargs):
        t_start = time.time()
        _result = self.function(*args, **kwargs)
        elapsed = time.time() - t_start
        name = self.function.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        result = repr(_result)
        print(self.fmt.format(**locals()))
        return _result


