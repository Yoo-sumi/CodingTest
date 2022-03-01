n=7
array=[15,11,4,8,5,2,4]
#array=[10,20,10,30,20,50]
d=[0]*n
d[0]=1
for i in range(1,n):
    if array[i]<array[i-1]:
        d[i]=d[i-1]+1
    else:
        d[i]=d[i-1]
print(d)
print(n-d[n-1])