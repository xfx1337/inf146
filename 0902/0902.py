N = int(input())
cieve = [True]*(N+1)
cieve[0] = False
cieve[1] = False
for i in range(2, int(N**0.5)+1):
    idx = i+i
    while idx < N+1:
        cieve[idx] = False
        idx += i

primes = []
for i in range(2, N+1):
    if cieve[i]:
        primes.append(i)

print(primes)
print(len(primes))