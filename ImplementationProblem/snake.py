direction=1

def change(c):
    global direction
    if c=='L':
        if direction==0:
            direction=3
        else:
            direction-=1
    elif c=='D':
        if direction==3:
            direction=0
        else:
            direction+=1

n=int(input())
array=[[0]*(n) for _ in range(n)]

k=int(input())
for i in range(k):
    x, y=map(int,input().split())
    array[x-1][y-1]=2

l=int(input())
data_change=[]
for i in range(l):
    x,c=map(str,input().split())
    data_change.append((x,c))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

direction=1
x=0
y=0
array[x][y]=1
q=[]
q.append((x,y))

count=0
while True:
    count+=1

    x+=dx[direction]
    y+=dy[direction]

    for xx,c in data_change:
        if int(xx)==count:
            change(c)
            break


    if x<0 or y<0 or x>=n or y>=n:
        break
    elif array[x][y]==1:
        break
    elif array[x][y]==2:
        array[x][y]=1
        q.append((x,y))
    else:
        array[x][y]=1
        q.append((x,y))
        a, b=q.pop(0)
        array[a][b]=0
print(count)
