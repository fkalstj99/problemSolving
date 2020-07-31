import sys
sys.setrecursionlimit(111111)

input = sys.stdin.readline

def DFS(i):
  global result
  visited[i] = True
  number = numbers[i]
  cycle.append(i)
  if visited[number]:
    if number in cycle:
      result += cycle[cycle.index(number):]
      return
  else:
    DFS(number)







testCase = int(input())

for _ in range(testCase):
  N = int(input())
  numbers = [0] + list(map(int, input().split()))
  visited = [False for i in range(N+1)]
  result = []

  for i in range(1, N+1):
    if not visited[i]:
      cycle = []
      DFS(i)

  print(N - len(result))

