#!/usr/bin/python3
"""This is the state module which iherits from BaseModel"""
from models.base_model import BaseModel

class State(BaseModel):
    """State class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of State"""
        super().__init__(*args, **kwargs)

