#!/usr/bin/python3
"""
console module :
this module contain class HBNBCommand that inherit from CMD class in cmd
module, it is considered the terminal of our airBnB project.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User



class HBNBCommand(cmd.Cmd):
    """
    console class to control our program using terminal.
    """
    prompt = "(hbnb) "
    class_dict = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                  "State": State, "City": City, "Amenity": Amenity,
                  "Review": Review}

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def do_EOF(self, arg):
        "EOF command to exit the program"
        return True

    def emptyline(self):
        pass
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg not in self.class_dict.keys():
            print("** class doesn't exist **")
        else:
            list_of_args = arg.split()
            if len(list_of_args) == 1:
                if arg in self.class_dict.keys():
                    new = self.class_dict[arg]()
                    new.save()
                    print(new.id)

    def do_show(self, arg):
        """ Prints string representation"""
        list_of_args = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif list_of_args[0] not in self.class_dict:
            print("** class doesn't exist **")
        elif len(list_of_args) > 1:
            key = list_of_args[0] + '.' + list_of_args[1]
            if key in storage.all():
                i = storage.all()
                print(i[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_destroy(self, arg):
        """Deletes an instance"""
        list_of_args = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif list_of_args[0] not in self.class_dict:
            print("** class doesn't exist **")
        elif len(list_of_args) > 1:
            key = list_of_args[0] + '.' + list_of_args[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
                return

    def do_all(self, arg):
        """  Prints all string representation of all instances"""
        if len(arg) == 0:
            print([str(k) for k in storage.all().values()])
        elif arg not in self.class_dict:
            print("** class doesn't exist **")
        else:
            list_of_values = []
            for k, v in storage.all().items():
                if arg in k:
                    list_of_values.append(str(v))
            print(list_of_values)

    def do_update(self, arg):
        """Updates an instance"""
        list_of_args = arg.split()
        if len(list_of_args) == 0:
            print('** class name missing **')
            return
        
        elif list_of_args[0] not in self.class_dict:
            print("** class doesn't exist **")
        elif len(list_of_args) == 1:
            print('** instance id missing **')
            
        ids = set()
        
        for value in storage.all().values():
            if value.__class__.__name__ == list_of_args[0]:
                ids.add(value.id)
 
        if list_of_args[1] not in ids:
            print("** no instance found **")
        elif len(list_of_args) == 2:
            print("** attribute name missing **")
        elif len(list_of_args) == 3:
            print("** value missing **")
        elif len(list_of_args) == 4:
            for value in storage.all().values():
                if value.id == list_of_args[1]:
                    # if (value.__dict__.get(list_of_args[2],None)) != None:
                    value.__dict__[list_of_args[2]] = list_of_args[3][1:-1]
                    storage.save()



if __name__ == "__main__":
    HBNBCommand().cmdloop()
