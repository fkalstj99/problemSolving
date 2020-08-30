import sys
input = sys.stdin.readline




A, B = map(int, input().split())

arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))
arr = arr_A + arr_B


print(*sorted(arr))

