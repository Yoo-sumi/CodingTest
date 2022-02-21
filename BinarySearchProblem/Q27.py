n,x=8,4
data=[1,1,2,2,2,2,2,3]
def first(target,start,end):
    while start<=end:
        mid=(start+end)//2
        if data[mid]==target and data[mid-1]!=target:
            return mid
        elif data[mid]<target:
            start=mid+1
        else:
            end=mid-1
def second(target,start,end):
    while start<=end:
        mid=(start+end)//2
        if data[mid]==target:
            start=mid+1
        elif data[mid]>target:
            end=mid-1
        else:
            return mid
    return start
first_index=first(x,0,n-1)
if first_index==None:
    print(-1)
else:
    print(second(x,first_index,n-1)-first_index)
from bisect import bisect_left,bisect_right
print(bisect_left(data,2))