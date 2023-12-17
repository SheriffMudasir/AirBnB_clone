#!/usr/bin/python3
""""This is the city mmodule which iherits from BaseModel"""
from models.base_model import BaseModel

class City(BaseModel):
    """The method city class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """This method handle initialization of City"""
        super().__init__(*args, **kwargs)

