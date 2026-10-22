server_ip = ("192.168.1.1",)
allowed_ips = ["192.168.1.2", "192.168.1.3"]


def update_allowed_ips(ip):
    allowed_ips.append(ip)
    print("Allowed IP added successfully")


print("Server IP:", server_ip)
print("Allowed IPs:", allowed_ips)

update_allowed_ips("192.168.1.4")

print("Updated Server IP:", server_ip)
print("Updated Allowed IPs:", allowed_ips)