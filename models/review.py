#!/usr/bin/python3
"""
this review module contain Review class
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Review class : this class inherit from BaseModel
    class.
    puplic class attributes:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
