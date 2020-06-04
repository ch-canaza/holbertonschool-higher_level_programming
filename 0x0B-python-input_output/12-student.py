#!/usr/bin/python3
""" creates a class called student """


class Student:
    """ A class called student
    first_name: first name of th student
    last_name: last name of the student
    age: age of the student """

    def __init__(self, first_name, last_name, age):
        """ initialization of instances """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of student """

        if type(attrs) is list and all(type(x) is str for x in attrs):
            dictionary = {}
            for i in attrs:
                if i in self.__dict__:
                    dictionary[i] = self.__dict__[i]
            return dictionary
        else:
            return self.__dict__
