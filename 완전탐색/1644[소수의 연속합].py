
N = int(input())

CHECK = [False] * (N+1)
Primes = []

for i in range(2, N+1):
    if not CHECK[i]:
        Primes.append(i)
        for j in range(2 * i, N+1, i):
            CHECK[j] = True

def solve():
    start = end = Sum = answer = 0
    K = len(Primes)
    while True:
        if Sum >= N:
            Sum -= Primes[start]
            start += 1
        else:
            if end == K:
                break
            Sum += Primes[end]
            end +=1
        
        if Sum == N:
            answer +=1
    print(answer)

solve()