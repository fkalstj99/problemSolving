N , M = map(int, input().split())

break_button = list(map(int, input().split()))

enable_button = [i for i in range(10)]

if M == 0:
    pass
else:
    enable_button -= break_button


result = abs(100 - N)
for i in range(1000000):
# 가야할 채널 번호가 500000 -> 주어진 번호가 7 -> 777777한 다음 5000000에서 뺀다 -> range를  500000 * 2 해야하는 이유 
    is_true = True
# is_true -> 조건 맞추는 역할 -> is_true가 False라면 조건에 맞지 않는 범위다 
# is_true -> True라면 조건에 맞는 범위  
    for part_num in enable_button:
        if part_num not in str(i):
            is_true = False
            break

#맞는 조건의 범위 내에서 최소값을 구한다. 
    if is_true == True:
        result = min(result , len(str(i)) + abs(N - i))

#len(str(i)) -> enable_button중 우리가 누른 번호의 수 -> 5455(4번) , 103(1번)
#abs(N-i) -> +, - 몇번 눌렀는지 확인 -> 5455 -> 5457 (2번)


