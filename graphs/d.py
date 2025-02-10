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

loop = False
def dfs2(v, got=[]): # проходимся по всем вершинам, соединённым с вершиной v
    global loop
    used.append(v)
    for i in g[v]:
        if len(got)>1:
            if i==got[0]:
                loop = True
                break
        if i in used: continue
        got.append(v)
        dfs2(i, got)
        del got[-1]

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

for i in range(n):
    dfs2(i)

if get_cnt()==1 and not loop:
    print("YES")
else:
    print("NO")