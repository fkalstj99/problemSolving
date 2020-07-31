Max = 1000000

Primes = [False]*(Max+1)

for i in range(2, Max + 1):
  if i*i > Max:
      break
      #불필요한 연산막기
  if Primes[i] == False:
    for j in range(2*i, Max+1, i):
      Primes[j] = True




while True:
  n = int(input())
  if n == 0:
    break
  
  
  for i in range(2,Max+1):
    if Primes[i] == False:

      if Primes[n - i] is False:
        print(n , "=", i, "+", n-i)
        break













#시간초과
Max = 1000000
Primes = []
Checks = [False, False] + [True]*(Max+1)

for i in range(2, Max + 1):
  if i*i > Max:
      break
  if Checks[i]:
    Primes.append(i)
    for j in range(2*i, Max+1, i):
      Checks[j] = False




while True:
  n = int(input())
  if n == 0:
    break
  
  
  for i in Primes:
    if n - i in Primes:
      print(n , "=", i, "+", n-i)
      break
