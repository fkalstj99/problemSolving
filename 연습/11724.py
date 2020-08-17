N, M = map(int,input().split())



adj_map = [[False]*(N+1) for _ in range(N+1)]

visit = [False] * (N+1)


for _ in range(M):
    vertex_lst = list(map(int,input().split()))
    adj_map[vertex_lst[0]][vertex_lst[1]] = 1
    adj_map[vertex_lst[1]][vertex_lst[0]] = 1



def DFS(start,visit):
    visit[start] = True
    for i in range(N+1):
        if visit[i] == False and adj_map[start][i] == 1:
            DFS(i, visit)

count = 0
for i in range(1 , N+1):
    if visit[i] == False:
        DFS(i,visit)
        count=+1


print(count)








