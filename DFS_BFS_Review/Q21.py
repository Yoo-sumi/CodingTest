from collections import deque
N,L,R=4,10,50
graph=[
    [10,100,20,90],
    [80,100,60,70],
    [70,20,30,40],
    [50,20,100,10]
]
'''N,L,R=2,20,50
graph=[
    [50,30],
    [20,100]
]'''
dx=[1,-1,0,0]
dy=[0,0,1,-1]
q=deque()
#visited=[[-1]*N for _ in range(N)]
def move(x,y,index):
    sum=0
    count=0
    q.append((x,y))
    visited[x][y]=index
    sum+=graph[x][y]
    count+=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<N:
                if visited[nx][ny]==-1:
                    if (L<=abs(graph[x][y]-graph[nx][ny])<=R):
                        q.append((nx,ny))
                        visited[nx][ny]=index
                        sum+=graph[nx][ny]
                        count+=1
    for i in range(N):
        for j in range(N):
            if visited[i][j]==index:
                graph[i][j]=sum//count
total_count=0

while True:
    visited=[[-1]*N for _ in range(N)]
    index=0
    for i in range(N):
        for j in range(N):
            if visited[i][j]==-1:
                move(i,j,index)
                index+=1
    if index==(N*N):
        break
    total_count+=1
print(total_count)