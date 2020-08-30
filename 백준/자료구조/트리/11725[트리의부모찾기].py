#재귀함수의 최대깊이를 늘려주지 않으면 런타임 에러가 발생한다.
#기본적으로 1000레벨까지로 정해져 있다.abs
#sys.setrecursionlimit(10 ** 9)을 통해 재귀의 깊이를 늘려줌

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


N = int(input())
tree = [[]for _ in range(N+1)]
#인접리스트 
for _ in range(N - 1):
  A,B = map(int, input().split())
#부모-자식 순서 X -> 랜덤 순서이기에 O 양뱡향으로 넣어줘야함
  tree[A].append(B)
  tree[B].append(A)


parents = [0 for _ in range(N+1)]


def DFS(start,tree,parents):
    for i in tree[start]:#연결된 노드 모두탐색
        if parents[i]==0:#한번도 방문한적이 없다면
           parents[i]=start#부모노드 저장
           DFS(i,tree,parents)
#DFS탐색 -> 탐색 방향 노드가 아직 방문되지 않았다면 
# 탐색 방향 노드 탐색 동시에 전 노드 -> 탐색 방향 노드 부모로 설정.


DFS(1, tree, parents)

for i in range(2,N+1):
    print(parents[i])

#1 DFS 탐색 -> 6, 4는 방문X 연결O | 6, 4 부모 -> 1 
#6 DFS 탐색 -> 3 방문x 연결 O     | 3 부모 -> 6
#3 DFS 탐색 -> 5 방문x 연결 O     | 5 부모 -> 3
#반복하면 모든 노드의 부모 알 수 있음


#트리란 그래프의 일종으로, 여러 노드가 한 노드를 가리킬 수 없는 구조이다.
#서로 다른 두 노드를 잇는 길이 하나뿐인 그래프를 트리라고 부른다.