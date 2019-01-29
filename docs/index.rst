.. PyRepositoryDocs documentation master file, created by
   sphinx-quickstart on Fri Jan 25 21:56:55 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PyRepository
############

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


SRC
============

源码。

base
------------

os_adapter.py
^^^^^^^^^^^^^

一个对操作系统进行兼容性适配的模块，主要适配Windows和Linux操作系统。

py_ver_adapter.py
^^^^^^^^^^^^^^^^^

一个对不同版本Python进行兼容性适配的模块，主要适配Python2和Python3。

singleton.py
^^^^^^^^^^^^

单例模块，提供了一个单例装饰器

如下的使用示例::

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


decorators
----------

一些装饰器。

clocker.py
^^^^^^^^^^

单步计时的装饰器函数，打印被装饰函数的单次调用用时。

参数：字符串格式fmt。*默认： [{elapsed:0.8f}s] {name}({arg_str}) -> {result}*。

如下的使用示例::

   import functools

   from src.decorators.clocker import clock


   def test_clocker():

       @functools.lru_cache()
       @clock()
       def fibonacci(n):
           if n < 2:
               return n
           return fibonacci(n - 2) + fibonacci(n - 1)

       _fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

       for i in range(0, 10, 1):
           assert fibonacci(i) == _fibonacci[i]

typechecker.py
^^^^^^^^^^^^^^

参数类型检查的装饰器函数，检查输入与输出的数目与类型。

参数：
   - in: 函数输入类型的元组。
   - out: 函数输出类型的元组。


如下的使用示例::

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


descriptors
------------

属性描述符。

demo_attr_desc.py
^^^^^^^^^^^^^^^^^^

一个属性描述符类的示范。

1. 属性的读值。
2. 属性的设值与设值保护。
3. 属性名在被装饰类的dir中名称设置。
4. 类继承层次。

如下的使用示例::

   import pytest

   import src.descriptors.demo_attr_desc as attr_desc


   def test_attr_desc():

       @attr_desc.entity
       class LineItem:
           description = attr_desc.NonBlank()
           weight = attr_desc.Quantity()
           price = attr_desc.Quantity()

           def __init__(self, description, weight, price):
               self.description = description
               self.weight = weight
               self.price = price

           def subtotal(self):
               return self.weight * self.price

       apple = LineItem("Apple", 2.4, 3.0)

       dir_apple = dir(apple)
       assert '_Quantity#weight' in dir_apple
       assert '_NonBlank#description' in dir_apple
       assert '_Quantity#price' in dir_apple

       assert 2.4 == apple.weight
       assert 3.0 == apple.price
       apple.weight = 7.0
       assert 7.0 == apple.weight

       with pytest.raises(ValueError, match='value must be > 0') as error:
           apple.weight = -5.5

       with pytest.raises(ValueError, match='value cannot be empty or blank') as error:
           apple.description = ''

demo_attr_factory.py
^^^^^^^^^^^^^^^^^^^^

与 `demo_attr_desc.py`_ 功能类型，但以属性的特性工厂的形式。

与 `demo_attr_desc.py`_ 中的属性描述符类的区别:
   - 难以重命名属性在被装饰类的dir中的名字。

如下的使用示例::

   import pytest

   import src.descriptors.demo_attr_factory as attr_factory


   def test_attr_desc():
       class LineItem:
           description = attr_factory.quantity()
           weight = attr_factory.quantity()
           price = attr_factory.quantity()

           def __init__(self, description, weight, price):
               self.description = description
               self.weight = weight
               self.price = price

           def subtotal(self):
               return self.weight * self.price

       apple = LineItem("Apple", 2.4, 3.0)

       assert 2.4 == apple.weight
       assert 3.0 == apple.price
       apple.weight = 7.0
       assert 7.0 == apple.weight

       with pytest.raises(ValueError, match='value must be > 0') as error:
           apple.weight = -5.5

       with pytest.raises(ValueError, match='value cannot be empty or blank') as error:
           apple.description = ''

       with pytest.raises(ValueError, match='unsupported data type') as error:
           apple.weight = []

