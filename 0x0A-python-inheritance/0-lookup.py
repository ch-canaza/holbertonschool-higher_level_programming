#!/usr/bin/python3
""" module containing funtion"""


def lookup(obj):
    """ function that returns a list of available attributes
        and methods of an object.
    """
    return (dir(obj))
