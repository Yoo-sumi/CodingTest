from collections import deque
n=8
graph=[
    [],
    [2,3],
    [1,7,8],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [2,7]
]
visited=[False]*(n+1)
def dfs(v):
    visited[v]=True
    print(v,end=" ")
    for i in graph[v]:
        if visited[i]==False:
            dfs(i)
q=deque()
def bfs(v):
    q.append(v)
    visited[v]=True
    while q:
        now=q.popleft()
        print(now,end=" ")
        for i in graph[now]:
            if visited[i]==False:
                q.append(i)
                visited[i]=True
#dfs(1)
bfs(1)