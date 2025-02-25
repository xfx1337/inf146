n = 20
g = []

used = [] # список вершин, где на пройденную вершину 1, а на не пройденную 0

content = ""
with open("input.txt") as f:
    content = f.readlines()

# tin[v] - "время"(на какой итерации) входа в вершину
# tup[v] - "время" подъёма минимального(далее будет понятнее)
# p - предок(вершина, из которой мы попали в данную)
# T - текущее "время"
T = 0
sochleny = 0
root = 0
def dfs(v, p): # проходимся по всем вершинам, соединённым с вершиной v
    cnt = 0
    used[v] = 1
    is_root = False
    if v == root:
        is_root = True 
    global sochleny, T
    T += 1
    tin[v] = T
    tup[v] = tin[v] # время прихода в вершину ВЫШЕ текущей или её дерева(время подъёма снизу вверх), если мы в неё попали из её ребёнка
    for to in g[v]:
        if to == p: continue # если идём в предка, то нет, не надо, мы там уже были
        if used[to]: # если мы из этой вершины можем попасть в ту, в которой уже были, значит мы для вершины, в которую можно попасть ставим минимальное время, в которое можно туда попасть
            tup[v] = min(tup[v], tin[to])
        else: # если в вершине ещё не были - идём туда смотреть её соседей
            dfs(to, v)
            if is_root:
                cnt+=1
            tup[v] = min(tup[v], tup[to]) # для текущей вершины проверяем минимальное время
            if tin[v]<=tup[to] and not is_root:
                sochleny+=1
            # если минимальное время подъёма из вершины to больше чем время входа в вершину v, значит это мост. не было обратного ребра в вершину, куда мы заходили. то есть цикл не замкнулся
            # обновляем tup 
    if is_root and cnt>1:
        sochleny+=1

def get_sochleny_count():
    for i in range(len(g)):
        if not used[i]:
            root = i
            dfs(i, -1)
    return sochleny
# чтение
n, m = map(int, content[0].split())
g = []
for i in range(n):
    g.append([])

used = [0]*n
tin = [0]*n
tup = [0]*n

for i in range(1,m+1):
    a, b = content[i].split()
    a = ord(a)-65
    b = ord(b)-65
    g[a].append(b)
    g[b].append(a)


# исполнение
print(get_sochleny_count())