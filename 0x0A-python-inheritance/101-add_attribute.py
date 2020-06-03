#!/usr/bin/python3
""" module 101-add_attribute contains the function add_attribute """


def add_attribute(obj, name, value):
    """ if possible, add a new attribute to an object """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError('can\'t add new attribute')
