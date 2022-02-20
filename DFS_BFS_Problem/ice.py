data=[
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]
sum=0
def ice(x,y):
    if x<0 or x>=4 or y<0 or y>=5:
        return False
    if data[x][y]==0:
        data[x][y]=1
        ice(x,y-1)
        ice(x,y+1)
        ice(x-1,y)
        ice(x+1,y)
        return True
    return False

for i in range(4):
    for j in range(5):
        if ice(i,j)==True:
            sum+=1
print(sum)