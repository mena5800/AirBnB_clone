import json
import os 

class FileStorage:
    __file_path = "../file.json"
    __objects = {}
    
    
    
    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        FileStorage.__objects["{}.{}".format("BaseModel", obj.id)] = obj.to_dict()
    
    def save(self):
        with open(FileStorage.__file_path, "w") as f:
            
            json.dump(FileStorage.__objects, f)
    
    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)

        
            
        
        