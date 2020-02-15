#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """Class inherits cmd module import"""

    prompt = '(HBNB)'

    def do_quit(self, value):
        """exits the console"""
        print("Cya")
        return True

    do_EOF = do_quit
    """Handles the EOF"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
