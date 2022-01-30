n, m =map(int, input().split())
array=list(map(int,input().split()))
array.sort()
start=0
end=max(array)
result=0
while start<=end:
    mid=(start+end)//2
    sum=0
    for i in range(n):
        if array[i]>mid:
            sum+=array[i]-mid
    if sum<m:
        end=mid-1
    else:
        result=mid
        start=mid+1
print(result)

