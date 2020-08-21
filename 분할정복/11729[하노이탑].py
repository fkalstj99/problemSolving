import sys

input = sys.stdin.readline



def hanoi(N, A, B, C):
    if N > 0:
        hanoi(N-1, A, C, B )
        Move 2 Discs from A to B using C

        3                   
        2                                  3 
        1                          1       2  
        A       B       C    ->    A       B       C   
        print(A, C)
        Move 1 Disc from A to C

                            
                3                          3 
        1       2                          2       1
        A       B       C    ->    A       B       C   

        hanoi(N-1, B , A, C)
        Move 2 Discs from B to C 
                                                   3     
                3                                  2 
                2       1                          1
        A       B       C    ->    A       B       C   



N = int(input())



print(2**N -1 )
hanoi(N, 1, 2, 3)


Tracing for 3 Discs

    1-3        1-2         3-2         1-3        2-1         2-3         1-3


--------------------------------------------------------------------------------
1-3



2
1               3
A       B       C





1-2




1       2       3
A       B       C




3-2

        3
1       2       
A       B       C





1-3

        3
        2       1
A       B       C



2-1

        
3       2       1
A       B       C



2-3

                2
3               1
A       B       C



1-3
                3
                2
                1
A       B       C