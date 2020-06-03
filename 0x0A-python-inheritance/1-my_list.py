#!/usr/bin/python3
""" module containing class mylist"""


class MyList(list):
    """ defines Mylist class """

    def __init__(self):
        """ initializes new Mylist object """
        pass

    def print_sorted(self):
        """ prints a sorted list """
        print(sorted(self))
