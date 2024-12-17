from itertools import *

def f(x,y,z):
    return (x and not z) or (not y and not z)

table = [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]
answers = [1,0,0,0,1,0,1,0]

for p in permutations("xyz"):
    if [f(**dict(zip(p, r))) for r in table] == answers:
        print(p)