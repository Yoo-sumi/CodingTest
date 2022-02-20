from collections import deque
n,k=3,3
graph=[
    [1,0,2],
    [0,0,0],
    [3,0,0]
]
S,X,Y=1,2,2
dx=[1,-1,0,0]
dy=[0,0,1,-1]
q=deque()
def bfs(index):
    for i in range(n):
        for j in range(n):
            if graph[i][j]==index:
                q.append((i,j))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if graph[nx][ny]==0:
                    graph[nx][ny]=graph[x][y]
count=0
while True:
    if count==S:
        break
    for num in range(1,k+1):
        bfs(num)
    count+=1
print(graph[X-1][Y-1])