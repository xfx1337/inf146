def f(x):
    return (x&41==0)<=((x&119!=0)<=(x&a!=0))

for a in range(1,100):
    if all(f(x)==1 for x in range(1,10000)):
        print(a)