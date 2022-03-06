import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)
n,m,start=3,2,1
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
def dijkstra(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)

result=0
count=0
for i in range(1,n+1):
    if distance[i]==INF:
        continue
    result=max(result,distance[i])
    count+=1
print(count-1,result)