n,m=8,5
data=[1,5,4,3,2,4,5,2]
array=[0]*(m+1)
for i in data:
    array[i]+=1
result=0
for i in range(1,m+1):
    n-=array[i]
    result+=array[i]*n
print(result)
'''count=0
for i in range(n):
    for j in range(i,n):
        if array[i]==array[j]:
            continue
        count+=1
print(count)'''