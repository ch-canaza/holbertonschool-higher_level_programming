#!/usr/bin/python3
""" function that  returns an object (Python data structure)
    represented by a JSON string: """


import json


def from_json_string(my_str):
    """ function that represents a python object forom json
        data structure """
    return json.loads(my_str)
