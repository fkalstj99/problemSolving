from collections import deque


def BFS(y,x):
  queue.append([y,x])
  while queue:
    ay, ax = queue.popleft()
    for i in range(4):
      ny = ay + dy[i]
      nx = ax + dx[i]      
      if 0 <= ny < N and 0 <= nx <M and Map[ny][nx] == '1':
        queue.append([ny,nx])
        Map[ny][nx] = int(Map[ay][ax]) + 1





N, M = map(int,input().split())

Map = [list(input()) for _ in range(N)]
dx , dy = (1,-1,0,0), (0,0,1,-1)
queue = deque()
BFS(0,0)
print(Map[N-1][M-1])
