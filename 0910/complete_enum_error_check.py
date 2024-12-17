import math


def brute(f, a, b, e):
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


#def f(x):
#    return math.sin(x)

def f(x):
    return 2*x+3

x = brute(f, -2, 100, 0.2)
print(x)