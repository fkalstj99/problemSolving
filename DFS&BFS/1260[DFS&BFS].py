N, M, V = map(int, input().split())
graph_matrix = [[0]*(N + 1) for _ in range(N + 1)]

for _ in range(M):
  edge = list(map(int, input().split()))
  graph_matrix[edge[0]][edge[1]] = 1
  graph_matrix[edge[1]][edge[0]] = 1



def BFS(start):
  queue = [start]
  result = [start]
  while queue:
    current_node = queue.pop(0)
    for i in range(len(graph_matrix[current_node])):
      if graph_matrix[current_node][i] and i not in result:
        result.append(i)
        queue.append(i)
  return result

#BFS(visited) : 1
#   Queue     : 1

#처음에는 start로 init하고 

#BFS(visited) : 1 2 3 4
#   Queue     : 1(pop) 2 3 4

# 1. queue에서 첫번째를 뺀다 => 조사를 끝마쳤다.
# 2. 조사된 node들(2, 3 ,4)을  BFS에 Queue에 넣는다. 

#BFS(visited) : 1 2 3 4
#   Queue     : 1(pop) 2(pop) 3(pop) 4(pop)

# visited에 모두 있기에 조사할 필요가 없다.




def DFS(start, visited):
  visited += [start]
  for i in range(len(graph_matrix[start])):
    if graph_matrix[start][i] == 1 and (i not in visited):
      DFS(i, visited)
  return visited


#DFS(visited) : 1
#   Stack     : 1

#BFS와 마찬가지로 start로 init하고

#DFS(visited) : 1 2
#   Stack     : 1 2


#1. 1 조사 -> 먼저 이어진 2를 visited, Stack에 넣는다.
#2. 2 조사 -> 먼저 이어진 4를 visited, Stack에 넣는다
#Stack에 들어가면서 초점이 1 -> 2로 바뀜

#DFS(visited) : 1 2 4
#   Stack     : 1 2 4

# 4 조사 -> 먼저 이어진 3을 visited, Stack에 넣는다

#DFS(visited) : 1 2 4 3
#   Stack     : 1 2 4 3

# 3 조사
# 이어져있는 1, 4는 visited에 있고 
# 이어져있지 않은 2도 visited에 있다. 
# 조사끝 



print(*DFS(V, []))
print(*BFS(V))
# *는 컨테이너 타입의 데이터를 unpacking 하는 경우에 사용
#for문을 쓰지 않아도 된다.
#[1, 2, 4, 3] -> 1 2 4 3