from itertools import permutations

N = int(input())

arr = permutations(list(map(int,input().split())))



for i in arr:
    sum = 0
    for j in range(N - 1):
        sum += arr[j] - arr[j+1]
    
    answer = max(answer, sum)

print(answer)













def perm(arr, depth, n, k): 
    if depth == k: 
        print(arr[:k]) 
        return 
    for i in range(depth, n): 
        arr[i], arr[depth] = arr[depth], arr[i] 
        perm(arr, depth + 1, n, k) 
        arr[i], arr[depth] = arr[depth], arr[i]





#https://comdoc.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%88%9C%EC%97%B4%EA%B3%BC-%EC%A1%B0%ED%95%A9



def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result
