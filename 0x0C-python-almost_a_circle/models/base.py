#!/usr/bin/python3
"""Base class module"""
import json
import os.path


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes instances """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ List of dictionaries to JSON string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes JSON string to file """
        list_dict = []
        file = "{}.json".format(cls.__name__)

        if list_objs is None:
            pass
        else:
            for i in range(len(list_objs)):
                list_dict.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dict)

        with open(file, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of dict represented by json_string """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Square":
            new = cls(1)
        else:
            new = cls(1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        file = "{}.json".format(cls.__name__)

        if os.path.exists(file) is False:
            return []

        with open(file, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_inst = []

        for index in range(len(list_cls)):
            list_inst.append(cls.create(**list_cls[index]))

        return list_inst
