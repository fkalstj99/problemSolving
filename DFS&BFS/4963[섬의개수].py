def DFS(y,x):
  Map[y][x] = 0
  for i in range(8):
    ny = x + dy[i]
    nx = y + dx[i]
    if 0<= ny < h and 0 <= nx <w:
      if Map[ny][nx] == 1:
        DFS(ny,nx)



dx = [1,-1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1,-1, 1, 1, -1, -1]

while True:
  w,h = map(int, input().split())
  if w == 0 and h == 0:
    break
  Map = [list(map(int,input().split())) for _ in range(h)]
  
  count = 0
  for i in range(h):
    for j in range(w):
      if Map[i][j] == 1:
        count +=1
        DFS(i,j)
  
  print(count)
        


#indent를 잘하자 

