import sys

n = int(sys.stdin.readline())

arr = [0 for i in range(10001)]

for i in range(n):
  arr[int(sys.stdin.readline())] += 1


for i in range(10001):
  if arr[i] > 0:
    for j in range(arr[i]):
      print(i)



CountingSort(계수 정렬)


입력 1 ~ 10000 

제한적이기에 CountingSort가 가장 적합했다.

입력받는 숫자의 최댓값까지의 배열을 만들어 놓고 -1