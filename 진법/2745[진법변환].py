n ,m = input().split()
N = int(m)
result = 0

for i, j in enumerate(n):
  try:
    if int(j):
      result += int(j)*(N**(len(n) - i - 1))
  except:
    result += (ord(j) -55)*(N**(len(n)- i - 1)) 

print(result)