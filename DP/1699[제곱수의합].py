a = int(input())
dp =[0]*(a+1)

for i in range(1, a+1):
  dp[i] = i
  for j in range(1,i):
    if (j*j) > i:
      break
    
    dp[i] = min(dp[i], dp[i - j*j] + 1)

print(dp[a])

# 자연수   :    1  2  3  4  5  6  7  8  9

# 제곱수의 합:  1  2  3  1  2  3  4  2  1

#dp[i - j*j]를 기준으로 + 1하면 값이나옴
#1*1 , 2*2, 3*3, 4*4 ........ n*n 차례대로 가야하기때문에 for문