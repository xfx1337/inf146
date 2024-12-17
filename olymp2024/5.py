X = int(input())
b = 1
c = int(X**0.5)
for i in range(1, c+1):
    if X%(i**2) == 0:
        b=i**2
print(int(X/b))