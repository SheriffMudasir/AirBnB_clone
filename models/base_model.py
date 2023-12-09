#!/usr/bin/python3
"""This module defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime

class BaseModel:
    """This class defines the Public instance attributes for other Public instance methods"""
    def __init__(self):
        """This method defines the Public instance attributes for other Public instance methods"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """This method returns a string representation of the attributes namely: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """This method updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """This method returns a dictionary containing all keys/values of __dict__ of the instance"""
        return_dict = self.__dict__.copy()
        return_dict['__class__'] = self.__class__.__name__
        return_dict['created_at'] = self.created_at.isoformat()
        return_dict['updated_at'] = self.updated_at.isoformat()
        return return_dict
    
