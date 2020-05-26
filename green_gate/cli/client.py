"""
    1. client use case
        ggate power-on <hostname>
        ggate power-off <hostname>

"""

from argparse import _SubParsersAction, ArgumentParser

# create the parser for the "foo" command
# parser_foo = subparsers.add_parser("foo")
# parser_foo.add_argument("-x", type=int, default=1)
# parser_foo.add_argument("y", type=float)
# parser_foo.set_defaults(func=foo)


class ClientActionsParser:

    parser_name = "client"

    def __init__(self, subparser: _SubParsersAction):

        self.parser: ArgumentParser = subparser.add_parser(
            self.parser_name, description="Client commands for controlling the server."
        )

        self._setup_power_on_command()

    def _setup_power_on_command(self):

        self.parser.add_argument(
            "--power-on",
            "-po",
            dest="on_target",
            help="Command used to power-on a machine on the servers network.",
        )

    def parse(self, args):
        return self.parser.parse_known_args(args)
