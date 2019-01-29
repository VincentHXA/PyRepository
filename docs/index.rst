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

单例模块，提供了一个单例装饰器（如下的代码示例）。

.. _如下的代码示例:

::

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


Bullet list:

- one
- two
- three

Enumerated list:

1. one
2. two
#. auto-enumerated

Definition list:

one
      one is a number.
two
      two is an another number.

TEST
============

Second document section

Subsection A
------------

*a long text to illustrate the style*

**a long text to illustrate the style**

Subsection B
------------

Let's continue our text.

links below:

Try `link line with spaces`_

Try linkLine_

Find the code example_

Subsection C
------------

-> go back to `Section 1`_



.. _`link line with spaces`: http://www.baidu.com
.. _linkLine: http://www.baidu.com