from green_gate.config import get_hosts

from flask import Flask

app = Flask(__name__)


@app.route("/host/<hostname>")
def find_host(hostname):
    print("TESTING!")
    for host in get_hosts("/home/dev/personal/git/green-gate/hosts.json"):
        if host["hostname"] == hostname:
            return host

    else:
        return "No host found"
