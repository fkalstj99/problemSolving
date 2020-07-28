import sys

num = int(input())



for i in range(num):
  a, b = map(int, sys.stdin.readline().split())
  A = a
  B = b
  while b > 0:
    temp = a % b
    a = b
    b = temp
  result = A * B // a
  print(result)





#재귀
import sys

num = int(input())


def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a%b)


for i in range(num):
  a, b = map(int, sys.stdin.readline().split())
  GCD = gcd(a,b)
  print(a*b//GCD)
    