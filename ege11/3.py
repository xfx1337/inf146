from math import *
per_user = ceil(31*1024*1024/252500)

for kod in range(1, 1000):
    bit = ceil(log2(kod))
    if ceil(261*bit/8) >= per_user:
        print(kod)
        break
