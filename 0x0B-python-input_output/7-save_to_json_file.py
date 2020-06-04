#!/usr/bin/python3
""" defines a function that write text using json representation """


import json


def save_to_json_file(my_obj, filename):
    """ function that writes an obect to a text file
        using json representation """

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dump(my_obj))
