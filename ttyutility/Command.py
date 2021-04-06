from abc import ABC


class Command(ABC):
    """
    Base class of Command
    """
    parser = None
    subparser = None

    def configure(self, name: str, parser, prog: str = None, help: str = None):
        """
        Configuration of command

        :param name: name of command
        :param parser: subparser
        :param prog: name of program in Usage information
        :param help: help text command
        :return: None
        """
        self.parser = parser

        if help is not None:
            self.subparser = parser.add_parser(name, prog=prog, help=help)
        else:
            self.subparser = parser.add_parser(name, prog=prog)

    def add_argument(self, name: str, n: int = 0, convert: object = str, help: str = ''):
        """
        Add new argument of command

        :param name: name of argument (argument, -a, --argument...)
        :param n: number of paameters of argument (default is optional)
        :param convert: type of conversion of argument parameters (str by defualt)
        :param help: help text argument command
        :return: None
        """
        if n == 0:
            nargs = '?'
        else:
            nargs = n

        self.subparser.add_argument(
            name,
            nargs=nargs,
            type=convert,
            help=help
        )

    def execute(self, args: dict):
        """
        Execute command

        :param args: dictionary of arguments pass in command line
        :return: None
        """
        pass
