def f(N):
    bN = bin(N)[2:]
    sm = 0
    for d in bN:
        sm += int(d)
    if sm % 4 == 0:
        bN = "10" + bN
    else:
        bN = "11" + bN
    if (int(bN, 2)) % 2 == 0:
        bN = bN + "1"
    else:
        bN = bN + "0"
    return int(bN, 2)

print(f(13))
mx = 0
for i in range(0, 500):
    x = f(i)
    if x <= 250 and x > mx:
        mx = x
    
print(mx)