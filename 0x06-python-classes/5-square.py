#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.__size = size

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
    if size == 0:
        print()
    for i in range(size):
        print("#" * size)
