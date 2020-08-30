import sys

input = sys.stdin.readline

N,M,K = map(int, input().split())

team = 0


while N >=0 and M>=0 and N+M>=K:
  N -= 2
  M -= 1
  team +=1

print(team)