n = int(input())
picture = [[' ']*((n-1)*2+1) for i in range(n)]
def draw(k,x,y):
    if k==3:
        picture[y][x] = '*'
        picture[y+1][x+1] = '*'
        picture[y+1][x-1] = '*'
        picture[y+2][x+1] = '*'
        picture[y+2][x-1] = '*'
        picture[y+2][x] = '*'
        picture[y+2][x-2] = '*'
        picture[y+2][x+2] = '*'
        return
    draw(k//2,x,y)
    draw(k//2,x-k//2,y+k//2)
    draw(k//2,x+k//2,y+k//2)

draw(n,n-1,0)


for i in picture:
    print(''.join(i))




#즉 가장 큰 삼각형에서 3개의 시작포인트에서 재귀를 해주면된다.

#마지막으로 n=3(k=1)이되었을때는 작은 삼각형을 출력해주면된다. 

#가장작은 삼각형은 삼각형 모양을 만들기위해 만든것같은데 보다시피 규칙을 적용할수가 없다.

