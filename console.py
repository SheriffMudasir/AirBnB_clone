#!/usr/bin/python3
"""
This module is the entry point of the command interpreter.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    This class serve as the command interpreter.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """This metthod do nothing on an empty input line."""
        pass

    def do_quit(self, arg):
        """This method quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """This method is the EOF command to exit the program."""
        print()
        return True

    def do_create(self, arg):
        """This method create a new instance, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = storage.create(arg)
            storage.save()
            print(new_instance.id)
        except Exception as e:
            print(f"Error: {str(e)}")

    def do_show(self, arg):
        """This method print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            obj = storage.get(class_name, instance_id)
            if obj:
                print(obj)
            else:
                print("** no instance found **")
        except Exception as e:
            print(f"Error: {str(e)}")

    def do_destroy(self, arg):
        """This method delete an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except Exception as e:
            print(f"Error: {str(e)}")

    def do_all(self, arg):
        """This method print all string representation of all instances."""
        args = arg.split()
        obj_list = []
        if not arg:
            for key, value in storage.all().items():
                obj_list.append(str(value))
            print(obj_list)
            return
        try:
            class_name = args[0]
            for key, value in storage.all().items():
                if class_name == key.split(".")[0]:
                    obj_list.append(str(value))
            if obj_list:
                print(obj_list)
            else:
                print("** class doesn't exist **")
        except Exception as e:
            print(f"Error: {str(e)}")

    def do_update(self, arg):
        """This method update an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attribute_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            attribute_value = args[3]
            obj = storage.all()[key]
            setattr(obj, attribute_name, attribute_value)
            obj.save()
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
