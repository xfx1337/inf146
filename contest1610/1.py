from math import *

expr = ""
func = None
left = None
right = None
eps = None

with open("input.txt", "r") as f:
    expr = f.readline().strip()
    func = lambda x: eval(expr)
    left = float(f.readline().strip())
    right = float(f.readline().strip())
    eps = float(f.readline().strip())

def solve_brute(f, a, b, e):
    dm = float('inf')
    xm = -float('inf')
    i = 0
    while i+a < b:
        d = abs(0-(f(a+i)))
        if d < dm:
            dm = d
            xm = a+i
        i += e
    return xm

x = solve_brute(func, left, right, eps)
with open("output.txt", "w") as f:
    f.write(str(x))