import random
import time

def _merge(a, b):
    i, j = 0, 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    
    return c

def merge_sort(a):
    if len(a) <= 1:
        return a
    
    mid = len(a)//2
    left = a[:mid]
    right = a[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return _merge(left, right)

with open("input_sort.txt", "r") as f:
    content = list(map(int, f.read().strip().split("\n")))

x = content

st_time = time.time_ns()
z = merge_sort(x)
t = (time.time_ns() - st_time) / (10**9)

#print(z)
print(f"execution time: {t}")