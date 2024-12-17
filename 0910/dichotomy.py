import math


def dichotomy(f, a, b, e):
    fa, fb = f(a), f(b)
    while b - a >= e:
        c = (a+b)/2
        fc = f(c)
        if fa*fc > 0:
            a, fa = c, fc
        else:
            b, fb = c, fc
    return c


#def f(x):
#    return math.sin(x)

def f(x):
    return 2*x+3

x = dichotomy(f, -2, 100, 0.1)
print(x)