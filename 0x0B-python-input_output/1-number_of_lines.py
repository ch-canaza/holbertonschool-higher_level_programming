#!/usr/bin/python3
""" defines a funcion that returns the number of lines o a text file """


def number_of_lines(filename=""):
    """ returns number of lines in a file """
    counter = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            counter += 1
        return counter
