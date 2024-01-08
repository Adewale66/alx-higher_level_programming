#!/usr/bin/python3

rectangle_class = __import__('9-rectangle').Rectangle

"""Square class module"""


class Square(rectangle_class):
    """Square class"""

    def __init__(self, size):
        """init method"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """area method"""
        return self.__size ** 2
