N = int(input())
arr = list(map(int,input().split()))
dp = [x for x in arr]


for i in range(N):
  for j in range(i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], arr[j] + dp[i])

print(max(dp))