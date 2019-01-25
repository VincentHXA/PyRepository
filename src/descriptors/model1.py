# coding: utf-8

"""
特性工厂函数
1. 属性的读值
2. 对属性的设值验证
"""

import numbers

def quantity():
    try:
        quantity.counter += 1
    except AttributeError:
        quantity.counter = 0

    storage_name = '_{}#{}'.format('quantity', quantity.counter)

    def qty_getter(instance):
        return getattr(instance, storage_name)

    def qty_setter(instance, value):
        if isinstance(value, str):
            value = value.strip()
            if len(value) != 0:
                setattr(instance, storage_name, value)
            else:
                raise ValueError('value cannot be empty or blank')
        elif isinstance(value, numbers.Real):
            if value > 0:
                setattr(instance, storage_name, value)
            else:
                raise ValueError('value must be > 0')
        else:
            raise ValueError("unsupported data type")

    return property(qty_getter, qty_setter)

# def entity(cls):
#     for key, attr in cls.__dict__.items():
#         if isinstance(attr, property):
#             type_name = type(attr).__name__
#             attr.storage_name = '_{}#{}'.format(type_name, key)
#     return cls
