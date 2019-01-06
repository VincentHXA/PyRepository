# coding: utf-8

'''
a decorator with parameters for adding a common clock
'''

import time
import functools

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({arg_str}) -> {result}'

def clock(fmt = DEFAULT_FMT):
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