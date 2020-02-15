#!/usr/bin/python3

import uuid
from datetime import date, datetime, time

class BaseModel:
    """BaseModel Class"""
    def __init__(self, *args, **kwargs):
        if len(kwargs) is not 0:
            for key, value in kwargs.items():
                if key in "id":
                    self.id = value
                elif key in "created_at":
                    self.created_at = datetime.now()
                elif key in "updated_at":
                    self.updated_at = datetime.now()
                elif key in "to_dict":
                    self.to_dict = to_dict
                elif key in "save":
                    self.save = save
        else:
            self.id = str(uuid.uuid4())
            self.save = save
            self.to_dict = to_dict
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Prints the BaseModel attributes"""
        return ('[' + str(type(self).__name__) + '] (' + str(self.id) + ') ' +
                str(self.__dict__))

    def save(self):
        """Update the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': str(type(self).__name__)})
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
