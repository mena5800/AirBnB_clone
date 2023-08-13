#!/usr/bin/python3
"""
this state module contain State class
"""
from .base_model import BaseModel


class State(BaseModel):
    """
    State class : this class inherit from BaseModel
    class and has a public class attribute name
    """
    name = ""
