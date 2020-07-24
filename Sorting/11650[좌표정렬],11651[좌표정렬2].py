import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
so.sort(key = lambda x: (x[0], x[1]))
# 아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬하고,
# 다음 두 번째 인자를 기준으로 내림차순으로 정렬하게 하려면, 
#e = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]
# f = [(0, 3), (0, 1), (1, 5), (1, 4), (1, 3), (2, 4)]



#key값은 정렬하는 기준
for i in so:
    print(i[0], i[1])

#첫번째 세로줄부터 정렬하는것




import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
so.sort(key = lambda x: (x[1], x[0]))
#e = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]
#f = [(0, 1), (0, 3), (1, 3), (1, 4), (2, 4), (1, 5)]






#key값은 정렬하는 기준
for i in so:
    print(i[0], i[1])

#두번째 세로줄부터 정렬하는것
#so.sort(key = lambda x: (x[1], x[0])) 0 1이 바뀌었다