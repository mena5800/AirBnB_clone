"""
this amenity module contain amenity class
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class : this class inherit from BaseModel
    class and has a public class attribute name
    """
    name = ""
    objects = []
