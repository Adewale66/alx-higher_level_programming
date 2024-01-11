#!/usr/bin/python3
from models.rectangle import Rectangle

"""Square module"""


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ init method """
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if (value <= 0):
            raise ValueError("size must be > 0")
        super().width(value)
        super().height(value)
        self.__size = value
