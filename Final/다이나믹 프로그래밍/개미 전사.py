n=int(input())
arr=list(map(int,input().split()))
d=[0]*n

for i in range(n):
    if i==0:
        d[i]=arr[i]
        continue
    if i-2<0:
        d[i]=max(arr[i],d[i-1])
        continue
    d[i]=max(arr[i]+d[i-2],d[i-1])
print(d[n-1])