#!/usr/bin/python3
"""This script contains the base_model that defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime

class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initialize instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, str(self.__dict__)
        )

    def save(self):
        """Update the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of the instance"""
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result

