n,m=map(int,input().split())
data=list(map(int,input().split()))
weight=[0]*(m+1)
for i in data:
    weight[i]+=1
count=0

for i in range(1,m+1):
    n-=weight[i]
    count+=weight[i]*n


'''for i in range(n-1):
    for j in range(i+1,n):
        if data[i]!=data[j]:
            count+=1'''


print(count)