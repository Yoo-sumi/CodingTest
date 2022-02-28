n,m=2,15
coin=[2,3]
d=[10001]*(m+1)
d[0]=0
for i in range(n):
    for j in range(coin[i],m+1):
        if(j-coin[i]!=10001):
            d[j]=min(d[j],d[j-coin[i]]+1)
'''for i in range(0,m+1):
    for j in coin:
        if i+j>m:
            break
        if i+j!=10001:
            d[i+j]=min(d[i+j],d[i]+1)'''
if d[m]!=10001:
    print(d[m])
else:
    print(-1)