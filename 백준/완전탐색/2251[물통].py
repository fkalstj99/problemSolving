from collections import deque

def pour(x,y):
    if not visited[x][y]:
        visited[x][y] = True
        queue.append([x,y])

def BFS():
  queue.append([0,0])
  visited[0][0] = True
  while queue:
      x, y = queue.popleft()
      z = c-x-y
      #3번째 물통 물의양
      #물의 총량은 변하지 않는다.
      if x == 0:
        result.append(z)

      water = min(x, b-y)
#min(x, b-y)을 왜 할까? 
#총 물통의 양을 넘어서는 안되니깐 한계를 설정해준다. 
      pour(x-water, y+water)
      water = min(x, c-z)
      pour(x-water, y)
      water = min(y, a-x)
      pour(x+water, y-water)
      water = min(y, c-z)
      pour(x, y-water)
      water = min(z, a-x)
      pour(x +water,y)
      water = min(z, b-y)
      pour(x, y+water)

a, b, c = map(int, input().split())
result = []
visited = [[False]*(201) for _ in range(201)] 
queue = deque()
print(' '.join(map(str, sorted(result))))


C(물통 C의 양) = C(물통 C의 부피) - a(물통 A의 남은 물의 양) - b(물통 B의 남은 물의 양)
