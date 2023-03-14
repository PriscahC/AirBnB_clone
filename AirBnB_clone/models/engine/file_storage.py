#!/usr/bin/python3
"""FileStorage module"""
import json
import datetime
import os


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""
    def __init__(self, file_path="file.json"):
        """initializes the arguments for the FileStorage class"""
        self.__objects = {}
        self.__file_path = file_path

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
