from collections import deque


def DFS_grouping(y,x):
    Map[y][x] = group_num
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if 0<=ny<N and 0<=nx<N and Map[ny][nx] == 1:
        DFS_grouping(ny,nx) 


def BFS_bridge(start):
  queue = deque()
  global ans
  visit = [[-1]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if Map[i][j] == start:
        queue.append([i,j]) 
        visit[i][j] = 0

  while queue:
    y,x=queue.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<N and 0<=nx<N:
          if Map[ny][nx] and Map[ny][nx] != start:
            ans = min(ans, visit[y][x])
            return 
          if not Map[ny][nx] and visit[ny][nx] == -1:
              visit[ny][nx] = visit[y][x] + 1
              queue.append([ny,nx])





N = int(input())

Map = [list(map(int,input().split())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
group_num = 1
ans = 10**9
for i in range(N):
  for j in range(N):
    if not Map[i][j]:
      group_num += 1
      DFS_grouping(i,j)

for i in range(2, group_num+1):
  BFS_bridge(i)

print(ans)