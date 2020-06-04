#!/usr/bin/python3
""" defines a function that reads a file text """


def read_file(filename=""):
    with open("my_file_0.txt", encoding="UTF8") as f:
        for line in f:
            print(line, end="")
