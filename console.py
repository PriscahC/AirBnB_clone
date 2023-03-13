#!/usr/bin/python3
"""This module is for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
import json

class HBNBCommand(cmd.Cmd):
    """This class is the entry point of the command interpreter."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            arg = arg.split()
            if arg[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            else:
                key = arg[0] + "." + arg[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
        else:
            arg = arg.split()
            if arg[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            else:
                key = arg[0] + "." + arg[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if not arg:
            for key, value in storage.all().items():
                print(value)
        else:
            arg = arg.split()
            if arg[0] != "BaseModel":
                print("** class doesn't exist **")
