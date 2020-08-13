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

#3개의 이어질 수 없는 값에서 최대값구하기 