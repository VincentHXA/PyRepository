
import src.base.meta_singleton as singleton

def test_singleton_decorator():
    @singleton.singleton
    class Cat:
        def __init__(self):
            pass

    assert id(Cat()) == id(Cat())


def test_singleton_metaclass():

    class Cat(metaclass=singleton.MetaSingleton):
        pass

    assert id(Cat()) == id(Cat())
