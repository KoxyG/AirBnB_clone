#!/usr/bin/python3

from models.base_model import BaseModel

class Review(BaseModel):
    """This is a class module that manages reviews"""

    place_id = ""
    user_id = ""
    text = ""
