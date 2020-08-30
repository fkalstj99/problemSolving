import sys

a = int(sys.stdin.readline())

arr= []
for i in range(a):
  arr.append(list(sys.stdin.readline().split()))
 

arr.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(a):
  print(arr[i][0])