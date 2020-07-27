
import sys

arr = list(sys.stdin.readline().strip())
result = 0
stack = []

for i in range(len(arr)):
  if arr[i] == ")" and arr[i-1] == "(":
    stack.pop()
    result += len(stack)
    continue

  if arr[i] == "(":
    stack.append("(")
  else:
    stack.pop()
    result += 1


print(result)



