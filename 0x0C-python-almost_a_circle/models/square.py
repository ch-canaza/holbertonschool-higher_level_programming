#!/usr/bin/python3
""" defines a class square """
from models.rectangle import Rectangle
#import turtle

class Square(Rectangle):
    """ class square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ method that defines a square """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ define size """
        return self.width

    @size.setter
    def size(self, value):
        """ validates size is same as width and height """
        self.width = value
        self.height = value

    def __str__(self):
        """ return str representation of square """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ defines a method that asigns a tributes """
        if len(args) != 0:
            i = 0
            sqr_attributes = ["id", "size", "x", "y"]
            for arg in args:
                setattr(self, sqr_attributes[i], args[i])
                i += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ method that returns a dictionary representation of a square """
        sqr_dict_rpr = {}
        sqr_args = ['id', 'x', 'size', 'y']
        for args in sqr_args:
            sqr_dict_rpr[args] = getattr(self, args)
        return sqr_dict_rpr

#turtle.done()
