from collections import deque
from itertools import combinations
n,m=4,6
graph=[
    [0,0,0,0,0,0],
    [1,0,0,0,0,2],
    [1,1,1,0,0,2],
    [0,0,0,0,0,2]
]
temp=[[0]*m for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
q=deque()
# bfs
def virus(x,y):
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if temp[nx][ny]==0:
                    q.append((nx,ny))
                    temp[nx][ny]=2
# dfs
'''def virus(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return
    if temp[x][y]==1:
        return
    if temp[x][y]==0:
        temp[x][y]=2
        for i in range(4):
            virus(x+dx[i],y+dy[i])'''
def re():
    for i in range(n):
        for j in range(m):
            print(temp[i][j],end=" ")
        print()
def init():
    for i in range(n):
        for j in range(m):
            temp[i][j]=graph[i][j]
def get_score():
    count=0
    for i in range(n):
        for j in range(n):
            if temp[i][j]==0:
                count+=1
    return count
a=[]
maxx=0
for i in range(n):
    for j in range(m):
        a.append((i,j))
data=list(combinations(a,3))
for i in data:
    init()
    for x,y in i:
        if temp[x][y]==0:
            temp[x][y]=1
    for ii in range(n):
        for jj in range(m):
            if temp[ii][jj]==2:
                #temp[ii][jj]=0 #dfs일 경우
                virus(ii,jj)
    maxx=max(get_score(),maxx)
print(maxx)
