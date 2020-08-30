import sys

input = sys.stdin.readline


def DFS(inputList, combList, index):
    global answer
    if index >= len(combList):
        if sum(combList) == S:
            answer += 1  
        return
    
    DFS(inputList, combList+inputList[index], index+1)
    DFS(inputList, combList, index+1)


N,S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

DFS(arr, [], 0)
print(answer)