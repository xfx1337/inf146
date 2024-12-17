import random as rnd

with open("input_sort.txt", "w") as f:
    for i in range(15000000):
        f.write(f"{rnd.randint(1, 10000)}\n")
