def rotate(key):
    m=len(key)
    rotate_key=[[0]*m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            rotate_key[i][j]=key[m-1-j][i]
    return rotate_key
def check(new_lock):
    length=len(new_lock)//3
    for i in range(length,length*2):
        for j in range(length,length*2):
            if new_lock[i][j]!=1:
                return False
    return True

def solution(key, lock):
    n=len(lock)
    m=len(key)
    new_lock=[[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n]=lock[i][j]
    for h in range(4):
        key=rotate(key)
        for x in range(0,(n*3)-n+1):
            for y in range(0,(n*3)-n+1):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=key[i][j]
                if check(new_lock)==True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-=key[i][j]
    return False
key=[[0,0,0],[1,0,0],[0,1,1]]
lock=[[1,1,1],[1,1,0],[1,0,1]]

print(solution(key,lock))
n=2
m=2
