#!/usr/bin/python3
"""
Defines a FileStorage class
"""
import json
import os.path
from datetime import datetime, date, time
from models.base_model import BaseModel


class FileStorage:
    """Defines a FileStorage class"""
    __filepath = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes __objects to the jsone file"""
        with open(self.__filepath, 'w') as f:
            new_dict = {key: obj.to_dict() for key, obj in
                        self.__objects.items()}
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the json file to __objects"""
        if os.path.isfile(self.__filepath):
            with open(self.__filepath, 'r') as f:
                for key, value in json.load(f).items():
                    self.__objects[key] = eval(key.split('.')[0])(**value)
