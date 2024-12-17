x1, y1, x2, y2 = map(int, input("x1 y1 x2 y2: ").split())

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        elif b >= a:
            b = b % a
    return a + b

nod = gcd(abs(x2-x1), abs(y2-y1))
print(nod+1)