from math import ceil
a = 1500*1024/1200
for i in range(1, 1000):
    if ceil(80*i/8) < a:
        print(i)
