n=5
array=[
    [7],
    [3,8],
    [8,1,0],
    [2,7,4,4],
    [4,5,2,6,5]
]
d=[[0]*(i+3) for i in range(n)]
for i in range(n):
    for j in range(1,i+2):
        d[i][j]=array[i][j-1]

def show(a):
    for i in a:
        for j in range(len(i)):
            print(i[j], end=" ")
        print()
    print()
for i in range(1,n):
    for j in range(1,i+2):
        d[i][j]=max(d[i-1][j-1],d[i-1][j])+d[i][j]

show(d)
result=0
for i in d[n-1]:
    result=max(result,i)
print(result)