'''n,m=2,15
coin=[2,3]'''
n,m=3,4
coin=[3,5,7]

d=[10001]*(m+1)
d[0]=0
for i in range(m):
    for j in coin:
        if i+j>m:
            continue
        if d[i]!=10001:
            d[i+j]=min(d[i]+1,d[i+j])
result=d[m]
if result!=10001:
    print(d[m])
else:
    print(-1)
