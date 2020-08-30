N = int(input())

dp = [[0]*10 for _ in range(N)]
divisor = 10007

for i in range(0,10):
    dp[0][i] = 1


for i in range(1, N):
    for j in range(10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] 

print(sum(dp[N-1]) % divisor)