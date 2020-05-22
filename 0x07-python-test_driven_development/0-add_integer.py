#!/usr/bin/python3
"""
function that adds 2 integers
"""


def add_integer(a, b=98):

    """ c (int) receives the result of the sum
    Args:
        a (int): integer value
        b (int): integer value if put other wise 98
    Return:
        c (int) as result of the sum
    Raise:
        TypeError: if a or b are not integer
    """

    if a is None or  type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float and  type(b) is not int:
        raise TypeError("b must be an integer")

    c = int(a) + int(b)
    return c
