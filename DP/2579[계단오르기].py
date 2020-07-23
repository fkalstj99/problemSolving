a = int(input())

stair = []

for i in range(a):
  stair.append(int(input()))

dp = [stair[0]]

dp.append(max(dp[0]+stair[1], stair[1]))

dp.append(max(dp[0]+ stair[2], stair[1] + stair[2]))

for i in range(3, a):
  dp.append(max(dp[i-3] + stair[i] + stair[i-1], dp[i-2] + stair[i]))

print(dp[a-1])
