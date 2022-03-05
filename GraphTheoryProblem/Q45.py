from collections import deque
import copy
n=4
degree=[0]*(n+1)

data=list(map(int,input().split()))

graph=[[] for _ in range(n+1)]
graph_copy=[[] for _ in range(n+1)]

for i in range(n-1,0,-1):
    graph[data[i]].append(data[i-1])
    degree[data[i-1]]+=1
graph_copy=copy.deepcopy(graph)
m=3
for i in range(m):
    a,b=map(int,input().split())
    if graph[b].count(a)>0:
        print("IMPOSSIBLE")
        break
    if graph[a].count(b)>0:
        graph[a].remove(b)
        degree[b]-=1
        for j in graph_copy[b]:
            graph[a].append(j)
            graph[b].remove(j)
    graph[b].append(a)
    degree[a]+=1
print(degree)
print(graph)
def topology_sort():
    q=deque()
    result=[]
    for i in range(1,n+1):
        if degree[i]==0:
            q.append(i)
    while q:
        now=q.popleft()
        result.append(now)

        for i in graph[now]:
            degree[i]-=1
            if degree[i]==0:
                q.append(i)
    print(result)
topology_sort()