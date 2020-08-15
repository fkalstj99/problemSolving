N = int(input())

arr= list(map(int, input().split()))

dp = [1]*(N)
dp2 = [1]*(N)



for i in range(N):
  for j in range(i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] +1)



for i in range(N-1,-1,-1):
  for j in range(N-1,i,-1):
    if arr[i] > arr[j]:
      dp2[i] = max(dp2[i], dp2[j] +1)



Max = 0
for i in range(N):
  Max = max(Max, dp[i]+dp2[i]) 

print(Max - 1)
