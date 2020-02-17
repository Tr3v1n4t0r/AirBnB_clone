#!/usr/bin/python3

import cmd
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Class inherits cmd module import"""
    print("Welcome!")
    prompt = '(HBNB)'
    def do_quit(self, value):
        """exits the console"""
        print("Cya")
        return True

    do_EOF = do_quit
    """Handles the EOF"""

    def do_create(self, value):
        """Creates a new instance of a class, prints its ID and saves it"""
        args = value
        if (len(args) == 0):
            print("** class name missing **")
            return

    def do_show(self, value):
        """Prints the string representation of an instance based on the class name and id"""
        args = value
        if (len(args) == 0):
            print("** class name missing **")
            return

    def do_all(self, value):
        """Prints all string representation of all instances based or not on the class name"""
        args = value
        if args is None:
            print("** class doesn't exist **")
            return

    def do_destroy(self, value):
        """Deletes an instance based on the class name and id"""
        args = value
        if (len(args) == 0):
            print("** class name missing **")
            return

        if args is None:
            print("** class doesn't exist **")
            return

    def do_update(self, value):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = value
        if (len(args) == 0):
            print("** class name missing **")
            return

        if args is None:
            print("** class doesn't exist **")
            return
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()
