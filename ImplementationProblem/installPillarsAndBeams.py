n=5
#build_frame=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
def judge(array,x,y,a):
    if a==0: # 기둥 설치
        if y==0 or ((array[x-1][y]==1) ^ (array[x][y]==1)) or array[x][y-1]==0:
            return True
        else:
            return False
    elif a==1: # 보 설치
        if ((array[x][y-1]==0) ^ (array[x+1][y-1]==0)) or (array[x-1][y]==1 and array[x+1][y]==1):

            return True
        else:return False

def delete(array,x,y,a):
    if a==0: #기둥 삭제:
        if not judge(array,x,y,a):
            array[x][y]=-1
    elif a==1: #기둥 삭제:
        if not judge(array,x,y,a):
            array[x][y]=-1
    '''array[x][y]=-1
    if a==0: #기둥 삭제
        if not (judge(array,x-1,y,1) and judge(array,x,y,1) and judge(array,x-1,y+1,1) and judge(array,x,y+1,1) and judge(array,x,y-1,0) and judge(array,x,y+1,0)):
            array[x][y]=0
    elif a==1: #보 삭제
        if not (judge(array,x-1,y,1) and judge(array,x+1,y,1) and judge(array,x,y-1,0) and judge(array,x+1,y-1,0) and judge(array,x,y,0) and judge(array,x+1,y,0)):
            array[x][y]=1'''
def solution(n, build_frame):
    array=[[-1]*(n+1) for _ in range(n+1)]
    for x,y,a,b in build_frame:
        if b==1: # 설치
            if a==0:
                if judge(array,x,y,a):
                    array[x][y]=0
            if a==1:
                if judge(array,x,y,a):
                    array[x][y]=1
        elif b==0: # 삭제
            delete(array,x,y,a)
    result=[]
    for i in range(n+1):
        for j in range(n+1):
            if array[i][j]!=-1:
                result.append(list((i,j,array[i][j])))
    return result


print(solution(n,build_frame))