import math


def brute(f, a, b, e):
    dl = float('inf')
    du = float('inf')
    xl = -float('inf')
    xu = float('-inf')

    i = 0
    while i+a < b:
        d = 0-(f(a+i))
        if d > 0:
            if d < dl:
                dl = d
                xl = a+i
        if d < 0:
            d = abs(d)
            if d < du:
                du = d
                xu = a+i

        i += e
    return (xl+xu)/2


#def f(x):
#    return math.sin(x)

def f(x):
    return 2*x+3

x = brute(f, -2, 100, 0.2)
print(x)