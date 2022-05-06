import sys
input=sys.stdin.readline
n,k=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.sort()
B.sort(reverse=True)
count=0
for i in range(n):
    if count==k:
        break
    if A[i]>=B[i]:
        break
    A[i],B[i]=B[i],A[i]
    count+=1

print(sum(A))
