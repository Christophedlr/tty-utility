import argparse

from ttyutility import Command


class Console:
    """
    Console manager
    """

    commands: dict = {}
    parser = None
    subparser = None

    def __init__(self):
        """
        Init of class.
        Register parser & subparser.
        """
        self.parser = argparse.ArgumentParser()
        self.subparser = self.parser.add_subparsers(dest='command')

    def register(self, name: str, command: Command):
        """
        Register new command, and load configure method of command

        :param name: name of command
        :param command: instance of Command base class
        """
        self.commands[name] = command
        self.commands[name].configure(name, self.subparser)

    def run(self, args: tuple = None):
        """
        Run console with an optional args for simulate command line

        :param args: list of command line
        """
        if args is not None:
            arguments = self.parser.parse_args(args)
        else:
            arguments = self.parser.parse_args()

        for name in self.commands:
            if vars(arguments)['command'] == name:
                self.commands[name].execute(vars(arguments))
