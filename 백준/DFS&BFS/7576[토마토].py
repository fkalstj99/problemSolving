from collections import deque

def BFS():
  days = 0
  while queue:
    for _ in range(len(queue)):
        ay, ax = queue.popleft()
        for i in range(4):
          ny = ay + dy[i]
          nx = ax + dx[i]
          if 0<= ny < N and 0 <= nx < M and Map[ny][nx] == 0:
            Map[ny][nx] = Map[ay][ax] + 1
            queue.append([ny,nx])
            days = Map[ny][nx]
  
  for i in range(N):
    for j in range(M):
      if Map[i][j] == 0:
        return -1

  return days - 1





M, N = map(int,input().split())

Map = [list(map(int,input().split())) for _ in range(N)]
dx , dy = (1,-1,0,0), (0,0,1,-1)
queue = deque()
for i in range(N):
  for j in range(M):
    if Map[i][j] == 1:
       queue.append([i,j])
#이렇게 해줘야 하는 이유 => 한번씩 교차로 실행되어야 한다.

print(BFS())



