#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Singleton(type):
    """
    一个样例
    """
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls._instance not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)

        return cls._instance[cls]


def singleton(cls):
    """
    decorator for singleton
    :param cls:
    :return:
    """
    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton