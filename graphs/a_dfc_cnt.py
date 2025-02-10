n = 20
g = []

used = [] # список вершин, где на пройденную вершину 1, а на не пройденную 0

content = ""
with open("input.txt") as f:
    content = f.readlines()

def dfs(v): # проходимся по всем вершинам, соединённым с вершиной v
    used[v] = 1
    for i in g[v]:
        if used[i]: continue
        dfs(i)

def get_cnt():
    c = 0
    for i in range(len(g)):
        if not used[i]:
            dfs(i)
            c+=1
    return c

n, m = map(int, content[0].split())
g = []
for i in range(n):
    g.append([])

used = [0]*n

for i in range(1,m+1):
    a, b = content[i].split()
    a = ord(a)-65
    b = ord(b)-65
    g[a].append(b)
    g[b].append(a)

print(get_cnt())