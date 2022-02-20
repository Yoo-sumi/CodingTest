n=5
array=[
    ['X','S','X','X','T'],
    ['T','X','S','X','X'],
    ['X','X','X','X','X'],
    ['X','T','X','X','X'],
    ['X','X','T','X','X']
]
'''n=4
array=[
    ['S','S','S','T'],
    ['X','X','X','X'],
    ['X','X','X','X'],
    ['T','T','T','X']
]'''

temp=[['X']*n for _ in range(n)]

def get_score(x,y,direction):
    if x<0 or y>=n or y<0 or x>=n:
        return True
    if temp[x][y]=='O':
        return True
    if temp[x][y]=='S':
        return False
    else:
        if direction==0:
            result=get_score(x-1,y,0)
        if direction==1:
            result=get_score(x+1,y,1)
        if direction==2:
            result=get_score(x,y-1,2)
        if direction==3:
            result=get_score(x,y+1,3)
    return result
re=[]
def dfs(count):
    global temp,re
    if count==3:
        for i in range(n):
            for j in range(n):
                temp[i][j]=array[i][j]
        flag=True
        for i in range(n):
            for j in range(n):
                if temp[i][j]=='T':
                    up=get_score(i-1,j,0)
                    down=get_score(i+1,j,1)
                    left=get_score(i,j-1,2)
                    right=get_score(i,j+1,3)
                    if not (up and down and left and right):
                        flag=False
        re.append(flag)
        return
    for i in range(n):
        for j in range(n):
            if array[i][j]=='X':
                array[i][j]='O'
                dfs(count+1)
                array[i][j]='X'
dfs(0)
if True in re:
    print("YES")
else:
    print("NO")