n,m=6,6
INT=int(1e9)
graph=[[INT]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
result=[False]*(n+1)
result_count=0
for i in range(1,n+1):
    count=0
    for j in range(1,n+1):
        if graph[i][j]!=INT or graph[j][i]!=INT:
            count+=1
    if count==n:
        result[i]=True
        result_count+=1

print(result_count)