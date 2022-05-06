import sys
input=sys.stdin.readline

n=int(input())
array=list(map(str,input().split()))

def solution():
    x,y=1,1
    for i in array:
        nx,ny=x,y
        if i=='U':
            nx=x-1
        elif i=='D':
            nx=x+1
        elif i=='L':
            ny=y-1
        elif i=='R':
            ny=y+1
        if not 1<=nx<=n or not 1<=ny<=n:
            continue
        x,y=nx,ny
    return x,y

print(solution())

