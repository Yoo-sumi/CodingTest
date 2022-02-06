n=int(input())
k=int(input())
apple=[]
rotate=[]
for i in range(k):
    row,column=map(int,input().split())
    apple.append((row,column))
l=int(input())
for i in range(l):
    x,c=map(str,input().split())
    rotate.append((x,c))
left=[(-1,0),(1,0),(0,-1),(0,1)]
right=[(1,0),(-1,0),(0,1),(0,-1)]
x=0
y=0
array=[[0]*(n) for _ in range(n)]
for (r,c) in apple:
    array[r-1][c-1]=2
array[x][y]=1
direction=0
q=[(x,y)]
