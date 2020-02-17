#!/usr/bin/python3

import cmd
import json

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

    """"def do_create(self):
        if 
    def do_show(self):
    def do_destroy(self):
    def do_all(self):
    def do_update(self):"""
