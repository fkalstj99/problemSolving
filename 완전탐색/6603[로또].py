def DFS(inputList, combStr, index):
    if len(combStr) == 6:
        print(" ".join(combStr))
        return

    if index >= len(inputList): 
        return;

#무한히 재귀가 깊어질 수는 없고 inputList 길이 보다 깊어질 수 없습니다.

    DFS(inputList, combStr + [inputList[index]], index+1)
    DFS(inputList, combStr, index+1)


while True:
    lotto = list(map(str, input().split()))
    
    if lotto[0] == 0:
        break
    combStr = []
    DFS(lotto[1::], combStr, 0)