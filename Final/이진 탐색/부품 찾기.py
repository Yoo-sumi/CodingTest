import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
m=int(input())
li=list(map(int,input().split()))

arr.sort()
answer=[]

for i in range(m):
    flag=True
    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==li[i]:
            answer.append("yes")
            flag=False
            break
        if arr[mid]<li[i]:
            left=mid+1
        elif arr[mid]>li[i]:
            right=mid-1
    if flag:
        answer.append("no")
print(answer)