import sys
input = sys.stdin.readline


def BFS_binary(v, visited, color):
  queue = [v]
  visited[v] = True
  color[v] = 1
  while queue:
    current = queue.pop(0)
    for next in adj_list[current]:
      if not visited[next]:
        queue.append(next)
        color[next] = 3 - color[current]
        visited[next] = True
      else:
        if color[current] == color[next]:
          return False
  return True



testCase = int(input())
for i in range(testCase):
  N, M = map(int, input().split())
  adj_list = [[] for _ in range(N + 1)]

  for j in range(M):
    a ,b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

  visited = [False for _ in range(N+1)]
  color = [0 for _ in range(N + 1)]
  flag = True

  for node in range(1, N+1):
    if visited[node] == False:
      if BFS_binary(node, visited, color) == False:
        flag = False
        break
  
  if flag == False:
    print("NO")
  else:
    print("YES")



#탐색중 방문 노드 -> 기존은 true(1) 표현

#but, 해당 문제-> 1(RED), 2(BLUE),0(방문x)으로 표현 


#bfs
#시작 노드 색상-> RED(아무색상). 
#시작 노드와 연결노드들 ->반대색상(BLUE)로 지정.
#방식 -> queue

#dfs
#시작 노드 색상-> RED(아무색상)
#시작 노드와 연결노드들 -> 반대색상(BLUE)으로 지정.
#방식 -> 재귀함수 

#이분그래프 
#인접한 정점 -> 서로 다른색 -> 모든 정점은 두가지 색으로 나뉨

#1. BFS, DFS 탐색 -> 두가지 색 중 하나 칠함
#2. 다음 정점을 방문-> 자신과 인접한 정점 -> 자신과 다른색
#3. 탐색 진행중 인접한 정점 색이 자신과 동일 -> 이분 그래프 아님
#4. 모든 정점 방문-> 3의 경우가 없다면 이분 그래프 
#모든 정점 방문 이유 -> 비연결 그래프일 수 있기에