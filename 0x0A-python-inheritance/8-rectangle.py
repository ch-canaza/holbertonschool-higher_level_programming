#!/usr/bin/python3
""" module Rectangle class that inherits from
    class Base Geometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ defines class rectangle """

    def __init__(self, width, height):
        """ iniyializes a rectangle method
            and validade if its arguments are
            positive integer """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
