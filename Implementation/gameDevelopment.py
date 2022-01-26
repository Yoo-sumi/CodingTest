n, m = map(int, input().split())
x, y, direction =list(map(int, input().split()))
x-=1
y-=1
array=[]
gone_list=[]
for i in range(4):
    array.append(list(map(int, input().split())))
steps=0
while True:
    count=0

    for i in range(4):
        if direction==0:
            next_x=x
            next_y=y-1
        elif direction==1:
            next_x=x-1
            next_y=y
        elif direction==2:
            next_x=x
            next_y=y+1
        elif direction==3:
            next_x=x+1
            next_y=y
        toggle=0 # 없다
        print(gone_list)
        for j in gone_list:
            if (next_x>=0 and next_y>=0 and next_x<4 and next_y<4):
                if str(next_x)+str(next_y)==j:
                    #print("구 리스트에 있다")
                    toggle=1
                    break
        if toggle==0:

            if (next_x>=0 and next_y>=0 and next_x<4 and next_y<4):
                if array[next_x][next_y]==1:
                    x=next_x
                    y=next_y
                    gone_list.append(str(x)+str(y))
                    steps+=1
                    #print("pl")
            else:
                if direction==0:
                    direction=3
                else:
                    direction-=1

            count+=1
        else:
            if direction==0:
                direction=3
            else:
                direction-=1
            count+=1
    if count==4:
        if direction==0:
            next_x=x+1
            next_y=y
        elif direction==1:
            next_x=x
            next_y=y-1
        elif direction==2:
            next_x=x-1
            next_y=y
        elif direction==3:
            next_x=x
            next_y=y+1
        if (next_x<0 and next_y<0 and next_x>3 and next_y>3):
            if array[next_x][next_y]==0:
                break
print(steps)


