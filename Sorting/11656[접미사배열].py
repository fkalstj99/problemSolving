import sys

str = sys.stdin.readline()

result = []


for i in range(len(str) - 1):
  result.append(str[i:len(str)-1])


result.sort()

for i in result:
  print(i)
