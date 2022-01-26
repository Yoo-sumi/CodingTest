y,x=map(str,input())

row=['1','2','3','4','5','6','7','8']
col=['a','b','c','d','e','f','g','h']
count=0

for i in range(len(row)):
    if x == row[i]:
        x=i
for i in range(len(col)):
    if y == col[i]:
        y=i

if (y+2)<8: # 오른쪽 수평
    if (x+1)<8: # 아래로 한칸
        count+=1
    if (x-1)>=0: # 위로 한칸
        count+=1
if (y-2)>=0: # 왼쪽 수평
    if (x+1)<8: # 아래로 한칸
        count+=1
    if (x-1)>=0: # 위로 한칸
        count+=1

if (x+2)<8: # 아래 수평
    if (y+1)<8: # 오른쪽으로 한칸
        count+=1
    if (y-1)>=0: # 왼쪽으로 한칸
        count+=1
if (x-2)>=0: # 위로 수평
    if (y+1)<8: # 아래로 한칸
        count+=1
    if (y-1)>=0: # 왼쪽으로 한칸
        count+=1
print(count)
