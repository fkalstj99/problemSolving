import sys
from collections import deque

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def BFS():
    days = -1
  
    while queue:
        days += 1
        for _ in range(len(queue)):
            x,y = queue.popleft()
    
    
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx < H) and (0 <= ny < W) and (Map[nx][ny] == 0):
                    Map[nx][ny] = Map[x][y] + 1
                    queue.append([nx,ny])
  
        for i in range(H):
            for j in range(W):
                if Map[i][j] == 0:
                return -1

        return days




W, H = map(int, input().split())
Map = [list(map(int,input().split())) for _ in range(H)]
queue = deque()

for i in range(H):
  for j in range(W):
    if Map[i][j] == 1:
          queue.append([i,j])



print(BFS())


