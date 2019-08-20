#!/usr/bin/env python

from __future__ import print_function

class Person(object):
    """ The Person class
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        """
        name getter
        :return: name
        """
        return self.name

    @name.setter
    def name(self, val):
        self.name = val

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, val):
        self.age = val


def dog():
    return True


def cat(name, age=3, *args, **kwargs):
    return name, age, args, kwargs



