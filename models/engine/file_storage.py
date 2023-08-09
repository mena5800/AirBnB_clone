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
            "BaseModel", obj.id)] = obj.to_dict()

    def save(self):
        "serializes __objects to the JSON file (path: __file_path)"

        with open(FileStorage.__file_path, "w") as f:

            json.dump(FileStorage.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn't exist,
        no exception should be raised)"""

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
