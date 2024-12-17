from math import *

expr = ""
exprp = ""
func = None
funcp = None
x0 = None
eps = None

with open("input.txt", "r") as f:
    expr = f.readline().strip()
    func = lambda x: eval(expr)
    exprp = f.readline().strip()
    funcp = lambda x: eval(exprp)
    x0 = float(f.readline().strip())
    eps = float(f.readline().strip())

def solve_newton(f, fp, x0, e, n=1000):
    i = 0
    while True:
        x = x0 - f(x0) / fp(x0)
        i += 1
        if abs(x0-x) < e or i > n:
            break
        x0 = x
    return x


x = solve_newton(func, funcp, x0, eps)
with open("output.txt", "w") as f:
    f.write(str(x))