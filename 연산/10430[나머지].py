import sys

A, B, C = map(int, sys.stdin.readline().split())

for i in range(4):
  if i == 0:
    print((A+B)%C)
  if i == 1:
    print(((A%C) + (B%C))%C)
  if i == 2:
    print((A*B)%C)
  if i == 3:
    print(((A%C) * (B%C))%C)
  