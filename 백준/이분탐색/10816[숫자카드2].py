from collections import Counter

def binary_search(num):
  start , end = 0 , len(card) - 1
  while start <= end:
    mid = (start + end)//2

    if card[mid] == num:
      return 1
    if num > card[mid]:
      start = mid + 1
    else:
      end = mid - 1
  
  return - 1



N = int(input())
card = list(map(int,input().split()))
M = int(input())
check = list(map(int, input().split()))
card.sort()
count = Counter(card)
result = []

for i in check:
  if binary_search(i):
    result.append(count[i])

print(*result)