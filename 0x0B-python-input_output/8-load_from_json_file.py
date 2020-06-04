#!/usr/bin/python3
""" defines a function that adds all arguments
    to a Python list, and then save them to a file: """


import json


def load_from_json_file(filename):
    """ funtion that add arguments to a python list and
       save them in to a file """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
