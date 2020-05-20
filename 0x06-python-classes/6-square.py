#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    # get method
    @property
    def size(self):
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
