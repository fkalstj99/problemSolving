arr = input()

answer = ''
num = 1

while len(arr) % 3 != 0:
  arr = '0' + arr 



for i in range(len(arr)-1, -1, -1):
  if num % 3 ==0:
    answer = answer + str(int(arr[i:i+3]) % 8)
  
  num += 1






print(answer[::-1])