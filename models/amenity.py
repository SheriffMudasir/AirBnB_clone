#!/usr/bin/python3
"""This module amenity inherits from BaseModel"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of Amenity"""
        super().__init__(*args, **kwargs)

