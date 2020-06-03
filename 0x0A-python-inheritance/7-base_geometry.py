#!/usr/bin/python3
""" empty class"""


class BaseGeometry():
    """ public instance method """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ defines integer validator as method """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
