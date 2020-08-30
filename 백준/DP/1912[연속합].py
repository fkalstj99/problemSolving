N = int(input())



arr = list(map(int, input().split()))
dp = [arr[0]]


for i in range(0,N - 1):
    dp.append(max(dp[i] + arr[i+1], arr[i+1]))

print(max(dp))

# 일단 더해보고 그다음수랑 판단한다 -> 어쩌피 다 dp에 기록 되니깐