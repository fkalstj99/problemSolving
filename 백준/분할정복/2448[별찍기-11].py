import sys

sys.setrecursiontime(10**9)

n = int(input())

Map = [" "*(2*n) for _ in range(n)]

def star(y,x,N:int):
    if N == 3:#더이상 나눌수없을떄 2를 기준으로 나누니까
        Map[y][x] = "*"
        Map[y+1][x-1] = "*"
        Map[y+1][x+1] = "*"
        Map[y+2][x-2] = "*"
        Map[y+2][x-1] = "*"
        Map[y+2][x] = "*"
        Map[y+2][x+1] = "*"
        Map[y+2][x+2] = "*"
        return #더이상 나누면 안된다 

    div = N//2
    star(y,x,div)
    star(y+div,x-div,div)
    star(y+div,x+div,div)


star(0, N-1,N)
    print("".join(myMap[i]))



#즉 가장 큰 삼각형에서 3개의 시작포인트에서 재귀를 해주면된다.

#마지막으로 n=3(k=1)이되었을때는 작은 삼각형을 출력해주면된다. 

#가장작은 삼각형은 삼각형 모양을 만들기위해 만든것같은데 보다시피 규칙을 적용할수가 없다.

