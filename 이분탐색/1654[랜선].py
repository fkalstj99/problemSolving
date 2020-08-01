K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
start, end = 1, max(lan)


while start <= end:
  mid = (start + end) // 2

  lines = 0

  for i in lan:
    lines += i // mid

  if lines >= N: #랜선의 개수가 분기점 
    start = mid + 1
  else:
    end = mid - 1

print(end)

#high와 low로 가장 긴 길이와 가장 작은 길이를 구한 후
#, 이분 탐색을 통해서 점점 필요한 길이를 찾기