from math import *

a = 276*1024/862
for i in range(1, 1000):
    if ceil(10*i/8) < a:
        print(i)
