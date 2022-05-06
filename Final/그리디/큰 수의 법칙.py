import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
answer=0
count=0
for _ in range(m):
    if count==k:
        answer+=arr[1]
        count=0
        continue
    answer+=arr[0]
    count+=1
print(answer)