import sys

while True:
  str = sys.stdin.readline().rstrip('\n')
  Upper, Lower, Number, Space = 0, 0, 0, 0

  if not str:
    break

  for i in str:
    if i.isupper():
      Upper += 1
    if i.islower():
      Lower += 1
    if i.isdigit():
      Number += 1
    if i.isspace():
      Space += 1

  
  print("{} {} {} {}".format(Lower, Upper, Number, Space))
