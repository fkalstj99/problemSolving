
# BOJ 1525
from collections import deque

def bfs():
    while q:
        d = q.popleft()
        if d == 123456789:
            print(dist[d])
            return
        s=str(d)
        zero=s.find('9')
        # x는 행 y는 열
        x,y = zero//3, zero%3
#9자리 수의 문자열에 문자 '9'의 위치를 k라 하고, 3*3 퍼즐의 각 좌표를 (x, y)라고 하자.
#이때, x = k/3, y = k%3으로 나타낼 수 있다.

        for dx, dy in (1,0), (-1,0), (0,1), (0,-1):
            nx, ny = x+dx, y+dy
            if 0<=nx<3 and 0<=ny<3:
                k = nx*3+ny
#9를 상하좌우로 옮기면서, 원래 있던 숫자와 교환한다.
                ns = list(s)
                ns[k], ns[zero] = ns[zero], ns[k]
                nd = int(''.join(ns))
                if not dist.get(nd):
                    dist[nd]=dist[d]+1
                    q.append(nd)
#퍼즐을 움직일 수 있을 때까지 움직이면서, 
#퍼즐 상태가 123456789라면 퍼즐 이동 횟수를 출력하고 바로 종료한다    
    print(-1)
#더 이상 못 움직일 때까지 퍼즐을 123456789로 못 맞춘다면, 
# -1을 출력한다



q = deque()
# dist의 key:value=정수:옮긴횟수
dist = {}
puzzle = [list(map(int, input().split())) for _ in range(3)]
m=0
for i in range(3):
    for j in range(3):
        n = puzzle[i][j]
        if n==0:
            n=9
        m = m*10 + n
q.append(m)
dist[m]=0
bfs()