from collections import deque
n=5
degree=[0]*(n+1)
time=[0]*(n+1)

graph=[[] for i in range(n+1)]
for i in range(1,n+1):
    a=list(map(int,input().split()))
    time[i]=a[0]
    for j in a[1:-1]:
        graph[j].append(i)
        degree[i]+=1
def topology_sort():
    result=[0]*(n+1)
    q=deque()

    for i in range(1,n+1):
        if degree[i]==0:
            q.append(i)
            result[i]=time[i]
    while q:
        now=q.popleft()

        for i in graph[now]:
            result[i]=max(result[i],time[i]+result[now])
            degree[i]-=1
            if degree[i]==0:
                q.append(i)

    for i in result[1:]:
        print(i)
topology_sort()