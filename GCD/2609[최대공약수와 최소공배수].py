a,b = map(int, input().split())

def gcd_r(a, b):
  if b == 0:
    return a
  else:
    return gcd_r(b, a%b)

def gcd(a,b):
  while b>0:
    temp = a%b
    a = b
    b = temp
  return a

def lcm(a,b):
  return a * b // gcd(a,b)

print(gcd_r(a, b))
print(lcm(a, b))