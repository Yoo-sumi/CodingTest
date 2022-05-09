from collections import deque
n,m,x=map(int,input().split())
distance=[1e9]*(n+1)
graph=[[] for _ in range(n+1)]
result=-1
count=-1
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

q=deque()
q.append(x)
distance[x]=0

while q:
    now=q.popleft()
    for i in graph[now]:
        distance[i[0]]=min(distance[i[0]],distance[now]+i[1])
        q.append(i[0])
for i in distance[1:]:
    if i!=1e9:
        result=max(result,i)
        count+=1
print(count,result)