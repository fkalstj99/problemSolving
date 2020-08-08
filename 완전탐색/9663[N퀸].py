N = int(input())

a = [False]*N
|
diagnol1= [False]*(2*N-1)
\
diagnol2= [False]*(2*N-1)
/

answer = 0

#i는 row
def solve(i):
    global answer
    if i == n:
        answer+=1
        return
    
    for j in range(N):
        if not(a[j] or diagnol1[i+j] or diagnol2[i-j+N-1]):
            a[j] = diagnol1[i+j] = diagnol2[i-j+N-1] = True
            solve(i+1)
            a[j] = diagnol1[i+j] = diagnol2[i-j+N-1] = False

