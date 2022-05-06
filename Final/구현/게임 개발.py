import sys
input=sys.stdin.readline

def change_direction(dd):
    if dd==0:
        return 3
    return dd-1

def solution():
    n,m=map(int,input().split())
    x,y,d=map(int,input().split())
    graph=[]
    for i in range(n):
        graph.append(list(map(int,input().split())))
    path=[]
    path.append((x,y))
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    dir=d
    count=0
    while True:
        if count==4:
            nx=x-dx[dir]
            ny=y-dy[dir]
            if not 0<=nx<n or not 0<=ny<m:
                break
            if graph[nx][ny]==1:
                break
            x,y=nx,ny
            if not (x,y) in path:
                path.append((x,y))
            count=0
            continue
        dir=change_direction(dir)
        count+=1
        nx=x+dx[dir]
        ny=y+dy[dir]
        if not 0<=nx<n or not 0<=ny<m:
            continue
        if graph[nx][ny]==0:
            if (nx,ny) in path:
                continue
            x,y=nx,ny
            path.append((x,y))
            count=0
    return len(path)
print(solution())