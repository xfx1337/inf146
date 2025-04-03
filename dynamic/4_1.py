nums = list(map(int, input().split()))
k = int(input())
requests = []
for i in range(k):
    requests.append(list(map(int, input().split())))

s = [0]*(len(nums)+1)
for i in range(1, len(nums)+1):
    s[i] = s[i-1] + nums[i-1]

for r in requests:
    print(s[r[1]+1]-s[r[0]])