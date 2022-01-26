n, m = map(int, input().split())
x, y, direction =list(map(int, input().split()))
x-=1
y-=1
array=[]
gone_list=[]
for i in range(4):
    array.append(list(map(int, input().split())))

