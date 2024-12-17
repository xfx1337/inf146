def count_M(x):
    M = 0
    for i in range(2, int(x**0.5+1)):
        if x % i == 0:
            M = i + int(x/i)
            break
    return M

i = 8000000
counter = 0
while True:
    if counter == 5:
        break
    i+=1
    m = count_M(i)
    l1 = m % 10
    l2 = m % 100 // 10
    x = l2 * 10 + l1
    if x == 14:
        print(f"{i} {m}")
        counter += 1