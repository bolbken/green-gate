from subprocess import Popen, PIPE
import re

def ping_ip(ip: str) -> str:
    pid = Popen(["ping", "-c", "3", ip], stdout=PIPE)
    s = pid.communicate()[0]
    print("-------\nPing Return: ", s , '\n')


def get_mac_from_ip(ip: str) -> str:
    # do_ping(IP)
    # The time between ping and arp check must be small, as ARP may not cache long
    pid = Popen(["arp", "-n", ip], stdout=PIPE)
    s = pid.communicate()[0]
    print(s)
    mac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s).groups()[0]
    print("Mac Adress Found: ", mac)
    return mac