import sys
import heapq
input=sys.stdin.readline
n, m , c=map(int,input().split()) # 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C
INF=int(1e9)
graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b,d=map(int,input().split())
    graph[a].append((b,d))

distance=[INF]*(n+1)

def dijkstra(start):
    q=[]

    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist, now=heapq.heappop(q) # 최단거리 pop
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)

count=0
max_distance=0
for i in range(1,n+1):
    if not distance[i]==INF:
        max_distance=max(distance[i],max_distance)
        if not distance[i]==0:
            count+=1
print(count,max_distance)
