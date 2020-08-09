N,M = map(int,input().split())
arr = list(map(int, input().split()))

def solve():
    start = end = answer = sum = 0
    while True:
        if sum >= M:
            sum -= arr[start]
            start += 1
        else:
            if end == N:
                break
            sum += arr[end]
            end+=1
        
        if sum == M:
            answer += 1
    return answer 

print(solve())

