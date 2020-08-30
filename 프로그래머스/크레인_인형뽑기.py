def solution(board, moves):
    stack = []
    result = 0
    for i in moves:
        for arr in board:
            if arr[i-1]:
                stack.append(arr[i-1])
                arr[i-1] = 0
                break

        if len(stack) >= 2:
            if stack[-1] == stack[len(stack)-2]:
                stack.pop()
                stack.pop()
                result += 2

    return result