K, N = map(int,input().split())
arr = []
for i in range(K):
  arr.append(int(input()))

start , end = 1 , max(arr)


while start <= end:
  mid = (start + end) //2
  result = 0

  for num in arr:
    result += num//mid
  
  if result >= N:
    start = mid + 1

  else :
    end = mid - 1
  

print(end)




#high와 low로 가장 긴 길이와 가장 작은 길이를 구한 후
#, 이분 탐색을 통해서 점점 필요한 길이를 찾기