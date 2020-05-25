#!/usr/bin/python3
""" defines a class Rectangle"""


class Rectangle:
    """Represents a Rectangle
    Attribute:
        __width (int)
        __heihgt (int)
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initializes Rectangle
        Args:
            width(int)
            height (int)
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        string = "{}".format('\n'.join([str(self.print_symbol) * self.__width
                                        for i in range(0, self.__height)]))
        return string

    def __repr__(self):
        return ("Rectangle(" + str(self.__width) + ", " +
                str(self.__height) + ")")

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """ Returns Rectangles Area """
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
