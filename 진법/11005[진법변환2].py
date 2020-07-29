hash = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n,m = map(int,input().split())

answer = ''

while n != 0:
  answer += str(hash[n%m])
  n = n//m


print(answer[::-1])






