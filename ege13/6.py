from ipaddress import *

# номер компьютера = его адрес - адрес сети

ip1 = ip_address("192.168.156.235")
ip2 = ip_address("192.168.156.224")

print(int(ip1)-int(ip2))