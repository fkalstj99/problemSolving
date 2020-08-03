def nine_tree(x, y, n):
    global matrix, minus, zero, plus
    type = matrix[y][x] #첫 타입과 나머지 타입이 같아야함
    double_break = False #for문 탈출용 double_break
    
    for i in range(x, x+n):
        if double_break:
            break
            
        for j in range(y, y+n):
            if matrix[j][i] != type: #하나라도 틀릴시에 재귀문 생성
                k = n//3
                
                #9분면으로 잘라 실행
                nine_tree(x, y, k)
                nine_tree(x + k, y, k)
                nine_tree(x + 2*k, y, k)
                nine_tree(x, y + k, k)
                nine_tree(x + k,  y+ k, k)
                nine_tree(x + 2*k, y + k, k)
                nine_tree(x, y + 2*k, k)
                nine_tree(x + k, y + 2*k, k)
                nine_tree(x + 2*k, y + 2*k, k)
                
                double_break = True #탈출!
                break
    
    if not double_break:
        if matrix[y][x] == -1:
            minus += 1
        elif matrix[y][x] == 0:
            zero += 1
        else:
            plus += 1


N = int(input())
matrix = []
minus = 0
zero = 0
plus = 0

for _ in range(N):
    matrix.append(list(map(int, input().split())))


nine_tree(0,0,N)
print(minus)
print(zero)
print(plus)



#-----------------------------------------------------------------






import sys 

N = int(sys.stdin.readline())

matrix = [] 
result = [0] * 3 

for _ in range(N): 
    matrix.append(list(map(int, sys.stdin.readline().split()))) 


def check(start_x: int, start_y: int, n: int): 
    temp = matrix[start_x][start_y] 
    for i in range(n): 
        for j in range(n): 
            if temp != matrix[start_x + i][start_y + j]: 
                return False 
                
    return True 


def divide(start_x: int, start_y: int, n: int): 
        if check(start_x, start_y, n): 
            result[matrix[start_x][start_y] + 1] += 1 
        else: 
            for i in range(3): 
                for j in range(3): 
                    divide(start_x + i* n//3, start_y + j* n//3, n//3) 
                    #이 부분을 계산을 잘해야함. 칸 옮기고 줄여나가는
                    
        return 
        
        


divide(0, 0, N) 

for i in range(3): 
    print(result[i])

#https://atez.kagamine.me/12

9


풀이
---------------------------------------------------------------------


1. 모든 종이를 확인해서 같은 수인지 판단 -> size(9^9)


0  0  0  1  1  1 -1 -1 -1
0  0  0  1  1  1 -1 -1 -1
0  0  0  1  1  1 -1 -1 -1

1  1  1  0  0  0  0  0  0
1  1  1  0  0  0  0  0  0
1  1  1  0  0  0  0  0  0

0  1 -1  0  1 -1  0  1 -1
0  -1 1  0  1 -1  0  1 -1
0  1 -1  1  0 -1  0  1 -1



-----------------------------------------------------------------------

2. 당연히 아니니까 -> size(3^3)로 나눔
    a. -1 -> 1개
    b. 1  -> 2개
    c. 0  -> 3개 


0  0  0 | 1  1  1 | -1 -1 -1
0  0  0 | 1  1  1 | -1 -1 -1
0  0  0 | 1  1  1 | -1 -1 -1


1  1  1 | 0  0  0 | 0  0  0
1  1  1 | 0  0  0 | 0  0  0
1  1  1 | 0  0  0 | 0  0  0



-----------------------------------------------------------------------

3. 나머지 종이 확인 -> size(1^1)로 나눔 -> 하나씩 확인 
    a. -1 -> 9개
    b. 1  -> 9개
    c. 0  -> 9개 


0  1 -1  0  1 -1  0  1 -1
0  -1 1  0  1 -1  0  1 -1
0  1 -1  1  0 -1  0  1 -1

------------------------------------------------------------------------

4. 결론

-1 -> 10개
1  -> 11개
0  -> 12개






