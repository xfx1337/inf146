from itertools import *

s1 = "1246 21345 325 41267 5237 6147 7456"
s2 = "АБВГ БАГД ВАГЕ ГАБВД ДГБЕК ЕВДК КДЕ"
s2 = {x[0]:set(x[1:]) for x in s2.split()}

for p in permutations("АБВГДЕК"):
    s3 = s1
    for x, y in zip("1234567", p):
        s3 = s3.replace(x,y)
    s3 = {x[0]:set(x[1:]) for x in s3.split()}
    if s2 == s3:
        print("1 2 3 4 5 6 7    ")
        print(*p)
        print()
