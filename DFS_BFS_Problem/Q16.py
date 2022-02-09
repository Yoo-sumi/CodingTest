n,m=map(int,input().split())
data=[]
temp=[[0]*m for _ in range(n)]
for i in range(n):
    data.append(list(map(int,input().split())))

def virus(x,y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(4):
        next_x=x+dx[i]
        next_y=y+dy[i]
        if next_x>=0 and next_x<n and next_y>=0 and next_y<m:
            if temp[next_x][next_y]==0:
                temp[next_x][next_y]=2
                virus(next_x,next_y)
def getscore():
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score
result=0
def dfs(count):
    global result
    if count==3:
        for i in range(n):
            for j in range(m):
                    temp[i][j]=data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        result=max(getscore(),result)
        return
    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j]=1
                count+=1
                dfs(count)
                data[i][j]=0
                count-=1

dfs(0)
print(result)