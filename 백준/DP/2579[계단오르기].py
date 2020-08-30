a = int(input())

stair = []

for i in range(a):
  stair.append(int(input()))

dp = [stair[0]]

dp.append(max(dp[0]+stair[1], stair[1]))
#2번째 계단 -> 모든 경우의 수

dp.append(max(dp[0]+ stair[2], stair[1] + stair[2]))
#3번째 계단 -> 모든 경우의 수


for i in range(3, a):
  dp.append(max(dp[i-3] + stair[i] + stair[i-1], dp[i-2] + stair[i]))

print(dp[a-1])

# 마지막 계단은 무조건 밟아야 하므로 마지막 계단을 기준으로 점화식
# dp[n] = dp[n-3] + arr[n] + arr[n-1]
# dp[n] = dp[n-2] + arr[n] 
