from collections import deque
'''N,L,R=2,20,50
array=[
    [50,30],
    [20,40]
]'''
'''N,L,R=2,40,50
array=[
    [50,30],
    [20,40]
]'''
'''N,L,R=3,5,10
array=[
    [10,15,20],
    [20,30,25],
    [40,22,10]
]'''
N,L,R=map(int,input().split())

array=[[] for _ in range(N)]
for i in range(N):
    array[i]=list(map(int,input().split()))
q=deque()
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(x,y,index):
    united=[]
    count=1
    united.append((x,y))
    summary=array[x][y]
    union[x][y]=index
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if L<=abs(array[x][y]-array[nx][ny])<=R and union[nx][ny]==-1:
                    q.append((nx,ny))
                    united.append((nx,ny))
                    summary+=array[nx][ny]
                    union[nx][ny]=index
                    count+=1
    for i in range(N):
        for j in range(N):
            if union[i][j]==index:
                array[i][j]=summary//count
total_count=0
while True:
    union=[[-1]*N for _ in range(N)]
    index=0
    for i in range(N):
        for j in range(N):
            if union[i][j]==-1:
                bfs(i,j,index)
                index+=1
    if index==N*N:
        break
    total_count+=1


print(total_count)