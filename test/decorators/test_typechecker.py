
import pytest
from src.decorators.typechecker import type_checker

def test_typechecker():
    class Demo:
        @type_checker((int, int))
        def meth1(self, int1, int2):
            print('received {} and {}'.format(int1, int2))

        @type_checker((str,), (int,))
        def meth2(self, phrase):
            print('received {}'.format(phrase))
            return 12

        @type_checker((str,), (int,))
        def meth3(self, phrase):
            print('received {}'.format(phrase))
            return "hello"

    demo = Demo()

    assert demo.meth1(1, 2) is None
    assert demo.meth2('hello') == 12

    with pytest.raises(TypeError, match='argument count is wrong'):
        assert demo.meth1(1, 2, 3)

    with pytest.raises(TypeError, match='arg .* should be .*'):
        assert demo.meth1(1, "hello")

    with pytest.raises(TypeError, match='arg .* should be .*'):
        assert demo.meth2(13)

    with pytest.raises(TypeError, match='arg .* should be .*'):
        assert demo.meth3('hello')

