n,m=4,2
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]
x,k=3,4

for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
if graph[1][k]==INF or graph[k][x]==INF:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])