#!/usr/bin/python3
""" defines a function that reads a file text """


def read_file(filename=""):
    """ function that reads a text and prints in
        stdout """
    with open("my_file_0.txt", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
