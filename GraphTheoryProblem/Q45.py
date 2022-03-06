from collections import deque
import copy
n=3
m=0
data=list(map(int,input().split()))
graph=[[] for i in range(n+1)]
degree=[0]*(n+1)
for i in range(n):
    for j in range(i+1,n):
        a=data[i]
        b=data[j]
        graph[a].append(b)
        degree[b]+=1

for i in range(m):
    x,y=map(int,input().split())
    if graph[x].count(y)>0:
        degree[y]+=1
        continue
    graph[x].append((y))
    graph[y].remove((x))
    degree[y]+=1
    degree[x]-=1

def topology_sort():
    q=deque()
    result=[]
    cycle=False
    certain=True
    for i in range(1,n+1):
        if degree[i]==0:
            q.append(i)

    for ii in range(n):
        if len(q)==0:
            cycle=True
            break
        if len(q)>=2:
            certain=False
            break
        now=q.popleft()
        result.append(now)
        for i in graph[now]:
            degree[i]-=1
            if degree[i]==0:
                q.append(i)
    if cycle==True:
        print("IMPOSSIBLE")
    elif certain==False:
        print("?")
    else:
        print(result)
topology_sort()

