A, B = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))


num = 0
result = []
for i in range(m):
  num += arr.pop()*(A**i)

print(num)

while num:
  result.append(num%B)
  num //= B


for i in range(len(result)-1, -1, -1):
  print(result[i], end=" ")