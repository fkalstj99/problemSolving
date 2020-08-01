dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
def bfs(i, j):
    Map[i][j] = 0
    queue = [[i, j]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(8):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < h and 0 <= y < w and Map[x][y] == 1:
                Map[x][y] = 0
                queue.append([x, y])
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    Map = []
    cnt = 0
    for i in range(h):
        Map.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if Map[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)


#indent를 잘하자 

