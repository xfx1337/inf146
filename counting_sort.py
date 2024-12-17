import random
import time

with open("input_sort.txt", "r") as f:
    content = list(map(int, f.read().strip().split("\n")))

m = max(content)
a = content

def counting_sort(a):
    c = [0] * (m + 1)
    for b in a:
        c[b] += 1
    
    d = []
    for i, j in enumerate(c):
        d += [i] * j
    
    return d


st_time = time.time_ns()
z = counting_sort(a)
t = (time.time_ns() - st_time) / (10**9)

#print(z)
print(f"execution time: {t}")