import time


with open("input_sort.txt", "r") as f:
    content = list(map(int, f.read().strip().split("\n")))


def bubble_sort(s_list):
    for j in range(len(s_list)-1):
        sort_st = True
        for i in range(len(s_list)-1-j):
            if s_list[i] > s_list[i+1]:
                s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
                sort_st = False
        if sort_st == True:
            break

st_time = time.time_ns()
bubble_sort(content)
t = (time.time_ns() - st_time) / (10**9)

print(content)
print(f"execution time: {t}")