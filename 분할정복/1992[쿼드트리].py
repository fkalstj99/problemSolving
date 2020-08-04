#쿼드 트리 함수 정의
def quad_tree(x, y, n):
    global matrix, answer #배열 정보와 답이 될 변수를 끌어옴
    color = matrix[y][x] #첫 색깔(흑백)과 나머지 색이 같아야함
    double_break = False #for문 탈출용 double_break
    
    for i in range(x, x+n):
        
        if double_break:
            break
            
        for j in range(y, y+n):
            if matrix[j][i] != color: #하나라도 틀릴시에 재귀문 생성
            
                answer += '(' #문 열고
                quad_tree(x, y, n//2) #1사분면
                quad_tree(x + n//2, y, n//2) #2사분면
                quad_tree(x, y + n//2, n//2) #3사분면
                quad_tree(x + n//2, y + n//2, n//2) #4사분면
                answer += ')' #문 닫고
                
                double_break = True #탈출!
                break
    
# 지정된 size안의 다른 색깔이 없다는 뜻 
    if not double_break:
        if matrix[y][x] == 1: #검정색이라면
            answer += '1'
        else:
            answer += '0' #흰색이라면


N = int(input())
matrix = []
answer = ''

for _ in range(N):
    matrix.append(list(map(int, str(input()))))

quad_tree(0,0,N)
print(answer)

#https://yabmoons.tistory.com/450
#https://soojong.tistory.com/entry/python%EB%B0%B1%EC%A4%80-%EC%BF%BC%EB%93%9C%ED%8A%B8%EB%A6%AC

#그리고 쿼드트리는 단순히 노드가 4개 있는 것이라고 생각하면 된다.

#즉, 4개로 쪼개서 4개의 노드가 생겨난다고 생각하면 된다.








(0(0011)(0(0111)01)1









                            0 0 8(color: 1) (8*8)
                          1.  result += '('
                            (
        0 0 4(color: 1, 4*4)
        2. result += '('
          ((

        12.result+= ' )'
        ((110(0101))
0 0 2(color: 1, 2*2) 2 0 2(color: 1, 2*2) 0 2 2(color: 0, 2*2)              2 2 2(color: 0 2*2)
3.result += '1'       4.result += '1'       5.result += '0'                 6.result += '('
                                                                            
((1                  ((11                 ((110                             ((110(

                                                                            11.result += ')'
                                                                            
                                                                            ((110(0101)
                                                                            
                                                                            2 2 1(color:0 1*1)   3 2 1(color:1 1*1)    2 3 1(color:0 1*1)     3 3 1(color:1 1*1)
                                                                            7.result += '0'      8.result += '1'       9.result += '0'        10.result += '1'
                                                                            ((110(0              ((110(01              ((110(010              ((110(0101
