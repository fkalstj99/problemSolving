import sys
input = sys.stdin.readline

ts = int(input())



def DFS(start):
  visited[start] = True
  number = nums[start]
  if not visited[number]:
    DFS(number)




for _ in range(ts):
  N = int(input())
  nums = [0] + list(map(int, input().split()))
  visited = [False for i in range(N+1)]

  result = 0

  for i in range(1, N+1):
    if not visited[i]:
      DFS(i)
      result += 1

  print(result)