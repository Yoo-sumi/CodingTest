n=5
a=['R','R','R','U','D','D']

start_x=1
start_y=1

for i in a:
    if i=='L' and start_y>1:
        start_y-=1
    if i=='R' and start_y<n:
        start_y+=1
    if i=='U' and start_x>1:
        start_x-=1
    if i=='D' and start_x<n:
        start_x+=1
    print(start_x,start_y)
print(start_x,start_y)