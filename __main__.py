from green_gate.config import remote_hosts
from green_gate.network import ping_ip, get_mac_from_ip

for host in remote_hosts:

    ping_ip(host)
    mac = get_mac_from_ip(host)