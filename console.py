#!/usr/bin/python3
"""This is the console that serve as the entry point of the command interpreter"""
import cmd
class HBNBCommand(cmd.Cmd):
    """"This class define the console"""
    prompt = "(hbnb)"
    def do_EOF(self, line):
        """This method enable quit command interpreter"""
        return True

    def do_quit(self, line):
        """This method enable quit the interpreter"""
        return self.doEOF(line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
