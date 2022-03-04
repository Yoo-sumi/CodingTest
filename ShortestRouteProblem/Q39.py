n=7
INF=int(1e9)
graph=[[INF]*(n*n) for _ in range(n*n)]
#array=[3,7,2,0,1,2,8,0,9,1,1,2,1,8,1,9,8,9,2,0,3,6,5,1,5]
array=[9,0,5,1,1,5,3,
       4,1,2,1,6,5,3,
       0,7,6,1,6,8,5,
       1,1,7,8,3,2,3,
       9,4,0,7,6,4,1,
       5,8,3,2,4,8,3,
       7,4,8,4,8,3,4]
for i in range(n*n):
    graph[i][i]=0
    node=i//n
    #up
    if i-n>=0:
        graph[i][i-n]=array[i-n]
    #down
    if i+n<n*n:
        graph[i][i+n]=array[i+n]
    #left
    if i-1>=(n*node):
        graph[i][i-1]=array[i-1]
    #right
    if i+1<n+(n*node):
        graph[i][i+1]=array[i+1]

for k in range(n*n):
    for i in range(n*n):
        for j in range(n*n):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

print(array[0]+graph[0][n*n-1])