ca = list(map(int, input().split()))
cb = list(map(int, input().split()))

def awin():
    ca.append(ca[0])
    del ca[0]
    ca.append(cb[0])
    del cb[0]

def bwin():
    cb.append(ca[0])
    del ca[0]
    cb.append(cb[0])
    del cb[0]

c = 1
while c < 10**6+1:
    a = ca[0]
    b = cb[0]
    if a > b:
        if a == 11 and b == 0:
            bwin()
        else:
            awin()
    else:
        if b == 11 and a == 0:
            awin()
        else:
            bwin()
    
    if len(ca) == 0:
        print(f"second {c}")
        break
    elif len(cb) == 0:
        print(f"first {c}")
        break
    else:
        c += 1
if c > 10**6:
    print("game draw")