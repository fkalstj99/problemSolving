str = input()

table = [-1 for i in range(26)]


for i in range(len(str)):
  if table[ord(str[i]) - 97] >= 0:
    continue

  table[ord(str[i]) - 97] = i





for i in table:
  print(i, end=" ")
