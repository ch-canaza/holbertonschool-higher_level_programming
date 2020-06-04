#!/usr/bin/python3
""" defines a function that appends text to a file """


def append_write(filename="", text=""):
    """ function that apends a line of text to a file if exist or create it
        if does not """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
