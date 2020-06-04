#!/usr/bin/python3
""" defines a funcion that returns the number of lines o a text file """


def number_of_lines(filename=""):
    counter = 0
    with open("my_file_0.txt") as f:
        for line in f:
            counter += 1
        return counter
