n,m=4,4
a,b,d=1,1,0
array=[
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1]
]
gone=[]
gone.append((a,b))
move=[(0,-1),(-1,0),(0,1),(1,0)]
back=[(1,0),(0,-1),(-1,0),(0,1)]
def change_direction(d):
    if d==0:
        return 3
    return d-1
count=0
while True:
    if count==4:
        nx=a+back[d][0]
        ny=b+back[d][1]
        if array[nx][ny]==0:
            a=nx
            b=ny
            count=0
        else:
            break
    nx=a+move[d][0]
    ny=b+move[d][1]
    print(nx,ny)
    if array[nx][ny]==0 and not (nx,ny) in gone:
        a=nx
        b=ny
        gone.append((a,b))
        count=0
    else:
        count+=1
    d=change_direction(d)
print(len(gone))
print(gone)