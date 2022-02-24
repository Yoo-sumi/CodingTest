'''n=7
day=[3,5,1,1,2,4,2]
money=[10,20,10,20,15,40,200]'''
'''n=10
day=[1,1,1,1,1,1,1,1,1,1]
money=[1,2,3,4,5,6,7,8,9,10]'''
'''n=10
day=[5,5,5,5,5,5,5,5,5,5]
money=[10,9,8,7,6,10,9,8,7,6]'''
n=10
day=[5,4,3,2,1,1,2,3,4,5]
money=[50,40,30,20,10,10,20,30,40,50]

d=[0]*(n+1)
max_value=0
for i in range(n-1,-1,-1):
    time=day[i]+i
    if time<=n:
        d[i]=max(money[i]+d[time],max_value)
        max_value=d[i]
    else:
       d[i]=max_value
print(max(d))

