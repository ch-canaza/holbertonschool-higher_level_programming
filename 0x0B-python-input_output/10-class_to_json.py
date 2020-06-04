#!/usr/bin/python3
""" creates a function that returns a dict for json object """



def class_to_json(obj):
    """ returns the dictionary that describes the object """

    return obj.__dict__
