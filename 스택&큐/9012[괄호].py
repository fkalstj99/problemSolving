n = int(input())


for i in range(n):
  a = input()
  VPS = list(a)
  count = 0

  for j in VPS:
    if j == "(":
      count += 1
    if j == ")":
      count -= 1

    if count < 0:
      print('NO')
      break
  
  if count > 0:
    print('NO')
  elif count == 0: 
    print('YES')       