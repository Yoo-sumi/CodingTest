'''n,m=3,4
array=[
    [1,3,3,2],
    [2,1,4,1],
    [0,6,4,7]
]'''
n,m=4,4
array=[
    [1,3,1,5],
    [2,2,4,1],
    [5,0,2,3],
    [0,6,1,2]
]

d=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        d[i][j]=array[i][j]
for i in range(1,m):
    for j in range(0,n):
        if j-1>-1:
            d[j][i]=max(d[j-1][i-1]+array[j][i],d[j][i])
        d[j][i]=max(d[j][i-1]+array[j][i],d[j][i])
        if j+1<n:
            d[j][i]=max(d[j+1][i-1]+array[j][i],d[j][i])
mmax=0
for i in range(n):
    mmax=max(d[i][m-1],mmax)
print(mmax)
print(d)