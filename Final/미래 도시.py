from collections import deque
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[1e9]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
x,k=map(int,input().split())

q=deque()
q.append((1,0))
distance[1]=0
while q:
    now=q.popleft()
    for i in graph[now[0]]:
        if distance[i]==1e9:
            q.append((i,now[1]+1))
            distance[i]=min(distance[i],now[1]+1)
if distance[x]+distance[k]>=1e9:
    print(-1)
else:
    print(distance[x]+distance[k])
