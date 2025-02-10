# breadth first search
# обход в ширину

from queue import Queue

dc = {}

def bfs(v, queue):
    used[v] = 1
    for vx in g[v]:
        if used[vx]: continue
        queue.push(vx)



content = ""
with open("input.txt") as f:
    content = f.readlines()

n, m = map(int, content[0].split())

g = []
for i in range(n):
    g.append([])
used = [0]*n
q = Queue()
for i in range(1,m+1):
    a, b = content[i].split()
    a = ord(a)-65
    b = ord(b)-65
    g[a].append(b)
    g[b].append(a)

q.push(0) # first is A
while not q.is_empty: bfs(q.pop(), q)
