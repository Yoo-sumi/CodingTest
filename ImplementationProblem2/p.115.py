s='c2'
x=int(s[1])
y=ord(s[0])-96
steps=[(1,2),(-1,2),(1,-2),(-1,-2),(-2,1),(-2,-1),(2,1),(2,-1)]
count=0
for (ix,iy) in steps:
    nx=x+ix
    ny=y+iy
    if 0<nx<9 and 0<ny<9:
        count+=1
print(count)