#!/usr/bin/python3

import cmd
from model.base_model import BaseModel
from models import storage
import json
import re


class HBNBCommand(cmd.Cmd):
    """This is a class file that contains the entry point of the command interpreter"""

    prompt = "(hbnb)"


    def do_EOF(self, line):
        """End of file, exit"""
        return True

    def do_quit(self, line):
        """exits the program"""
        return True

    def do_create(self, line):
        """This command creates new instances and saves its to JSON file and prints id"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage:
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """prints the string representation of an instance based on class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split('')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """this module deletes an instance based on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split('')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
                list_str = [str(obj) for key, obj in storage.all().items()]
                print(list_str)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** classname missing **")
        elif classname not in storage:
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname.uid)
            if key not in storage.all():
                print("** no instance found **")
            elif attribute is None:
                print("** attribute name missing **")
            elif value is None:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*$', value):
                    cast = float
                  else:
                    cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


            


if __name__ == '__main__':
    HBNBCommand().cmdloop()
