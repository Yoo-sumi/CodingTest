'''n,m=7,7
graph=[
    [2,0,0,0,1,1,0],
    [0,0,1,0,1,2,0],
    [0,1,1,0,1,0,0],
    [0,1,0,0,0,0,0],
    [0,0,0,0,0,1,1],
    [0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0]
]'''
'''n,m=4,6
graph=[
    [0,0,0,0,0,0],
    [1,0,0,0,0,2],
    [1,1,1,0,0,2],
    [0,0,0,0,0,2]
]'''
n,m=8,8
graph=[
    [2,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,2],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]
temp=[[0]*(m) for _ in range(n)]
def virus(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return
    if temp[x][y]==1:
        return
    if temp[x][y]==0:
        temp[x][y]=2
        virus(x,y-1)
        virus(x,y+1)
        virus(x+1,y)
        virus(x-1,y)
'''dx=[-1,0,1,0]
dy=[0,1,0,-1]
def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)'''

def get_score():
    sum=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                sum+=1
    return sum
result=0
def dfs(count):
    global result
    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    #
                    temp[i][j]=0
                    virus(i,j)
        result=max(get_score(),result)
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                count+=1
                dfs(count)
                count-=1
                graph[i][j]=0

for i in range(n):
    for j in range(m):
        print(graph[i][j],end=" ")
    print()

dfs(0)
print(result)