import argparse
from green_gate.cli import parser
from green_gate.cli.client import ClientActionsParser


parser: argparse.ArgumentParser = argparse.ArgumentParser(prog="ggate")


def main():

    subparser = parser.add_subparsers()
    client_actions = ClientActionsParser(subparser)

    args = parser.parse_args()

    print(args)
