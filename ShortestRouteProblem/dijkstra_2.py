import heapq
import sys
input=sys.stdin.readline
#v,e=map(int,input().split())
#start=int(input())
v,e=6,11
start=1
#graph=[[] for _ in range(v+1)]
distance=[int(1e9)]*(v+1)
graph=[
    [],
    [(2,2),(3,5),(4,1)],
    [(3,3),(4,2)],
    [(2,3),(6,5)],
    [(3,3),(5,1)],
    [(3,1),(6,2)],
    []
]
'''for i in range(e):
    a,b,d=map(int,input().split())
    graph[a].append((d,b))'''

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

for i in distance:
    print(i,end=" ")

