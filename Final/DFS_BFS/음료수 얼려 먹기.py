import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for i in range(n):
    arr=str(input())
    for s in arr[:-1]:
        graph[i].append(int(s))
def dfs(x,y,num):
    global graph
    if not 0<=x<n or not 0<=y<m:
        return
    if graph[x][y]==0:
        graph[x][y]=num
        dfs(x+1,y,num)
        dfs(x-1,y,num)
        dfs(x,y+1,num)
        dfs(x,y-1,num)
num=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            num-=1
            dfs(i,j,num)
print(-num)
