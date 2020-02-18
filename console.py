#!/usr/bin/python3

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Class inherits cmd module import"""

    prompt = '(HBNB)'

    classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
               'Review']

    functions = ['update', 'create', 'show', 'destroy', 'quit']

    def precmd(self, line):
        """Parses the input string"""
        for c in self.classes:
            for f in self.functions:
                pref = "{}.{}".format(c, f)
                if line.startswith(pref):
                    remain = line[len(pref) + 1:-1].replace(",", "")
                    remain = remain.replace(":", "")
                    remain = remain.replace("}", "")
                    remain2 = shlex.split(remain, posix=False)
                    if (len(remain2) == 1):
                        id_attr = remain2[0].strip("\"'")
                        return "{} {} {}".format(f, c, id_attr)
                    elif (len(remain2) == 2):
                        id_attr = remain2[0].strip("\"'")
                        attr_name = remain2[1].strip("\"'")
                        return "{} {} {} {}".format(f, c, id_attr, attr_name)
                    elif (len(remain2) >= 3):
                        id_attr = remain2[0]
                        attr_name = remain2[1]
                        if not attr_name.startswith('{'):
                            attr_val = remain2[2]
                            return "{} {} {} {} {}".format(f, c, id_attr,
                                                           attr_name, attr_val)
                        for i in range(1, len(remain2) // 2 + 1):
                            if len(remain2) >= 2 * i + 1:
                                attr_name = remain2[2 * i + 1].strip("\"'{}:")
                                attr_value = remain2[2 * i].strip("\"'{}:")
                            if (i >= len(remain2) // 2):
                                return "{} {} {} {} {}".format(f, c, id_attr,
                                                               attr_name,
                                                               attr_val)
                            else:
                                self.cmdqueue.append(f + ' ' + c + ' ' +
                                                     id_attr + ' "' +
                                                     attr_name + '" "' +
                                                     attr_val + '"')
                    new_line = "{} {} {}".format(f, c, remain)
                    return new_line
        return line

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

    def do_EOF = do_quit
    """Handles the EOF"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
