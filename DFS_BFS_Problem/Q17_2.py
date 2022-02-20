'''n,k=3,3
graph=[
    [1,0,2],
    [0,0,0],
    [3,0,0]
s,x,y=2,3,2
]'''
n,k=3,3
graph=[
    [1,0,2],
    [0,0,0],
    [3,0,0]
]
s,x,y=1,2,2
temp=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        temp[i][j]=graph[i][j]


dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(count):
    if count==s:
        return
    for v in range(1,k+1):
        for i in range(n):
            for j in range(n):
                if graph[i][j]==v:
                    for c in range(4):
                        nx=i+dx[c]
                        ny=j+dy[c]
                        if nx>=0 and nx<n and ny>=0 and ny<n:
                            if graph[nx][ny]==0:
                                temp[nx][ny]=v
        for ii in range(n):
            for jj in range(n):
                graph[ii][jj]=temp[ii][jj]
    dfs(count+1)
dfs(0)
for i in range(n):
    for j in range(n):
        print(temp[i][j],end=" ")
    print()
print(graph[x-1][y-1])
