import re

ip = input("Enter IP address: ")

pattern = r'^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3}$'

if re.match(pattern, ip):
    print("Valid IP address")
else:
    print("Invalid IP address")