N, M = map(int, input().split())
arr = list(map(int, input().split()))



def solve():
    start = end = Sum = 0
    ans = 1e9
    while True:
        if Sum >= M:
            Sum -= arr[start]
            start+=1
        else:
            if end == N:
                break
            Sum += arr[end]
            end += 1

        if Sum == M:
            ans = min(ans, end - start)
    
    print(ans if ans != 1e9 else 0)
solve()