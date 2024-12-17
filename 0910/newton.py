import math


def newton(f, f1, x0, e, n=1000):
    i = 0
    while True:
        x = x0 - f(x0) / f1(x0)
        i += 1
        if abs(x0 -x) < e or i > n:
            break
        x0 = x
    return x



def f(x) # function to check:
    return 2*x+3

def f1(x): # proizvodnaya
    return 2

x = newton(f, f1, 0, 0.1)
print(x)