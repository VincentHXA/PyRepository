#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MetaSingleton(type):
    """
    meta class of singleton
    """
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            # cls._instance[cls] = super().__call__(*args, **kwargs)
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)

        return cls._instance[cls]


def singleton(cls):
    """
    decorator for singleton
    :param cls:
    :return:
    """
    _instances = {}

    def _singleton(*args, **kw):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kw)
        return _instances[cls]

    return _singleton