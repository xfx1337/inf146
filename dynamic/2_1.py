def minc():
    if n == 0:
        return 0, []
    d = [float('inf')] * n
    d[0] = price[0]
    path = [-1]*n

    for i in range(1, n):
        for s in range(1, 4):
            if i-s >= 0:
                curr = d[i-s] + price[i]
                if curr < d[i]:
                    d[i] = curr
                    path[i] = i-s
    traj = []
    curr = n-1
    while curr != -1:
        traj.append(curr+1)
        curr = path[curr]
    traj = traj[::-1]            
    return d[n-1], traj

price = list(map(int, input().split()))
n = len(price)
r = minc()
print(r[0])
print(r[1])