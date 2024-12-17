def ds(d, m, y, ms):
    days = 0
    full_years = (y - 1)
    days += full_years * sum(ms)
    for i in range(m - 1):
        days += ms[i]
    days += d
    return days


def calculate(d1, m1, y1, d2, m2, y2, N, ms):
    start_days = ds(d1, m1, y1, ms)
    end_days = ds(d2, m2, y2, ms)
    duration = end_days - start_days + 1
    return duration


d1 = int(input())
m1 = int(input())
y1 = int(input())
d2 = int(input())
m2 = int(input())
y2 = int(input())
N = int(input())

ms = []
for i in range(N):
    ms.append(int(input()))

print(calculate(d1, m1, y1, d2, m2, y2, N, ms))