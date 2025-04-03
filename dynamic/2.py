price = list(map(int, input().split()))
n = len(price)

#@lru_cache(None) # 
def f(fr, to, pay, traj):
    if fr>to: return [float('inf'), traj]
    if fr==to: return [pay, traj]
    h = []
    if len(price) > fr+1-1:
        h.append(f(fr+1, to, pay+price[fr+1-1], traj+[fr+1]))
    if len(price) > fr+2-1:
        h.append(f(fr+2, to, pay+price[fr+2-1], traj+[fr+2]))
    if len(price)> fr+3-1:
        h.append(f(fr+3, to, pay+price[fr+3-1], traj+[fr+3]))
    h.append([float('inf'), traj])
    return min(h, key=lambda x: x[0])

# for i in range(1,n):
#     f(1,i,price[0], [1])
res = f(1,n, price[1-1], [1])
print(res[0])
print(res[1])