#!/usr/bin/python3
"""The module amenity inherits from BaseModel"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """The class amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """This method handle initialization of Amenity"""
        super().__init__(*args, **kwargs)

