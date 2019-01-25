
"""
self-defined context manager
"""

from contextlib import contextmanager

@contextmanager
def context_illustration():
    print('entering context')                    # 相当于 __enter__

    try:
        yield                                    # 相当于被装饰函数的代码块处理部分
    except Exception as e:                       # 相当于 __exit__
        print('leaving context')
        print('with an error (%s)' % e)
        raise
    else:
        print('leaving context')
        print('with no error')

class ContextIllustration:
    def __enter__(self):
        print('entering context')

    def __exit__(self, exc_type, exc_value, traceback):
        print('leaving context')

        if exc_type is None:
            print('with no error')
        else:
            print('with an error (%s)' % exc_value)



if __name__ == '__main__':
    with ContextIllustration():
        # raise RuntimeError('raise some error')
        print('do something')

    with context_illustration():
        # raise RuntimeError('raise some error')
        print('do something')
