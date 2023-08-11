"""
file_storage module :
this module has class FileStorage that use to store instances in json file
"""

import json
import os


class FileStorage:
    """
    FileStorage class :
    it is the class we use to store objects from base class.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        "returns the dictionary __objects"
        return FileStorage.__objects

    def new(self, obj):
        "sets in __objects the obj with key <obj class name>.id"
        FileStorage.__objects["{}.{}".format(
            obj.__class__.__name__, str(obj.id))] = obj

    def save(self):
        "serializes __objects to the JSON file (path: __file_path)"
        with open(FileStorage.__file_path, "w") as f:
            new_dict = {}
            for key, value in FileStorage.__objects.items():
                obj_dict = value.to_dict()
                new_dict[key] = obj_dict
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn't exist,
        no exception should be raised)"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                json_obj = json.load(f)
                for k, v in json_obj.items():
                    FileStorage.__objects[k] = eval(
                        v['__class__'])(**v)
