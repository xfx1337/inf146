from itertools import *

s1 = '248 157 456 136 23 34 28 17'
s2 = 'FBE AHE FGH GH AB AC CD CDB'

s2 = {frozenset(x) for x in s2.split()}

for p in permutations("ABCDEFGH"):
    s3 = s1
    for x,y in zip('12345678', p):
        s3 = s3.replace(x,y)
    s3 = {frozenset(x) for x in s3.split()}
    if s2 == s3:
        print("1 2 3 4 5 6 7 8")
        print(*p)
