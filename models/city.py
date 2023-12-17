#!/usr/bin/python3
""""This is the city mmodule which iherits from BaseModel"""
from models.base_model import BaseModel

class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of City"""
        super().__init__(*args, **kwargs)

