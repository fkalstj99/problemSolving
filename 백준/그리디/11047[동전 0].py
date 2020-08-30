import sys

input = sys.stdin.readline


def solution(money):
    global price
    answer = 0
    for i in range(N):
        if price // money[i] > 0:
            answer += (price // money[i])
            price -= money[i] * ((price // money[i]))
  
    return answer






N, price = map(int,input().split())


money = []


for _ in range(N):
    money.append(int(input()))


money.sort(reverse=True)

print(solution(money))
