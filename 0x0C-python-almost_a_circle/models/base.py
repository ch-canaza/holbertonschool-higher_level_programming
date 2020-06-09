#!/usr/bin/python3
""" defining a class named Base """

import json
import csv
from os import path


class Base:
    """ empty class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method that returns JSON string
            representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ method that writes the JSON string
            representation of list_objs to a file """
        new_list = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns a list of JSON strings representation """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            object = cls(1, 1)
        elif cls.__name__ == "Square":
            object = cls(1)
        cls.update(object, **dictionary)
        return object

    @classmethod
    def load_from_file(cls):
        """ return list of instances """
        new_list = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                new_list = cls.from_json_string(f.read())
            for i, j in enumerate(new_list):
                new_list[i] = cls.create(**new_list[i])
        except:
            pass
        return new_list
