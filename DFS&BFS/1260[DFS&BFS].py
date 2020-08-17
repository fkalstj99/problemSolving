from collections import deque

N,M,start_v = map(int,input().split())
visit = [False] * (N+1)

adj_map = [[False]*(N+1) for _ in range (N+1)]



for i in range(M):
  vertex_list = map(int,input().split())
  adj_map[vertex_list[0]][vertex_list[1]] = 1
  adj_map[vertex_list[1]][vertex_list[0]] = 1



def DFS(start,visit):
  visit[start] = True
  result =+ [start]
  for i in adj_map[start]:
    if visit[i] == False and i not in result == 1:
      DFS(visit, i)
  return result



def BFS(start):
  
  result = [start]
  queue = deque()
  queue.append(start)

  while queue:
    current = queue.popleft()
    for i in adj_map[current]:
      if i not in result:
        result.append(i)
        queue.append(i)
  
  return result
        

print(*DFS(start_v, []))
print(*BFS(start_v))
