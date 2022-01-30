def binary_search(array, target, start, end):
    if start>end:
        return None
    mid=(start+end)//2
    if target==array[mid]:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)


n=int(input())
data=list(map(int, input().split()))
data.sort()

m=int(input())
input_data=list(map(int, input().split()))
input_data.sort()

for i in range(m):
    result=binary_search(data,input_data[i],0,n-1)

    if result==None:
        print("No",end=" ")
    else:
        print("yes", end=" ")