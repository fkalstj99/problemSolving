import sys
from collections import Counter

input = sys.stdin.readline


def binarySearch(key):
      low, high = 0 , len(card) -1

      while low <= high:
            mid = (low+ high) //2
            if key == card[mid]:
               return 1
            elif key > card[mid]:
                low = mid + 1
            else:
                high = mid - 1
  
      return -1




N = int(input())
card = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))
card.sort()

count = Counter(card)
result = []

for i in check:
    if binarySearch(i):
        result.append(count[i])

print(*result)
