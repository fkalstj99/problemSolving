
#https://suri78.tistory.com/152


1. 완전탐색

import sys


input = sys.stdin.readline

def move(now, depth):
    global charge, ans
    if depth == N:
        #마지막 깊이일때 -> 1로 회귀하여야 한다. 
        if matrix[now][0] > 0:
          # 1로 회귀할때의 값
            ans = min(ans, charge+matrix[now][0])
        return
    
    visit[now] = True
    for l in adj_list[now]:
        if not visit[l]:
            charge += matrix[now][l]
            move(l, depth+1)
            charge -= matrix[now][l]
    visit[now] = False


N = int(input())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visit = [False]*N
adj_list = {}
charge, ans = 0, 10**7


for i in range(N):
  adj_list[i] = []
  for j in range(N):
      if matrix[i][j] > 0:
         adj_list[i].append(j)

move(0,1)
print(ans)





2. 비트마스크, DP

이번 문제에서는 N의 범위가 작았기 때문에 충분히 완전 탐색으로 해결할 수 있었지만,
N이 커질 경우에는 비트마스크를 사용한 풀이가 필수적이라 생각된다.

A, B, C, D, E -> 5개의 도시
A->B->C->D->E->A
A->C->B->D->E->A
D->E->A 공통된 부분이 생기게 된다.

두 경로 모두 D에 도착했을때 D->E->A의 비용만 더해주면 된다.


