#!/usr/bin/python3

import json
import os

class FileStorage:
    """This class serializes and deserializes instances to a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This module returns the dictionary __objects"""

        return FileStorage.__object

    def new(self, obj):
        """This module sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """This module serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__object.items()}
            json.dump(d, f)


    def reload(self):
        """This module deserializes the JSON file to __objects (only if the JSON file (__file_path)"""

        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                    for k, v in obj_dict.items()}
            FileStorage.__object = obj_dict



