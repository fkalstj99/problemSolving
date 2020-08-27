
def solve(start, depth):
    global result, charge
    #base Condition
    if depth == N:
        if matrix[start][0] > 0:
            answer = min(answer, charge + matrix[start][0])
            return 
    #재귀에는 항상 return값이 있어야 한다.

    visit[start] = True
    for i in range(N):
        if matrix[start][i] != 0 and visit[i] == False:
            charge += matrix[start][i]
            solve(i, depth+1)
            charge -= matrix[start][i]
    visit[start] = False 
#Backtracking할때 항상 기본값으로 돌려줘야 한다. -> 


N = int(input())
#도시 수

matrix = [list(map(int,input().split())) for _ in range(N)]

visit = [False] * N

result, charge = 10**9, 0

solve(0, 1)

print(result)





2. 비트마스크, DP

이번 문제에서는 N의 범위가 작았기 때문에 충분히 완전 탐색으로 해결할 수 있었지만,
N이 커질 경우에는 비트마스크를 사용한 풀이가 필수적이라 생각된다.

A, B, C, D, E -> 5개의 도시
A->B->C->D->E->A
A->C->B->D->E->A
D->E->A 공통된 부분이 생기게 된다.

두 경로 모두 D에 도착했을때 D->E->A의 비용만 더해주면 된다.


