n,m=map(int,input().split())
arr=[]
for _ in range(n):
    li=sorted(list(map(int,input().split())))
    arr.append(li)
maxx=0
for i in range(n):
    maxx=max(maxx,arr[i][0])
print(maxx)

