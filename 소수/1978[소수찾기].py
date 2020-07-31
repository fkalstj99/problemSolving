CHECK = [False, False] + [True] * 1001
Primes = []

for i in range(2, 1001):
  if CHECK[i]:
    Primes.append(i)
    for j in range(2 * i, 1001, i):
      CHECK[j] = False
      


num = int(input())
arr = list(map(int, input().split()))

count = 0

for i in Primes:
  if i in arr:
    count+=1

print(count)