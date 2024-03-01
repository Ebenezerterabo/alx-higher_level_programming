#!/usr/bin/python3

"""The base module which contains a class"""
import json
import csv


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
        if json_string is None or json_string == "":
            return []
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

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as file:
                list_dict = cls.from_json_string(file.read())
                return [cls.create(**data) for data in list_dict]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializing a csv file"""
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or len(list_objs) == 0:
                csvfile.write("[]")
            elif cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]

            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for obj in list_objs:
                csvwriter.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializing a csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in data.items())
                                   for data in list_dicts]
                return [cls.create(**data) for data in list_dicts]
        except IOError:
            return []
