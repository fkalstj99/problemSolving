n,m = map(int, input().split())
Check = [False, False] + [True]*(m-1)
Primes = []


for i in range(2, m+1):
  if Check[i]:
    Primes.append(i)
    for j in range(2*i, m+1, i):
      Check[j] = False

for j in Primes:
  if m >= j and j >= n:
    print(j)
    
 


