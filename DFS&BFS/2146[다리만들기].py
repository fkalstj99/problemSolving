import sys
from collections import deque
sys.setrecursionlimit(10**6)

n = int(input())
Map = [list(map(int, input().split())) for _ in range(n)]
check = [[False]*n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans, group_num = 10**9, 1

def DFS_grouping(x, y):
    check[x][y] = True
    Map[x][y] = group_num
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:   
          if check[nx][ny] == False and Map[nx][ny]:
          #안들렸고 바다가 아니라면
             DFS_grouping(nx,ny)

def BFS_bridge(z):
    global ans
    dist = [[-1]*n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if Map[i][j] == z:
                q.append((i, j))
                dist[i][j] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if Map[nx][ny] and Map[nx][ny] != z:
               #다른 섬이 존재하고 다른 그룹일때
                ans = min(ans, dist[x][y])
                return
            if not Map[nx][ny] and dist[nx][ny] == -1:
                #조사되지 않았고 바다일때
                dist[nx][ny] = dist[x][y]+1
                q.append((nx, ny))

for i in range(n):
    for j in range(n):
        if not check[i][j] and Map[i][j]:
            DFS_grouping(i, j)
            group_num += 1
for i in range(1, group_num+1):
    BFS_bridge(i)
print(ans)

