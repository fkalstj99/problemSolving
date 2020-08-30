
import sys

sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())

graph_matrix = [[0] * (N + 1) for i in range(N + 1)]

visit = [0 for i in range(N + 1)]

count = 0

def DFS(i):
  visit[i] = 1
  for k in range(1, N+1):
    if graph_matrix[i][k] == 1 and visit[k] == 0:
      DFS(k)


for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph_matrix[a][b] = 1
    graph_matrix[b][a] = 1


for i in range(1, N + 1):
  if visit[i] == 0:
    DFS(i)
    count += 1

print(count)




#adjacent list 
def dfs(v):
    visited[v] = True
    for e in adj_list[v]:
        if not visited[e]:
            dfs(e)
            
N, M = map(int, input().split())
adj_list = [[] for i in range(N+1)]
visited = [False] * (N + 1)
cnt = 0
 
for i in range(M):
    input_data = list(map(int, input().split()))
    adj_list[input_data[0]].append(input_data[1])
    adj_list[input_data[1]].append(input_data[0])
    
for i in range(1, len(visited)):
    if not(visited[i]):
        cnt += 1
        dfs(i)
        
print(cnt)