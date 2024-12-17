def bubble_sort(s_list):
    for j in range(len(s_list)-1):
        for i in range(len(s_list)-1-j):
            if s_list[i] > s_list[i+1]:
                s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
                print("".join(s_list))

def bubble_sort2(s_list):
    for j in range(len(s_list)-1):
        for i in range(len(s_list)-1-j):
            if s_list[i] < s_list[i+1]:
                s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
                print("".join(s_list))

word = list(input())
bubble_sort(word)
bubble_sort2(word)