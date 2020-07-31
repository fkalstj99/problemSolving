T = int(input())
NUMS = list(map(int, input().split(' ')))
CHECK = [False, False] + [True] * 1001
Primes = []

for i in range(2, 1001):
  if CHECK[i]:
    Primes.append(i)
    for j in range(2 * i, 1001, i):
      CHECK[j] = False