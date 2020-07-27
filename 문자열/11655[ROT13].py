import sys


str = sys.stdin.readline()

answer = ""

for i in str:
  if i.isalpha():
    if ord(i) >= 78 and ord(i) <= 90:
      answer += chr(ord(i) - 13)
    elif ord(i) >= 110 and ord(i) <= 122:
      answer += chr(ord(i) - 13)
    else:
      answer += chr(ord(i) + 13)
  else:
    answer += i


print(answer)