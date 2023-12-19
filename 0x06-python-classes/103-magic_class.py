#!/usr/bin/python3
import math

"""Magic Class"""


class MagicClass:
    """Magic Class"""
    def __init__(self, radius=0) -> None:
        """Initialize Magic Class

        Args:
            radius (float or int, optional): Radius. Defaults to 0.
        """
        self.radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Area of a circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Circumference of a circle"""
        return 2 * math.pi * self.__radius
