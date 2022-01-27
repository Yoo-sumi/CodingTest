# 내가 작성한 코드
n, m = map(int, input().split())
x, y, direction =list(map(int, input().split()))
steps=1
array=[]
gone_list=[[0]*m for i in range(n)]
gone_list[x][y]=1
for i in range(4):
    array.append(list(map(int, input().split())))

def search_direction():
    if direction==0:
        new_x=x-1
        new_y=y
    elif direction==1:
        new_x=x
        new_y=y+1
    elif direction==2:
        new_x=x+1
        new_y=y
    elif direction==3:
        new_x=x
        new_y=y-1
    return  new_x,new_y
def change_direction():
    global direction
    if direction==0:
        direction=3
    else:
        direction-=1
def back_direction():
    if direction==0:
        new_x=x+1
        new_y=y
    elif direction==1:
        new_x=x
        new_y=y-1
    elif direction==2:
        new_x=x-1
        new_y=y
    elif direction==3:
        new_x=x
        new_y=y+1
    return new_x,new_y

count=0
while True:
    change_direction()
    new_x,new_y=search_direction()
    if gone_list[new_x][new_y]==0 and array[new_x][new_y]==0:
        x=new_x
        y=new_y
        gone_list[x][y]=1
        count=0
        steps+=1
    else: count+=1

    if count==4:
        new_x,new_y=back_direction()
        if array[new_x][new_y]==0:
            x=new_x
            y=new_y
            count=0
            print("뒤로 감 ")
            print(str(x)+str(y)+str(direction))
        else:
            print(str(x)+str(y)+str(direction))
            break
    print(str(x)+str(y)+str(direction))
print(steps)
print(gone_list)
