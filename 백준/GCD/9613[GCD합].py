n = int(input())


def gcd(a, b) :
    if b==0:
        return a
    else :
        return gcd(b,a%b)


for i in range(n):
  arr = list(map(int, input().split()))
  k = arr.pop(0)
  sum = 0
  for i in range(k):
    for j in range(i+1,k):
      sum += gcd(arr[i], arr[j])

  print(sum)