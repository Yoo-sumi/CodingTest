import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for i in range(n):
    arr=str(input())
    for j in arr[:-1]:
        graph[i].append(int(j))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()
q.append((0,0))
while q:
    x,y=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if not 0<=nx<n or not 0<=ny<m:
            continue
        if graph[nx][ny]==1:
            graph[nx][ny]+=graph[x][y]
            q.append((nx,ny))
print(graph[n-1][m-1])