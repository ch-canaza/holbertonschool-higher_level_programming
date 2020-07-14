#!/usr/bin/python3
""" defines a class Rectangle """

from models.base import Base
#import turtle


class Rectangle(Base):
    """ class Rectangle that inherits from Base """
    #don = turtle.Turtle()
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes values in the clas rectangle

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0."""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
       
    @property
    def width(self):
        """ getting width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setting width """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ getting height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setting height """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ getting x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setting x """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ getting """
        return self.__y

    @y.setter
    def y(self, value):
        """ setting y """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ definde a method that returns area calculation """
        return self.__width * self.__height

    def display(self):
        """ dfefines a function that prints the
          rectangle with '#' """
        don.penup()
        print("\n" * self.y, end="")
        for row in range(self.height):
            print(" " * self.x, end="")
            for col in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        """ defines a method that returns str representation of
            rectangle  """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ updates a rectangle """
        if len(args) != 0:
            i = 0
            attributes = ['id', 'width', 'height', 'x', 'y']
            for arg in args:
                setattr(self, attributes[i], args[i])
                i += 1
        else:
            for j, k in kwargs.items():
                setattr(self, j, k)

    def to_dictionary(self):
        """ method that returns the dictionary
            representation of a rectangle """
        rect_dict_rpr = {}
        rect_args = ['id', 'width', 'height', 'x', 'y']
        for args in rect_args:
            rect_dict_rpr[args] = getattr(self, args)
        return rect_dict_rpr

                     #urtle.done()
