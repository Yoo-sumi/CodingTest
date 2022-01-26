n=int(input())
data=list(map(str, input().split()))

x,y=1,1 # 시작좌표는 (1,1)

for i in data:
    if i=="U" and x!=1:
        x-=1
    elif i=="D" and x!=n:
        x+=1
    elif i=="L" and y!=1:
        y-=1
    elif i=="R" and y!=n:
        y+=1
print(x,y)