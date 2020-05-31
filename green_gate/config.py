import json



def get_hosts(path: str = "./hosts.json") -> dict:
    with open(path, "r") as hosts_file:
        return json.load(hosts_file)


if __name__ == "__main__":
    hosts = get_hosts("/home/dev/personal/git/green-gate/hosts.json")

    for host in hosts:
        print(host["address"]["ipv4"])
