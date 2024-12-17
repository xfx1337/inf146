from itertools import *

s1 = "1247 2148 3578 4126 538 647 7136 8235"
s2 = "ABHE BAH CEGD DFC EAGC FHGD GEFC HABF"
s2 = {x[0]:set(x[1:]) for x in s2.split()}

for p in permutations("ABCDEFGH"):
    s3 = s1
    for x, y in zip("12345678", p):
        s3 = s3.replace(x,y)
    s3 = {x[0]:set(x[1:]) for x in s3.split()}
    if s2 == s3:
        print("1 2 3 4 5 6 7 8")
        print(*p)
        print()
