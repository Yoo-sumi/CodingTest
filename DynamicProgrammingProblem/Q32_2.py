n=5
array=[
    [7],
    [3,8],
    [8,1,0],
    [2,7,4,4],
    [4,5,2,6,5]
]
d=[[0]*i for i in range(1,n+1)]

for i in range(n):
    for j in range(i+1):
        d[i][j]=array[i][j]
d[0][0]=array[0][0]

for i in range(1,n):
    for j in range(len(array[i])):
        if j<len(array[i-1]): #오른쪽
            d[i][j]=max(d[i][j],d[i-1][j]+array[i][j])
        if j-1>-1: #왼쪽
            d[i][j]=max(d[i][j],d[i-1][j-1]+array[i][j])
print(d)
print(max(d[n-1]))