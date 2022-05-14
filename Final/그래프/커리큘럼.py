from collections import deque
import copy
n=int(input())
graph=[[] for _ in range(n+1)]
parent=[0]*(n+1)
result=[0]*(n+1)
time=[0]*(n+1)
for i in range(1,n+1):
    li=list(map(int,input().split()))
    time[i]=li[0]
    for j in li[1:-1]:
        graph[j].append(i)
        parent[i]+=1

q=deque()
result=copy.deepcopy(time)
for i in range(1,n+1):
    if parent[i]==0:
        q.append(i)
while q:
    now=q.popleft()
    for i in graph[now]:
        result[i]=max(result[i],result[now]+time[i])
        parent[i]-=1
        if parent[i]==0:
            q.append(i)
print(result)
print(time)