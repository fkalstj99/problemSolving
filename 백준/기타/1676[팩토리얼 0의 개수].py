result = [i for i in range(1,int(input())+1)]


sum = 1
for i in result:
  sum = sum*i

Factorial = str(sum)

result = 0
for j in range(len(Factorial)-1, -1 , -1):
  if Factorial[j] == "0":
    result += 1
  else:
    break
print(result)