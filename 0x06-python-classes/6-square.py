#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a size of the square
        __position (tuple): position of the square in 2D space
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        Args:
            size (int): size of a side of the square
            position (tuple): positoin of the square in 2D space
        Returns:
            None
        """
        self.__size = size
        self.__position = position

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return self.__size ** 2

    # get method
    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return(self.__size)

    # set method
    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): size of a side of the square
        Returns:
            None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints the square
        Returns:
            None
        """
        size = self.__size
        pos1 = self.__position[0]
        pos2 = self.__position[1]
        if size == 0:
            print()
        for line in range(pos2):
            print()
        for row in range(size):
            print((" " * pos1) + ("#" * size))

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        error_msg = ("position must be a tuple of 2 positive integers")
        if tye(value) != tuple or len(value) < 2:
            raise TypeError(error_msg)
    for items in value:
        if type(items) != int or items < 0:
            raise TypeError(error_msg)
    self.__position = value
