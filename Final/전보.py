import heapq
n,m,x=map(int,input().split())
distance=[1e9]*(n+1)
graph=[[] for _ in range(n+1)]
result=-1
count=-1
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

q=[]
heapq.heappush(q,(0,x))
distance[x]=0
while q:
    dist,v=heapq.heappop(q)
    if distance[v]<dist:
        continue
    for index,cost in graph[v]:
        if distance[index]>dist:
            distance[index]=dist+cost
            heapq.heappush(q,(distance[index],index))
for i in distance[1:]:
    if i!=1e9:
        result=max(result,i)
        count+=1
print(distance)
print(count,result)