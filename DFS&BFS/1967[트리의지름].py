import sys
from collections import deque

input = sys.stdin.readline


def BFS(v):

    queue = deque()
    queue.append(v)
    distance = [-1] * (N+1)
    distance[v] = 0
    while queue:
         x = queue.popleft()
         for nxt, nxt_dist in adj_list[x]:
           if distance[nxt] == -1:
                distance[nxt] = distance[x] + nxt_dist
                queue.append(nxt)
        
  
    return distance


      
      





N = int(input())

adj_list = [[] for _ in range(N+1)]


for _ in range(N-1):
    A, B, W = map(int, input().split())
    adj_list[A].append([B,W])
    adj_list[B].append([A,W])



original_distance = BFS(1)

max_v = (original_distance.index(max(original_distance)))


print(max(BFS(max_v)))
