#!/usr/bin/python3
""" defines json module string function """


import json
""" import json module """


def to_json_string(my_obj):
    """ defines a function that returns json representation of an object """

    return json.dumps(my_obj)
