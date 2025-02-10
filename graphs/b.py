content = ""
with open("input.txt") as f:
    content = f.readlines()

m,n = map(int, content[0].split())

mtx = []

def myconvert(l):
    return (True if l=="." else False)

for i in range(1,m+1):
    s = content[i].strip()
    mtx.append(list(map(myconvert, list(s))))
g = []
used = [0]*n*m
for i in range(n*m):
    g.append(set())
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if not mtx[i][j]: g[i*n+j] = None
        if j>=1:
            if mtx[i][j-1] == mtx[i][j] and mtx[i][j]:
                g[i*n+j-1].add(i*n+j)
                g[i*n+j].add(i*n+j-1)
        if i<len(mtx)-1:
            try:
                if mtx[i][j] == mtx[i+1][j] and mtx[i][j]:
                    g[i*n+j].add(n*(i+1)+j)
                    g[n*(i+1)+j].add(n*(i)+j)
            except:
                breakpoint()

def dfs(v): # проходимся по всем вершинам, соединённым с вершиной v
    used[v] = 1
    for i in g[v]:
        if used[i]: continue
        dfs(i)

def get_cnt():
    c = 0
    for i in range(len(g)):
        if g[i]:
            if not used[i]:
                dfs(i)
                c+=1
        if g[i] == set():
            c+=1
    return c
print(get_cnt())