#!/usr/bin/python3
"""Modules documentation"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City
import json
import re
from models import storage


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand documentation"""

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """do_EOF is a method provided by the cmd.Cmd module. It is called when
the user presses Ctrl+D (Unix-like systems) or Ctrl+Z (Windows). By default,
it returns True, which will exit the command loop and terminate the program.
This is why when you press Ctrl+D in the interactive shell, it exits the
program.You can override this method to customize the behavior when EOF
is encountered. For example, if you want to ignore EOF and continue processing,
you can return False."""
        return True

    def emptyline(self):
        """Method called when an empty line is entered in response to the
prompt. If this method is not overridden, it repeats the last nonempty command
entered."""
        pass

    def do_create(self, arg):
        """ Creates a new instance of Classes, saves it (to the JSON file)
and prints the id"""
        toClasses = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'City': City, 'State': State, 'Amenity': Amenity
        }

        m_list = arg.split()
        if len(m_list) < 1:
            print("** class name missing **")
            return
        class_name = m_list[0]
        if class_name not in toClasses.keys():
            print("** class doesn't exist **")
            return
        new_ins = eval(m_list[0])()
        new_ins.save()
        print(new_ins.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
class name and id"""
        toClasses = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'City': City, 'State': State, 'Amenity': Amenity
        }

        if len(arg.split()) < 1:
            print("** class name missing **")
            return
        if (arg.split()[0] not in toClasses.keys()):
            print("** class doesn't exist **")
            return
        if len(arg.split()) < 2:
            print("** instance id missing **")
            return

        storage.reload()

        for k, v in storage.all().items():
            if k == f"{arg.split()[0]}.{arg.split()[1]}":
                print(v)
                return

        print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""
        flag = False
        if (len(arg.split()) < 1):
            print("** class name missing **")
            return
        if (arg.split()[0] != "BaseModel"):
            print("** class doesn't exist **")
            return
        if (len(arg.split()) < 2):
            print("** instance id missing **")
            return
        with open(storage.__file_path, "r+", encoding="utf8") as f:
            for line in f:
                match = re.search(r"\[(.*?)\]\s\((.*?)\)\s(.*?)$", line)
                if match:
                    class_name = match.group(1)
                    the_id = match.group(2)
                    the_dict = match.group(3)
                    if (class_name == arg.split()[0] and
                            the_id == arg.split()[1]):
                        del line
                        flag = True
        if not flag:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
