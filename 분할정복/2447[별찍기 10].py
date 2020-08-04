from sys import*
setrecursionlimit(10**6)

def draw(x, y, n):
   if n == 1:
       matrix[y][x]='*'
       return
   div = int(n/3)            
   draw(x, y, div)
   draw(x, y+div, div)
   draw(x, y+div+div, div)
   draw(x+div, y, div)
   draw(x+div, y+div+div, div)
   draw(x+div+div, y, div)
   draw(x+div+div, y+div, div)
   draw(x+div+div, y+div+div, div)



N = int(input())
matrix = [[' 'for _ in range(N)] for _ in range(N)]

draw(0,0,N)

for i in range(N):
  print(''.join(matrix[i]))