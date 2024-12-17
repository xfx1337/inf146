from math import ceil

a = 213*1024/708
for i in range(0, 1000):
    if ceil(i*9/8) < a:
        print(i)
