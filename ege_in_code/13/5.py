from ipaddress import *
net = ip_network("185.178.54.144/255.255.255.240")
k = 0
for ip in net:
    print(ip, f"{ip:b}")
    print(bin(int(ip))[2:].zfill(32)) # old ver
    b = f"{ip:b}"
    if '111' in b:
        k += 1
print(k)