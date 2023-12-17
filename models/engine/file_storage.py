#!/usr/bin/python3
"""This module handle serialization and deserialization"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """This class serializes instances to a JSON file and deserializes a JSON file to instances."""

    __file_path = "file.json"
    __objects = {}
    CLASSES = {
        'BaseModel': BaseModel,
        'User': User
    }

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_ = globals()[class_name]
                    instance = class_(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass

