#!/usr/bin/python3
""" defines a class Rectangle"""


class Rectangle:
    """Represents a Rectangle
    Attribute:
        __width (int)
        __heihgt (int)
    """

    def __init__(self, width=0, height=0):
        """initializes Rectangle
        Args:
            width(int)
            height (int)
        """
        self.height = height
        self.width = width

    # get method
    @property
    def width(self):
        """ getter of __width
        Returns the width of the rectangle
        """
        return self.__width

    # set method
    @width.setter
    def width(self, value):
        """ setter of __width
        Args:
            Value : width of the rectangle
        Returns:
            None
        """
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    # get method
    @property
    def height(self):
        """ getter of __height
        Returns the height of a rectangle
        """
        return self.__height

    # set method
    @height.setter
    def height(self, value):
        """ setter of __height
        Args:
            Value: height of the rectangle
        Return:
            None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
