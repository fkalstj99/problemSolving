N = int(input())


i = 2

while i <= N:
  if N % i == 0:
    print(i)
    N /= i
  else:
    i+=1
#나눌때 나머지가 0이 되지 않으면 +1