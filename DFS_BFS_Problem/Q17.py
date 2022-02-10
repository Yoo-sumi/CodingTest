from collections import deque

n,k=map(int,input().split())
graph=[]
data=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

s,x,y=map(int,input().split())
x-=1
y-=1

for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            data.append((graph[i][j],0,i,j))
data.sort()

q=deque(data)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

while q:
    
    virus, count, tx, ty = q.popleft()

    if count==s:
        break
    # 상하좌우
    for i in range(4):
        n_dx=tx+dx[i]
        n_dy=ty+dy[i]
        if n_dx>=0 and n_dx<n and n_dy>=0 and n_dy<n:
            if graph[n_dx][n_dy]==0:
                graph[n_dx][n_dy]=virus
                q.append((graph[n_dx][n_dy],count+1,n_dx,n_dy))
print(graph[x][y])