import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def merge_sort(low, high):
    global result,arr

    mid = (low + high) // 2
    
    if high - low < 2:
        return

    merge_sort(low, mid)
    merge_sort(mid, high)

    temp = []
    l, h = low, mid
    count = 0
    while l < mid and h < high:
        if arr[l] < arr[h]:
            temp.append(arr[l])
            l += 1
            result += count
        else:
            temp.append(arr[h])
            h += 1
            count+=1

    while l < mid:
        temp.append(arr[l])
        l += 1
        result += count
    while h < mid:
        temp.append(arr[h])
        h += 1

    for i in range(len(temp)):
        arr[low + i] = temp[i]
      


N = int(input())
result = 0
arr = list(map(int, input().split()))

merge_sort(0,N)
print(result)
#1. 왼쪽 리스트의 값을 새로운 리스트에 채울 경우 result += cnt
    #오른쪽 리스트에서 새로운 리스트로 먼저 채워진만큼 swap

#2. 오른쪽 리스트의 값을 새로운 리스트에 채울 경우 cnt += 1
    #왼쪽 리스트아직 추가되지 않은 인덱스 수만큼 증가

#왼쪽 리시트, 오른쪽 리스트는 정렬된 상태 
#왼쪽리시트의 값이 
