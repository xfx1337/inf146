from ipaddress import *

 # 0 - disable strict mode
for mask in range(1,33):
    net1 = ip_network(f"167.77.194.104/{mask}", 0)
    net2 = ip_network(f"167.77.206.210/{mask}", 0)
    if net1!=net2:
        for ip in net2:
            if mask==32:
                print(ip)
            if "167.77.206.210" == str(ip):
                for ip in net1:
                    if mask == 32:
                        print(ip)
                    if "167.77.194.104" == str(ip):
                        print(mask)