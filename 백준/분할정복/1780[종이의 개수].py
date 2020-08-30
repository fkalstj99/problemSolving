def nineTree(y,x,n):
    value = Map[y][x]
    tree_break = False

    for i in range(x,x+n):
        if tree_break:
            break
        # N * N 종이의 개수 -> N // 3 * N // 3으로 넘어갔다는 말
        for j in range(y+n):
            if not value == Map[i][j]:
                k = n//3
                nine_tree(y, x, k)
                nine_tree(y + k, x, k)
                nine_tree(y + 2*k, x, k)
                nine_tree(y, x + k, k)
                nine_tree(y + k,  x+ k, k)
                nine_tree(y + 2*k, x + k, k)
                nine_tree(y, x + 2*k, k)
                nine_tree(y + k, x + 2*k, k)
                nine_tree(y + 2*k, x + 2*k, k)


                tree_break = True
                #tree_break의 존재 -> N * N의 종이에서는 다른 것이 나왔다는 뜻
                break

    if not tree_break:
        result[str(value)] += 1




N = int(input())

Map = [list(map(str,input().split())) for _ in range(N)]

result = {
    "-1":0,
    "0": 0,
    "1":0
}



nineTree(0,0,N)



print(result, end="\n")



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def check(y,x,n):
    value = Map[y][x]
    for i in range(n):
        for j in range(n):
            if value != Map[i][j]:
                return False





def nineTree(y,x,n):
    
    if check(y,x,n):
        result[str(Map[y][x])] += 1
    else:
        for i in range(3):
            for j in range(3):
                nineTree(y + i*n//3, x + i*n//3, n//3)





N = int(input())

Map = [list(map(str,input().split())) for _ in range(N)]

result = {
    "-1":0,
    "0": 0,
    "1":0
}



nineTree(0,0,N)

print(result, end="\n")








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






