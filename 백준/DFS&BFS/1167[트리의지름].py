import sys


def dfs(v):
    vst[v] = True
    for nxt, nxt_d in adj_lst[v]:
        if not vst[nxt]:
            d[nxt] = d[v] + nxt_d
            dfs(nxt)


v = int(sys.stdin.readline())
adj_lst = [[] for _ in range(v + 1)]
for _ in range(v):
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(arr) - 1, 2):
        adj_lst[arr[0]].append([arr[i], arr[i + 1]])

vst = [False] * (v + 1)
d = [0] * (v + 1)
dfs(1)


max_v = d.index(max(d))
vst = [False] * (v + 1)
d = [0] * (v + 1)
dfs(max_v)

print(max(d))


#트리에 존재하는 모든 경로 중에서 가장 긴 것의 길이를 트리의 지름이라고 한다.
#트리의 지름은 탐색 2번으로 구할 수 있다.
#루트에서 모든 정점까지의 거리를 구한다. 이 때, 가장 먼 거리 였던 정점을 A라고 한다.
#A를 루트라고 하고 모든 정점까지의 거리를 구한다. 이 때 구한 가장 먼 거리가 지름이다.