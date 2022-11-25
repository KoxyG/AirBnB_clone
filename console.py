#!/usr/bin/python3

import cmd
from model.base_model import BaseModel


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
