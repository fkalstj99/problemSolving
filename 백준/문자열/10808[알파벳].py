str = input()

table = [0 for i in range(26)]


for i in str:
  table[ord(i) - ord('a')] += 1

for i in table:
  print(i, end=" ")

