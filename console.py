import cmd
import models

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

if __name__=='__main__':
    HBNBCommand().cmdloop()
