#!/usr/bin/python3
"""This module FileStorage class for serialization and deserialization of instance to JSON file"""

import json

class FileStorage:
    """This  class serializes instances to a JSON file and deserializes JSON file to instances"""
    def __init__(self, file_path='file.json'):
        """This method creates a Private class attributes"""
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """This method returns the dictionary __objects"""
        return self.__objects


    def new(self, obj):
        """
        This method sets in __object in obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """This method serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
        except:
            pass

