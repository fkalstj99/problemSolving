import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

visit = [0 for _ in range(100001)]

queue = deque()
depth = deque()
depth.append(0)
queue.append(N)

while True:
    #현재위치와 depth
    subin = queue.popleft()
    _time = depth.popleft()
    
    #방문하지 않았던 곳이면 실행
    if not visit[subin]:
        visit[subin] = 1

        if subin - 1 >= 0:
            queue.append(subin - 1)
            depth.append(_time + 1)
        if 2 * subin <= 100000:
            queue.append(2*subin)
            depth.append(_time+1)
        if subin+1 <= 100000:
            queue.append(subin+1)
            depth.append(_time+1)
        

    if subin == M:
        print(_time)
        break