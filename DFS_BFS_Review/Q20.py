from itertools import combinations
n=4
wall=[]
graph=[
    ['S','S','S','T'],
    ['X','X','X','X'],
    ['X','X','X','X'],
    ['T','T','T','X']
]
temp=[['X']*n for _ in range(n)]
def init():
    for i in range(n):
        for j in range(n):
            temp[i][j]=graph[i][j]
def judge(x,y,direction):
    if x<0 or x>=n or y<0 or y>=n:
        return True
    if temp[x][y]=='O':
        return True
    if temp[x][y]=='S':
        return False
    else:
        if direction==0:
            return judge(x-1,y,0)
        if direction==1:
            return judge(x+1,y,1)
        if direction==2:
            return judge(x,y-1,2)
        if direction==3:
            return judge(x,y+1,3)

for i in range(n):
    for j in range(n):
        if graph[i][j]=='X':
            wall.append((i,j))
data=list(combinations(wall,3))
flag=False

for i in data:
    init()
    answer=[]
    for x,y in i:
        temp[x][y]='O'
    for ii in range(n):
        for jj in range(n):
            if temp[ii][jj]=='T':
                up=judge(ii,jj,0)
                down=judge(ii,jj,1)
                left=judge(ii,jj,2)
                right=judge(ii,jj,3)
                if up and down and left and right:
                    answer.append(True)
                else:
                    answer.append(False)
    if not False in answer:
        flag=True
if flag:
    print("YES")
else:
    print("NO")