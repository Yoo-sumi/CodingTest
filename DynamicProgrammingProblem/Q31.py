'''n,m=3,4
array=[
    [],
    [1,3,3,2],
    [2,1,4,1],
    [0,6,4,7],
    []
]'''
n,m=3,3
array=[
    [],
    [1,3,3],
    [2,1,4],
    [0,6,4],
    []
]
'''n,m=4,4
array=[
    [],
    [1,3,1,5],
    [2,2,4,1],
    [5,0,2,3],
    [0,6,1,2],
    []
]'''

d=[[-1]*m for _ in range(n+2)]
def pr():
    for i in range(n+2):
        for j in range(m):
            print(d[i][j],end=" ")
        print()
    print()

for i in range(1,n+1):
    d[i][0]=array[i][0]

for i in range(1,m):
    for j in range(1,n+1):
        d[j][i]=max(d[j-1][i-1],d[j][i-1],d[j+1][i-1])+array[j][i]
pr()
result=-1
for i in range(1,n+1):
    result=max(result,d[i][m-1])
print(result)