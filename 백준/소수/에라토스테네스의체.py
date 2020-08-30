
N = int(input())

CHECK = [False] * (N+1)
Primes = []

for i in range(2, N+1):
    if not CHECK[i]:
        Primes.append(i)
        for j in range(2 * i, N+1, i):
            CHECK[j] = True








N = int(input())

CHECK = [False] * (N+1)
Primes = []

for i in range(2, N+1):
    if i*i > N:
        break
    if not CHECK[i]:
        Primes.append(i)
        for j in range(2 * i, N+1, i):
            CHECK[j] = True


