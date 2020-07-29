dict = {
"11":'1',
"12":'10',
"13":'11',
"0" :'000',
"1" :'001',
"2" :'010',
"3" :'011',
"4" :'100',
"5" :'101',
"6" :'110',
"7" :'111'
}






arr = input()


answer = ''

for i in range(len(arr)):
  if i == 0 and int(arr[i]) < 4:
    answer = answer + dict["1"+arr[i]]
  else:
    answer = answer + dict[arr[i]]
  
print(answer)