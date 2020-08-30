n = int(input())

wine_list = [0]

for i in range(n):
    wine_list.append(int(input()))
    
dp=[0]

dp.append(wine_list[1])

if n>1:
    dp.append(wine_list[1] + wine_list[2])
    
    
for j in range(3, n+1):
    dp.append(max(dp[j-3] + wine_list[j] + wine_list[j-1], dp[j-2] + wine_list[j], dp[j-1]))
    
    
print(dp[n])

#1. 안마시는 경우  -> 그 전 N - 1 최대값
#    D[N] = D[N-1] 


#2. 1번째 연속 마신다 -> 그전 N - 1은 마시지 않았단 소리 -> N-2는 마셨든 안마셨든 알 수 없는 상태
#   D[N] = D[N-2] + A[N]


#3. 2번쨰 연속 마신다 -> N - 1마시고 , N-2는 반드시 마시지 않았다 -> N-3은 마셨는지 안마셨는지 알수 없다
#   D[N] = D[N-3] + A[N-1] + A[N]