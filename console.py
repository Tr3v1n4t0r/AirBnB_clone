#!/usr/bin/python3

import cmd
import shlex
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Class inherits cmd module import"""

    prompt = '(HBNB)'

    def do_all(self, line):
        """Prints all instances"""
        if not line:
            my_list = [str(value) for key, value in storage.all().items()]
            if len(my_list) != 0:
                print(my_list)
            else:
                args = lint.split()
                if args[0] in self.classes:
                    my_list = []
                    for key, value in storage.all().items():
                        if str(key.split('.')[0]) == args[0]:
                            my_list.append(str(value))
                    if len(my_list) != 0:
                        print(my_list)
                else:
                    print("** class doen't exist **")

    def do_update(self, line):
        """Updates an instance based on class name and id"""
        if not line:
            print('** class name missing **')
            return

        args = shlex.split(line, posix=False)
        if args[0] not in self.classes:
            print('** instance id missing **')
            return
        elif:
            try:
                key = args[0] + '.' + args[1]
                storage.all()[key]
            except:
                print('** no instance found **')
                return

        if len(args) < 2:
            print('** attribute id missing **')
        elif len(args) == 3:
            print('** value missing **')
        else:
            key = args[0] + '.' + args[1]
            try:
                if '.' in args[3]:
                    value = float(args[3])
                else:
                    value = int(args[3])
            except ValueError:
                value = str(args[3]).strip("\"':")
                value = str(value)
            setattr(storage.all()[key], args[2].strip("\"':"), value)
            storage.save()

    def do_create(self, line):
        """Create a new instance of Base Model"""
        if not line:
            print('** class name missing **')
            return
        args = line.split()
        try:
            new = eval(args[0] + '()')
            print(new.id)
            new.save()
        except:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints an instance based on class name and id"""
        if not line:
            print('** class name missing **')
            return

        args = line.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            try:
                key = args[0] + '.' + args[1]
                print(storage.all()[key])
            except KeyError:
                print('** no instance found **')

    def do_destroy(self, line):
        """Deletes in instance based on class name and id"""
        if not line:
            print('** class name missing **')
            return

        args = line.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            try:
                key = args[0] + '.' + args[1]
                del storage.all()[key]
                storage.save()
            except:
                print('** no instance found **')

    def do_quit(self, value):
        """exits the console"""
        print("Cya")
        return True

    do_EOF = do_quit
    """Handles the EOF"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
