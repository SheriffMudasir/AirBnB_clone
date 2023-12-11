#!/usr/bin/python3
"""This module defines all common attributes/methods for other classes"""
from models import storage
import uuid
from datetime import datetime


class BaseModel:
    """This class defines the Public instance attributes for other Public instance methods"""

    def __init__(self, *args, **kwargs):
        """This method defines the Public instance attributes for other Public instance methods"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """This method updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This method returns a dictionary containing all keys/values of __dict__ of the instance"""
        return_dict = self.__dict__.copy()
        return_dict['__class__'] = self.__class__.__name__
        return_dict['created_at'] = self.created_at.isoformat()
        return_dict['updated_at'] = self.updated_at.isoformat()
        return return_dict