from __future__ import print_function

import os
import sys
import unittest
import inspect

import samples

class TestInspect(unittest.TestCase):

    def setUp(self):
        print("========================================")

    @unittest.skip('test_getmembers')
    def test_getmembers(self):
        print(' ===== class =====')
        a = inspect.getmembers(samples.Person)
        for _ in a:
            print(_)

        print(' ===== method =====')
        b = inspect.getmembers(samples.Person.name)
        for _ in b:
            print(_)

        print(' ===== method =====')
        c = inspect.getmembers(str)
        for _ in c:
            print(_)

        print(' ===== class methods =====')
        d = inspect.getmembers(samples.Person, inspect.ismethod)
        d = inspect.getmembers(samples.Person, inspect.isbuFiltin)
        for _ in d:
            print(_)

    def test_modules(self):
        self.assertEqual(inspect.getmodulename('/Users/hexiaoan/PycharmProjects/PyRepository/src/builtIns/samples.py'), 'samples')

    def test_type_checking(self):
        self.assertTrue(inspect.ismodule(samples))
        self.assertTrue(inspect.isbuiltin(id))
        self.assertTrue(inspect.isclass(samples.Person))
        #self.assertTrue(inspect.ismethod(samples.Person.__init__))
        self.assertTrue(inspect.isfunction(samples.dog))
        self.assertTrue(inspect.isfunction(lambda f: True))

    def test_retrieving_source_code(self):
        print(inspect.getdoc(samples.Person))
        print(inspect.getdoc(samples.Person.name))

        print(inspect.getfile(samples.Person))
        print(inspect.getfile(samples.dog))
        print(inspect.getmodule(samples.Person))

        print(inspect.getsourcefile(samples.Person))
        print(inspect.getsourcelines(samples.dog))
        print(inspect.getsource(samples.dog))

    def test_signature(self):
        print(inspect.signature(samples.cat))

    def test_cls_and_func(self):
        print(inspect.getargspec(samples.cat))
        print(inspect.getfullargspec(samples.cat))

    def test_interpreter_stack(self):
        frame = inspect.currentframe()
        try:
            print(frame)
            print(inspect.getframeinfo(frame))
            print(inspect.getouterframes(frame))
            stack = inspect.stack()
            for _ in stack:
                print(_)
        finally:
            del frame


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()