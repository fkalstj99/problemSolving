def quadTree(y,x,n):
    value = Map[y][x]
    tree_break = False
    global result

    for i in range(y, y+n):
        if tree_break:
            break
        for j in range(x, x+n):
            if value != Map[i][j]:
                result += "("
                quadTree(y,x,n//2)
                quadTree(y,x+n//2,n//2)
                quadTree(y+n//2,x,n//2)
                quadTree(y+n//2,x+n//2,n//2)
                result += ")"

                tree_break = True
                break

    if not tree_break:
        result += str(value)

    






N = int(input())

Map = [list(input()) for _ in range(N)]
result = ""

quadTree(0,0,N)
print(result)







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
