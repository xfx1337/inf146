s = 0
min_sum = 0
sm = 0
for x in map(int, input().split()):
    s+=x
    min_sum = min(min_sum,s)
    sm = max(s-min_sum, sm)
print(sm)