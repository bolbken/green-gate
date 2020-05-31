"""

client initial use case
```bash
ggate client --power-on <hostname>
```

What needs to be in place to make this happen?

The client computer needs to have a file that sets up the connection to the server.
On second thought... this should likely be an optional argument at the cli

So like this 
```bash
ggate client --power-on <hostname> \
    --public-address <internet domain name/ip> \
    --port <ggate server port number> \
    --client-cert <file path> 
```
    
This type of input can then be abstracted by using a file handler under the hood with a config use...

**SSH'd into server: get a client config
ggate server --client-config-template -o yaml > ...

#YAML##################
server:
    network:
        mac:
        ipv4:
        hostname:
    service:
        port:
        api: <url>
client:
    id:
    uid:
    cert:
########################

** Secure Copy the file to the client
scp server client ~/.green-gate/config

** On client machine
ggate client setup --auto
or for custom location
ggate client apply -f ~/...

then can simply say...
ggate client -po <hostname>

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
        self._setup_server_address()
        self._setup_port()
        self._setup_client_cert()

    def _setup_power_on_command(self):
        self.parser.add_argument(
            "--power-on",
            "-po",
            dest="on_target",
            help="Command used to power-on a machine on the remote servers network.",
        )

    def _setup_server_address(self):
        self.parser.add_argument(
            "--server-address",
            "-s",
            dest="public_address",
            help="A valid IPV4 or DNS Hostname accesible on the public internet.",
        )

    def _setup_port(self):
        self.parser.add_argument(
            "--port",
            "-p",
            dest="public_address",
            help="A valid IPV4 or DNS Hostname accesible on the public internet.",
        )

    def _setup_client_cert(self):
        self.parser.add_argument(
            "--client-cert",
            "-crt",
            dest="client_crt_path",
            help="A relative or full path pointing to a client certificate to be used to authenticate with the server.",
        )

    def parse(self, args):
        return self.parser.parse_known_args(args)
