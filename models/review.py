#!/usr/bin/python3
"""This is the review mmodule that inherits from BaseModel"""
from models.base_model import BaseModel

class Review(BaseModel):
    """The method review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Handles initialization of Review"""
        super().__init__(*args, **kwargs)


