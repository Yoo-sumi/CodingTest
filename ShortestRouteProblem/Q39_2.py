import heapq
n=7
INF=int(1e9)
distance=[[INF]*n for _ in range(n)]
'''graph=[
    [3,7,2,0,1],
    [2,8,0,9,1],
    [1,2,1,8,1],
    [9,8,9,2,0],
    [3,6,5,1,5]
]'''
graph=[
    [9,0,5,1,1,5,3],
    [4,1,2,1,6,5,3],
    [0,7,6,1,6,8,5],
    [1,1,7,8,3,2,3],
    [9,4,0,7,6,4,1],
    [5,8,3,2,4,8,3],
    [7,4,8,4,8,3,4]
]

q=[]
heapq.heappush(q,(graph[0][0],0,0))
distance[0][0]=graph[0][0]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
while q:
    dist,x,y=heapq.heappop(q)
    if distance[x][y]<dist:
        continue
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            cost=dist+graph[nx][ny]
            if cost<distance[nx][ny]:
                distance[nx][ny]=cost
                heapq.heappush(q,(cost,nx,ny))
print(distance[n-1][n-1])