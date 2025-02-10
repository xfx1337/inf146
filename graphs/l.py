# breadth first search
# обход в ширину

class Queue:
    def __init__(self):
        self._queue = []
    
    def push(self, el):
        self._queue.append(el)
    
    def pop(self):
        if not self.is_empty:
            return self._queue.pop(0)        

    def peek(self):
        return self._queue[0]
    
    @property
    def is_empty(self):
        return len(self._queue) == 0
    
    @property
    def length(self):
        return len(self._queue)

loops = [] 
def dfs(v, used=[]): # проходимся по всем вершинам, соединённым с вершиной v
    global loops # i want to easily store answers for now
    for i in g[v]:
        if len(used) > 0 and used[0] == i:
            loops.append(used.copy())
            break
        if i in used:
            break
        used.append(v)
        dfs(i, used)

content = ""
with open("input.txt") as f:
    content = f.readlines()

n, m = map(int, content[0].split())

g = []
for i in range(n):
    g.append([])
used = [0]*n
for i in range(1,m+1):
    a, b = map(int, content[i].split())
    g[a].append(b)
    g[b].append(a)

for i in range(len(g)):
    dfs(i)
print(*sorted(min(loops)))


# for i in range(len(g)):
#     dc = {}
#     used = [0]*n
#     q.push(i) # first is A
#     dc[i]=""
#     while not q.is_empty: bfs(q.peek(), q)
# print(max(ways, key=len)[0], max(ways, key=len)[-1])