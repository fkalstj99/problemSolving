def DFS(start, visit):
  visit[start] = True
  for i in adj_list[start]:
    if visit[i] == False:
      DFS(i,visit)


testCase = int(input())
for _ in range(testCase):
  N = int(input())
  adj_list= [[] for _ in range(N+1)]
  arr = [0] + list(map(int, input().split()))
  for i in range(1,N+1):
    adj_list[i].append(arr[i])
    adj_list[arr[i]].append(i)
  
  visit = [False]*(N+1)
  count = 0
  for i in range(1,N+1):
    if visit[i] == False:
      DFS(i,visit)
      count+=1

  print(count)