import sys


input = sys.stdin.readline


def solution(result):
    if "0" not in result:
       return -1
  

    sum = 0
    for i in result:
        sum += int(i)
    

    
    if sum % 3 == 0:
       return "".join(result)
    else:
       return -1



arr = list(input().rstrip())
arr.sort(reverse=True)

print(solution(arr))






30의 배수를 찾기위해선

숫자의 끝이 0이 되어야 한다.

0을제외한 모든 숫자의 합이 3의 배수여야 한다.

2931 -> 0이 없음(30의 배수 아님)

80875542 -> 88755420

0을 제외 숫자합이 3의 배수임