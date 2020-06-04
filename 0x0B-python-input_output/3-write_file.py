#!/usr/bin/python3
""" defines a write_file function """


def write_file(filename="", text=""):
    """ writes a string to a text file and return number of characters """

    with open(filename, 'r+', encoding='utf-8') as f:
        return f.write(text)
