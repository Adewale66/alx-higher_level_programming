#!/usr/bin/python3

"""Student module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dict of Student object"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict
