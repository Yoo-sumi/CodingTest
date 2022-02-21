n,m=4,6
array=[19,15,10,17]
array.sort()
def get_value(v):
    total=0
    for i in array:
        if i>=v:
            total+=(i-v)
    return total
def binary_search(target,start,end):
    while start<=end:
        mid=(start+end)//2
        value=get_value(mid)
        if value==target:
            return mid
        elif value<target:
            end=mid-1
        else:
            start=mid+1
print(binary_search(m,0,max(array)))

