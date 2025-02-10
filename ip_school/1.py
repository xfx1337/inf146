from ipaddress import *

 # 0 - disable strict mode

for mask in range(1,33):
    net1 = ip_network(f"192.1.115.185/{mask}", 0)
    net2 = ip_network(f"192.1.115.156/{mask}", 0)
    if net1==net2:
        print(mask)