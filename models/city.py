#!/usr/bin/python3
"""
this city module contain City class
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    City class : this class inherit from BaseModel
    class and has a public class attribute name and state_id.
    """
    state_id = ""
    name = ""
    objects = []
