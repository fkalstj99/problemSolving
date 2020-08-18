testCase = int(input())

def DFS(start):
  global result
  visit[start] = True
  nxt = adj_list[start]
  cycle.append(start)
  if visit[nxt]:
    if nxt in cycle:
      result += cycle[cycle.index(nxt):]
      return
  else:
    DFS(nxt)




for _ in range(testCase):
  N = int(input())
  adj_list =[0] + list(map(int, input().split()))
  visit = [False]*(N+1)
  result = []

  for i in range(1, N+1):
    if visit[i] == False:
      cycle = []
      DFS(i)
  print(N - len(result))
 
