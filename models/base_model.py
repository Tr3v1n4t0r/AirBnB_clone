#!/usr/bin/python3
"""
Defines a BaseModel
"""
import uuid
from datetime import date, datetime, time


class BaseModel:
    """Defines a BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel class"""
        if (kwargs):
            for key, value in kwargs.items():
                if (key == 'created_at' or key == 'updated_at'):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if (key == '__class__'):
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
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
