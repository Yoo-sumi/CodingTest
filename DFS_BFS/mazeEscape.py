n,m=map(int,input().split())
graph=[]

for i in range(n):
    graph.append(list(map(int,input())))

def bfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return 0
    if graph[x][y]==1:
        graph[x][y]=2
        bfs(x-1,y)
        bfs(x+1,y)
        bfs(x,y-1)
        bfs(x,y+1)
        return 1
    return 0

for i in range(n):
    for j in range(m):
        bfs(i,j)
