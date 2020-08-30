import sys
input = sys.stdin.readline


def next(A, P):
  a = str(A)
  answer = 0
  for i in a:
    answer += pow(int(i), P)
  return answer

def dfs(A,P,visited,check):
  if visited[A] != 0:
    return visited[A] - 1
  visited[A] = count
  b = next(A, P)
  count += 1
  return dfs(b,P,visited,check)





A, P =map(int, input().split())

visited = [0]*250000

count =1

print(dfs(A,P,count,check))


#check[57] 1할당 -> check[74] 2할당 -> check[65] 3할당 -> check[61] 4할당 -> check[37] 5할당
#다시 반복
#check[58] 6할당 -> check[89] 7할당 -> check[145] 8할당 -> check[42] 9할당 -> check[20] 10할당 
#check[4] 11할당 -> check[16] 12할당 -> check[37] 이미 5할당되어있음

#57, 74, 65, 61