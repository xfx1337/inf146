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

def solve_dichotomy(func, a, b, eps):
    y_a, y_b = func(a), func(b)
    while b - a >= eps:
        c = (a+b)/2
        y_c = func(c)
        if y_a*y_c > 0:
            a, y_a = c, y_c
        else:
            b, y_b = c, y_c
    return c


x = solve_dichotomy(func, left, right, eps)
with open("output.txt", "w") as f:
    f.write(str(x))