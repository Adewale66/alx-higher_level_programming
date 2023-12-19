#!/usr/bin/python3

"""Sqaure class"""


class Square:
    """Sqaure class with size attribute"""
    def __init__(self, size=0):
        """Initialize Square with size attribute"""
        self.__size = size

    @property
    def size(self):
        """Get size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of Square"""
        self.__size = value

    def area(self):
        """Return area of Square"""
        return self.__size ** 2
