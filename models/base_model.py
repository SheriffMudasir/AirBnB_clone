#!/usr/bin/python3
"""This script contains the base_model that defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """This class defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """
        Constructor for BaseModel class.

        Args:
            *args: Unused.
            **kwargs: Dictionary containing attribute values for the instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def save(self):
        """Updates the public instance attribute 'updated_at' with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()
        models.storage.new(self)

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.

        Returns:
            dict: Dictionary representation of the instance.
        """
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict

    def __str__(self):
        """String representation of the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


