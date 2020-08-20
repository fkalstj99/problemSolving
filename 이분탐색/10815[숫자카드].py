N = int(input())
card = list(map(int,input().split()))
M = int(input())
check = list(map(int, input().split()))
card.sort()

for num in check:
  start , end = 0, len(card) - 1
  while True:
    mid = (start + end)//2
    if start > end:
      print("0", end=" ")
      break
    if num == card[mid]:
      print("1", end = " ")
      break
    elif num > card[mid]:
      start = mid + 1
    else:
      end = mid - 1


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