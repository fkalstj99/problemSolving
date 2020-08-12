N = int(input())

dp = [0]*(N+1)

dp[0]= 0
dp[1] = 0

for i in range(2, N+1):
  if i%2 == 0:
    dp[i] = min(dp[i-1],dp[i//2]) +1
  elif i%3 == 0:
    dp[i] = min(dp[i-1], dp[i//3]) + 1
  else:
    dp[i] = dp[i-1] + 1

print(dp[N])