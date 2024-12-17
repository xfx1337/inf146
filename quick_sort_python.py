import time

with open("input_sort.txt", "r") as f:
    content = list(map(int, f.read().strip().split("\n")))

st_time = time.time_ns()
z = sorted(content)
t = (time.time_ns() - st_time) / (10**9)

#print(z)
print(f"execution time: {t}")