from collections import deque
n,m=5,6
array=[
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
q=deque()
def bfs(x,y):
    q.append((x,y))
    while q:
        nx,ny=q.popleft()
        for i in range(4):
            next_x=nx+dx[i]
            next_y=ny+dy[i]
            if next_x<0 or next_x>=5 or next_y<0 or next_y>=6:
                continue
            if array[next_x][next_y]==1:
                array[next_x][next_y]=array[nx][ny]+1
                q.append((next_x,next_y))
bfs(0,0)
print(array)
#[[3, 0, 5, 0, 7, 0], [2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 8], [14, 13, 12, 11, 10, 9], [15, 14, 13, 12, 11, 10]]