from collections import deque
n, m, k, x = map(int,input().split())
data=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int, input().split())
    data[a].append(b)

distance=[-1]*(n+1)
distance[x]=0

q=deque()
q.append(x)

while q:
    now=q.popleft()
    for i in data[now]:
        if distance[i]==-1:
            q.append(i)
            distance[i]=distance[now]+1
flag=False
for i in range(1,n+1):
    if distance[i]==k:
        if flag==False:
            flag=True
        print(i)
if flag==False:
    print(-1)