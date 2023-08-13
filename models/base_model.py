#!/usr/bin/python3
"""
base_model module :
this module contain BaseModel class this class consider
our base calss for our AirBnB project.
"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """Base Model Class:
    this class has a lot of functions and consider the base class of
    many others classe.
    """

    def __init__(self, *args, **kwargs):
        """constructor"""
        if kwargs:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """print object representation"""

        return ('[' + type(self).__name__ + '] (' +
                str(self.id) + ') ' + str(self.__dict__))

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
