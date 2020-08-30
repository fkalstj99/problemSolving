v = [int(input()) for i in range(int(input()))] 
 
# merge sort
def merge(left, right) :
    v=[]
    i=0;j=0
    while(i<len(left) and j<len(right)) :
        if left[i]<=right[j] :
            v.append(left[i])
            i+=1
        else :
            v.append(right[j])
            j+=1
    if i==len(left) : 
        v = v + right[j:len(right)]
    if j == len(right): 
        v = v + left[i:len(left)]
    return v
 
def merge_sort(v) :
    if len(v) <= 1 : return v
    m = len(v)//2
    left = merge_sort(v[0:m])
    right = merge_sort(v[m:len(v)])
    return merge(left, right)
 
m = merge_sort(v)
print(*m, sep="\n")




#merge sort 사용
#나눠서 정렬한다음에 합친다.

#https://wkdgusdn3.tistory.com/entry/MergeSort%EB%B3%91%ED%95%A9%EC%A0%95%EB%A0%AC