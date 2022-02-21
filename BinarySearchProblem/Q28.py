'''n=5
data=[-15,-6,1,3,7]'''
n=7
data=[-15,-4,3,8,9,13,15]
data.sort()

def binary_search(start,end):
    while start<=end:
        mid=(start+end)//2
        if mid==data[mid]:
            return mid
        elif mid>data[mid]:
            start=mid+1
        else:
            end=mid-1
    return -1
print(binary_search(0,n-1))
