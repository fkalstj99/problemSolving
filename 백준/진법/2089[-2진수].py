n = int(input())


result = ''

if n==0:
    print(0)
    exit()

while n:
  if n%(-2):
    result = '1' + result
    n = n//-2 +1
  else:
    result = '0' + result
    n //= -2

print(result)


# -13 = -2*(7) + 1

#  7  = -2*(-3) + 1

# -3  = -2*(2) + 1

#  2  = -2*(-1) + 0

# -1  = -2*(1) + 1

#  1  = -2*(0) + 1


# -2로 나눠 떨어지지 않는 경우 N//-2를 한 후에 +1 =>
#  13//-2 == 6이기 떄문에 +1 해서 7