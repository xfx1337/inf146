from itertools import *

def f(w,x,y,z):
    return ((w <= y) or not (y <= z)) and not x and not(x==z)

for a in product([0,1], repeat=5):
    table = [
        (0,a[0],1,a[1]),
        (1,a[2],a[3],1),
        (0,a[4],1,1)
    ]
    answers = [1,1,1]

    if len(table) == len(set(table)):
        for p in permutations("wxyz"):
            if [f(**dict(zip(p, r))) for r in table] == answers:
                print(p)