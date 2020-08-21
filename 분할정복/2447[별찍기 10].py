from sys

sys.setrecursiontime(10**9)


def star(y,x,N):
    if N == 1:
        Map[y][x] = "*"
        return # 더 이샹 내려가면 안되니까
    div = N//3
    star(y,x,div)
    star(y+div,x,div)
    star(y+div+div,x,div)
    star(y,x+div,div)
    star(y,x+div+div,div)
    star(y+div,x+div+div,div)
    star(y+div+div,x+div,div)
    star(y+div+div,x+div+div,div)    
#가운데만 빼놓고 전부다






N = int(input())

Map = [" "*(N) for _ in range(N)]
for i in range(N):
    print("".join(Map[i])) 
