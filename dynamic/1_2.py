def minc():
    if n == 0:
        return 0
    d = [0] * n
    d[0] = price[0]
    if n > 1:
        d[1] = price[0] + price[1]
    for i in range(2, n):
       d[i] = min(d[i-1], d[i-2]) + price[i]
    return d[n-1]

n = int(input())
price = list(map(int, input().split()))
print(minc())