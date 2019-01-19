# coding: utf-8

import functools

_infos = {}

def typechecker(in_ = (), out = (type(None),)):
    def _typechecker(func):
        func_name = func.__name__
        _infos[func_name] = (in_, out)
        def _check_types(elements, types):
            if len(elements) != len(types):
                raise TypeError('argument count is wrong')
            typed = enumerate(zip(elements, types))
            for index, couple in typed:
                arg, of_the_right_type = couple
                if isinstance(arg, of_the_right_type):
                    continue
                raise TypeError('arg #{} should be {}'.format(index, of_the_right_type))

        @functools.wraps(func)
        def __typechecker(*_args, **_kwargs):
            # 检查输入的内容
            checkable_args = _args[1:]      # 去掉self
            _check_types(checkable_args, in_)

            res = func(*_args, **_kwargs)

            if not type(res) in (tuple, list):
                checkable_res = (res,)
            else:
                checkable_res = res
            _check_types(checkable_res, out)

            return res
        return __typechecker
    return _typechecker



if __name__ == '__main__':
    class Demo:
        @typechecker((int, int))
        def meth1(self, int1, int2):
            print('received {} and {}'.format(int1, int2))

        @typechecker((str,), (int,))
        def meth2(self, phrase):
            print('received {}'.format(phrase))
            return 12

    demo = Demo()
    demo.meth1(1, 2)
    demo.meth2("hello")
    print(_infos)
    demo.meth2(2)
