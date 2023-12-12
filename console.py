#!/usr/bin/python3
"""This is the console that serves as the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """"This class defines the console"""
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """This method enables quitting the command interpreter"""
        return True

    def do_quit(self, line):
        """This method enables quitting the interpreter"""
        return self.do_EOF(line)
    
    def do_help(self, arg):
        """Show help message for each command"""
        cmd.Cmd.do_help(self, arg)

    def do_create(self, line):
        """This method creates a new instance of BaseModel, saves it (to the JSON file), and prints the id.
        Ex: $ create BaseModel"""
        if not line:
            print("** class name missing **")
            return
        try:
            create_instance = eval(line)()
            create_instance.save()
            instance_id = create_instance.id
            print(instance_id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """This method prints the string representation of an instance based on the class name and id."""
        arguments = line.split()

        if not arguments:
            print("** class name missing **")
            return

        class_name = arguments[0]

        if len(arguments) < 2:
            print("** instance id missing **")
            return

        instance_id = arguments[1]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, line):
        """This method deletes an instance based on the class name and id (saves the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234."""
        arguments = line.split()

        if not arguments:
            print("** class name missing **")
            return

        class_name = arguments[0]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(arguments) < 2:
            print("** instance id missing **")
            return

        instance_id = arguments[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """This method prints all string representations of all instances based or not on the class name.
        Ex: $ all BaseModel or $ all."""
        arguments = line.split()
        if arguments and arguments[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        instances = storage.all().values()
        class_name = arguments[0] if arguments else None
        if class_name:
            filtered_instances = [instance for instance in instances if instance.__class__.__name__ == class_name]
        else:
            filtered_instances = instances

        print([str(instance) for instance in filtered_instances])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating an attribute
        (saves the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"."""
        arguments = line.split()

        if not arguments:
            print("** class name missing **")
            return

        class_name = arguments[0]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(arguments) < 2:
            print("** instance id missing **")
            return

        instance_id = arguments[1]

        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(arguments) < 3:
            print("** attribute name missing **")
            return

        attribute_name = arguments[2]

        if len(arguments) < 4:
            print("** value missing **")
            return

        attribute_value = arguments[3]

        instance = storage.all()[key]
        instance_attr_names = instance.__dict__.keys()

        if attribute_name not in instance_attr_names:
            print("** attribute name missing **")
            return

        attr_type = type(getattr(instance, attribute_name))

        try:
            casted_value = attr_type(attribute_value)
        except ValueError:
            print("** invalid value **")
            return

        setattr(instance, attribute_name, casted_value)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
