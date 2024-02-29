#!/usr/bin/python3

"""The base module which contains a class"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert dictionary to json string"""
        if list_dictionaries is None:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return json_string

    @staticmethod
    def from_json_string(json_string):
        """convert Json string to list"""
        if json_string is None:
            return "[]"
        json_obj = json.loads(json_string)
        return json_obj

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of instances to a JSON file"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []

        with open(filename, "w") as file:
            obj_list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(obj_list)
            file.write(json_string)
