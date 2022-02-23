'''n=7
day=[3,5,1,1,2,4,2]
money=[10,20,10,20,15,40,200]'''
n=10
day=[1,1,1,1,1,1,1,1,1,1]
money=[1,2,3,4,5,6,7,8,9,10]
d=[0]*(n)

for i in range(n):
    now=i
    next=i+day[i]
    if d[now]==0 and next<n:
        d[now]=money[now]
    while True:
        print(now,next)
        if next<n and next+day[next]<n:
            d[next]=max(d[next],d[now]+money[next])
            now=next
            next=now+day[now]
            print(d)
        else:
            break
print(max(d))

