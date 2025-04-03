s = int(input())
banknots = list(map(int,input().split()))

su = [0]*(s+1)

def count(x):
    m = float('inf')
    for a in banknots:
        if x-a>=0:
            m = min(m, su[x-a]+1)
    return m

for i in range(1, s+1):
    su[i] = count(i)
if su[-1] != float('inf'):
    print(su[-1])
else:
    print(-1)