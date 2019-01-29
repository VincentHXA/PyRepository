
import src.base.singleton as singleton


def test_singleton_decorator():
    @singleton.singleton
    class Cat:
        def __init__(self):
            pass

    assert id(Cat()) == id(Cat())

    class Dog:
        def __init__(self):
            pass

    assert not id(Dog()) == id(Dog())
