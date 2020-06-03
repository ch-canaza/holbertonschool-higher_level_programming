#!/usr/bin/python3
""" defines a new class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defines a class square wich inherits from Rectangle"""

    def __init__(self, size):
        """ initializes a rectangle method and
            validate if args are positive integer """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ Returns string representation os square """
        return "[Square] {}/{}".format(self.__size, self.__size)
