n = 20
g = []

used = [] # список вершин, где на пройденную вершину 1, а на не пройденную 0

content = ""
with open("input.txt") as f:
    content = f.readlines()

order = []
def dfs1(v):                                          
    used[v] = 1
    for to in g[v]:
        if not used[to]:
            dfs1(to)
    order.append(v)

def dfs2(v):
    used[v] = 1                                   
    for to in g_inv[v]:
        if not used[to]:
            dfs2(to)

def get_cnt():
    component_count = 0
    used = [0]*n
    for i in range(len(g)):
        if not used[i]:
            dfs1(i)
    
    used = [0]*n
    for i in range(len(g_inv)):
        v = order[len(g_inv)-1-i]
        if not used[v]:
            dfs2(v)
            component_count += 1
    return component_count

n, m = map(int, content[0].split())
g = []
g_inv = []
for i in range(n):
    g.append([])
    g_inv.append([])

used = [0]*n

for i in range(1,m+1):
    a, b = content[i].split()
    a = ord(a)-65
    b = ord(b)-65
    g[a].append(b)
    g_inv[b].append(a)

print(get_cnt())