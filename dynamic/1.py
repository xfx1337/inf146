from functools import lru_cache
n = int(input())
price = list(map(int, input().split()))

@lru_cache(None) # 
def f(fr, to, pay):
    if fr>to: return float('inf')
    if fr==to: return pay
    h = []
    if len(price) > fr+1-1:
        h.append(f(fr+1, to, pay+price[fr+1-1]))
    if len(price) > fr+2-1:
        h.append(f(fr+2, to, pay+price[fr+2-1]))
    h.append(float('inf'))
    return min(h)

for i in range(1,n):
    f(1,i,price[0])

print(f(1,n, price[1-1]))