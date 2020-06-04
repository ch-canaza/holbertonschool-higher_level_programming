#!/usr/bin/python3
""" defines a finction that prints n lines of a file """


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file """
    counter = 0
    with open(filename, encoding='utf-8') as f:
            for lines in f:
                counter += 1
                if nb_lines <= 0 or nb_lines >= counter:
                    print(lines, end="")
            else:
                for lines in range(nb_lines):
                    print(f.readline(), end="")
