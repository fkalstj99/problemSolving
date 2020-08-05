#답(result)에 가기 위해서는 두가지의 방법이 있다.

#숫자 버튼을 통해 목표 채널에 도달한다.
#숫자 버튼을 통해 가까운 채널로 이동한 후, + 또는 - 버튼을 통해 목표 채널에 도달한다.
#+ 또는 - 버튼을 통해 목표 채널에 도달한다.




import sys


input = sys.stdin.readline

N = int(input())
M = int(input())

enable_btn = {str(i) for i in range(10)}

if M == 0:
    pass
else:
    break_set = set(input().split())
    enable_btn == break_set


result = abs(N-100)
#100에서부터 +,- 로만 이동한 수 
 
#채널의 수(0~500000)
for i in range(1000000):
    is_true = True
    for part_num in str(i):
        if part_num not in enable_btn:
           is_true= False
           break
    if is_true is True:
        result = min(result, abs(N-i)+len(str(i)))



case 1

abs(N - 100)의 값을 구한다.
(채널 100번에서 +,- 버튼만 채널을 이동하는 것이다)

 

case 2

0번부터 1,000,000까지 브루트 포스를 진행한다. 
(이동하려고 하는 채널의 최댓값이 500,000 이기 때문에 500,000 보다 크면서 모든 숫자의 경우의 수를 거치는 1,000,000까지를 범위로 잡았다.)