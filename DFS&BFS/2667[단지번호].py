

N = int(input())
Map = [list(map(int,input())) for _ in range(N)]

dx, dy = (1,0,-1,0), (0,1,0,-1)




count = 0
result = []

def DFS(x,y):
    global count
    Map[x][y] = 0
    count+=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0 <= ny < N:
            if Map[nx][ny] == 1:
                DFS(nx,ny)
    


for i in range(N):
  for j in range(N):
    if Map[i][j] == 1:
        count = 0
        DFS(i,j)
        result.append(count)

print(len(result))
for i in sorted(result):
    print(i)
