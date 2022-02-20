from collections import deque
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9

q=deque()

def dfs(graph,visited,v):
    visited[v]=True
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,visited,i)

def bfs(graph,visited,v):
    q.append(v)
    visited[v]=True
    while q:
        now=q.popleft()
        print(now,end=" ")
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
#dfs(graph,visited,1)
bfs(graph,visited,1)