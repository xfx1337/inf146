from math import *

expr = ""
func = None
x0 = None
x1 = None
eps = None

with open("input.txt", "r") as f:
    expr = f.readline().strip()
    func = lambda x: eval(expr)
    x0 = float(f.readline().strip())
    x1 = float(f.readline().strip())
    eps = float(f.readline().strip())

def solve_sec(f, a, b, e):
    i = 0
    x = a
    while abs(f(b) - f(x)) > e:
        b = x - (f(x) * (b - x) / (f(b) - f(a)))
        x = b
    return b

def ends(f, a, b, e):
    l = []
    while a < b:
        if f(a) * f(a+e) < 0:
            l.append((a,a + e))
        a += h
    return l


l = ends(f, x0, x1, eps)[0]
for t in s:
   print(sec(f, x0, x1, 0.0000001))

x = solve_sec(func, x0, x1, eps)
with open("output.txt", "w") as f:
    f.write(str(x))