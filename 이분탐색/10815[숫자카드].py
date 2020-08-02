import sys

input = sys.stdin.readline

N = int(input())
num_card = list(map(int, input().split()))
num_card.sort()
M = int(input())
check_card = list(map(int, input().split()))



for num in check_card:
    low, high = 0,N-1
    while True:
        if low > high:
            print("0", end = " ")
            break
        mid = (low + high)//2
        if num == num_card[mid]:
            print("1", end=" ")
            break
        elif num > num_card[mid]:
            low = mid + 1
        else:
            high = mid - 1

#메모리106896	시간3868


#



def binarySearch(arr, key):
    lo, hi = 0, len(arr) -1
    while lo <= hi:
        mid = (lo + hi) >> 1
        if arr[mid] == key:
            return '1'
        elif arr[mid] > key:
            hi = mid - 1
        else:
            lo = mid + 1
    return '0'

N = int(input())
card = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))
card.sort()
result = []
for i in check:
    result.append(binarySearch(card, i))
print(' '.join(result))

#메모리108540	시간2360