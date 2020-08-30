import sys
from collections import deque
input = sys.stdin.readline


def BFS():
    queue = deque()
    queue.append(S)
    dist[S] = 0
    while queue:
        now = queue.popleft()
        if now == G:
            print(dist[now])
            return
        for nx in (now + U), (now - D):
            if 1 <= nx <= F and dist[nx] == -1:
                queue.append(nx)
                dist[nx] = dist[now] + 1
    print("use the stairs")


    



F,S,G,U,D = map(int,input().split())
#빌딩의 층수 -> F층
#스타트링크가 있는층 -> G층
#강호가 있는층 -> S층
#위로 U층을 가는 버튼 -> U 
#아래로 D층을 가는 버튼 -> D
#만약 U층 위 , D층 아래에 해당하는 층이 없을때 -> 엘리베이터는 움직이지 않는다.

#강호가 G층에 도착하려면 버튼을 적어도 몇번 눌러야 하나 ?

dist = [-1]*(F+1)
BFS()
