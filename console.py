import cmd
import models
from models.base_model import BaseModel

classes = {'BaseModel': BaseModel}

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True
    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True
    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, args):

        args = args.split()

        if len(args) == 0:
            print('** class name missing **')

        class_name = arg[0]

        if class_name not in classes:
            print('** class doesn't exist **')

        instance_obj = classes[class_name]()
        instance_obj.save()

if __name__=='__main__':
    HBNBCommand().cmdloop()
