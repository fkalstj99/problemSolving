import sys

input = sys.stdin.readline

N = int(input())
Map = [list(input()) for _ in range(N)]
count = 0
address = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]




def DFS(x,y):
  global count
  #방문 표시
  Map[x][y] = '0'
  count += 1
  for i in range(4):
    #상하좌우 비교
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
      continue
    #방문안됨(1) -> 호출
    if Map[nx][ny] == '1':
      DFS(nx, ny)


for i in range(N):
  for j in range(N):
    if Map[i][j] == '1':
      #DFS하기전 0으로 초기화
      count = 0
      DFS(i,j)
      #DFS후 count값 넣어줌
      address.append(count)


print(len(address))
address.sort()
for i in address:
  print(i)
