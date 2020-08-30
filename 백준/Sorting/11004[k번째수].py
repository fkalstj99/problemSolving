import sys

m,n = map(int,sys.stdin.readline().split())
l = list(map(int,sys.stdin.readline().split()))

l.sort()


print(l[n-1])