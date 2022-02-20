from collections import deque
n,m,k,x=4,4,1,1
graph=[
    [],
    [2,3],
    [3,4],
    [],
    []
]
visited=[-1]*(n+1)
q=deque()
def bfs(v):
    q.append(v)
    visited[v]=0
    while q:
        now=q.popleft()
        for i in graph[now]:
            if visited[i]==-1:
                q.append(i)
                visited[i]=visited[now]+1
bfs(x)
flag=False
for i in range(n+1):
    if visited[i]==k:
        print(i)
        flag=True
if flag==False:
    print(-1)

