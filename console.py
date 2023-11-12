#!/usr/bin/python3
"""Modules documentation"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
import json
import re
from models import storage


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand documentation"""

    prompt = '(hbnb) '

    def precmd(self, arg):
        """Hook method executed just before the command is processed."""

        if re.search(".+.all()", arg) or arg == ".all()":
            return f"all {arg[:-6]}"

        elif re.search(".+.count()", arg) or arg == ".count()":
            return f"count {arg[:-8]}"

        elif re.search(".+.show(.*)", arg):
            _ = arg[arg.find('\"')+1:arg.rfind('\"')]
            return f"show {arg[:arg.find('.show')]}" + " " + _

        elif re.search(".+.destroy(.*)", arg):
            _ = arg[arg.find('\"')+1:arg.rfind('\"')]
            return f"destroy {arg[:arg.find('.destroy')]}" + " " + _

        elif re.search(".+.update(.*)", arg):
            return "update {} {} {} {}".format(
                arg[:arg.find('.update')],
                arg[arg.find('\"')+1:arg.find('\",')],
                arg[arg.find(' \"')+1:arg.rfind(',')],
                arg[arg.rfind(' ')+1:arg.rfind(')')])

        return arg

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
            'City': City, 'State': State, 'Amenity': Amenity, 'Review': Review
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
            'City': City, 'State': State, 'Amenity': Amenity, 'Review': Review
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
        Classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'City': City, 'State': State, 'Amenity': Amenity, 'Review': Review
        }
        if (len(arg.split()) < 1):
            print("** class name missing **")
            return
        if (arg.split()[0] not in Classes.keys()):
            print("** class doesn't exist **")
            return
        if (len(arg.split()) < 2):
            print("** instance id missing **")
            return
        storage.reload()
        key_to_del = "{}.{}".format(arg.split()[0], arg.split()[1])

        if key_to_del in storage.all():
            del storage.all()[key_to_del]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
the class name."""
        dic = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'City': City, 'State': State, 'Amenity': Amenity, 'Review': Review
        }
        storage.reload()
        m_list = []
        if (not arg):
            for key, value in storage.all().items():
                m_list.append(str(value))

        if (len(arg.split()) == 1):
            if (arg.split()[0] in dic):
                for k, v in storage.all().items():
                    if v.__class__.__name__ == arg.split()[0]:
                        m_list.append(str(v))
            else:
                print("** class doesn't exist **")
                return
        print(m_list)

    def do_count(self, arg):
        dic = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'City': City, 'State': State, 'Amenity': Amenity, 'Review': Review
        }
        storage.reload()
        m_list = []
        if (not arg):
            for key, value in storage.all().items():
                m_list.append(str(value))

        if (len(arg.split()) == 1):
            if (arg.split()[0] in dic):
                for k, v in storage.all().items():
                    if v.__class__.__name__ == arg.split()[0]:
                        m_list.append(str(v))
            else:
                print("** class doesn't exist **")
                return

        print(len(m_list))

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
or updating attribute"""
        dic = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'City': City, 'State': State, 'Amenity': Amenity, 'Review': Review
        }
        if (len(arg.split()) < 1):
            print("** class name missing **")
            return
        if (arg.split()[0] not in dic.keys()):
            print("** class doesn't exist **")
            return
        if (len(arg.split()) < 2):
            print("** instance id missing **")
            return
        if (len(arg.split()) < 3):
            print("** attribute name missing **")
            return
        storage.reload()
        instances = storage.all()
        key = "{}.{}".format(arg.split()[0], arg.split()[1])
        if key not in instances:
            print("** no instance found **")
            return
        if (len(arg.split()) < 4):
            print("** value missing **")
            return
        instance = instances[key]
        attribute_name = arg.split()[2]
        attribute_value = arg.split()[3]
        if not hasattr(instance, attribute_name):
            setattr(instance, attribute_name, attribute_value)
        setattr(instance, attribute_name,
                type(getattr(instance, attribute_name))(attribute_value))
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
