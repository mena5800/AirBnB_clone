#!/usr/bin/python3
""" User Class """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class:
        it inherit from BaseModel class that condider our base class,
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
