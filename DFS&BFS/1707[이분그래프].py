from collections import deque

testCase = int(input())

def BFS(start, visit, color):
  queue = deque()
  queue.append(start)
  visit[start] = True
  color[start] = 2
  while queue:
    current = queue.popleft()
    for nxt in adj_list[current]:
      if not visit[nxt]:
        color[nxt] = 3 - color[current]
        visit[nxt] = True
        queue.append(nxt)
      if color[current] == color[nxt]:
        return False

  return True


for _ in range(testCase):
  N, M = map(int,input().split())
  adj_list = [[] for _ in range(N+1)] 
  for i in range(M):
    lst = map(int,input().split())
    adj_list[lst[0]].append(lst[1])
    adj_list[lst[1]].append(lst[0])

  visit = [False] * (N+1)
  color = [1] * N+1
  flag = True

  for start in range(1, N+1):
    if visit[start] == False:
      if BFS(start, visit, color) == False:
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