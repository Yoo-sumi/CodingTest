n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
d=[1e9]*(m+1)
d[0]=0
for i in range(n):
    for j in range(arr[i],m+1):
        if d[j-arr[i]]!=1e9:
            d[j]=min(d[j],d[j-arr[i]]+1)
if d[m]==1e9:
    print(-1)
else:
    print(d[m])