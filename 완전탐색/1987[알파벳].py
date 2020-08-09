import sys

input = sys.stdin.readline

R,C = map(int, input().split())
Map = [list(input().rstrip()) for _ in range(R)]
Stack = set()



def DFS(i, j):
    step = 1
    Stack.add((i,j,str(Map[i][j])))
    while Stack:
        y, x, value = Stack.pop()
        for dy, dx in (1,0), (-1,0),(0,1),(0,-1):
            ny = y + dy
            nx = x + dx
            if 0<=ny< R and 0 <= nx < C:
                if not Map[ny][nx] in value:
                    Stack.add((ny,nx,value + Map[ny][nx]))
                    if len(value) >= step:
                        step = len(value) + 1
    return step

print(DFS(0,0))

#Set은 pop하면 뒤가아닌 앞에서 나온다.
#{1, 2}
#Stack.pop() -> 1
#{2}



{(0, 0, 'C')}
{(0, 1, 'CA'), (1, 0, 'CA')}
{(1, 1, 'CAD'), (1, 0, 'CA')}
{(1, 0, 'CA')}
{(1, 1, 'CAD')}
