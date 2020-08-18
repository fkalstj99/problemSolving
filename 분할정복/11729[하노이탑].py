import sys

input = sys.stdin.readline



def hanoi(N, A, B, C):
    if N > 0:
        hanoi(N-1, A, C, B )
        print(A, C)
        hanoi(N-1, B , A, C)



N = int(input())




print(2**N -1 )
hanoi(N, 1, 2, 3)