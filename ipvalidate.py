import re

def validate_ip(ip):
    ipv4 = r"^(\d{1,3}\.){3}\d{1,3}$"
    ipv6 = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$:"

    if re.match(ipv4, ip):
        parts = ip.split(".")
        for part in parts:
            if int(part) > 255:
                return False
            return True

    elif re.match(ipv6, ip):
        return True

    return False

ip = input("Enter an IP address: ")

print("Valid IP address:", validate_ip(ip))